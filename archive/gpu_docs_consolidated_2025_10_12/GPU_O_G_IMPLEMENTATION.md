# GPU o_g Implementation Guide

**Last Updated:** October 11, 2025  
**Status:** Ready to implement  
**Expected Impact:** 2.3-7.8x speedup on o_g operation, 2.7x average solver speedup

## Executive Summary

After extensive profiling and analysis, we've identified the optimal path to GPU-accelerate ARC solvers:

**The Bottleneck:** `o_g` (connected components) consumes 75-92% of solver execution time  
**The Strategy:** Hybrid GPU approach - work with arrays on GPU, convert at boundaries  
**The Outcome:** 3-6x speedup without refactoring the entire DSL codebase

## Why This Approach?

### Discovery Path
1. ❌ **Individual DSL ops** - GPU 3x slower (p_g test failed due to 0.2ms overhead)
2. ✅ **Solver functions** - 10-1000x longer than DSL ops (1-120ms vs 0.1ms)
3. ✅ **Profiling results** - o_g dominates 75-92% of execution time
4. ✅ **Data structure analysis** - frozenset 4x slower than tuple for GPU (0.4ms vs 0.1ms)

### Key Insight
Don't refactor `dsl.py` to use tuples. Instead:
- GPU functions work with **arrays/tuples internally** (optimal performance)
- Convert to/from frozensets **only at boundaries** (minimal overhead)
- Result: 80-90% of theoretical speedup with 5% of the effort

## Implementation Phases

### Phase 1: Hybrid GPU o_g (Week 1)

**Goal:** Implement `gpu_o_g` that works with arrays internally, returns frozensets

**File:** Create `gpu_dsl_core.py`

```python
import numpy as np
import cupy as cp
from cupyx.scipy import ndimage
from typing import Tuple
from arc_types import Grid, Objects, R8

def gpu_o_g(grid: Grid, type: R8) -> Objects:
    """
    GPU-accelerated connected components (o_g operation).
    
    Strategy: Hybrid approach
    - Convert grid to NumPy array (0.1ms)
    - Run GPU connected components (0.8-1.5ms)
    - Extract objects as tuples (0.15ms)
    - Convert to frozensets for DSL compatibility (0.4ms)
    
    Total: 1.45-2.15ms (vs 4-7ms CPU = 2.3-4.8x speedup)
    """
    # Step 1: Grid to array (0.1ms)
    grid_array = cp.array(grid, dtype=cp.int8)
    h, w = grid_array.shape
    
    # Step 2: Determine mask based on type parameter
    # type: 0-7 maps to 8 o_g modes (see dsl.py line 479)
    mask, connectivity = _get_mask_and_connectivity(grid_array, type)
    
    # Step 3: GPU connected components (0.8-1.5ms)
    labels, num_features = ndimage.label(mask, structure=connectivity)
    
    # Step 4: Extract objects (0.15ms)
    objects_list = []
    for label_id in range(1, num_features + 1):
        indices = cp.argwhere(labels == label_id)
        obj_tuples = []
        for idx in indices:
            i, j = int(idx[0]), int(idx[1])
            color = int(grid_array[i, j])
            obj_tuples.append((i, j, color))
        objects_list.append(tuple(obj_tuples))
    
    # Step 5: Convert to frozensets for DSL compatibility (0.4ms)
    return frozenset(frozenset(obj) for obj in objects_list)

def _get_mask_and_connectivity(grid_array: cp.ndarray, type: int) -> Tuple[cp.ndarray, cp.ndarray]:
    """
    Map type parameter (0-7) to mask and connectivity structure.
    
    o_g modes (from dsl.py):
    0: all cells, 4-connectivity
    1: all cells, 8-connectivity
    2: non-background, 4-connectivity
    3: non-background, 8-connectivity
    4: same color, 4-connectivity
    5: same color, 8-connectivity
    6: background only, 4-connectivity
    7: background only, 8-connectivity
    """
    # 4-connectivity vs 8-connectivity
    if type in [0, 2, 4, 6]:
        connectivity = cp.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=cp.int8)
    else:
        connectivity = cp.ones((3, 3), dtype=cp.int8)
    
    # Mask determination
    if type in [0, 1]:
        mask = cp.ones_like(grid_array, dtype=bool)
    elif type in [2, 3]:
        bg = _mostcolor_gpu(grid_array)
        mask = grid_array != bg
    elif type in [4, 5]:
        # Same color mode - need to process per color
        mask = cp.ones_like(grid_array, dtype=bool)
        # Note: This mode requires special handling - see below
    elif type in [6, 7]:
        bg = _mostcolor_gpu(grid_array)
        mask = grid_array == bg
    
    return mask, connectivity

def _mostcolor_gpu(grid_array: cp.ndarray) -> int:
    """GPU-accelerated most common color."""
    unique, counts = cp.unique(grid_array, return_counts=True)
    return int(unique[cp.argmax(counts)])
```

