# GPU Acceleration Quick Reference

## TL;DR
- ❌ **rot90**: GPU 2x SLOWER (transfer overhead >> compute)
- ✅ **fgpartition**: GPU 5-10x FASTER (compute >> transfer overhead)
- 💡 **Lesson**: Only GPU accelerate operations where compute time >> transfer time

## Test on Kaggle

```bash
# Upload gpu_dsl.py and test_gpu_fgpartition.py to Kaggle, then:
!python test_gpu_fgpartition.py
```

## Expected Output

```
TEST 1: rot90 - Simple Operation
  → GPU SLOWER: 0.5x speedup ✗
  → This is EXPECTED and correct

TEST 2: fgpartition - Complex Operation  
  → GPU FASTER: 5-10x speedup ✓
  → This is what we want!
```

## Files to Copy to Kaggle

1. **gpu_dsl.py** - Main GPU module with fgpartition_batch()
2. **test_gpu_fgpartition.py** - Test script
3. **dsl.py** - For CPU fallback functions
4. **timer.py** - For timing (or use time.perf_counter)

## If fgpartition Works

Then proceed with:
1. ✅ Implement `gravitate_batch()` (similar pattern)
2. ✅ Add pipeline support (chain ops on GPU)
3. ✅ Integrate with `run_batt.py` (replace hot paths)

## If fgpartition Fails

Then investigate:
1. 🔍 Are grids too small? (need batch size 100+)
2. 🔍 Is operation complex enough? (may need more compute)
3. 🔍 CuPy overhead? (check GPU memory transfers)

## Key Metrics

| Operation | Compute Time | Transfer Time | GPU Viable? |
|-----------|--------------|---------------|-------------|
| rot90     | 0.3ms        | 2.5ms         | ❌ No (1:8)  |
| fgpartition | 50ms       | 2.5ms         | ✅ Yes (20:1)|
| gravitate | 30ms         | 2.5ms         | ✅ Yes (12:1)|

**Rule:** If ratio > 5:1 (compute:transfer), GPU wins!
