# Type Hints Cache Implementation - Validation Plan

**Implementation Date**: October 16, 2025  
**Status**: ✅ Code Complete, Awaiting Kaggle Validation  
**Priority**: 🔴 P1 (Quick Win)

---

## What Was Implemented

### Changes Made

**File 1: `dsl.py`**
- Added `import sys` to imports
- Added `_TYPE_HINTS_CACHE` global dictionary (line ~3820)
- Implemented `_build_type_hints_cache()` function to build cache at module load time
- Exposed public API: `get_type_hints_cached(func_or_name)` for use in other modules
- Cache built once when dsl.py is imported (zero runtime cost during execution)

**File 2: `safe_dsl.py`**
- Changed imports to use cached version instead of typing.get_type_hints
- Updated `_get_safe_default()` to call `get_type_hints_cached()` instead of `get_type_hints()`
- Added fallback import handling for safety

### Expected Impact

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| **get_type_hints calls** | 3,773 per 100 tasks | ~50-100 lookups | 98% reduction |
| **Type hint time** | 0.378s per 100 tasks | 0.038s per 100 tasks | 90% speedup |
| **Total wall-clock** | 3.05s per 100 tasks | ~2.71s per 100 tasks | 1.1x speedup |
| **Cache overhead** | N/A | ~1-2ms build time | Negligible |

---

## Validation Steps

### Step 1: Local Testing (Already Done ✓)
```bash
cd /Users/pierre/dsl/tokpidjin

# Test import
python -c "from dsl import get_type_hints_cached; print('✓ Cache loaded')"
# Output: ✓ Cache loaded

# Test with card.py
python card.py -c 2
# Result: Runs successfully, no errors

# Test with profiler (2 tasks)
python profile_batt_framework.py --top 10
# Result: _get_safe_default shows only 84 calls (down from expected 3,773)
```

### Step 2: Kaggle Validation (NEXT)
```bash
# Run on 32 tasks to see real speedup
bash run_card.sh -c -32

# Expected time: ~2-3 seconds (vs current 3.05s for 100 tasks)
# If linear: 32 tasks should take ~1s (was 0.97s baseline)
# With cache: should be ~0.87s (1.1x faster)

# After completing, profile to verify:
python profile_batt_framework.py --top 10

# Expected:
# - _get_safe_default or get_type_hints_cached calls: << 3,773
# - Type hints category: << 0.378s
# - Total time: << 3.05s for 100 tasks (implies ~2.71s or better)
```

### Step 3: Full Validation (100 Tasks)
```bash
# If 32-task test shows speedup, run full test:
bash run_card.sh -c -100

# Expected time: ~2.7-2.8 seconds (down from 3.05s)
# Speedup: 1.09-1.13x

# Profile to confirm:
python profile_batt_framework.py --top 10
```

---

## Success Criteria

### Must Have ✓
- [ ] Code compiles without errors on Kaggle
- [ ] No import errors or circular dependencies
- [ ] Cache loads at module import time
- [ ] Cache is used (get_type_hints_cached is called, not get_type_hints)
- [ ] Wall-clock time shows measurable improvement (1.05-1.15x speedup expected)

### Should Have
- [ ] get_type_hints calls reduced by 90%+ (from 3,773 to <100)
- [ ] Profile shows type hints category time reduced by 90%
- [ ] Total framework time reduced by ~0.34s

### Nice to Have
- [ ] Cache statistics logged for debugging
- [ ] Graceful fallback if import fails
- [ ] Backwards compatible with existing code

---

## Monitoring Checklist

When running Kaggle tests, check for:

1. **Performance**:
   - [ ] Wall-clock time is lower than 3.05s for 100 tasks
   - [ ] No hanging or infinite loops detected
   - [ ] All 100 tasks complete without timeout

2. **Correctness**:
   - [ ] Generated solvers are valid
   - [ ] No new errors in error logs
   - [ ] Results match previous run (solver count, quality)

3. **Cache Health**:
   - [ ] No import errors
   - [ ] No attribute errors (get_type_hints_cached not found)
   - [ ] Cache is being used (profiler shows reduced calls)

4. **Edge Cases**:
   - [ ] Handles infinite loops correctly (timeout still works)
   - [ ] Memory usage hasn't increased
   - [ ] No cache pollution (old values cached incorrectly)

---

## Troubleshooting Guide

### If Cache Doesn't Load
```python
# Error: ImportError: cannot import name 'get_type_hints_cached'
# Solution: Check dsl.py has the function defined at module level
# Fix: Restart Python/Kaggle kernel to reload dsl module
```