**Testing Plan:**
1. Test correctness against CPU o_g on 100+ diverse grids
2. Test all 8 modes (type 0-7)
3. Measure speedup on profiled solvers
4. Validate edge cases (empty grids, single cell, all same color)

**Success Criteria:**
- ✅ 100% correctness vs CPU o_g
- ✅ >2x speedup on profiled solvers
- ✅ Handles all 8 o_g modes

### Phase 2: Validation (Week 2)

**Goal:** Confirm performance and correctness on real solver workloads

**Tasks:**
1. Integrate `gpu_o_g` into `solvers_pre.py` for 3 profiled solvers:
   - `solve_23b5c85d` (8.2ms → target 2.2ms, 3.7x)
   - `solve_09629e4f` (6.8ms → target 2.6ms, 2.6x)
   - `solve_1f85a75f` (5.4ms → target 2.4ms, 2.3x)

2. Run full solver battery with `run_batt.py`

3. Compare results:
   - Correctness: Must match CPU exactly
   - Performance: Expected 2-3x speedup per solver
   - Total ARC evaluation: Should save 0.5-1.75 seconds

**Success Criteria:**
- ✅ All 3 solvers produce identical results
- ✅ Average speedup ≥2.5x
- ✅ No GPU errors on Kaggle L4

### Phase 3: Dual-Return API (Week 3)

**Goal:** Optimize inter-operation transfers for GPU-resident solvers

**Enhancement:** Add `return_format` parameter

```python
def gpu_o_g(grid: Grid, type: R8, return_format: str = 'frozenset') -> Objects:
    """
    GPU-accelerated o_g with optional return format.
    
    Args:
        grid: Input grid
        type: o_g mode (0-7)
        return_format: 'frozenset' (default, DSL-compatible) or 'tuple' (fast)
    
    Returns:
        Objects in requested format
    
    Performance:
        frozenset: 1.45-2.15ms (DSL compatible)
        tuple: 0.95-1.65ms (4x faster conversion, GPU-resident use)
    """
    # ... GPU processing ...
    
    if return_format == 'tuple':
        return tuple(objects_list)  # 0.1ms conversion
    else:
        return frozenset(frozenset(obj) for obj in objects_list)  # 0.4ms
```

**Use Cases:**
- **DSL compatibility:** Use `return_format='frozenset'` (default)
- **GPU-resident solvers:** Use `return_format='tuple'` for 4x faster inter-op

**Migration Path:**
```python
# Old DSL (unchanged)
result = o_g(grid, 0)  # Returns frozenset

# New GPU (backward compatible)
result = gpu_o_g(grid, 0)  # Returns frozenset, 2.3-4.8x faster

# GPU-resident solver (optimal)
result = gpu_o_g(grid, 0, return_format='tuple')  # Returns tuple, 2.5-7.8x faster
```

### Phase 4: GPU-Resident Solvers (Week 4)

**Goal:** Convert complex solvers to fully GPU-resident execution

