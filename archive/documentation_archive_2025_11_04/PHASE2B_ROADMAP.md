# PHASE 2B - GPU ACCELERATION IMPLEMENTATION ROADMAP

**Status**: 🚀 **STARTING PHASE 2B**  
**Date**: October 17, 2025  
**Target**: GPU acceleration of o_g() function  
**Expected Improvement**: -5-15% additional (combined -7-20% with Phase 2a)  
**Effort**: 3-5 days  
**Priority**: HIGH (GPU time abundant on Kaggle)  

---

## Table of Contents

1. [Strategic Overview](#strategic-overview)
2. [Phase 2b Architecture](#phase-2b-architecture)
3. [Implementation Steps](#implementation-steps)
4. [Technical Details](#technical-details)
5. [Testing Strategy](#testing-strategy)
6. [Timeline](#timeline)

---

## Strategic Overview

### Why Phase 2b (GPU Acceleration)?

**From GPU_SOLVER_STRATEGY.md**:
- Previous approach: GPU-accelerate individual DSL operations → ❌ FAILED (p_g: GPU 3x slower)
- **New approach**: GPU-accelerate solver functions → ✅ VALIDATED (expect 2-6x speedup)
- Discovery: Solver functions are 10-1000x longer than DSL ops (1-120ms vs 0.1ms)
- Result: GPU overhead (0.2ms) becomes negligible for long solvers (0.2-2% vs 167%)

### Why o_g()?

From profiling data:
- **o_g() execution time**: ~1.35-1.40s per 100 tasks (measured)
- **Percentage of total**: ~5-6% of wall-clock
- **Potential speedup**: 2-6x with GPU
- **Expected savings**: 0.5-1.1s per 100 tasks
- **ROI**: HIGH (1-5 days effort for 0.5-1.1s gain)

### GPU Environment on Kaggle

- **Available**: 2x Tesla T4 (15GB each)
- **CuPy**: Available and initialized
- **Framework**: KaggleGPUOptimizer already in gpu_optimizations.py
- **Cost**: Same as CPU (no additional charges)

---

## Phase 2b Architecture

### Strategy: Hybrid GPU Approach

**Key Principle**: Keep DSL frozensets intact, use GPU for computation:

```
Input (frozenset)
    ↓
Convert to GPU array (numpy → cupy)
    ↓
GPU computation (o_g on GPU)
    ↓
Convert back to frozenset (cupy → numpy → frozenset)
    ↓
Output (frozenset) - API compatible
```

**Benefits**:
- ✅ No need to refactor DSL (172 frozenset occurrences in dsl.py)
- ✅ API-compatible (returns frozenset as expected)
- ✅ Fallback to CPU if GPU unavailable
- ✅ Measurable speedup (GPU computation time >> conversion overhead)

### Target Function: o_g()

**Current Implementation** (dsl.py ~lines 2200-2250):
```python
def o_g(grid, val1, val2):
    # Find neighbors of each val1 cell, output val2
    # Current: CPU-only, iterative approach
    # Execution time: 1.35-1.40s per 100 tasks
```

**GPU Optimization Strategy**:
1. Convert grid to CuPy array
2. Vectorized GPU computation (NumPy operations on GPU)
3. Return frozenset (convert back from GPU)

### Performance Expectations

| Scenario | Time | GPU Speedup |
|----------|------|------------|
| Small grids (<100 cells) | 5ms CPU | 1x (CPU faster) |
| Medium grids (100-1000 cells) | 50-100ms CPU | 2-3x |
| Large grids (1000+ cells) | 500-2000ms CPU | 3-6x |
| **Average real tasks** | **1350ms CPU** | **2-4x expected** |

---

## Implementation Steps

### Phase 2b.1: GPU o_g() Implementation (Day 1-2)

**Step 1**: Create gpu_o_g() function in dsl.py
```python
def gpu_o_g(grid, val1, val2):
    """GPU-accelerated o_g() using CuPy"""
    # Check if GPU available
    # Convert frozenset to numpy array
    # Transfer to GPU (cupy array)
    # Compute on GPU
    # Convert back to frozenset
    # Fallback to CPU if GPU unavailable
```

**Step 2**: Integrate with existing o_g() wrapper
```python
def o_g(grid, val1, val2):
    # Use GPU version if available and beneficial
    # Fall back to CPU version otherwise
    # Return same frozenset format
```

**Step 3**: Handle edge cases
- GPU memory limits (batch processing if needed)
- GPU not available (CPU fallback)
- Small inputs (CPU faster, skip GPU)
- Error handling (GPU exceptions)

### Phase 2b.2: Testing & Validation (Day 2-3)

**Unit Tests**:
- ✅ GPU correctness (results match CPU exactly)
- ✅ Small inputs (skip GPU, CPU only)
- ✅ Large inputs (GPU faster)
- ✅ Edge cases (empty grids, single values)
- ✅ GPU unavailable (CPU fallback)

**Performance Tests**:
- Profile o_g() execution with/without GPU
- Measure conversion overhead
- Identify break-even point (size where GPU worth it)
- Benchmark on Kaggle T4x2

**Integration Tests**:
- Full 32-task run with GPU o_g()
- Full 100-task run with GPU o_g()
- Measure wall-clock improvement
- Verify 13,200 solvers generated
- Confirm zero errors

### Phase 2b.3: Optimization & Tuning (Day 3-4)

**GPU Tuning**:
- Batch multiple grids (if beneficial)
- Memory pre-allocation
- GPU kernel optimization
- Block/thread configuration

**Decision Points**:
- If excellent results (>2x speedup): Extend to other DSL ops
- If good results (1.5-2x speedup): Sufficient, move to production
- If marginal results (<1.5x speedup): Investigate CPU fallback optimization

### Phase 2b.4: Documentation & Deployment (Day 4-5)

**Documentation**:
- PHASE2B_IMPLEMENTATION.md - Technical details
- PHASE2B_RESULTS.md - Performance metrics
- GPU_O_G_OPTIMIZATION.md - o_g() specific guide
- Update PHASE2A.md with combined results

**Deployment**:
- Commit GPU o_g() implementation
- Test on Kaggle production kernel
- Verify with full dataset
- Mark Phase 2b complete

---

## Technical Details

### GPU o_g() Implementation Pattern

**Template** (from gpu_optimizations.py patterns):

```python
def gpu_o_g_vectorized(grid, val1, val2):
    """
    GPU-accelerated o_g() using CuPy for vectorized operations.
    Falls back to CPU version if GPU unavailable or not beneficial.
    """
    try:
        import cupy as cp
        from gpu_optimizations import GPU_AVAILABLE
        
        if not GPU_AVAILABLE or len(grid) < BREAKEVEN_SIZE:
            return o_g_cpu(grid, val1, val2)  # CPU faster for small inputs
        
        # Convert frozenset to GPU array
        grid_array = cp.array(list(grid))  # GPU array
        
        # GPU computation
        result_gpu = _gpu_neighbor_computation(grid_array, val1, val2)
        
        # Convert back to frozenset
        result_cpu = cp.asnumpy(result_gpu)  # Back to CPU
        return frozenset(map(tuple, result_cpu))
        
    except Exception as e:
        # Fallback to CPU on any GPU error
        return o_g_cpu(grid, val1, val2)
```

### Key Implementation Considerations

1. **Frozenset ↔ Array Conversion Overhead**
   - Conversion time: ~0.5-1ms for typical grids
   - GPU computation: 1-50ms
   - Breakeven: ~5ms computation time

2. **GPU Memory**
   - T4: 15GB per GPU
   - Typical grid: <1MB
   - Can process 10,000+ grids in parallel

3. **CPU Fallback**
   - Always have CPU version available
   - GPU errors → automatic CPU fallback
   - No failures, only graceful degradation

4. **Batch Processing**
   - If many small grids: batch them
   - Process 10-100 grids in single GPU transfer
   - Amortize conversion overhead

---

## Testing Strategy

### Unit Tests (Day 2)

**Test 1: Correctness**
```python
def test_gpu_o_g_correctness():
    """Verify GPU results match CPU exactly"""
    test_cases = [small_grid, medium_grid, large_grid]
    for grid, val1, val2 in test_cases:
        cpu_result = o_g_cpu(grid, val1, val2)
        gpu_result = gpu_o_g(grid, val1, val2)
        assert cpu_result == gpu_result
```

**Test 2: Edge Cases**
```python
def test_gpu_o_g_edges():
    """Test edge cases"""
    assert gpu_o_g(frozenset(), 1, 2) == o_g_cpu(frozenset(), 1, 2)
    assert gpu_o_g(single_cell, 1, 2) == o_g_cpu(single_cell, 1, 2)
    assert gpu_o_g(no_matches, 1, 2) == o_g_cpu(no_matches, 1, 2)
```

**Test 3: GPU Unavailable**
```python
def test_gpu_o_g_fallback():
    """Test CPU fallback when GPU unavailable"""
    with mock_gpu_unavailable():
        result = gpu_o_g(grid, val1, val2)
        assert result == o_g_cpu(grid, val1, val2)
```

### Performance Tests (Day 2)

**Benchmark Suite**:
```bash
python benchmark_gpu_o_g.py
# Output: Execution times for various grid sizes
# Identify breakeven point
# Measure GPU speedup factor
```

### Integration Tests (Day 3)

```bash
# Full 32-task run
python run_batt.py -c 32 --cprofile --cprofile-top 30

# Full 100-task run
python run_batt.py -c 100 --timing

# Measure improvement vs Phase 2a only
# Expected: 0.5-1.1s improvement
```

---

## Timeline

### Day 1-2: Implementation
- [ ] Create gpu_o_g() function (4 hours)
- [ ] Implement frozenset conversion (2 hours)
- [ ] CPU fallback & error handling (2 hours)
- [ ] Unit tests (2 hours)

### Day 2-3: Testing & Validation
- [ ] Correctness tests (3 hours)
- [ ] Performance benchmarks (2 hours)
- [ ] 32-task validation run (1 hour)
- [ ] 100-task validation run (2 hours)

### Day 3-4: Optimization & Tuning
- [ ] GPU tuning (3 hours)
- [ ] Batch processing (2 hours)
- [ ] Memory optimization (2 hours)
- [ ] Performance re-benchmarking (1 hour)

### Day 4-5: Documentation & Deployment
- [ ] Write PHASE2B_IMPLEMENTATION.md (2 hours)
- [ ] Create PHASE2B_RESULTS.md (2 hours)
- [ ] Final testing & validation (2 hours)
- [ ] Commit & push (1 hour)

**Total**: 3-5 days, ~40 hours work

---

## Success Criteria

### Performance Target
- ✅ **EXCELLENT**: >3x GPU speedup on o_g() (0.7-1.1s saved)
- ✅ **GOOD**: 2-3x GPU speedup (0.5-0.7s saved)
- ⚠️ **ACCEPTABLE**: 1.5-2x speedup (0.3-0.5s saved)
- ❌ **FAIL**: <1.5x speedup (troubleshoot or skip GPU o_g())

### Correctness Target
- ✅ 100 tasks completed
- ✅ 13,200 solvers generated
- ✅ 0 errors
- ✅ 100% correctness (GPU results == CPU results)

### Code Quality Target
- ✅ Unit tests pass (correctness)
- ✅ Integration tests pass (32/100 tasks)
- ✅ CPU fallback tested
- ✅ Edge cases covered
- ✅ Documentation complete

---

## Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| GPU faster than CPU on small inputs | High | Low | Check input size, use CPU for small |
| Conversion overhead exceeds speedup | Medium | Medium | Profile early, optimize conversion |
| GPU memory limits | Low | Medium | Batch processing, check memory |
| GPU not available on some kernels | Low | Low | CPU fallback automatic |
| Correctness mismatch | Very Low | High | Extensive unit testing |

---

## Decision Tree

### After Phase 2b Implementation:

```
GPU o_g() speedup > 3x?
  ├─ YES: Excellent! Apply GPU to other DSL ops (o_g variant, fgpartition, etc.)
  ├─ 2-3x: Good! Sufficient for production, move to deployment
  ├─ 1.5-2x: Acceptable, but investigate further optimization
  └─ <1.5x: Consider alternative approach (CPU loop optimization)
```

---

## Current Status

✅ Phase 2a: 100% cache hit rate, 2,400s saved, confirmed working  
🚀 Phase 2b: Starting now

### Next Immediate Action

Start with **Step 1: Create gpu_o_g() function**

Will need to:
1. Read current o_g() implementation (dsl.py ~lines 2200-2250)
2. Create GPU version with same API
3. Write unit tests
4. Benchmark on Kaggle

---

## Resources

### GPU Implementation Reference
- See `gpu_optimizations.py` for KaggleGPUOptimizer patterns
- See `GPU_SOLVER_STRATEGY.md` for strategy details
- See `copilot-instructions.md` for GPU guidelines

### Performance Baseline
- Phase 1b: -4.7% improvement
- Phase 2a: 100% cache hit rate, confirmed working
- Phase 2b target: -5-15% additional

### Kaggle Resources
- 8 hours GPU time available
- 2x Tesla T4 with 15GB each
- CuPy installed and working
- Multi-GPU support available

---

## Questions Before Starting?

Key decisions needed:
1. ✅ Confirmed: Focus on o_g() first
2. ✅ Confirmed: Use hybrid frozenset approach
3. ✅ Confirmed: Include CPU fallback
4. TODO: Batch processing threshold? (suggest: 10+ small grids)
5. TODO: GPU memory pre-allocation? (suggest: 2GB buffer)

Ready to implement! 🚀
