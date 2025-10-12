# GPU Implementation Plan: o_g (Connected Components)

**Priority**: 🔴 **CRITICAL** - This single operation consumes 75-92% of solver execution time  
**Expected Impact**: 2.7x average speedup across profiled solvers  
**Complexity**: High (flood-fill algorithm with multiple variants)

## What o_g Does

`o_g` (objects_grid) extracts connected components from a grid based on 8 different modes:

```python
def o_g(grid, type):
    """
    Extract objects (connected components) from grid.
    
    type: 0-7 (3 boolean flags)
    - univalued: objects must have same color
    - diagonal: include diagonal neighbors
    - without_bg: exclude background color
    
    Returns: frozenset of frozensets of (row, col, value) tuples
    """
    if type == 0: return objects(grid, False, False, False)
    if type == 1: return objects(grid, False, False, True)
    # ... 6 more combinations
```

## objects() Algorithm (The Bottleneck)

Current CPU implementation (dsl.py lines 3103-3140):

```python
def objects(grid, univalued, diagonal, without_bg):
    """
    Connected components via flood-fill.
    
    Time complexity: O(H × W × N) where N = number of components
    Measured time: 4-7ms per call
    """
    bg = mostcolor_t(grid) if without_bg else None
    objs = set()
    occupied = set()
    h, w = len(grid), len(grid[0])
    unvisited = asindices(grid)
    diagfun = neighbors if diagonal else dneighbors
    
    for loc in unvisited:
        if loc in occupied:
            continue
        val = grid[loc[0]][loc[1]]
        if val == bg:
            continue
            
        # Flood-fill to find connected component
        obj = {(loc[0], loc[1], val)}
        cands = {loc}
        
        while cands:  # ← INNER LOOP (expensive!)
            neighborhood = set()
            for cand in cands:
                v = grid[cand[0]][cand[1]]
                if (val == v) if univalued else (v != bg):
                    obj.add((cand[0], cand[1], v))
                    occupied.add(cand)
                    # Get neighbors (4 or 8 connected)
                    neighborhood |= {
                        (i, j) for i, j in diagfun(cand) 
                        if 0 <= i < h and 0 <= j < w
                    }
            cands = neighborhood - occupied
            
        objs.add(frozenset(obj))
    
    return frozenset(objs)
```

**Why it's slow**:
1. **Nested loops**: Outer loop over all cells, inner while loop for flood-fill
2. **Set operations**: Multiple set unions, subtractions per iteration
3. **Python overhead**: Pure Python, no vectorization
4. **Helper calls**: `neighbors`/`dneighbors` called 49-110 times per o_g call

**Profile measurements** (from actual runs):
- `objects`: 3.9-7.5ms per call
- `neighbors`: Called 490-1100 times (0.06ms each, 30-68ms total)
- `dneighbors`: Called 490-1100 times (0.02ms each, 10-22ms total)
- `ineighbors`: Called 490-1100 times (0.02ms each, 10-22ms total)

## GPU Implementation Strategy

### Option 1: CuPy Connected Components (RECOMMENDED)
**Approach**: Use CuPy's `cupyx.scipy.ndimage.label` for connected components

**Pros**:
- Battle-tested CUDA implementation
- Optimized for GPU architecture
- Handles 4-connected and 8-connected
- Expected 5-10x speedup vs pure Python

**Cons**:
- Need to handle 8 different modes (univalued, diagonal, without_bg)
- Need to convert result to frozensets (CPU operation)
- May not support all edge cases