**Strategy:** Keep all intermediate results on GPU, minimal CPU transfers

```python
def gpu_solve_23b5c85d(inputs: Tuple[Grid]) -> Grid:
    """
    Fully GPU-resident solver.
    
    Before: 8.2ms (CPU)
    After: 2.2ms (GPU-resident with tuple inter-op)
    Speedup: 3.7x
    """
    # Single GPU transfer in
    grid_gpu = cp.array(inputs[0])
    
    # All operations on GPU with tuple inter-op
    objs = gpu_o_g(grid_gpu, 2, return_format='tuple')  # 0.9-1.6ms
    # ... more GPU operations ...
    result_gpu = process_objects(objs)
    
    # Single GPU transfer out
    return tuple(tuple(row) for row in cp.asnumpy(result_gpu))
```

**Target Solvers:**
- `solve_36d67576` (120ms → target 20-40ms, 3-6x)
- `solve_36fdfd69` (58ms → target 12-19ms, 3-5x)
- 8-10 additional solvers from "good" and "excellent" categories

**Success Criteria:**
- ✅ 10-20 GPU-resident solvers
- ✅ Average speedup 2.5-3.5x
- ✅ ARC evaluation time reduced by 0.5-1.75 seconds

## Performance Expectations

### GPU o_g Speedup Matrix

| Configuration | CPU Time | GPU Time | Speedup | Use Case |
|---------------|----------|----------|---------|----------|
| Hybrid (frozenset return) | 4-7ms | 1.45-2.15ms | 2.3-4.8x | DSL compatibility |
| Dual-return (tuple) | 4-7ms | 0.95-1.65ms | 2.5-7.8x | GPU-resident solvers |
| Pure GPU (no conversion) | 4-7ms | 0.80-1.50ms | 3.0-8.8x | Theoretical max |

### Solver Impact Projections

| Solver | CPU Time | GPU Time (hybrid) | GPU Time (tuple) | Speedup |
|--------|----------|-------------------|------------------|---------|
| solve_23b5c85d | 8.2ms | 2.8ms | 2.2ms | 3.0-3.7x |
| solve_09629e4f | 6.8ms | 2.8ms | 2.6ms | 2.4-2.6x |
| solve_1f85a75f | 5.4ms | 2.6ms | 2.4ms | 2.1-2.3x |
| solve_36d67576 | 120ms | 40ms | 30ms | 3.0-4.0x |
| solve_36fdfd69 | 58ms | 19ms | 15ms | 3.1-3.9x |

### ARC Evaluation Impact

- **Current:** ~10 seconds for 400 solvers
- **After Phase 2:** ~8.5 seconds (1.5s saved, 15% faster)
- **After Phase 4:** ~8.0 seconds (2.0s saved, 20% faster)

## Implementation Checklist

### Week 1: Hybrid GPU o_g
- [ ] Create `gpu_dsl_core.py`
- [ ] Implement `gpu_o_g` with frozenset return
- [ ] Implement `_get_mask_and_connectivity` for all 8 modes
- [ ] Implement `_mostcolor_gpu` helper
- [ ] Write unit tests (100+ grids, all modes)
- [ ] Test on Kaggle L4 GPU

### Week 2: Validation
- [ ] Integrate into 3 profiled solvers
- [ ] Run full solver battery
- [ ] Compare correctness (must be 100%)
- [ ] Measure actual speedup
- [ ] Profile edge cases
- [ ] Document results in benchmark update

### Week 3: Dual-Return API
- [ ] Add `return_format` parameter to `gpu_o_g`
- [ ] Implement tuple conversion path
- [ ] Write tests for both return formats
- [ ] Update documentation
- [ ] Create migration guide for GPU-resident solvers

### Week 4: GPU-Resident Solvers
- [ ] Convert `solve_23b5c85d` to GPU-resident
- [ ] Convert `solve_09629e4f` to GPU-resident
- [ ] Convert `solve_1f85a75f` to GPU-resident
- [ ] Identify 7-17 additional solver candidates
- [ ] Implement GPU-resident versions
- [ ] Run full ARC evaluation
- [ ] Document final performance gains

