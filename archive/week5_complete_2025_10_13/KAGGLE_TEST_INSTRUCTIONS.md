# GPU Performance Test - Instructions for Kaggle

**Date**: October 13, 2025  
**Branch**: main (commit df53706)  
**Goal**: Measure actual GPU performance with 10 second timeout

---

## What Changed

1. **Timeout increased**: 1s → 10s (default)
2. **Fixed check_batt()**: Now uses passed timeout instead of hardcoded 5s
3. **Test script created**: `test_gpu_timeout.sh`

---

## How to Test on Kaggle

### Option 1: Use test script
```bash
bash test_gpu_timeout.sh
```

### Option 2: Manual test
```bash
# Single task
python run_batt.py -c 1 -b batt --timing

# 5 tasks
python run_batt.py -c 5 -b batt --timing
```

---

## What to Look For

### Key Timing Metrics

Look at the output for these lines:
```
Timing summary (seconds):
  batt.demo.parallel          X.XXX  ← Demo sample scoring time
  batt.test.call_with_timeout X.XXX  ← Test sample scoring time
```

### Expected Results

**If GPU overhead dominates (hypothesis):**
```
batt.demo.parallel: ~1.3-1.5s per sample
Total per task: ~4-6s (2 demo + 1 test)
```
→ **This confirms GPU makes it SLOWER** (should be ~430ms per sample on CPU)

**If GPU actually helps (surprising):**
```
batt.demo.parallel: <500ms per sample
Total per task: <2s
```
→ **GPU is helping** (need to understand why!)

### Interpretation

| Time per sample | Conclusion | Action |
|----------------|------------|--------|
| > 1.0s | GPU overhead dominates | Disable GPU batch calls |
| 0.5-1.0s | GPU marginal benefit | Consider disabling |
| < 0.5s | GPU helps! | Keep, investigate why |

---

## Analysis Questions

1. **Do calls complete?** (no more timeouts?)
2. **How long per batt() call?** (check `batt.demo.parallel`)
3. **How long per task?** (total time / task count)
4. **How many samples per task?** (usually 2 demo + 1 test = 3)

---

## Expected Baseline (CPU-only)

From analysis in WEEK5_TIMEOUT_ANALYSIS.md:

```
Per batt() call:
  - 1,076 operations × 0.4ms = 430ms
  - Should complete in <500ms

Per task (3 batt calls):
  - 3 × 430ms = 1,290ms ≈ 1.3s
  - Should complete in <2s

Full run (5 tasks):
  - 5 × 1.3s = 6.5s
  - Should complete in <10s
```

---

## Current Architecture Issue

**Problem**: `batch_process_samples_gpu(S)` gets tiny batches

```python
# S typically has 2-3 sample pairs
S = ((I1, O1), (I2, O2), (I3, O3))

# batch_process_samples_gpu processes:
# - 3 input grids
# - 3 output grids
# Total: 6 grids

# GPU overhead for 6 grids:
# - Transfer: 50ms
# - Compute: 5ms
# - Total: 55ms per call

# × 9 calls in batt.py = 495ms GPU overhead
```

**CPU would do same work in**: 90ms

**GPU is 5.5x slower** for tiny batches!

---

## Next Steps Based on Results

### Scenario A: GPU makes it slower (> 1s per sample)

1. **Disable GPU batch calls** in `batt_gpu.py`
2. Force CPU fallback always
3. Regenerate batt: `python card.py -fd -c 32 --vectorized -f batt.py`
4. Retest - expect 3x speedup (1.5s → 0.5s per sample)

### Scenario B: GPU helps (< 500ms per sample)

1. **Investigate why** - shouldn't work with tiny batches!
2. Check if S is larger than expected
3. Profile GPU operations
4. Document findings

---

## Files to Review After Test

1. **Terminal output** - timing summary
2. **Number of timeouts** - should be 0 now
3. **Per-sample times** - from `batt.demo.parallel`
4. **Overall speedup** - compare to baseline

---

## Quick Decision Tree

```
Run test → Check times
    ↓
Per sample > 1s?
    ├─ YES → GPU hurts performance
    │         → Disable GPU batch calls
    │         → Expect 3x faster
    │
    └─ NO → GPU helps or neutral
              → Keep investigating
              → Measure vs CPU baseline
```

---

## Commands Ready to Copy

```bash
# Pull latest changes
git pull

# Run test
bash test_gpu_timeout.sh

# OR manual test
python run_batt.py -c 5 -b batt --timing

# Check for any Python errors
python -c "import batt; import batt_gpu; print('Imports OK')"

# Check GPU initialization
python -c "from batt_gpu import USE_GPU, gpu_count; print(f'GPU: {USE_GPU}, Count: {gpu_count}')"
```

---

## Success Criteria

✅ **No timeouts** (all samples complete)  
✅ **Get real timing data** (see actual GPU performance)  
✅ **Clear decision** (disable GPU or keep investigating)

---

**Ready to test!** 🚀

Upload to Kaggle, run the test, and share the timing output.
