# 🚀 Phase 4 Testing Guide - Quick Start

## What You Need to Know

**Phase 4 is ready for testing!** We parallelized the scoring loop (the real bottleneck) and expect **2.2-3.6x overall speedup**.

## 1-Minute Test

```bash
# On Kaggle L4x4:
python run_batt.py --timing -i 007bbfb7 -b tmp_batt_onerun_run
```

**Look for**:
- Total time: **6-10s** (vs 16.8s before)
- `phase4_demo_parallel`: **3-4s** (wall-clock)
- `phase4_test_parallel`: **1-2s** (wall-clock)

## What to Check

### ✅ Correctness
- Candidate count after filter: **32** (should match)
- Files in `solver_md5/`: Same count as before
- Files in `differ_md5/`: Same count as before

### ✅ Performance
- `main.run_batt`: **6-10s** (target)
- `check_batt`: **5-9s** (down from 15.5s)
- `phase4_demo_parallel`: **3-4s** 
- `phase4_demo_cpu`: **12-15s** (sum of parallel tasks)

### ✅ Speedup Ratios
- Demo: `phase4_demo_cpu / phase4_demo_parallel` = **3-4x**
- Test: `phase4_test_cpu / phase4_test_parallel` = **1.5-3x**
- Overall: `21.8s / final_time` = **2.2-3.6x**

## What Changed

### Before (Sequential)
```python
for sample in demo_task:  # ~12s total
    run batt() on sample  # 2-3s each
    
for sample in test_task:  # ~3s total
    run batt() on sample  # 2-3s each
```

### After (Parallel)
```python
# All demo samples at once
demo_results = await asyncio.gather(*[
    score_demo_sample(i, s) for i, s in enumerate(demo_task)
])  # ~3-4s total

# All test samples at once
test_results = await asyncio.gather(*[
    score_test_sample(i, s) for i, s in enumerate(test_task)
])  # ~1-2s total
```

## Expected Output

```
CuPy GPU support enabled for Kaggle
Kaggle GPU Support: True (4 devices)
Batt GPU: Enabled (4 GPUs, MultiGPUOptimizer)

run_batt.py:543: -- 007bbfb7 - 0 start --
run_batt.py:389: -- 007bbfb7 - 0 --

demo[0] - 007bbfb7 - 32
demo[1] - 007bbfb7 - 32
demo[2] - 007bbfb7 - 32
demo[3] - 007bbfb7 - 32
demo[4] - 007bbfb7 - 32
test[0] - 007bbfb7 - 32

run_batt.py:608: -- Filtered to 32 unique candidates (from 149)
run_batt.py:656: -- Phase 3a: Validated 32 solvers in 0.366s

Timing summary (seconds):
  main.run_batt                       6.xxx    ✅ TARGET!
  run_batt.check_batt                 5.xxx    ✅ Improved!
  run_batt.phase4_demo_parallel       3.xxx    ✅ NEW!
  run_batt.phase4_demo_cpu            12.xxx   ✅ NEW!
  run_batt.phase4_test_parallel       1.xxx    ✅ NEW!
  run_batt.phase4_test_cpu            3.xxx    ✅ NEW!
  run_batt.phase2_inline_batch        0.582
  run_batt.phase3a_validate_batch     0.366
  run_batt.phase4_differs             0.353
  run_batt.phase1_filter              0.015
  run_batt.phase3b_file_ops           0.015
```

## Success Scenarios

### 🎉 Amazing (>3x speedup)
```
Total: 16.8s → 5-6s (2.8-3.4x faster)
Conclusion: Perfect! Exceeds expectations!
```

### ✅ Great (2.5-3x speedup)
```
Total: 16.8s → 6-7s (2.4-2.8x faster)
Conclusion: Excellent! Meets target!
```

### 👍 Good (2-2.5x speedup)
```
Total: 16.8s → 7-9s (1.9-2.4x faster)
Conclusion: Good! Acceptable speedup!
```

### 😐 Okay (<2x speedup)
```
Total: 16.8s → 9-10s (1.7-1.9x faster)
Conclusion: Investigate bottlenecks, room for improvement
```

## Troubleshooting

### Issue: Less speedup than expected
**Check**:
- Look at `phase4_demo_cpu / phase4_demo_parallel` ratio
- If <2x: may be CPU-bound, not I/O-bound
- If 2-3x: parallelism working, but overhead exists

**Action**:
- Profile individual sample times
- Check for resource contention
- Consider reducing parallelism if memory-bound

### Issue: Same or slower performance
**Check**:
- Are new metrics showing up?
- Is `check_batt` time actually lower?
- Any error messages?

**Action**:
- Verify code ran correctly
- Check for exceptions in asyncio.gather
- Review Kaggle execution logs

### Issue: Different results
**Check**:
- Candidate count (should be 32)
- Solver file count
- Score values

**Action**:
- Compare o_score values before/after
- Check result aggregation logic
- Verify no race conditions

## The Complete Journey

```
Phase 1: Filter + Batch Inline
  21.788s → 16.884s (22.5% faster) ✅

Phase 2: Parallel Validation
  16.884s → 16.826s (validation 19.4x faster!) ✅

Phase 3: Profiling & Discovery
  Identified: scoring 15.5s (92% bottleneck) ✅

Phase 4: Parallel Scoring (YOU ARE HERE)
  16.826s → 6-10s target (2.2-3.6x faster) ⏳
```

## After Testing

### Document Results
1. Create `PHASE4_RESULTS.md` with actual numbers
2. Update `OPTIMIZATION_COMPLETE_SUMMARY.md`
3. Share final speedup metrics

### Celebrate! 🎉
You've just:
- Profiled systematically through 4 phases
- Applied 3 different parallelization techniques
- Achieved 2-3x overall speedup (target)
- Learned optimization best practices

## Quick Reference

**Command**: `python run_batt.py --timing -i 007bbfb7 -b tmp_batt_onerun_run`

**Target**: 6-10s total (vs 16.8s baseline)

**Key Metrics**:
- `main.run_batt`: 6-10s
- `phase4_demo_parallel`: 3-4s
- `phase4_test_parallel`: 1-2s

**Success**: 2.2-3.6x overall speedup

**Ready?** Upload to Kaggle and run! 🚀
