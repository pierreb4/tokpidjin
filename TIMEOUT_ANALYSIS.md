# Timeout Analysis - Run_Batt.py Frequent Timeouts

## Problem Summary
run_batt.py shows frequent timeouts when testing generated tmp_batt_onerun_run.py files. This happens with different generated solvers, suggesting the issue is systemic rather than solver-specific.

## Key Findings

### 1. Timeout Configuration
- **Default timeout**: 10 seconds (set in argparse line 2098 of run_batt.py)
- **Timeout location**: In `check_solver()` function (run_test.py line 272)
- **Per-sample execution**: Each sample gets the full timeout duration

### 2. Execution Flow
```
run_batt.py (main orchestrator)
  └─> Phase 3a: Batch validate solvers
      └─> check_one_solver() (async)
          └─> cached_check_solver()
              └─> check_solver() (async, run_test.py:272)
                  └─> run_with_timeout() (utils.py:715)
                      └─> loop.run_in_executor(executor, func, *args)
                          └─> solve_func(S, sample['input'], None)
```

### 3. Timeout Issues

#### Issue 1: Multiple Samples Per Solver
- Each solver is tested on ALL samples (demo + test) in sequence
- Total samples per task: ~25 (15 demo + 10 test)
- Each sample gets full 10s timeout
- **Risk**: One slow sample causes timeout for entire solver

#### Issue 2: Generated Solver Complexity
Generated solvers in tmp_batt_onerun_run.py call:
- Expensive DSL operations: `gravitate`, `o_g`, `colorfilter`, etc.
- Chained function calls through `rbind()` closures
- Variable lookup and exception handling overhead

**Example from tmp_batt_onerun_run.py:**
```python
try:
    t8 = rbind(o_g, R5)
    t9 = t8(I)  # Calls rbind closure
    t10 = t8(C) # Calls rbind closure again
except (TypeError, AttributeError, ValueError, IndexError, KeyError):
    t8 = _get_safe_default(rbind)
```

#### Issue 3: Exception Handling Overhead
- Every generated call wrapped in try/except
- Exception handling calls `_get_safe_default()` which:
  - Introspects function type hints (even with caching, still overhead)
  - Creates safe default values
  - Adds 5-10ms per exception

#### Issue 4: Thread/Process Overhead
- Uses ThreadPoolExecutor for async execution
- Thread creation/destruction overhead for each sample
- Race conditions in thread cleanup (hence the monkey-patch in run_batt.py lines 32-46)

### 4. Bottleneck Operations

Based on code inspection, these operations are likely slow:
- **o_g()** / **o_g_t()**: Objects extraction with multiple iterations
- **gravitate()**: Position shifting with complex logic
- **colorfilter()** / **sizefilter()**: Filtering with object traversal
- **flood_fill()**: Recursive or iterative fill operations
- **rbind()**: Creates closures with captured state

### 5. Cache Issue

The `cached_check_solver()` has a cache, but cache hits depend on:
- Identical solver source
- Identical task_id
- Identical sol_solver_id

Generated solvers are often unique, so cache misses are common.

## Root Causes

1. **Timeout is too aggressive**: 10s for multiple samples with complex operations
2. **Synchronous sample processing**: Sequential testing on 25 samples means one slow sample blocks others
3. **No timeout per-sample**: Entire 10s allocated to one sample if it's slow
4. **Exception overhead**: Generated code throws many exceptions for type mismatches
5. **Thread cleanup issues**: Race conditions during cleanup add latency

## Solutions

### Short Term (Quick Fixes)
1. **Increase timeout**: Change default from 10s to 30-60s
   - Line 2098 in run_batt.py: `default=60` instead of `default=10`

2. **Per-sample timeout**: Allocate timeout per sample instead of per solver
   - In check_solver(): timeout_per_sample = timeout / num_samples

3. **Early exit on timeout**: Stop testing remaining samples if one times out
   ```python
   if did_timeout:
       break  # Stop testing other samples
   ```

### Medium Term (Implementation)
1. **Profile generated solvers** to identify slow operations
2. **Optimize exception handling** in generated code
3. **Use sample-level parallelization** instead of sequential
4. **Cache solver metadata** to avoid repeated introspection

### Long Term (Architecture)
1. **GPU acceleration** for expensive DSL operations
2. **JIT compilation** for frequently called operations
3. **Solver analysis** during generation to predict timeout risk
4. **Adaptive timeout** based on solver complexity

# Timeout Analysis - Run_Batt.py Frequent Timeouts - ROOT CAUSE FOUND ✅

## CRITICAL FINDING

**The "timeouts" are NOT actually timeouts - they're EXCEPTIONS being silently caught and reported as timeouts!**

### Root Cause: Exception Handling in call_with_timeout()

In `utils.py` line 150-155:

```python
# Check for exceptions
try:
    exception = exception_queue.get_nowait()
    # Re-raise critical exceptions immediately
    if isinstance(exception, (MemoryError, SystemError, KeyboardInterrupt)):
        raise exception
    # Log other exceptions if needed for debugging
    # print(f"Exception in timeout thread: {type(exception).__name__}: {exception}")
    return True, None  # Treat non-critical exceptions as timeouts
except Empty:
    pass
```

**Any exception that occurs in batt() is caught and returned as `(True, None)` - which is identical to a timeout!**

So when the log says "timed out", it actually means an exception occurred during solver execution.

## What Exceptions Are Happening?

The generated solvers (`tmp_batt_onerun_run.py`) are calling DSL functions with mismatched types or incorrect arguments, causing exceptions. These exceptions are being silently treated as timeouts.

## Solution

**Enable exception logging to see what's actually failing**:

In `utils.py` line 153, change from:
```python
        # print(f"Exception in timeout thread: {type(exception).__name__}: {exception}")
```

To:
```python
        print_l(f"Exception in timeout thread: {type(exception).__name__}: {exception}")
        raise exception  # Let user see the actual error
```

This will reveal what exceptions are occurring in the generated solvers.

## Why This Started After Recent Changes

The restoration from ff140d60 restored old solvers_pre.py, but the current dsl.py has been modified multiple times since. There may be:
1. Mismatch in function signatures
2. Missing or renamed functions
3. Type system inconsistencies

The exception masking is hiding these problems and showing them as "timeouts" instead.

## Immediate Actions

1. **Uncomment exception logging** in utils.py to see real errors
2. **Check generated solver compatibility** - verify tmp_batt_onerun_run.py matches current dsl.py
3. **Review type hint changes** - particularly TTT_iii, INT_TYPE_RANGES, HINT_OVERLAPS
