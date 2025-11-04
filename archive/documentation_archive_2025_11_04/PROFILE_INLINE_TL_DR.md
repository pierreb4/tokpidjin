# Profile inline_variables() Timeout - Quick Answer

## TL;DR - Commands to Run on Server

```bash
# Step 1: Generate a batt module (if needed)
timeout 120 bash run_card.sh -c -1

# Step 2: Profile the inline_variables() performance
python profile_inline_isolated.py | tee profile.log
tail -50 profile.log

# Step 3: If you need to find optimal timeout
python profile_inline_stress.py | tee stress.log
tail -50 stress.log
```

## What You Get

### From `profile_inline_isolated.py`
- Real timing data on 20+ solvers with current 1.0s timeout
- Statistics: mean, min, max, success/timeout/error counts
- ~10-30 second runtime
- Shows if current timeout is good or needs adjustment

### From `profile_inline_stress.py`
- Tests different timeout values: 0.1s, 0.5s, 1.0s, 2.0s, 5.0s
- Shows success rate at each level
- Identifies optimal timeout automatically
- ~30-60 second runtime
- Includes percentile analysis (p50, p95, p99)

## How to Use Results

**If profiling shows:**
- ✅ All solvers inline in < 100ms, no timeouts → 1.0s is good (keep it)
- ✅ All solvers inline in < 50ms, no timeouts → can reduce to 0.5s
- ⚠️ Some timeouts at 1.0s but not at 2.0s → increase to 2.0s
- ⚠️ Some very slow solvers (> 500ms) → check if AST errors or legitimate

**To adjust timeout:**
```bash
# Change default timeout in utils.py
sed -i 's/timeout_seconds=1/timeout_seconds=0.5/' utils.py  # For 0.5s
sed -i 's/timeout_seconds=1/timeout_seconds=2/' utils.py    # For 2.0s

# Verify change
grep "def inline_variables" utils.py

# Commit
git add utils.py && git commit -m "tune: Adjust inline_variables timeout to Xs"
```

## Current Configuration

| File | Location | Current Setting | Purpose |
|------|----------|-----------------|---------|
| `utils.py` | Line 322 | `timeout_seconds=1` | Core inlining function timeout |
| `run_batt.py` | Line 1560 | `timeout_per_item=1` | Solver batch inlining timeout |
| `run_batt.py` | Line 1808 | `timeout_per_item=1` | Differ batch inlining timeout |

**Performance baseline:**
- Normal solvers: 20-100ms
- Complex solvers: 100-500ms  
- Pathological cases: > 500ms (likely AST errors)

## Example Workflow (5 minutes)

```bash
# 1. Generate batt (1-2 min) - ONLY IF NEEDED
timeout 120 bash run_card.sh -c -1

# 2. Profile isolated (30 sec)
python profile_inline_isolated.py 2>&1 | tee profile.log

# 3. Read recommendations (5 sec)
tail -30 profile.log

# 4. If needed, stress test (1 min)
python profile_inline_stress.py 2>&1 | tee stress.log

# 5. Adjust timeout based on results (1 min)
sed -i 's/timeout_seconds=1/timeout_seconds=0.5/' utils.py
git add utils.py && git commit -m "tune: Reduce inline_variables timeout to 0.5s"
```

## Files Created

1. **`PROFILE_INLINE_QUICK_START.md`** ← Start here for quick reference
2. **`PROFILE_INLINE_VARIABLES.md`** ← Comprehensive documentation
3. **`profile_inline_isolated.py`** ← Run this first
4. **`profile_inline_stress.py`** ← Run this for detailed analysis
5. **`profile_inline_commands.sh`** ← Reference of all commands

## Most Important Command

```bash
python profile_inline_isolated.py 2>&1 | tee profile.log && tail -50 profile.log
```

This one command gives you all the information you need to make a decision about timeout tuning. Run it once, check the output, and decide based on the statistics shown.

## Decision Guide

```
Read the last section of profile_inline_isolated.py output:

SOLVER STATISTICS:
  Mean time:  45.23ms
  Max time:   120.34ms
  Min time:    0.98ms

If Max < 50ms:   Reduce timeout to 0.5s
If Max < 100ms:  Keep timeout at 1.0s (current)
If Max < 200ms:  Keep timeout at 1.0s or try 0.5s
If Max < 500ms:  Keep timeout at 1.0s
If Max > 500ms:  Increase to 2.0s or investigate AST errors
```

That's it! Run the profiler and you'll know what to do.
