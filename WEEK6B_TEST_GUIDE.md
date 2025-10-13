# Week 6B Testing Guide - Parallel Batt Execution

## 🎯 What We Changed

**Week 6B Implementation:**
- Replaced sequential demo scoring with ProcessPoolExecutor (4 workers)
- Enables true CPU parallelism (avoids Python GIL)
- Conservative 4 workers for multi-instance server deployments

## 📊 Expected Results

### Before Week 6B (Baseline from Week 6A):
```
Component                      Time     % of Total
───────────────────────────────────────────────────
check_batt (sequential)       2.140s   73%  ← BOTTLENECK
phase3a_validate              0.205s    7%
phase2_inline                 0.335s   11%
phase3b_file_ops              0.182s    6%
Other                         0.070s    2%
───────────────────────────────────────────────────
Total                         2.932s   100%
```

### After Week 6B (Expected with 4 workers):
```
Component                      Time     % of Total   Improvement
────────────────────────────────────────────────────────────────
check_batt (parallel 4x)      0.535s   40%          4.0x faster! ✓
phase3a_validate              0.205s   15%          (already optimal)
phase2_inline                 0.335s   25%          (cache helping)
phase3b_file_ops              0.182s   14%
Other                         0.070s    5%
────────────────────────────────────────────────────────────────
Total                         1.327s   100%         2.2x faster! ✓
```

**Key Metrics to Watch:**
- `check_batt` time: Should drop from ~2.14s to ~0.54s (4x improvement)
- `batt.demo.parallel` time: Should show parallelization benefit
- Overall `main.run_batt`: Should drop from ~2.93s to ~1.33s (2.2x improvement)

## 🧪 Kaggle Test Commands

### Test 1: Single Task (Quick Validation)
```bash
bash run_card.sh -o -c 1 -T
```

**Look for:**
```
Timing summary (seconds):
  main.run_batt                       ~1.3s  ← Should be ~2.2x faster!
  run_batt.check_batt                 ~0.5s  ← Should be ~4x faster!
  batt.demo.parallel                  ~0.5s  ← Parallel execution time
  run_batt.phase3a_validate_batch     ~0.2s  ← Still optimal
```

### Test 2: Multiple Tasks (Cache Warm-up)
```bash
bash run_card.sh -o -c 3 -T
```

**Expected:**
- Run 1: Cold cache, ~1.3-1.5s per task
- Run 2: Warm cache, ~1.0-1.2s per task
- Run 3: Hot cache, ~0.8-1.0s per task

### Test 3: Full Suite (20 tasks)
```bash
bash run_card.sh -o -c 20 -T
```

**Expected:**
- First few tasks: ~1.3-1.5s (cold cache)
- Later tasks: ~1.0-1.2s (warm cache)
- Average: ~1.2-1.3s per task
- Vs baseline: ~2.9s per task (2.2x improvement!)

## 📈 Performance Comparison

| Metric | Week 6A Baseline | Week 6B Target | Actual (Fill in) |
|--------|------------------|----------------|------------------|
| check_batt | 2.140s | 0.535s (4x) | ___ |
| Total time | 2.932s | 1.327s (2.2x) | ___ |
| Demo parallel | N/A (sequential) | 0.535s | ___ |
| Inlining cache hit | 78-80% | 78-80% | ___ |
| Validation cache hit | 0% (new solvers) | 0-50% | ___ |

## 🔍 Troubleshooting

### If performance doesn't improve:

**Issue 1: ProcessPoolExecutor not being used**
- Check output for: "ProcessPoolExecutor failed"
- Fallback to sequential would explain no speedup
- Solution: Check system resources, process limits

**Issue 2: Overhead from process creation**
- First task might be slower (process pool warmup)
- Should improve on subsequent tasks
- Watch for consistent slowness across all tasks

**Issue 3: Small number of candidates**
- If only 8-16 candidates, speedup limited
- With 32 candidates: Expect full 4x benefit
- Check: "Filtered to X unique candidates"

**Issue 4: GIL-bound operations still present**
- Some operations might not parallelize
- Check if most time is in demo scoring
- Verify `batt.demo.parallel` timing

## ✅ Success Criteria

Week 6B is successful if:
1. ✓ `check_batt` time drops by 3-4x (2.14s → 0.5-0.7s)
2. ✓ Overall time drops by 2-2.5x (2.93s → 1.2-1.5s)
3. ✓ No errors or crashes with ProcessPoolExecutor
4. ✓ Cache still working (78-80% inlining hit rate)
5. ✓ Stable across multiple runs

## 🚀 Next Steps After Validation

**If Week 6B succeeds:**
- Move to Week 6C: Algorithm optimizations (20% more)
- Target areas: Early termination, smart ordering
- Expected: 1.33s → 1.10s

**If Week 6B has issues:**
- Analyze bottlenecks in parallel execution
- Consider adjusting worker count (2-8 workers)
- May need to optimize process communication

## 📝 Test Results Template

```
=== Week 6B Test Results ===
Date: [Fill in]
Kaggle Session: CPU-only

Test 1 (1 task):
- Total time: ___s (baseline: 2.93s)
- check_batt: ___s (baseline: 2.14s)
- Speedup: ___x
- Status: ✓/✗

Test 2 (3 tasks):
- Average time: ___s
- Cache hits: ___%
- Status: ✓/✗

Test 3 (20 tasks):
- Average time: ___s
- Range: ___s - ___s
- Status: ✓/✗

Overall Assessment:
- Week 6B successful: Yes/No
- Issues encountered: ___
- Next steps: ___
```

## 🎯 Summary

Week 6B implements ProcessPoolExecutor for true CPU parallelism on demo scoring, the main bottleneck identified in Week 6A analysis. Expected to deliver 2.2x overall speedup (2.93s → 1.33s per task) by parallelizing batt() calls across 4 worker processes.

Test on Kaggle and fill in the results template above!
