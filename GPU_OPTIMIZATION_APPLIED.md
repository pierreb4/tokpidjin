# GPU-DSL Optimization Applied

## Problem Identified
The original `gpu_dsl.py` implementation was **slower** than CPU (0.5x speedup) due to:
1. Too many small GPU transfers (one per grid)
2. No GPU warmup (JIT compilation overhead on first run)
3. Batch size too small (min_batch_size=10 not enough)
4. Converting back to tuples immediately (wasting GPU memory)

## Optimizations Applied

### 1. Single Batch Transfer (`BatchTensor` class)
**Before:**
```python
batch_gpu = cp.asarray(batch)  # Single transfer
rotated_gpu = rot90_vectorized(batch_gpu)
rotated_cpu = cp.asnumpy(rotated_gpu)  # Single transfer back
```

**After (using BatchTensor):**
```python
batch_tensor = BatchTensor(grids)  # Prepare on CPU
batch_gpu = batch_tensor.to_gpu()  # SINGLE GPU transfer
result_gpu = rot90_vectorized(batch_gpu)  # Process on GPU
return batch_tensor.from_gpu(result_gpu)  # SINGLE CPU transfer
```

**Impact:** Eliminates per-grid transfer overhead

### 2. Increased Minimum Batch Size
**Before:**
```python
min_batch_size = 10  # Too small for GPU efficiency
```

**After:**
```python
min_batch_size = 20  # Based on Kaggle GPU benchmarks
```

**Impact:** Only uses GPU when it's actually faster

### 3. GPU Warmup (Critical!)
**Before:** No warmup - first run includes JIT compilation time

**After:**
```python
# In benchmark_rot90()
warmup_grids = [... 30 grids ...]
for _ in range(3):
    _ = rot90_batch(warmup_grids, min_batch_size=20)
```

**Impact:** Separates compilation time from measurement

### 4. Best-of-3 Timing
**Before:** Single measurement (includes noise)

**After:**
```python
cpu_times = []
for _ in range(3):
    start = timer()
    cpu_results = [rot90_cpu(g) for g in grids]
    cpu_times.append(timer() - start)
cpu_time = min(cpu_times)  # Best of 3
```

**Impact:** More accurate performance measurement

## Expected Performance

Based on `test_kaggle_gpu_optimized.py` patterns:

| Batch Size | Old (0.5x) | New (Expected) | Improvement |
|------------|------------|----------------|-------------|
| 10         | Slower     | CPU (skipped)  | Correct     |
| 20         | Slower     | 2-3x faster    | 4-6x better |
| 50         | Slower     | 3-5x faster    | 6-10x better|
| 100        | Slower     | 5-8x faster    | 10-16x better|
| 200+       | Slower     | 8-12x faster   | 16-24x better|

## How to Test on Kaggle

1. Upload `gpu_dsl.py` to Kaggle notebook
2. Run:
   ```python
   python test_gpu_dsl_optimized.py
   ```

3. You should see:
   ```
   Batch size  20: CPU   X.XXms | GPU   X.XXms | Speedup:  2.X x ✓
   Batch size  50: CPU   X.XXms | GPU   X.XXms | Speedup:  4.X x ✓
   Batch size 100: CPU   X.XXms | GPU   X.XXms | Speedup:  7.X x ✓
   Batch size 200: CPU   X.XXms | GPU   X.XXms | Speedup: 10.X x ✓
   ```

## Integration with Your Workflow

### Option 1: Direct replacement in DSL
```python
# In dsl.py
from gpu_dsl import rot90_batch, GPU_AVAILABLE

def rot90_smart(grids_or_single):
    """Automatically uses GPU for batches, CPU for single grids"""
    if isinstance(grids_or_single, list) and len(grids_or_single) >= 20:
        return rot90_batch(grids_or_single)
    elif isinstance(grids_or_single, list):
        return [rot90(g) for g in grids_or_single]
    else:
        return rot90(grids_or_single)  # Single grid
```

### Option 2: Use in run_batt.py for batch evaluation
```python
# When evaluating multiple solvers
input_grids = [task['input'] for task in tasks]  # Collect batch

# Old way:
# results = [solver(g) for g in input_grids]

# New way (if solver uses rot90):
from gpu_dsl import rot90_batch
# ... modify solver to accept batches
```

### Option 3: Use in card.py for mutations
```python
# When testing many mutations
mutations = [mutate(base_solver) for _ in range(100)]
test_grids = [...]

# Instead of testing one-by-one, batch the grid operations
# that happen inside the solvers
```

## Next Steps

1. **Test on Kaggle** - Verify the improvements
2. **Add more functions** - Apply same pattern to:
   - `flip` (very simple, should be fast)
   - `rot180`, `rot270` (similar to rot90)
   - `gravitate` (more complex, bigger gains)
3. **Profile end-to-end** - Measure actual workflow speedup
4. **Fine-tune batch sizes** - Based on your actual usage patterns

## File Structure

```
tokpidjin/
├── gpu_dsl.py                    # Optimized GPU functions
├── test_gpu_dsl_optimized.py     # Quick test script
├── test_kaggle_gpu_optimized.py  # Reference implementation
├── INTEGRATION_GUIDE.md          # Full integration guide
└── GPU_OPTIMIZATION_APPLIED.md   # This file
```
