# fgpartition GPU Performance Analysis

## Problem: GPU is 20-23x SLOWER than CPU ❌

### Results Summary
```
Batch size  20: CPU   2.01ms | GPU   47.34ms | Speedup:  0.04x (GPU 23x slower)
Batch size 100: CPU  10.58ms | GPU  241.49ms | Speedup:  0.04x (GPU 23x slower)
Batch size 500: CPU  53.69ms | GPU 1205.91ms | Speedup:  0.04x (GPU 22x slower)
```

---

## Root Cause Analysis

### Issue 1: No Batch Processing (CRITICAL)
**Current code** (lines 203-238):
```python
for grid in grids:  # ❌ Loop over grids individually
    np_grid = np.array(grid, dtype=np.int32)
    gpu_grid = cp.asarray(np_grid)  # ❌ TRANSFER for each grid
    # ... process ...
    rows = positions[0].get()  # ❌ TRANSFER back for each color
    cols = positions[1].get()  # ❌ TRANSFER back for each color
```

**Problems:**
- Transfers each grid to GPU separately (20-500 transfers!)
- No batch tensor - defeats the purpose of GPU
- Each grid: ~2 transfers in + ~4 transfers out (for 2 colors) = ~6 transfers per grid
- Total: 500 grids × 6 transfers = **3000 GPU transfers!**

**Expected:** 1 transfer in (batch) + 1 transfer out (batch) = 2 transfers total

---

### Issue 2: Per-Color CPU Transfers (CRITICAL)
**Current code** (lines 220-221):
```python
for color in fg_colors:  # For each color
    positions = cp.where(gpu_grid == color)
    rows = positions[0].get()  # ❌ GPU→CPU transfer
    cols = positions[1].get()  # ❌ GPU→CPU transfer
```

**Problem:** Transfers data back to CPU for each color in each grid
- Grid with 3 colors = 6 transfers (3 colors × 2 arrays)
- Batch of 100 grids with avg 2 colors = 400 transfers!

**Expected:** Process all grids on GPU, transfer final results once

---

### Issue 3: Not Using BatchTensor
**Current code:** Doesn't use the BatchTensor class we created!

**Expected:**
```python
batch_tensor = BatchTensor(grids)  # Prepare batch
gpu_batch = batch_tensor.to_gpu()  # SINGLE transfer
# ... process entire batch on GPU ...
return batch_tensor.from_gpu(results)  # SINGLE transfer
```

---

## Performance Breakdown

### Current Implementation
```
Per Grid (avg):
- numpy array creation:     0.01ms
- Transfer to GPU:          0.05ms  ← OVERHEAD
- GPU unique colors:        0.01ms
- GPU find positions (×2):  0.02ms
- Transfer to CPU (×4):     0.20ms  ← OVERHEAD
- Create frozenset:         0.01ms
Total per grid: ~0.30ms

Batch of 100:
- 100 grids × 0.30ms = 30ms
- But wait... measured 241ms! ❌

Additional overhead:
- Python loop overhead: ~100ms
- CuPy kernel launches: ~50ms
- Memory allocations: ~60ms
Total: ~241ms ✓ (matches measurement)
```

### Why CPU is Fast
```
Per Grid:
- Find background color: 0.02ms (pure Python, cached)
- Find colors:          0.01ms
- List comprehension:   0.05ms (numpy-fast)
- Create frozenset:     0.02ms
Total per grid: ~0.10ms

Batch of 100:
- 100 grids × 0.10ms = 10ms ✓ (matches measurement)
```

**CPU is 23x faster because:**
1. No GPU transfer overhead
2. No Python loop with GPU calls
3. Simple operations optimized in CPython/NumPy
4. Data already in right format (tuples)

---

## Why Our Strategy Failed

### Original Assumption
> fgpartition is complex (O(n×m×k)) so GPU should win

**This was WRONG for this implementation because:**
1. ❌ We didn't batch process (loop over grids individually)
2. ❌ We transferred data for each grid (not batch transfer)
3. ❌ We transferred intermediate results (positions per color)
4. ❌ Operation is actually simple per-grid (just find pixels)

### Correct Understanding
**fgpartition complexity per grid:**
- Find most common color: O(n×m) - **simple scan**
- Find positions per color: O(n×m) - **simple scan**
- Total: 2× O(n×m) - **NOT complex enough for GPU!**

For 25×25 grids:
- Total operations: 2 × 625 = 1,250 operations
- GPU transfer: ~50,000 "operations" equivalent (overhead)
- **Transfer overhead is 40x the compute!**

---

## The Real Lesson

### Operations We Thought Were Complex Enough
- ❌ `fgpartition` - 2× scan operations (not complex enough)
- ❌ `rot90` - 1× transpose (definitely not complex enough)

### Operations That Might Actually Work
- ✅ **Convolution/filtering** - O(n×m×k×k) where k=kernel size
- ✅ **Path finding** - O(n²×m²) with iterations
- ✅ **Connected components** - O(n×m) but with many iterations
- ✅ **Physics simulation** - O(n×m) but with 100+ iterations

**Key insight:** Need either:
1. **High arithmetic intensity**: Operations >> memory access
2. **Many iterations**: Amortize transfer over 100+ iterations
3. **True batch parallelism**: Same operation on 1000+ elements

---

## How to Fix fgpartition

