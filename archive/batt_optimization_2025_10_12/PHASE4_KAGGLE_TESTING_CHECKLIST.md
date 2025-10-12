# Phase 4 Kaggle Testing Checklist

## Pre-Upload Verification ✅
- [x] Code compiles without errors
- [x] utils.py: Dual thread pools implemented
- [x] run_batt.py: Parallel demo/test sample scoring
- [x] Backward compatibility: get_executor() still works

## Files to Upload to Kaggle
```
Modified files:
├── utils.py (dual thread pool architecture)
└── run_batt.py (parallel sample scoring)

Documentation:
├── PHASE4_DUAL_POOL_IMPLEMENTATION.md
└── DUAL_THREAD_POOL_STRATEGY.md
```

## Test Command
```bash
python run_batt.py --timing -i 007bbfb7 -b tmp_batt_onerun_run
```

## Expected Results

### Performance Targets
```
Metric                 | Phase 3 (Baseline) | Phase 4 (Target) | Speedup
-----------------------|--------------------|------------------|--------
Total time             | 16.826s            | 7-8s             | 2.1-2.4x
Demo scoring           | ~12s               | ~4s              | 3x
Test scoring           | ~3.5s              | ~3.5s            | 1x
validate_all           | 0.366s             | 0.366s           | 1x
filter_duplicates      | 0.015s             | 0.015s           | 1x
```

### Correctness Checks
- [ ] ⏳ No Python errors/exceptions
- [ ] ⏳ No NEW timeouts (especially demo[4])
- [ ] ⏳ 149 candidates generated (not 126)
- [ ] ⏳ Same solver files created as Phase 3
- [ ] ⏳ Results match Phase 3 output

## Key Metrics to Monitor

### 1. Timeout Status
```
Look for: "demo[X] timed out" or "test[X] timed out"
Expected: NO timeouts (Phase 3 had none)
Critical: demo[4] should NOT timeout (was Phase 4 initial failure)
```

### 2. Timing Breakdown
```
Look for timing output:
- Total elapsed time
- Individual sample times
- validate_all timing
- filter timing

Expected:
- Total: 7-10s (conservative estimate)
- Demo: 3-5s (3x faster than 12s sequential)
- Test: 3-4s (similar to sequential)
```

### 3. Candidate Count
```
Look for: "X candidates"
Expected: 149 candidates (same as Phase 3)
Warning: 126 means wrong task_type or missing candidates
```

### 4. File Generation
```
Look for: solver_xxx/ directory creation
Expected: Same files as Phase 3 run
Check: solver_xxx/*.py files exist
```

## Test Scenarios

### Scenario 1: Perfect Success (7-8s, no timeouts)
✅ **Action**: Document results, try tuning (6-8 high-level workers)
✅ **Next**: Update PHASE4_DUAL_POOL_RESULTS.md
✅ **Celebrate**: 2-3x overall speedup achieved! 🎉

### Scenario 2: Good Success (8-10s, no timeouts)
✅ **Action**: Still a win! 1.7-2.1x speedup
✅ **Next**: Analyze why not faster (bottleneck still exists?)
✅ **Tune**: Try increasing high-level workers to 6

### Scenario 3: Marginal (10-13s, no timeouts)
⚠️ **Action**: Better than Phase 4 failure (26s), but not target
⚠️ **Next**: Check profiling - is demo scoring still slow?
⚠️ **Consider**: Alternative optimizations (GPU acceleration?)

### Scenario 4: Failure (>15s or timeouts)
❌ **Action**: Revert to Phase 3 sequential version
❌ **Next**: Analyze logs, debug issue
❌ **Alternative**: Try different approach or lower worker count

## Debugging Guide

### Issue: New Timeouts Appear
**Check**:
1. Which sample timed out? (demo[X] or test[X])
2. Is it consistent or intermittent?
3. Does sequential version timeout?

**Potential Causes**:
- Resource contention (too many workers)
- Genuine timeout (solver is slow)
- asyncio.gather ordering issue

**Solutions**:
- Reduce worker count (try 3+3=6)
- Increase timeout (from 5s to 10s)
- Revert to sequential if persistent

### Issue: Slower Than Expected (>10s)
**Check**:
1. Is demo scoring faster than 12s?
2. Are all samples completing?
3. Is validation timing similar?

**Potential Causes**:
- Not enough parallelism (4 workers < 5 samples)
- Overhead from asyncio.gather
- System resource contention

**Solutions**:
- Increase high-level workers to 6-8
- Profile timing breakdown
- Check GPU/memory utilization

### Issue: Wrong Candidate Count (126 instead of 149)
**Check**:
1. Is task_type set correctly?
2. Are all solvers being processed?
3. Compare with Phase 3 output

**Potential Causes**:
- Same bug as Phase 4 initial attempt
- Filter logic changed
- Missing solver files

**Solutions**:
- Check task_type in code
- Compare solver_xxx/ directory
- Revert if persistent

### Issue: Results Don't Match Phase 3
**Check**:
1. Are output grids identical?
2. Are scores matching?
3. Are solver IDs the same?

**Potential Causes**:
- Aggregation logic error
- Ordering issue in parallel execution
- Score calculation bug

**Solutions**:
- Compare o['demo'][i] and o['test'][i]
- Check result aggregation code
- Revert and debug locally

## Success Metrics Summary

### Must Achieve (Core Success)
- ✅ No new timeouts (especially demo[4])
- ✅ Total time < 13s (at least 1.3x speedup)
- ✅ Same correctness (149 candidates, matching results)

### Target Achievement (Full Success)
- 🎯 Total time: 7-8s (2-2.4x speedup)
- 🎯 Demo scoring: 3-5s (3x speedup)
- 🎯 No timeouts or errors
- 🎯 Results match Phase 3 exactly

### Stretch Goals (Optimization)
- 🚀 Push to 5-6s with tuning
- 🚀 GPU utilization >50%
- 🚀 Memory efficient (<80% VRAM)
- 🚀 Document tuning for future reference

## Post-Test Documentation

### If Successful
Create `PHASE4_DUAL_POOL_RESULTS.md` with:
- Actual timing results
- Speedup achieved vs baseline
- Comparison with Phase 3
- Any issues encountered and resolved
- Tuning recommendations

### Update Files
- `BATT_OPTIMIZATION_FINAL.md`: Add Phase 4 results
- `README.md`: Update performance section
- Git commit: "feat: Phase 4 dual thread pool parallel scoring (Xx speedup)"

---

**Ready for Kaggle Testing!** 🚀

Upload modified files and run test command. Good luck!
