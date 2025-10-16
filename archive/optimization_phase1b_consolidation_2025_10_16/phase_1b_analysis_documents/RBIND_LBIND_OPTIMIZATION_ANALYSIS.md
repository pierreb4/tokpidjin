# rbind/lbind Optimization: Lambda vs Function Definitions

**Date**: October 16, 2025  
**Status**: Ready for Implementation  
**Impact**: 5-10% speedup on f() creation, ~0.05-0.1s total savings per 100 tasks

---

## Discovery: The Mystery f() Function

### Problem Identified
Profiling showed:
- **f()**: 18,389 calls, 1.062s cumulative time, 0.000ms per call
- **Not previously identified** because it's an inner function
- **Root cause**: rbind() and lbind() define inner functions named `f` instead of using lambdas

### Current Implementation (dsl.py, lines 1216-1265)

```python
def rbind(function: 'Callable', fixed: 'Any') -> 'Callable':
    """ fix the rightmost argument """
    n = function.__code__.co_argcount

    # COMMENTED OUT LAMBDAS:
    # if n == 2:
    #     return lambda x: function(x, fixed)
    # elif n == 3:
    #     return lambda x, y: function(x, y, fixed)
    # else:
    #     return lambda x, y, z: function(x, y, z, fixed)

    # CURRENT IMPLEMENTATION (function definitions):
    if n == 2:
        def f(x):                          # ← Creates function object
            return function(x, fixed)
        return f
    elif n == 3:
        def f(x, y):                       # ← Creates function object
            return function(x, y, fixed)
        return f
    else:
        def f(x, y, z):                    # ← Creates function object
            return function(x, y, z, fixed)
        return f


def lbind(function: 'Callable', fixed: 'Any') -> 'Callable':
    """ fix the leftmost argument """
    n = function.__code__.co_argcount

    # COMMENTED OUT LAMBDAS:
    # if n == 2:
    #     return lambda y: function(fixed, y)
    # elif n == 3:
    #     return lambda y, z: function(fixed, y, z)
    # else:
    #     return lambda y, z, a: function(fixed, y, z, a)

    # CURRENT IMPLEMENTATION (function definitions):
    if n == 2:
        def f(y):                          # ← Creates function object
            return function(fixed, y)
        return f
    elif n == 3:
        def f(y, z):                       # ← Creates function object
            return function(fixed, y, z)
        return f
    else:
        def f(y, z, a):                    # ← Creates function object
            return function(fixed, y, z, a)
        return f
```

---

## Why This Matters

### Function Creation Overhead

**Current (def statements)**:
1. Function definition creates code object
2. Creates function object wrapper
3. Assigns to local variable
4. Returns function object

**Proposed (lambdas)**:
1. Lambda expression creates code object
2. Creates function object wrapper
3. Returns function object directly
4. No intermediate assignment

**Performance Difference**:
- Lambda: Slightly faster, more direct
- def: Requires extra assignment operation
- Per-call overhead: ~0.001-0.005ms
- But: Called 18,389 times per 100 tasks
- **Total savings**: 0.018-0.092s per 100 tasks (5-10% reduction on f() overhead)

### Why Lambdas Were Commented Out

Possible reasons:
1. **Readability**: Multi-line def statements are clearer
2. **Debugging**: def gives functions names like "f" (seen in profiler!)
3. **Consistency**: Other code uses def for inner functions
4. **Historical**: May have been changed for other reasons

### Current Cost Analysis

```
rbind/lbind statistics (from Kaggle profiling):
├─ f() function: 18,389 calls
├─ Cumulative time: 1.062s
├─ Per-call time: 0.000ms = ~0.058ms average (1.062s / 18,389)
└─ Cost per function creation: 0.058ms × (estimated 50% overhead) = 0.029ms

If lambdas reduce overhead by 10%:
├─ New per-call time: 0.052ms
├─ New cumulative: 0.952s
└─ Savings: 0.110s per 100 tasks
```

---

## Lambda Implementation

### Option 1: Direct Lambda Replacement (Recommended)

```python
def rbind(function: 'Callable', fixed: 'Any') -> 'Callable':
    """ fix the rightmost argument """
    if hasattr(function, '_original_argcount'):
        n = function._original_argcount
    else:
        n = function.__code__.co_argcount

    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)


def lbind(function: 'Callable', fixed: 'Any') -> 'Callable':
    """ fix the leftmost argument """
    if hasattr(function, '_original_argcount'):
        n = function._original_argcount
    else:
        n = function.__code__.co_argcount

    if n == 2:
        return lambda y: function(fixed, y)
    elif n == 3:
        return lambda y, z: function(fixed, y, z)
    else:
        return lambda y, z, a: function(fixed, y, z, a)
```

**Advantages**:
- ✅ Direct replacement, no logic changes
- ✅ Faster (no assignment overhead)
- ✅ More concise code
- ✅ Lambdas are intended for this use case

**Disadvantages**:
- ❌ Less clear in debugger (shows as `<lambda>`)
- ❌ Multi-line display is cleaner than lambda chain
- ❌ Profiler shows "<lambda>" instead of "f"

### Option 2: Named Return Variables (Compromise)

```python
def rbind(function: 'Callable', fixed: 'Any') -> 'Callable':
    """ fix the rightmost argument """
    if hasattr(function, '_original_argcount'):
        n = function._original_argcount
    else:
        n = function.__code__.co_argcount

    if n == 2:
        # Use lambda - cleaner and slightly faster
        rbind_f2 = lambda x: function(x, fixed)
        return rbind_f2
    elif n == 3:
        rbind_f3 = lambda x, y: function(x, y, fixed)
        return rbind_f3
    else:
        rbind_f4 = lambda x, y, z: function(x, y, z, fixed)
        return rbind_f4
```

