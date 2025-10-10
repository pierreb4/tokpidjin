# p_g GPU Performance Analysis

**Date:** October 10, 2025  
**Operation:** `p_g` (extract palette from grid)  
**Result:** ❌ GPU 3x slower than CPU  

## Test Results

### Correctness: ✅ PASS
All 5 test cases match CPU output exactly.

### Performance: ❌ FAIL

| Metric | Time | vs CPU |
|--------|------|--------|
| CPU | 0.12 ms | 1.0x (baseline) |
| GPU (amortized) | 0.34 ms | **0.34x (3x slower)** |
| GPU (with transfer) | 0.48 ms | **0.24x (4x slower)** |

## Root Cause Analysis

### Why is GPU slower?

1. **Operation is too simple**
   - `p_g` just extracts unique values: `set(grid.flatten())`
   - CPU: ~0.12ms for 900 cells (30x30 grid)
   - This is **extremely fast** on CPU
   - Only ~133 nanoseconds per cell!

2. **GPU overhead dominates**
   - CuPy kernel launch overhead: ~0.1-0.2ms
   - `cp.unique()` kernel: ~0.05ms
   - Result transfer (10 values): ~0.05ms
   - **Total overhead > actual computation time**

3. **Small data size**
   - 30x30 = 900 cells = ~900 bytes
   - Result: ~10 colors = ~40 bytes
   - GPU excels at **big data** (millions of elements)
   - This is too small to benefit

### Mathematical Analysis

**Break-even point for GPU:**
```
GPU_overhead + (N * GPU_per_element) < CPU_time
0.2ms + (N * 0.0001ms) < N * 0.000133ms
0.2ms < N * 0.000033ms
N > 6060 elements
```

**For ARC grids:**
- Typical grid: 30x30 = 900 elements ❌ (too small)
- Large grid: 100x100 = 10,000 elements ✓ (would benefit)
- ARC grids rarely exceed 30x30

## Decision: DON'T GPU-accelerate p_g

### Rationale

1. **CPU is already fast** (0.12ms)
   - Even at 100 calls/batt, that's only 12ms total
   - Not worth the complexity

2. **GPU overhead too high** for this operation
   - Would need 10x larger grids to break even
   - ARC grids are typically small

3. **Better targets exist**
   - `o_g` (objects on grid) - much more complex
   - `fgpartition` - involves connectivity analysis
   - `difference` - larger data structures

### Impact on Overall Strategy

This **validates our adaptive approach**:
- ✅ Not all operations benefit from GPU
- ✅ Automatic CPU fallback is essential
- ✅ Need to measure, not assume

**Updated Priority 1 Operations:**

| Operation | Expected Benefit | Actual Benefit | Status |
|-----------|------------------|----------------|--------|
| ~~p_g~~ | 3-4x | **0.3x (worse!)** | ❌ Skip GPU |
| o_g | 3-4x | 🔄 Test next | 🟡 High priority |
| fgpartition | 3-4x | 🔄 Test next | 🟡 Test needed |

## Corrected Performance Estimates

### Original Estimate (Incorrect)
```
Priority 1 Operations:
- p_g: 100 calls × 0.5ms = 50ms → 15ms = 35ms saved
- o_g: 30 calls × 1.5ms = 45ms → 12ms = 33ms saved
- fgpartition: 20 calls × 1ms = 20ms → 5ms = 15ms saved
Total Priority 1: 83ms saved (wrong!)
```

### Revised Estimate (Correct)
```
Priority 1 Operations:
- p_g: 100 calls × 0.12ms = 12ms → DON'T GPU (0ms saved)
- o_g: 30 calls × 1.5ms = 45ms → 12ms = 33ms saved (if works)
- fgpartition: 20 calls × 1ms = 20ms → 5ms = 15ms saved (if works)
Total Priority 1: ~48ms saved (optimistic)
```

**Revised overall speedup estimate: 1.8-2.5x** (down from 2-4x)

## Lessons Learned

### 1. Simple Operations Don't Benefit
**Rule of thumb:** If CPU time < 0.5ms, GPU probably won't help

Operations to skip:
- `size()` - just `len()`
- `first()`, `second()` - tuple indexing
- `astuple()` - tuple construction
- **`p_g()`** - set extraction

### 2. GPU Overhead is Real
- Kernel launch: ~0.1-0.2ms
- Small transfers: ~0.05ms
- Must amortize over many operations

### 3. Batch Processing Helps
If we process 100 grids at once:
- Transfer overhead: 0.2ms (one-time)
- Per-grid cost: 0.001ms
- **Would be 100x faster than individual calls**

But our architecture (DAG execution) doesn't support batching easily.

## Recommendations

### Immediate
1. ✅ **Skip p_g GPU implementation** - use CPU fallback
2. 🔄 **Test o_g next** - more complex, likely to benefit
3. 🔄 **Test fgpartition** - connectivity analysis is GPU-friendly

### If o_g also fails
Consider **abandoning individual operation GPU acceleration** and instead:
- Profile to find actual bottlenecks
- Consider CPU optimization (vectorization, caching)
- Accept that ARC grid sizes are too small for GPU

### If o_g succeeds
- Focus only on complex operations (compute > 1ms)
- Build registry of "GPU-worthy" operations
- Keep simple operations on CPU

## Next Steps

1. **Implement o_g GPU version** (highest priority)
   - More complex: connected components, object extraction
   - Likely 2-10ms per call on CPU
   - If GPU < 1ms, that's a win

2. **If o_g works:**
   - Implement fgpartition
   - Test on real batt() execution
   - Measure actual end-to-end speedup

3. **If o_g fails:**
   - Document why GPU doesn't work for ARC
   - Focus on CPU optimizations instead
   - Update strategy documents

---

**Current Status:** 1 operation tested, 0 operations GPU-accelerated

**Confidence in 2x speedup:** 🟡 Medium (60% → 40%)

**Next action:** Implement and test o_g 🔄