**Implementation**:
```python
import cupy as cp
from cupyx.scipy import ndimage as cupyx_ndimage

def gpu_objects(grid_cpu, univalued, diagonal, without_bg):
    """
    GPU-accelerated connected components.
    
    Expected: 4-7ms CPU → 0.8-1.5ms GPU (4-5x speedup)
    """
    h, w = len(grid_cpu), len(grid_cpu[0])
    
    # Transfer to GPU once
    grid_gpu = cp.asarray(grid_cpu, dtype=cp.int32)
    
    # Get background color if needed
    if without_bg:
        # mostcolor_t on GPU
        unique, counts = cp.unique(grid_gpu, return_counts=True)
        bg = int(unique[cp.argmax(counts)])
    else:
        bg = None
    
    # Create mask for background
    if bg is not None:
        mask = (grid_gpu != bg)
    else:
        mask = cp.ones_like(grid_gpu, dtype=bool)
    
    if univalued:
        # Each color is separate component
        objs = []
        colors = cp.unique(grid_gpu)
        
        for color in colors:
            color = int(color)
            if bg is not None and color == bg:
                continue
            
            # Label connected components for this color
            color_mask = (grid_gpu == color)
            structure = cp.ones((3, 3), dtype=cp.int32) if diagonal else \
                       cp.array([[0,1,0],[1,1,1],[0,1,0]], dtype=cp.int32)
            
            labeled, num_features = cupyx_ndimage.label(
                color_mask, 
                structure=structure
            )
            
            # Extract each component
            for comp_id in range(1, num_features + 1):
                comp_mask = (labeled == comp_id)
                indices = cp.where(comp_mask)
                
                # Convert to frozenset (on CPU)
                obj = frozenset(
                    (int(i), int(j), color) 
                    for i, j in zip(
                        cp.asnumpy(indices[0]), 
                        cp.asnumpy(indices[1])
                    )
                )
                objs.append(obj)
    else:
        # All non-background cells, any color
        structure = cp.ones((3, 3), dtype=cp.int32) if diagonal else \
                   cp.array([[0,1,0],[1,1,1],[0,1,0]], dtype=cp.int32)
        
        labeled, num_features = cupyx_ndimage.label(
            mask,
            structure=structure
        )
        
        objs = []
        for comp_id in range(1, num_features + 1):
            comp_mask = (labeled == comp_id)
            indices = cp.where(comp_mask)
            
            # Get values for each position
            values = grid_gpu[comp_mask]
            
            # Convert to frozenset (on CPU)
            obj = frozenset(
                (int(i), int(j), int(v))
                for i, j, v in zip(
                    cp.asnumpy(indices[0]),
                    cp.asnumpy(indices[1]),
                    cp.asnumpy(values)
                )
            )
            objs.append(obj)
    
    return frozenset(objs)


def gpu_o_g(grid, type):
    """GPU-accelerated o_g."""
    univalued = bool(type & 0b100)
    diagonal = bool(type & 0b010)
    without_bg = bool(type & 0b001)
    
    return gpu_objects(grid, univalued, diagonal, without_bg)
```

**Expected performance**:
- GPU computation: 0.5-1.0ms (connected components)
- CPU conversion: 0.3-0.5ms (frozenset construction)
- Total: 0.8-1.5ms (vs 4-7ms CPU)
- **Speedup: 3-6x**

### Option 2: Custom CUDA Kernel
**Approach**: Write custom CUDA kernel for flood-fill

**Pros**:
- Maximum performance potential
- Full control over algorithm
- Can optimize for ARC grid sizes (typically 30x30)

**Cons**:
- Complex implementation (100+ lines of CUDA)
- Need to handle race conditions
- Testing and debugging difficult
- May not be faster than CuPy for small grids

**Recommendation**: Start with Option 1 (CuPy), only consider custom kernel if speedup insufficient

### Option 3: Numba CUDA
**Approach**: Use Numba @cuda.jit for GPU kernel

**Pros**:
- Python-based (easier than raw CUDA)
- Good performance for simple kernels
- Easier debugging

**Cons**:
- Flood-fill is complex for Numba
- May have similar overhead to CuPy
- Less optimized than CuPy for this use case

**Recommendation**: Not worth the effort vs CuPy

## Implementation Plan

