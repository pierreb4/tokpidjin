# GPU Acceleration Strategy for ARC DSL

## Key Finding: Simple Operations Don't Benefit

**rot90 test results on Kaggle:**
```
Batch size  20: GPU 2x SLOWER (0.5x speedup)
Batch size 500: GPU 2x SLOWER (0.5x speedup)
```

**Root cause:** Transfer overhead >> computation time for simple operations

## Transfer Cost Analysis

For any GPU operation:
```
Total Time = Transfer_to_GPU + Compute + Transfer_from_GPU

For rot90 (simple):
= 1.0ms + 0.3ms + 1.0ms = 2.3ms
vs CPU: 0.8ms per batch
Result: GPU is SLOWER ❌

For fgpartition (complex):
= 1.0ms + 50ms + 1.0ms = 52ms  
vs CPU: 300ms per batch
Result: GPU is 5.7x FASTER ✅
```

## Which Operations to Accelerate?

### ❌ DON'T Accelerate (Transfer > Compute)
1. `rot90` - Just transpose + reverse (0.3ms compute)
2. `flip` - Array reversal (0.2ms compute)
3. `transpose` - Memory reorg (0.3ms compute)
4. `shift` - Array slicing (0.4ms compute)
5. `crop` - Array indexing (0.2ms compute)

### ✅ DO Accelerate (Compute >> Transfer)

#### Priority 1: Object/Patch Operations (Heavy compute)
```python
def fgpartition(grid) -> Objects:
    # 1. Find all unique colors
    # 2. For each color, find all pixels
    # 3. Create frozensets for each object
    # 4. Return frozenset of objects
    # Complexity: O(n*m*k) where k=number of colors
```
**Current:** Has GPU code but not optimized for batching  
**Expected speedup:** 5-10x for batches >20  
**Action:** Implement `fgpartition_batch()` with BatchTensor

#### Priority 2: Iterative Operations (Many steps)
```python
def gravitate(source, destination):
    # Loop until adjacent
    while not adjacent(current_source, destination) and c < 42:
        c += 1
        current_source = shift(current_source, (i, j))
    # Up to 42 iterations!
```
**Current:** CPU only, iterative  
**Expected speedup:** 3-8x for batches >20  
**Action:** Vectorize shift operations, batch the loops

#### Priority 3: Neighbor/Connectivity Operations
```python
def neighbors(indices):
    # For each cell, check 4-8 neighbors
    # Matrix operations on GPU
```
**Expected speedup:** 4-12x for batches >50  
**Action:** Use GPU convolution/stencil operations

### ⚠️ MAYBE Accelerate (Pipeline approach)
If we chain operations and **stay on GPU** between steps:

```python
def solve_task_gpu(grid):
    gpu_grid = cp.asarray(grid)         # 1ms transfer
    gpu_grid = fgpartition_gpu(gpu_grid)  # 50ms on GPU
    gpu_grid = gravitate_gpu(gpu_grid)    # 20ms on GPU
    gpu_grid = fill_gpu(gpu_grid)         # 15ms on GPU
    return cp.asnumpy(gpu_grid)         # 1ms transfer
    # Total: 2ms transfer + 85ms compute = 87ms
    # vs CPU: 1ms + 300ms + 100ms + 80ms + 1ms = 482ms
    # Speedup: 5.5x ✅
```

**Key:** Only 2 transfers (in/out), not 8 (4 ops × 2 each)

## Implementation Plan

### Phase 1: Implement fgpartition_batch ✅ HIGHEST PRIORITY
**File:** `gpu_dsl.py`  
**Function:** 
```python
def fgpartition_batch(grids, min_batch_size=20):
    """Batch process multiple grids for foreground partition"""
    if len(grids) < min_batch_size:
        return [fgpartition_cpu(g) for g in grids]
    
    # Single GPU transfer
    batch_tensor = BatchTensor(grids)
    gpu_batch = batch_tensor.to_gpu()
    
    # Process on GPU
    results = []
    for i in range(len(grids)):
        gpu_grid = gpu_batch[i]
        colors = cp.unique(gpu_grid)
        bg_color = find_background_gpu(gpu_grid)
        
        objects = []
        for color in colors:
            if color != bg_color:
                positions = cp.where(gpu_grid == color)
                obj = frozenset(zip(positions[0].get(), 
                                   positions[1].get(), 
                                   [int(color)] * len(positions[0])))
                objects.append(obj)
        results.append(frozenset(objects))
    
    return results
```

**Expected:** 5-10x speedup for batch size 50+

### Phase 2: Implement gravitate_batch
**Approach:** Vectorize the iteration loop
```python
def gravitate_batch(sources, destinations, min_batch_size=20):
    # Parallel gravity simulation on GPU
    # All grids move simultaneously
```

### Phase 3: Pipeline Support (BIGGEST WIN)
**Approach:** Modify operations to accept GPU tensors
```python
def fgpartition(grid):
    # Check if input is already on GPU
    if isinstance(grid, cp.ndarray):
        return _fgpartition_gpu(grid)  # Stay on GPU
    else:
        return _fgpartition_cpu(grid)

def solve_pipeline(grid):
    gpu_grid = cp.asarray(grid)  # Single transfer in
    gpu_grid = fgpartition(gpu_grid)  # GPU → GPU
    gpu_grid = gravitate(gpu_grid)    # GPU → GPU
    gpu_grid = fill(gpu_grid)         # GPU → GPU
    return tuple_from_gpu(gpu_grid)  # Single transfer out
```

**Expected:** 10-30x speedup for pipelines with 3+ operations

### Phase 4: Integration with run_batt.py
**Identify hot paths:**
1. Find solvers that call fgpartition/gravitate repeatedly
2. Replace with batched GPU versions
3. Measure end-to-end speedup

## Success Metrics

### Phase 1 Target (fgpartition_batch)
- ✅ Correctness: CPU and GPU results match
- ✅ Performance: 5x+ speedup for batch size 50+
- ✅ Kaggle test: Show actual timing improvements

### Phase 2 Target (gravitate_batch)
- ✅ Correctness: Movement vectors match CPU
- ✅ Performance: 3x+ speedup for batch size 50+

### Phase 3 Target (Pipeline)
- ✅ Memory: Operations chain without CPU transfer
- ✅ Performance: 10x+ speedup for 3+ operation chains

### Phase 4 Target (Integration)
- ✅ End-to-end: Reduce run_batt.py time by 20-50%
- ✅ Kaggle: Win Kaggle notebook speedup competition

## Next Steps

1. ✅ Document why rot90 doesn't work (DONE)
2. ✅ Identify heavy operations (DONE - fgpartition, gravitate)
3. 🚧 Implement fgpartition_batch in gpu_dsl.py (NEXT)
4. ⏳ Test on Kaggle with timing
5. ⏳ Implement gravitate_batch
6. ⏳ Add pipeline support
7. ⏳ Integrate with run_batt.py

## References

- `test_kaggle_gpu_optimized.py` - Shows what operations benefit (complex ops, not simple)
- `gpu_dsl.py` - Current GPU DSL functions
- `dsl.py` lines 3157-3187 - fgpartition with basic GPU code
- `dsl.py` lines 2585-2610 - gravitate with iterative logic
