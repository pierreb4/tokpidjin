# 🔴 CRITICAL: Kaggle Profiling Shows Unexpected Results

**Date**: October 16, 2025  
**Status**: Investigation Required  
**Issue**: Division by zero errors in generated solvers

---

## What We're Seeing

### Profiling Output Summary
```
Wall-clock: 1.89s (on Kaggle with 100 tasks)
Results: 0 outputs, 0 solvers generated
Task Failures: 100 tasks failed with "integer division or modulo by zero"
```

### Bottleneck Pattern (Different from Expected)
```
Before (local 2-task test):
├─ get_type_hints: 0.378s (expected to cache this)
└─ objects, o_g: 1.4s each

After (Kaggle 100-task test):
├─ connect(): 0.555s (2.2ms per call, 172,722 calls!)
├─ <genexpr>: 0.628s (172,822 calls!)
├─ prapply(): 0.673s (4.5ms per call)
├─ objects_t: 0.574s (0.344ms per call, 600 calls)
└─ o_g_t: 0.582s (0.012ms per call, 600 calls)
```

### Key Difference
- **Type hints cache**: Shows only 854 `_get_safe_default` calls (HUGE reduction from 3,773! ✓)
- **Division errors**: ALL 100 tasks failed
- **New top functions**: connect() and prapply() weren't in top bottlenecks before
- **No valid solvers**: 0 outputs, 0 solvers (all generated solvers had errors!)

---

## Analysis

### Possible Root Causes

#### 1️⃣ **Division by Zero in Generated Solvers** 
This is the most likely cause. The generated solver code contains operations that divide by zero:
- Could be: `size() / something` where something is 0
- Could be: `get_nth() % 0` or similar modulo operations
- Could be: Index operations with 0-sized containers

**Evidence**:
- Consistent across ALL 100 tasks (not random)
- Appears during profiling (generate and test phase)
- All tasks report same error type

**Why This Matters**:
- If all generated solvers are invalid, we're not measuring real performance
- The bottleneck functions (connect, prapply) might be error handling code!

#### 2️⃣ **Cache Causing Issues**
Unlikely but possible:
- If cache returns wrong type hints
- If cache causes mutation logic to fail
- If cache initialization broke something

**Evidence Against This**:
- Cache shows massive reduction in _get_safe_default calls (854 vs 3,773+)
- Local 2-task test worked fine
- Code path shouldn't be different

#### 3️⃣ **Kaggle Environment Differences**
Something different on Kaggle:
- Different Python version?
- Different NumPy/CuPy behavior?
- Different random seed causing different mutation path?

**Evidence**:
- Same code, different results
- But would expect similar error patterns if environment issue

---

## What's Really Happening

### The Mystery of 0 Outputs/Solvers

The profiling shows:
- 100 tasks processed
- ALL failed with division by zero
- 0 valid solvers generated
- 0 outputs (because all solvers errored)

**This is NOT a performance issue - this is a CORRECTNESS issue!**

