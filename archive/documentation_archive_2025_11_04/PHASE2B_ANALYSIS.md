# PHASE 2B - GPU objects() Implementation

**Status**: 🚀 **STARTING IMPLEMENTATION**  
**Target**: GPU-accelerate objects() and objects_t() functions  
**Expected**: 2-6x speedup on large grids  
**Strategy**: Hybrid approach (GPU computation, frozenset API)

---

## Current Bottleneck Analysis

### objects() Function (dsl.py lines 3117-3167)

```python
def objects(grid, univalued, diagonal, without_bg):
    # Current implementation:
    # 1. Iterative neighbor discovery (CPU-based BFS)
    # 2. Set operations for occupied/neighborhood tracking
    # 3. Frozenset wrapping for return value
    # 
    # Execution time: ~1.35-1.40s per 100 tasks
    # Percentage of wall-clock: ~5-6%
    # GPU speedup potential: 2-6x
```

### Why GPU Helps

1. **Grid lookup**: `grid[i][j]` operations are highly parallelizable
2. **Neighborhood discovery**: Neighbor iteration can be vectorized
3. **Set operations**: Can be converted to array operations
4. **Large grids**: 1000+ cell grids benefit most (GPU overhead justified)

### GPU Strategy

```
Input: grid (frozenset of tuples), params
  ↓
Convert: frozenset → numpy array
  ↓
Transfer: numpy → cupy (GPU)
  ↓
Compute: GPU vectorized neighbor discovery
  ↓
Convert: cupy → numpy
  ↓
Convert: numpy → frozenset
  ↓
Output: frozenset (identical to CPU version)
```

---

## Implementation Plan

### Step 1: Create GPU Helper Functions

Add to dsl.py (after imports, before o_g definition):

```python
# GPU-accelerated objects() using CuPy
GPU_OBJECTS_AVAILABLE = False
try:
    import cupy as cp
    from gpu_optimizations import GPU_AVAILABLE
    GPU_OBJECTS_AVAILABLE = GPU_AVAILABLE
except ImportError:
    GPU_AVAILABLE = False
    GPU_OBJECTS_AVAILABLE = False


def _grid_to_array(grid):
    """Convert grid tuple structure to 2D numpy array"""
    if not grid:
        return None
    return np.array(grid, dtype=np.int8)


def _array_to_grid(array):
    """Convert numpy array back to grid tuple structure"""
    return tuple(tuple(row) for row in array)


def _frozenset_to_indices(fs):
    """Convert frozenset of tuples to 2D indices"""
    if not fs:
        return np.array([], dtype=np.int32).reshape(0, 2)
    return np.array(list(fs), dtype=np.int32)


def _indices_to_frozenset(indices):
    """Convert 2D indices back to frozenset of tuples"""
    if len(indices) == 0:
        return frozenset()
    return frozenset(map(tuple, indices))
```

### Step 2: GPU objects() Implementation

Add to dsl.py (after helper functions):

```python
def objects_gpu(
    grid: 'Grid',
    univalued: 'Boolean',
    diagonal: 'Boolean',
    without_bg: 'Boolean'
) -> 'Objects':
    """
    GPU-accelerated objects() using CuPy for vectorized operations.
    Falls back to CPU version if GPU unavailable or input too small.
    """
    try:
        if not GPU_OBJECTS_AVAILABLE:
            return objects(grid, univalued, diagonal, without_bg)
        
        import cupy as cp
        
        # Check if input is large enough to benefit from GPU
        grid_size = len(grid) * len(grid[0]) if grid and grid[0] else 0
        if grid_size < 100:  # Breakeven: small grids faster on CPU
            return objects(grid, univalued, diagonal, without_bg)
        
        # Convert grid to GPU array
        grid_array = cp.array(grid, dtype=cp.int8)
        h, w = grid_array.shape
        
        # Get background color if needed
        if without_bg:
            bg = cp.asarray(mostcolor_t(grid))
        else:
            bg = None
        
        # Pre-compute offset arrays
        if diagonal:
            offsets_gpu = cp.array([(-1, 0), (1, 0), (0, -1), (0, 1), 
                                     (-1, -1), (-1, 1), (1, -1), (1, 1)], dtype=cp.int32)
        else:
            offsets_gpu = cp.array([(-1, 0), (1, 0), (0, -1), (0, 1)], dtype=cp.int32)
        
        # GPU computation: vectorized neighbor discovery
        # This is the main speedup area
        objs = _gpu_compute_objects(grid_array, offsets_gpu, univalued, without_bg, bg, h, w)
        
        return objs
        
    except Exception as e:
        # Fallback to CPU on any GPU error
        return objects(grid, univalued, diagonal, without_bg)


def _gpu_compute_objects(grid_array, offsets, univalued, without_bg, bg, h, w):
    """Core GPU computation for objects()"""
    import cupy as cp
    
    objs = []
    occupied = set()
    unvisited = set((i, j) for i in range(h) for j in range(w))
    
    for loc in unvisited:
        if loc in occupied:
            continue
        
        val = int(grid_array[loc[0], loc[1]])
        
        if without_bg and val == int(bg):
            continue
        
        obj = []
        cands = {loc}
        
        while cands:
            neighborhood = set()
            
            for cand in cands:
                cell_val = int(grid_array[cand[0], cand[1]])
                
                if (val == cell_val) if univalued else (cell_val != int(bg if bg is not None else -1)):
                    cell = (cand[0], cand[1], cell_val)
                    
                    if cell not in obj:  # Avoid duplicates
                        obj.append(cell)
                    
                    occupied.add(cand)
                    
                    # Neighbor discovery: compute valid neighbors
                    for di, dj in offsets:
                        ni, nj = cand[0] + di, cand[1] + dj
                        if 0 <= ni < h and 0 <= nj < w:
                            neighborhood.add((ni, nj))
            
            cands = neighborhood - occupied
        
        objs.append(frozenset(obj))
    
    return frozenset(objs)
```

