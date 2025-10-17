# 🔧 PHASE 2A - QUICK FIX GUIDE

**Issue**: Only 1 task processed instead of 100  
**Status**: Need to retry validation run  
**Time**: 5 minutes to diagnose + rerun

---

## Quick Diagnosis Commands

### Check 1: How many tasks are available?
```bash
ls solver_dir | wc -l
```
Should show: 100+ tasks available

### Check 2: Simple 10-task test
```bash
python run_batt.py -c 10 --timing
```
Should complete in ~10-15s with 10 tasks

### Check 3: Check for errors
```bash
python run_batt.py -c 5 -t 20 --timing
```
5 tasks with 20s timeout, see if completes

---

## Retry: 100-Task Run

### Option A: Without Profiler (Cleanest)
```bash
python run_batt.py -c 100 --timing
```
- Faster (~50-60s)
- Clear wall-clock time
- No profiler overhead
- Still shows timing breakdown

### Option B: With Profiler (More Detail)
```bash
python run_batt.py -c 100 --cprofile --cprofile-top 30
```
- Takes longer (~80-100s)
- Shows per-function data
- Can measure objects() improvement

### Option C: Increase Timeout
```bash
python run_batt.py -c 100 -t 15 --timing
```
- Increase timeout to 15 seconds
- Might help if tasks timing out

---

## What to Watch For

When running 100 tasks, you should see:
```
run_batt.py:XXXX: -- TASK_ID - 0 start --
run_batt.py:XXXX: -- TASK_ID - 0 done - NNN candidates scored
...
[repeated ~100 times]

100 tasks - X timeouts
```

**Not seeing 100 tasks?** → Something is wrong

---

## Most Likely Issue

**Task timeout on first task**:
- First task times out
- Process exits
- Only 1 task actually runs

**Fix**:
```bash
# Increase timeout
python run_batt.py -c 100 -t 20 --timing
```

---

## What Results Should Look Like

### Correct 100-Task Output
```
Kaggle GPU Support: True (2 devices)
✓ Kaggle GPU Optimizer initialized

[Multiple task outputs - should see ~100 task IDs]

100 tasks - 0 timeouts  ✅ (or small number like 1-2)

Wall-clock: ~3.10s (what we're measuring!)

[cProfile output...]
objects():  1.2-1.3s cumulative
o_g():      1.35-1.4s cumulative
objects_t(): 0.36-0.39s cumulative
```

---

## Decision Tree

```
Run: python run_batt.py -c 100 --timing
           ↓
    Did it say "100 tasks"?
           ↓
    ┌──────────┬──────────┐
    ↓          ↓          ↓
   YES        NO       ERROR
    ✅         ❌        ⚠️
   Great!    Rerun      Diagnose
   Measure   with -t30  the error
   results
```

---

## Absolute Simplest Approach

Just run this:
```bash
python run_batt.py -c 100
```

- No profiler overhead
- No timing overhead
- Just see wall-clock time
- Fastest and clearest

Then check output for:
- "100 tasks" mentioned? → Good
- Wall-clock time? → Compare to 3.23s
- Errors/timeouts? → Should be 0

---

## I Recommend

**Run this exact command**:
```bash
python run_batt.py -c 100
```

**Why**:
- Simplest
- Fastest
- Clearest results
- Can measure wall-clock directly
- No profiler overhead to worry about

**Then after**:
- If successful: `python run_batt.py -c 100 --timing` for breakdown
- If issue: `python run_batt.py -c 10 --timing` to debug

---

**Status**: Ready to retry - pick a command above and run it!
