# Fix: Profile Scripts Error - What to Do

## Problem
The profiling scripts failed with `ZeroDivisionError` because they couldn't find the batt module.

## Solution (2 Steps)

### Step 1: Generate a batt module first
```bash
timeout 120 bash run_card.sh -c -1
```

This creates `tmp_batt_onerun_run.py` which contains the solver and differ functions needed for profiling. 

**Time**: 2-5 minutes depending on CPU

**Expected output**: Should see progress messages ending with something like:
```
1 tasks - 1 timeouts
```

### Step 2: Run the profiler
```bash
python profile_inline_isolated.py 2>&1 | tee profile_inline.log
tail -50 profile_inline.log
```

**Time**: 30-60 seconds

**Expected output**: Should show timing statistics for 20+ solvers

## What Changed

The profiling scripts now:
- ✅ Check if batt module exists first
- ✅ Show clear error message with fix instructions
- ✅ Handle division by zero gracefully
- ✅ Provide helpful guidance on what to do next

## If Still Having Issues

**Error: "Could not find tmp_batt_onerun_run.py"**
→ Run `timeout 120 bash run_card.sh -c -1` first

**Error: "No solvers or differs found"**
→ The batt module generated but has no functions
→ Try running the generation command again

**Error: "ZeroDivisionError"**
→ Should be fixed now with the updated scripts
→ Try running the scripts again

## Complete Workflow on Server

```bash
# 1. Generate batt (2-5 min)
timeout 120 bash run_card.sh -c -1

# 2. Profile (30-60 sec)
python profile_inline_isolated.py 2>&1 | tee profile.log

# 3. Read output
tail -50 profile.log

# 4. Optional: Stress test (if needed)
python profile_inline_stress.py 2>&1 | tee stress.log
```

That's it! The scripts should now work without errors.
