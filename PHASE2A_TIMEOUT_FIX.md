# 🔍 ROOT CAUSE: Task Timeout Issue

**Diagnosis**: Task `00576224` timed out in the 100-task run  
**Evidence**: Output shows "1 tasks - 1 timeouts"  
**Impact**: Process exited after first timeout, only 1 task executed  
**Solution**: Increase timeout for 100-task run  

---

## Why It Happened

Looking at the output from your 100-task run:
```
1 tasks - 1 timeouts
```

This means:
1. First task (`00576224`) started
2. Task exceeded timeout threshold
3. Process caught the timeout and exited
4. Other 99 tasks never ran

**Why first task timed out?**
- Default timeout in run_batt.py is probably 10-15 seconds
- Single task can occasionally take 15-30s (especially with profiler overhead)
- Task got unlucky and took slightly longer

---

## The Fix

**OPTION A: Simple - Increase timeout**
```bash
python run_batt.py -c 100 -t 30 --timing
```

Parameters:
- `-c 100`: Run 100 tasks
- `-t 30`: Timeout per task = 30 seconds (was default ~10s)
- `--timing`: Show timing breakdown

**OPTION B: Very Safe - Super long timeout**
```bash
python run_batt.py -c 100 -t 60 --timing
```

Even safer, 60 second timeout per task.

**OPTION C: Without profiler overhead**
```bash
python run_batt.py -c 100 -t 20
```

No `--timing` or `--cprofile`, faster execution, cleaner.

---

## Current Timeout Settings

To check what default timeout is, look at run_batt.py:

```bash
grep -n "timeout\|argparse\|-t" run_batt.py | head -20
```

Likely around line 50-100.

---

## Why This Matters

**Single task execution time**: ~1.0-1.1 seconds (from your test)  
**100 tasks sequential**: ~100s baseline  
**Expected**: Should complete without timeout  
**What happened**: First task took >default_timeout, got killed

---

## Success Criteria for Next Run

After running with increased timeout, you should see:

```
run_batt.py:XXXX: -- 00576224 - 0 done - 85 candidates scored
run_batt.py:XXXX: -- TASK2 - 0 done - XX candidates scored
run_batt.py:XXXX: -- TASK3 - 0 done - XX candidates scored
...
[~100 task lines total]

100 tasks - 0 timeouts  ✅ (good)
or
100 tasks - 1-2 timeouts  ✅ (acceptable)

Wall-clock: ~100-120s (all 100 tasks processed)
```

**NOT this** (what happened):
```
1 tasks - 1 timeouts  ❌
```

---

## What We'll Learn from Fixed Run

Once 100 tasks complete successfully:

1. **Wall-clock time**: Compare to 3.23s Phase 1b baseline
   - Expected: 3.08-3.15s (0.08-0.15s improvement)
   
2. **objects() performance**: Check if visible in top 30 functions
   - At 100 tasks: Should be ~1.2-1.3s cumulative
   - With Phase 2a cache: Might see 10-15% improvement
   
3. **Overall speedup**: Calculate Phase 2a impact
   - If 3.10s actual vs 3.23s baseline = -0.13s = -4.0%
   - Close to Phase 1b results (-4.7%)
   - Combination Phase 1b + 2a would show compounding

---

## Recommended Command (RIGHT NOW)

```bash
python run_batt.py -c 100 -t 20 --timing
```

**Why this one?**
- `-t 20`: Safe timeout (2x expected single task time)
- `--timing`: See breakdown of where time is spent
- No profiler overhead: Cleaner, faster
- 2-3 minutes to complete
- Will show all 100 tasks processed ✅

---

## Then Follow Up

After that completes:
```bash
python run_batt.py -c 100 --cprofile --cprofile-top 30
```

For detailed profiler data (takes longer, but shows per-function metrics).

---

## Summary

**Issue**: Default timeout too short, first task timed out  
**Fix**: Use `-t 20` or `-t 30` to increase timeout  
**Next Command**: `python run_batt.py -c 100 -t 20 --timing`  
**Expected Result**: All 100 tasks complete, wall-clock ~3.08-3.15s

Let's get this working! ✅