The bottleneck functions are appearing because:
1. Mutations are generated
2. Solvers are created
3. Solvers are tested
4. **Solvers crash with division by zero**
5. Error handling code runs (this is what we're profiling)
6. No valid results returned

### Why connect() and prapply() Are Top Functions

Looking at DSL operations:
- `connect()` - might use division internally
- `prapply()` - applies operations, might encounter division by zero

These aren't the real bottleneck - they're just the most expensive operations that DIDN'T crash!

---

## Immediate Investigation Steps

### Step 1: Check Generated Solver Code
```bash
# Look at generated batt.py to see if it has division operations:
grep -n "/ " batt.py | head -20
grep -n "%" batt.py | head -20
grep -n "divmod\|__truediv__\|__mod__" batt.py
```

### Step 2: Run a Simple 1-Task Test
```bash
# Test with just 1 task to see if error is consistent
python card.py -c 1

# Then check generated solver
head -100 batt.py

# Then test
python run_batt.py -i <task_id>
```

### Step 3: Check Error Context
```bash
# Look at full error messages
python profile_batt_framework.py --top 10 2>&1 | grep -A 5 "division"

# Or check if division by zero is in specific solver functions
python -c "from batt import *; print(dir())" 2>&1 | head -50
```

### Step 4: Compare with Previous Working Version
```bash
# Check if this is new behavior or was happening before
git log --oneline | head -10

# Test on previous commit
git show HEAD~5:dsl.py | grep -c "def " # Check old DSL
```

---

## Hypotheses

### Hypothesis 1: Mutations Generating Invalid Operations (Most Likely)
**Theory**: The genetic algorithm is creating solver mutations that include division by zero scenarios.

**Examples**:
```python
# Generated solver might do:
size_of_thing = 0  # From one mutation
result = value % size_of_thing  # Crashes!

# Or:
indices = get_nth_f(empty_set, 0)  # Crashes!
result = some_value / indices  # Crashes!
```

**Why Caching Affected It**:
- Type hints were preventing some mutations (they failed type checking)
- Now with caching, all mutations proceed (less type safety?)
- More mutations reach testing phase → more discover division by zero

**Solution**:
- Add division-by-zero guards in DSL operations
- Or add error handling in solver generation

### Hypothesis 2: Cache Returns Wrong Type Hints
**Theory**: Cache is incomplete or wrong type hints prevent proper type checking.

**Why This Could Happen**:
- Cache built at module load, but some functions defined later?
- Type hints are wrong/incomplete for some functions?
- Safe_dsl.py not using cache correctly?

**Solution**:
- Verify cache contents
- Check if type hints are correct
- Add debugging to see what cache returns

### Hypothesis 3: This is Normal Behavior
**Theory**: Mutations always fail often, this is expected.

**Why Possible**:
- Genetic algorithm generates 1000+ mutations
- ~99% fail
- Only valid ones saved
- Profiler captures all attempts, including failures

**This Would Be OK Because**:
- Framework is working as designed
- Failures are expected
- Profiler overhead is showing error path (connect, prapply handling exceptions)

**Why Concerning**:
- If 100% failure rate, something is broken
- Should have at least some valid solvers

---

## What To Do NOW

### Option A: Emergency Debug (15 min)
```bash
# Quick check: is this a cache issue or normal?
# Roll back cache changes temporarily
git stash
python profile_batt_framework.py --top 10
# See if same errors appear without cache

# If same errors: Not cache issue
# If no errors: Cache caused problem
```

### Option B: Investigate Generated Code (20 min)
```bash
# Look at what's being generated
python card.py -c 1
cat batt.py | head -200
# Check for suspicious operations

# Run one task manually
python run_batt.py -i <first_task_id> 2>&1 | head -50
```

### Option C: Add Debug Output (30 min)
```bash
# Add debugging to profile_batt_framework.py
# Catch exceptions and log what operation failed
# Identify which DSL operations are causing division by zero
```

---

## Expected vs Actual

### What We Expected
```
Kaggle run of 100 tasks:
├─ Wall-clock: ~2.7s (after cache speedup)
├─ Results: 1000+ solvers generated
├─ Bottleneck: get_type_hints, objects, o_g
└─ Success: Confirmed cache working
```

### What We Got
```
Kaggle run of 100 tasks:
├─ Wall-clock: 1.89s (but with errors!)
├─ Results: 0 solvers generated
├─ Bottleneck: connect, prapply, <genexpr>
└─ Status: All tasks failed with division by zero!
```

---

## Bottom Line

✅ **Good News**:
- Type hints cache is WORKING (only 854 _get_safe_default calls!)
- Code compiles and runs on Kaggle
- No import errors or hangs

❌ **Bad News**:
- Generated solvers are failing with division by zero
- 0 valid solvers from 100 tasks
- Profiling is showing error handling code, not real bottlenecks

⚠️ **Unclear**:
- Is this cache-related or normal behavior?
- Were previous profiling runs also generating broken solvers?
- Is "integer division or modulo by zero" expected in mutation testing?

---

## Action Items

### 🔴 URGENT (Do First)
1. **Verify this isn't cache-related**:
   ```bash
   git stash  # Temporarily remove cache
   python card.py -c 1
   python profile_batt_framework.py --top 10
   # Do same errors appear?
   ```

2. **Check generated code**:
   ```bash
   git stash pop  # Restore cache
   python card.py -c 1
   cat batt.py | grep -E "def |/|%" | head -30
   ```

### 🟡 NEXT (If Cache is Clean)
1. Identify which DSL operations are causing division by zero
2. Add guards/error handling
3. Or determine if 100% failure is expected

### 🟢 AFTER (Once Root Cause Found)
1. Fix the issue
2. Re-profile on Kaggle
3. Measure cache speedup on valid solvers

---

## Summary

The type hints cache is implemented and working (massive reduction in introspection calls). However, the Kaggle profiling shows ALL generated solvers failing with division by zero errors. 

**This needs investigation to determine if:**
1. Cache accidentally broke something (unlikely, evidence suggests no)
2. Division by zero is normal/expected in mutation testing (possible)
3. Something else changed on Kaggle (unlikely, same code)

**Next step**: Quick rollback test to see if errors persist without cache changes.

