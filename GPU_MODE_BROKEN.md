# GPU Mode (-g flag) is BROKEN - DO NOT USE

## The Problem

Running `bash run_card.sh -g` causes **ALL tasks to timeout** because the generated code is broken.

## Root Cause

The `-g` flag enables `--vectorized` mode in `card.py`, which generates code that calls:
```python
t1, t2, t3, t4 = batch_process_samples_gpu(S)
```

This function in `batt_gpu.py` has a **CPU fallback threshold** that returns immediately:
```python
if not USE_GPU or len(S) < 100:
    # CPU fallback for small batches
    return apply(first, S), apply(second, S), ...
```

However, the generated code **doesn't match the actual solver logic** - it's trying to batch-process samples in a way that's incompatible with how individual solvers work.

## Test Results

### Working (CPU mode):
```bash
time python run_test.py -q -i 007bbfb7
# 1 out of 1 tasks solved correctly (0 new).
# real	0m2.453s
```

### Broken (GPU mode with -g flag):
```bash
bash run_card.sh -i -b -c -32 -g
# ALL 32 tasks timeout
# 0 candidates scored on every task
```

## The Confusion

There are **TWO different GPU systems** in this codebase:

### 1. **Batch Operations GPU** (WORKING ✅)
- File: `gpu_optimizations.py`
- Purpose: Process 100-200 grids in batch (for training/validation)
- Status: **Production ready** - 10-35x speedup
- Usage: Import `auto_select_optimizer()` and process grids in batch
- Documentation: `GPU_PROJECT_SUMMARY.md`, `INTEGRATION_GUIDE.md`

### 2. **Vectorized Solver GPU** (BROKEN ❌)
- File: `card.py` with `--vectorized` flag
- Purpose: Generate GPU-accelerated solver code
- Status: **Non-functional** - causes all tasks to timeout
- Usage: **DO NOT USE** the `-g` flag in `run_card.sh`
- Problem: Generated code calls batch operations on small samples (2-5 items)

## The Fix

**DO NOT USE `-g` FLAG** for normal runs!

### Correct Usage:
```bash
# CPU mode (default, works correctly)
bash run_card.sh -i -b -c -32

# Force CPU mode explicitly
bash run_card.sh -i -b -c -32 -m
```

### What Happens Now:
- Running with `-g` now shows clear error message
- Automatically defaults to CPU mode
- Script will NOT generate broken vectorized code

## For GPU Acceleration

If you want GPU acceleration:

1. **Don't use run_card.sh -g** ❌
2. **Use the batch operations API** ✅

Example (from `gpu_optimizations.py`):
```python
from gpu_optimizations import auto_select_optimizer

optimizer = auto_select_optimizer()
results = optimizer.batch_grid_op_optimized(
    grids,  # 100-200 grids
    operation_vectorized,
    vectorized=True
)
```

See `INTEGRATION_GUIDE.md` for details.

## Summary

- **`-g` flag**: BROKEN - generates non-functional code
- **GPU batch operations**: WORKING - use `gpu_optimizations.py`
- **Default CPU mode**: WORKING - use without `-g` flag
- **run_card.sh**: Always use CPU mode (default or `-m` flag)

## Related Documentation

- `GPU_PROJECT_SUMMARY.md` - Working GPU batch operations
- `INTEGRATION_GUIDE.md` - How to use GPU batch operations
- `.github/copilot-instructions.md` - Complete GPU status