---

## Issue: Full Vectorization Challenge

After careful analysis, **full GPU vectorization of BFS is complex**:

1. **BFS inherently sequential**: Neighbor discovery depends on previous results
2. **Frozenset operations**: Not directly GPU-friendly
3. **Conversion overhead**: May exceed computation savings for small grids

### Revised Strategy: Hybrid Approach

**Better approach for Phase 2b**:
1. Keep BFS logic on CPU (already optimized with offset constants)
2. GPU-accelerate only the **neighbor lookups** (grid[i][j] operations)
3. Batch process multiple grids if available
4. Focus on **batch mode** rather than single-grid GPU acceleration

---

## Recommended Phase 2b Implementation

Given the constraints, **better ROI path**:

### Option A: Batch Processing (Recommended)
- Accelerate grid[i][j] lookups across multiple grids
- Process 10-100 grids in parallel on GPU
- Amortize conversion overhead
- Expected: 2-3x speedup on bulk operations

### Option B: Specific Operation GPU Acceleration
- Identify which DSL ops are actually bottlenecks
- Profile to find operations >10ms (GPU-worth)
- Accelerate those specific operations
- Expected: 1.5-3x speedup where applied

### Option C: Skip GPU for objects(), Focus on Other Ops
- objects() has complex BFS logic (hard to GPU)
- Focus on simpler operations (p_g, rot90, transpose, etc.)
- Accelerate batch processing infrastructure
- Expected: 2-4x speedup on simpler ops

---

## Decision Point: What Should We Do?

Based on analysis:

1. ✅ **Full objects() GPU acceleration**: Complex, likely not worth effort
2. ✅ **Batch processing GPU**: High ROI, scalable
3. ✅ **Simpler DSL op acceleration**: Easy wins, good for learning
4. ❌ **Individual o_g() GPU**: Complex, diminishing returns

### Recommended Path Forward

**Phase 2b.1 (This Sprint)**: 
- Implement batch processing GPU infrastructure
- Accelerate simple bulk operations (dtype conversion, grid transformation)
- Expected: 2-3x speedup on batch operations
- Effort: 2-3 days

**Phase 2b.2 (Future)**:
- Profile actual solver bottlenecks
- Accelerate specific DSL operations
- Focus on operations that take >10ms consistently

---

## Action Items

Need your decision:

1. **Should we pursue batch GPU acceleration** instead of single-object GPU?
2. **Focus area**: Which DSL operations would you like GPU-accelerated?
   - Simple: p_g, rot90, flip, transpose (easy)
   - Medium: o_g, objects, dneighbors (hard)
   - Batch: Multiple grid processing (scalable)

3. **Timeline**: Adjust based on complexity level

Recommend: **Start with batch processing infrastructure + simple operations** for better ROI than struggling with BFS GPU vectorization.

---

## Summary

Phase 2a proved GPU potential (100% cache hit rate). Phase 2b GPU acceleration requires strategic approach:

- ❌ Full objects() GPU: Complex, low ROI
- ✅ Batch processing: High ROI, scalable
- ✅ Simple operations: Easy, good returns

**Ready to implement**. Which direction preferred?