### If Type Hints Still Slow
```python
# Check: Are we actually calling the cached version?
# Debug: Add print statement to dsl.py in get_type_hints_cached()
# Verify: Profile shows get_type_hints_cached being called, not get_type_hints
```

### If Speedup Doesn't Match Expected
```python
# Possible issues:
# 1. Cache not being used (still calling get_type_hints directly)
# 2. Other bottleneck dominating (like DSL operations)
# 3. Kaggle environment different from local
# 
# Debug steps:
# a) Verify _get_safe_default is being called (profiler)
# b) Check call count for _get_safe_default (should be <<< 3,773)
# c) Look at profiler output for "get_type_hints" - should be gone
# d) If get_type_hints still appears, find where it's being called
```

---

## Next Steps After Validation

### If Speedup Confirmed (Expected: 1.1x = 0.34s saved) ✅
1. Proceed to Priority 2: Investigate setcomp bottleneck (todo #2)
2. Look for where 161,488 set comprehensions are coming from
3. Goal: Find another 0.5-1.0s of savings

### If Speedup Not Confirmed (Unexpected)
1. Debug why cache isn't helping
2. Options:
   - Safe_dsl.py not actually using cache (verify in profiler)
   - Cache overhead > savings (unlikely, should be <1ms to build)
   - Other bottleneck masking improvement (run full profiler)
3. Don't proceed until root cause found

### If Speedup Exceeded (Possible: 1.15x+ = 0.4s+ saved)
1. Cache working even better than expected
2. Might indicate get_type_hints was being called more than expected
3. Proceed with confidence to Priority 2

---

## Rollback Plan

If any issues discovered:

```bash
# Revert changes to previous working version
git revert HEAD

# Or manually:
git checkout HEAD~1 -- dsl.py safe_dsl.py

# Commit the revert
git commit -m "revert: Cache implementation caused issues, reverting to working version"

# Re-test on Kaggle
bash run_card.sh -c -32
```

---

## Performance Prediction

Based on investigation findings:

### Best Case Scenario (Cache working perfectly)
```
Current: 3.05s (100 tasks)
With cache: 2.71s (100 tasks)  ← -0.34s
Speedup: 1.12x
Per task: 27.1ms (down from 30.5ms)
```

### Realistic Case (Cache working, 75% reduction)
```
Current: 3.05s
With cache: 2.79s  ← -0.26s
Speedup: 1.09x
```

### Conservative Case (Cache working, 50% reduction)
```
Current: 3.05s
With cache: 2.86s  ← -0.19s
Speedup: 1.07x
```

### Worst Case (Cache overhead > savings)
```
Current: 3.05s
With cache: 3.07s  ← +0.02s (!)
Speedup: 0.99x (worse!)
Note: Very unlikely - cache build is <1ms
```

We expect **Best to Realistic case**: **1.07-1.12x speedup = 0.19-0.34s saved**

---

## Timeline

```
Today:
├─ Implement cache ✓ DONE
├─ Local testing ✓ DONE
└─ Commit ✓ DONE

Tomorrow:
├─ Run on Kaggle (32 tasks) - 5 min
├─ Validate results - 5 min
└─ Decide on Priority 2

This Week:
├─ Priority 2: Investigate setcomps (20 min)
├─ Priority 2: Implement mutation optimization (30-60 min)
└─ Re-profile for cumulative impact

Expected: 3.05s → 1.85s (1.6x speedup) by end of week
```

---

## Commands Ready to Run on Kaggle

```bash
# Full pipeline (takes ~5-10 min total)
cd /Users/pierre/dsl/tokpidjin

# Test with 32 tasks
echo "Running 32 tasks..." && time bash run_card.sh -c -32

# Profile results
echo "Profiling..." && python profile_batt_framework.py --top 10

# Extract performance metrics
echo "Extracting metrics..."
grep -E "Wall-clock|Cumulative|get_type_hints|_get_safe_default" profile_batt_framework_*.txt | tail -20

# Commit results if good
git add -A && git commit -m "perf: Validate type hints cache on Kaggle (32 tasks)"
```

---

## Status

✅ **Implementation**: Complete  
⏳ **Local Testing**: Complete  
⏳ **Kaggle Validation**: Ready to run  
⏳ **Full Validation**: Pending cache results  

**Next Action**: Run `bash run_card.sh -c -32` on Kaggle and check for speedup!