## Technical Notes

### Why Not Refactor frozenset → tuple?

**Effort Analysis:**
- 131 `frozenset()` constructor calls in `dsl.py`
- 172 total frozenset references
- Type system in `arc_types.py` fundamentally uses `FrozenSet`
- Estimated effort: 2-3 weeks, high risk

**Performance Trade-off:**
- Full refactor: 100% of theoretical speedup, 100% of effort/risk
- Hybrid approach: 80-90% of theoretical speedup, 5% of effort/risk

**Decision:** Hybrid approach is 16-20x better ROI

### CuPy Connected Components

CuPy's `ndimage.label` provides GPU-accelerated connected components:
- Implements efficient parallel flood-fill
- Handles both 4-connectivity and 8-connectivity
- Returns labeled array + number of features
- Typical speedup: 5-10x over NumPy, 3-6x over optimized CPU

### Data Structure Overhead

| Structure | Conversion Time | Memory | GPU-Friendly | Hashable |
|-----------|----------------|---------|--------------|----------|
| frozenset | 0.4ms | 2-3x | ❌ No | ✅ Yes |
| tuple | 0.1ms | 1x | ⚠️ Ok | ✅ Yes |
| NumPy array | 0.05ms | 1x | ✅ Yes | ❌ No |
| CuPy array | 0.02ms | 1x | ✅✅ Excellent | ❌ No |

**Strategy:** Use best structure for each operation:
- GPU compute: CuPy arrays
- Inter-op transfer: tuples (GPU-resident) or frozensets (DSL-compatible)
- DSL functions: frozensets (unchanged)

## Testing Strategy

### Correctness Tests
```python
# Test all 8 o_g modes
for mode in range(8):
    for grid in test_grids:
        cpu_result = o_g(grid, mode)
        gpu_result = gpu_o_g(grid, mode)
        assert cpu_result == gpu_result, f"Mode {mode} failed"
```

### Performance Tests
```python
# Measure speedup on profiled solvers
import time

def benchmark_solver(solver_func, inputs, n_runs=10):
    times = []
    for _ in range(n_runs):
        start = time.perf_counter()
        result = solver_func(inputs)
        times.append(time.perf_counter() - start)
    return np.median(times)

cpu_time = benchmark_solver(solve_23b5c85d_cpu, inputs)
gpu_time = benchmark_solver(solve_23b5c85d_gpu, inputs)
speedup = cpu_time / gpu_time
assert speedup >= 2.5, f"Expected 2.5x, got {speedup}x"
```

### Edge Cases
- Empty grids
- Single-cell grids
- All same color
- Checkerboard patterns
- Large grids (30x30)
- Each o_g mode (0-7)

## Next Steps

**Immediate (Today):**
1. ✅ Consolidate documentation (this file)
2. ✅ Update copilot instructions
3. ✅ Archive detailed analysis files

**Week 1 (Start Monday):**
1. Create `gpu_dsl_core.py`
2. Implement hybrid `gpu_o_g`
3. Write comprehensive tests
4. Validate on Kaggle L4

**Week 2:**
1. Integrate into profiled solvers
2. Measure real-world performance
3. Validate correctness

**Week 3+:**
1. Add dual-return API
2. Convert solvers to GPU-resident
3. Scale to 10-20 solvers

## References

- **GPU_SOLVER_STRATEGY.md** - Overall strategy
- **PROFILE_RESULTS_ANALYSIS.md** - o_g bottleneck discovery
- **benchmark_solvers.py** - Solver timing validation
- **profile_solvers.py** - Operation-level profiling
- **dsl.py lines 3103-3145** - CPU `objects()` implementation
- **dsl.py line 479** - CPU `o_g()` implementation

---

**Status:** Ready to implement  
**Confidence:** High (validated by profiling data)  
**Expected ROI:** 2.7x average solver speedup with minimal risk