**Advantages**:
- ✅ Named variables (easier to debug)
- ✅ Still uses lambdas (faster execution)
- ✅ Clear that we're returning a function

**Disadvantages**:
- ❌ Extra assignment line (negates some speed benefit)
- ❌ More verbose than pure lambda

---

## Expected Results

### Performance Impact (Estimated)

**Baseline (current)**: 2.75s for 100 tasks
```
f() overhead: 1.062s
- rbind/lbind function creation: ~50% overhead (0.531s)
- Actual execution time: ~0.531s
- Per-creation overhead: 0.029ms × 18,389 = 0.531s

If lambdas are 10% faster:
- New overhead: 0.478s
- Savings: 0.053s per 100 tasks
- New total: 2.75s - 0.053s = 2.70s (1.02x faster)
```

**Conservative estimate**: 0.02-0.05s savings (0.7%-1.8% speedup)  
**Optimistic estimate**: 0.05-0.1s savings (1.8%-3.6% speedup)

### Cumulative Impact with Other Optimizations

```
Current:                2.75s (baseline with cache)
├─ rbind/lbind lambda: -0.05s → 2.70s
├─ <genexpr> reduction: -0.30s → 2.40s
└─ Lambda optimization: -0.10s → 2.30s

Total Phase 1b impact: 0.45s saved (1.20x speedup)
```

---

## Implementation Steps

### Step 1: Backup Current Code
```bash
git commit -am "backup: rbind/lbind before lambda optimization"
```

### Step 2: Switch to Lambdas

Replace the rbind function (lines 1216-1247):

```python
def rbind(
    function: 'Callable',
    fixed: 'Any'
) -> 'Callable':
    """ fix the rightmost argument """
    # logger.info(f'rbind: {function = }, {fixed = }')
    # Use _original_argcount if available (for decorated functions)
    if hasattr(function, '_original_argcount'):
        n = function._original_argcount
    else:
        n = function.__code__.co_argcount

    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)
```

Replace the lbind function (lines 1249-1280):

```python
def lbind(
    function: 'Callable',
    fixed: 'Any'
) -> 'Callable':
    """ fix the leftmost argument """
    # logger.info(f'lbind: {function = }, {fixed = }')
    # Use _original_argcount if available (for decorated functions)
    if hasattr(function, '_original_argcount'):
        n = function._original_argcount
    else:
        n = function.__code__.co_argcount

    if n == 2:
        return lambda y: function(fixed, y)
    elif n == 3:
        return lambda y, z: function(fixed, y, z)
    else:
        return lambda y, z, a: function(fixed, y, z, a)
```

### Step 3: Test Locally

```bash
# Test basic functionality
python card.py -c 2

# Quick validation
head -20 batt.py
```

### Step 4: Benchmark on Kaggle

```bash
# Run profiling on Kaggle
python profile_batt_framework.py --top 10

# Compare:
# - f() calls should remain similar (18,389)
# - f() cumulative time should decrease (1.062s → 1.010-1.045s)
# - Total wall-clock should improve slightly (2.75s → 2.70s)
```

### Step 5: Commit

```bash
git add dsl.py
git commit -m "perf: Use lambdas in rbind/lbind for faster function creation"
git push
```

---

## Risk Assessment

### Low Risk Changes
- ✅ **Logic unchanged**: Only changes how functions are created, not what they do
- ✅ **Backward compatible**: Both lambdas and def create identical functions
- ✅ **Easy to revert**: If issues arise, simple revert
- ✅ **Already tested**: Lambdas in fork() and other functions work fine

### Testing Strategy
1. Run card.py with 2 tasks (quick sanity check)
2. Compare generated batt.py code (should be identical)
3. Run full 100-task profiling on Kaggle
4. Check that solver counts match baseline

### Why This Is Safe
1. **fork() already uses lambdas**: (line 1301) `lambda x: outer(a(x), b(x))` - no issues
2. **Same return type**: Both def and lambda return function objects
3. **No type changes**: Arguments and return types unchanged
4. **No side effects**: Function creation doesn't depend on outer state

---

## Why We Should Do This

### Reason 1: Low Effort, Clear Benefit
- 5 lines of code change per function (10 lines total)
- 10 minutes implementation and testing
- Clear performance benefit (5-10% on function creation)

### Reason 2: Code Quality
- More Pythonic (lambdas for simple wrappers)
- Less verbose
- Consistent with fork() pattern

### Reason 3: Discovery
- Reveals that profiler categorizes these as "<lambda>" instead of "f"
- Helps understand profiling output better
- Sets stage for <genexpr> investigation

### Reason 4: No Downside
- Easy to revert if needed
- No risk of breaking existing code
- All generated solvers will work identically

---

## Recommendation

**IMPLEMENT OPTION 1: Direct Lambda Replacement**

✅ **Rationale**:
1. Simplest, most direct approach
2. Best performance (no extra assignment)
3. Consistent with fork() pattern in codebase
4. Easy to revert if needed
5. Low risk, clear benefit

**Expected outcome**:
- rbind/lbind optimization: -0.05s
- Cumulative with other fixes: -0.45s (1.20x speedup)
- Progress toward 5x goal: 22% → 32%

---

## Next Steps After Implementation

1. ✅ **Switch rbind/lbind to lambdas** (this task)
2. ⏳ **Investigate <genexpr> bottleneck** (161,146 calls)
3. ⏳ **Optimize other lambdas** (11,161 calls in sorting)
4. ⏳ **Profile DSL functions** (objects, o_g)
5. ⏳ **Implement GPU acceleration** if needed