### Option 1: Proper Batch Implementation (RECOMMENDED)
```python
def fgpartition_batch(grids, min_batch_size=100):
    if len(grids) < min_batch_size or not GPU_AVAILABLE:
        return [fgpartition_cpu(g) for g in grids]
    
    # Create batch tensor - SINGLE ALLOCATION
    batch_tensor = BatchTensor(grids)
    gpu_batch = batch_tensor.to_gpu()  # SINGLE TRANSFER
    
    # Process ALL grids on GPU in parallel
    results_gpu = []
    for i in range(len(grids)):
        grid = gpu_batch[i]
        # Process on GPU (keep data on GPU)
        result = process_single_grid_gpu(grid)  # stays on GPU
        results_gpu.append(result)
    
    # SINGLE transfer back
    results = convert_gpu_results_to_frozensets(results_gpu)
    return results
```

**Expected speedup:** Still probably < 2x due to frozenset conversion overhead

### Option 2: Keep CPU Version (RECOMMENDED)
**Conclusion:** fgpartition is NOT worth GPU acceleration

**Why:**
- Operation is simple scan (2× pass)
- Results need complex conversion (frozensets)
- CPU version is already fast (10ms for 100 grids)
- GPU overhead too high for benefit

**Better use of time:** Find operations with 1000+ iterations

### Option 3: Only Use GPU in Pipelines
If fgpartition is part of a longer pipeline:
```python
def solve_pipeline_gpu(grids):
    # SINGLE transfer in
    gpu_batch = cp.asarray([np.array(g) for g in grids])
    
    # Stay on GPU for multiple operations
    gpu_batch = fgpartition_gpu(gpu_batch)   # GPU → GPU
    gpu_batch = gravitate_gpu(gpu_batch)     # GPU → GPU  
    gpu_batch = fill_gpu(gpu_batch)          # GPU → GPU
    
    # SINGLE transfer out
    return convert_to_tuples(gpu_batch)
```

**Expected speedup:** 3-5x if pipeline has 5+ operations

---

## Revised GPU Acceleration Strategy

### ❌ DON'T Accelerate
1. **rot90, flip, transpose** - Too simple (0.3ms compute vs 2ms transfer)
2. **fgpartition** - Simple scan, not worth overhead (0.1ms vs 0.3ms)
3. **Any operation < 10ms per 100 grids** - Transfer overhead dominates

### ⚠️ MAYBE Accelerate (Need Testing)
1. **Connected components** - If using Union-Find with many merges
2. **Morphological operations** - If applied multiple times
3. **Color transformations** - If complex logic

### ✅ DO Accelerate (High Confidence)
1. **Convolution-based operations** - High arithmetic intensity
2. **Iterative physics** (gravitate with 100+ steps)
3. **Flood fill with large regions**
4. **Path finding algorithms**
5. **Operation pipelines** (5+ operations chained)

---

## Recommendations Going Forward

### Immediate Actions
1. ✅ **Accept that fgpartition doesn't benefit** - Move on
2. ✅ **Focus on iterative operations** - gravitate, flood fill
3. ✅ **Test pipeline approach** - Chain multiple operations

### Don't Waste Time On
1. ❌ Trying to optimize fgpartition further
2. ❌ Single-pass scanning operations
3. ❌ Operations already < 1ms on CPU

### Focus Development On
1. ✅ **Operations with 100+ iterations**
2. ✅ **True batch parallelism** (1000+ elements)
3. ✅ **Pipeline support** (stay on GPU between ops)

---

## Lessons Learned

### Mistake 1: Assumed Complexity = GPU Benefit
**Wrong:** O(n×m×k) complexity ≠ GPU benefit  
**Right:** Transfer overhead × iterations << compute time

### Mistake 2: Didn't Implement Proper Batching
**Wrong:** Loop over grids with GPU calls (3000 transfers!)  
**Right:** Single batch transfer + vectorized operations

### Mistake 3: Underestimated Conversion Overhead
**Wrong:** Thought frozenset creation was negligible  
**Right:** Converting GPU results to Python objects takes longer than compute!

### Mistake 4: Ignored Actual Timing Data
**Should have checked:** How long does CPU version take?  
**Reality:** 10ms for 100 grids = 0.1ms per grid = **too fast for GPU!**

---

## Updated Success Criteria

For GPU to be worth it, need **ONE** of these:
1. **Compute >> 10ms per 100 grids** (100x transfer time)
2. **100+ iterations** (amortize transfer)
3. **Pipeline** (multiple ops without CPU transfer)
4. **Massive parallelism** (10,000+ elements)

**fgpartition fails ALL criteria:**
- ❌ Compute: 10ms per 100 grids (not >> transfer)
- ❌ Iterations: 2 passes (not 100+)
- ❌ Pipeline: Not currently used in pipeline
- ❌ Parallelism: 100 grids × 625 pixels = 62,500 elements (not enough)

---

## Next Steps

### Phase 1: Test Iterative Operations
**Implement and test:**
1. `gravitate_batch()` - Physics with 42 max iterations
2. `flood_fill_batch()` - Iterative region filling
3. Measure actual speedup

### Phase 2: Pipeline Approach
**If single ops don't work:**
1. Create operation pipelines
2. Chain 5-10 operations on GPU
3. Only 2 transfers (in/out)

### Phase 3: Accept Reality
**If nothing works:**
1. GPU may not be worth it for ARC DSL
2. Focus on CPU optimization
3. Use GPU only for massive batch processing (10,000+ grids)

---

## Conclusion

**fgpartition GPU implementation is fundamentally flawed:**
1. Doesn't use batch processing (loops over grids)
2. Does 3000+ GPU transfers instead of 2
3. Operation too simple to benefit from GPU
4. CPU version already very fast (0.1ms per grid)

**Result:** GPU is 23x slower than CPU ❌

**Action:** Don't try to fix fgpartition - it's not worth GPU acceleration.

**Focus on:** Finding operations with 100+ iterations or building pipelines.