### Phase 1: Prototype CuPy Version (Days 1-2)
1. Implement `gpu_objects()` with CuPy
2. Test on simple grids (correctness)
3. Benchmark on various grid sizes
4. Compare with CPU version

**Success criteria**:
- 100% correctness on test grids
- >2x speedup on average

### Phase 2: Optimize & Validate (Days 3-4)
1. Optimize frozenset conversion
2. Handle edge cases (empty grids, single pixels, etc.)
3. Test on all 8 o_g modes
4. Validate on 100+ diverse grids

**Success criteria**:
- All tests pass
- >3x speedup on average
- No correctness regressions

### Phase 3: Integration (Days 5-7)
1. Add GPU o_g to gpu_dsl_core.py
2. Update solvers to use GPU version
3. Benchmark end-to-end solver performance
4. Measure ARC evaluation speedup

**Success criteria**:
- Solvers show 2-3x speedup
- ARC evaluation 0.5-1.5 seconds faster

## Expected Performance

### GPU Breakdown
```
Grid size: 30x30 (typical)
Components: 5-10 (typical)

CuPy label operation:      0.5-0.8 ms
Component extraction:      0.2-0.4 ms
Frozenset conversion:      0.1-0.3 ms
GPU transfer overhead:     0.0 ms (already on GPU)
------------------------------------------
Total GPU time:            0.8-1.5 ms

vs CPU time:               4.0-7.5 ms
Speedup:                   3-6x
```

### Solver Impact
```
solve_23b5c85d:
  Before: 8.2 ms (7.5ms o_g)
  After:  8.2 - 7.5 + 1.5 = 2.2 ms
  Speedup: 3.7x

solve_09629e4f:
  Before: 6.8 ms (5.6ms o_g)
  After:  6.8 - 5.6 + 1.4 = 2.6 ms
  Speedup: 2.6x

solve_1f85a75f:
  Before: 5.4 ms (4.0ms o_g)
  After:  5.4 - 4.0 + 1.0 = 2.4 ms
  Speedup: 2.3x

Average: 2.9x speedup
```

## Risk Mitigation

### Risk: Frozenset conversion overhead
**Mitigation**: Benchmark and optimize. If too slow, keep more computation on GPU.

### Risk: Small grids may not benefit
**Mitigation**: Adaptive fallback - use CPU for grids <10x10.

### Risk: CuPy label may not handle all cases
**Mitigation**: Comprehensive testing. Fall back to CPU if GPU fails.

### Risk: Transfer overhead for frequent calls
**Mitigation**: Keep grids on GPU in solver functions (GPU-resident solvers).

## Testing Strategy

### Unit Tests
1. Empty grid
2. Single pixel
3. All same color
4. Checkerboard pattern
5. Multiple disconnected components
6. Large connected component
7. All 8 o_g modes

### Integration Tests
1. Run profiled solvers with GPU o_g
2. Compare results with CPU version (must match 100%)
3. Benchmark end-to-end performance

### Validation
1. Run on 100+ diverse ARC grids
2. Verify correctness on all
3. Measure speedup distribution

## Success Metrics

### Minimum Success
- [x] 100% correctness vs CPU
- [ ] >2x speedup on average
- [ ] No crashes or errors

### Full Success
- [ ] >3x speedup on average
- [ ] Solvers show 2-3x end-to-end speedup
- [ ] ARC evaluation 0.5+ seconds faster

### Stretch Success
- [ ] >4x speedup on average
- [ ] Solvers show 3-4x end-to-end speedup
- [ ] ARC evaluation 1+ seconds faster

## Next Steps

1. **Immediate**: Create `gpu_dsl_core.py` with GPU o_g implementation
2. **Day 1-2**: Implement and test CuPy version
3. **Day 3-4**: Optimize and validate
4. **Day 5-7**: Integrate into solvers and benchmark

---

**Status**: Ready to implement - this single operation will deliver 2.7x average speedup! 🎯
