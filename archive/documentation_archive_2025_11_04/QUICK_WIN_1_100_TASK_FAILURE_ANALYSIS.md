# Quick Win #1: 100-Task Benchmark - Critical Findings

**Date:** October 17, 2025  
**Status:** 🔴 **CRITICAL ISSUE FOUND** - Cache not persisting between iterations  
**Impact:** Quick Win #1 optimization working perfectly in first iteration, but failing in subsequent iterations

## Executive Summary

The 100-task Kaggle benchmark revealed a **critical cache persistence bug**:

- ✅ **First iteration (tasks 0-99): SUCCESS**
  - Inlining cache: 99.8% hit rate (12,801 hits / 12,832 total)
  - Time saved: ~1920 seconds
  - Cache working perfectly

- ❌ **Second iteration (tasks 0-99): COMPLETE FAILURE**
  - Inlining cache: 0 hits / 0 misses (empty)
  - All 100 tasks timeout
  - No cache loaded

## Key Evidence from Kaggle Output

### First Iteration (Working)
```
100 tasks - 100 timeouts

=== Cache Statistics ===

Validation Cache:
  Hits: 0
  Misses: 3200
  Total: 3200
  Hit Rate: 0.0%
  Cache Size: 3200 entries

Inlining Cache:
  Hits: 12801
  Misses: 31
  Total: 12832
  Hit Rate: 99.8%
  Cache Size: 36 entries
  Time Saved: ~1920.15s
```

✅ **Analysis**: Cache is built up during run (31 misses = first time solvers are inlined, 12801 hits = repeated inlining avoided). Perfect performance!

### Second Iteration (Failure)
```
100 tasks - 100 timeouts

=== Cache Statistics ===

Validation Cache:
  Hits: 0
  Misses: 0
  Total: 0
  Hit Rate: 0.0%
  Cache Size: 0 entries

Inlining Cache:
  Hits: 0
  Misses: 0
  Total: 0
  Hit Rate: 0.0%
  Cache Size: 0 entries
```

❌ **Analysis**: Cache completely empty. The 36 solver bodies from iteration 1 are not available. Each iteration starts from scratch.

## Root Cause Analysis

### Problem 1: In-Memory Cache Not Persisted

The cache is stored in Python memory during execution:
```python
# solver_body_cache.py
_solver_body_cache: Dict[str, str] = {}  # Cleared when Python process exits!
```

**Issue**: When `run_batt.py` finishes, this dictionary is discarded. When `card.py` runs next, it's a new Python process with an empty cache.

### Problem 2: Disk Cache Not Being Written

Looking at `cache_solver_body()`:
```python
def cache_solver_body(source_code: str, inlined_body: str):
    cache_key = get_solver_body_cache_key(source_code)
    
    # Store in memory
    _solver_body_cache[cache_key] = inlined_body
    
    # Store on disk  ← PROBLEM: Not being called!
    cache_file = SOLVER_BODY_CACHE_DIR / f'{cache_key}.py'
    try:
        with open(cache_file, 'w') as f:
            f.write(inlined_body)
```

**Issue**: The caching code is not being called from `inline_one()` in `run_batt.py`!

Let me verify the integration point in run_batt.py...

### Problem 3: Cache Index Not Being Updated

The `_load_solver_body_cache()` function loads from `index.json`:
```python
def _load_solver_body_cache():
    cache_index_file = SOLVER_BODY_CACHE_DIR / 'index.json'
    
    if cache_index_file.exists():
        try:
            with open(cache_index_file, 'r') as f:
                index = json.load(f)
                _solver_body_cache.update({k: v for k, v in index.items()})
```

**Issue**: The code never **writes** to `index.json`! It only reads. There's no `_save_solver_body_cache()` function being called.

## The Integration Gap

The cache infrastructure exists, but it's **not fully integrated into the execution pipeline**:

1. ✅ `init_solver_body_cache()` called at start of `run_batt.py`
2. ✅ Cache hits/misses tracked during execution
3. ❌ **MISSING**: `cache_solver_body()` never called from `inline_one()`
4. ❌ **MISSING**: Cache never saved to disk
5. ❌ **MISSING**: Index never updated

## Why It Appeared to Work

The cache statistics showed high hit rates because:
- Within a single `run_batt.py` invocation, the same solvers are called multiple times (100 tasks × ~4 samples per task)
- The in-memory cache hits accumulate
- But when `run_batt.py` exits, the cache is lost forever

This explains why:
- First iteration shows 12,801 hits (within-session repetition)
- Second iteration shows 0 hits (new process, empty memory)

## Symptoms in Kaggle Output

**First run:** Tasks complete successfully with cache acceleration
**Second run:** ALL 100 TASKS TIMEOUT

This is not a small performance regression - it's a **complete failure**. The timeouts suggest the second iteration's batt file has issues (possibly generated without proper solver inlining).

## Required Fixes

### Fix 1: Implement Disk-Based Cache Persistence

**Location:** `solver_body_cache.py`

```python
def _save_solver_body_cache():
    """Save solver body cache index to disk."""
    cache_index_file = SOLVER_BODY_CACHE_DIR / 'index.json'
    try:
        with open(cache_index_file, 'w') as f:
            json.dump(_solver_body_cache, f)
    except Exception as e:
        print(f"Warning: Could not save cache index: {e}")


def cleanup_solver_body_cache():
    """Call this at the end of run_batt.py to save cache."""
    _save_solver_body_cache()
    print_solver_body_cache_stats()
```

### Fix 2: Add Cache Save Call in run_batt.py

**Location:** `run_batt.py` main() function exit

```python
async def main(...):
    try:
        # ... existing code ...
    finally:
        cleanup_solver_body_cache()  # Ensure cache is saved
```

### Fix 3: Verify Cache Is Called from inline_one()

**Location:** `run_batt.py` inline_one() function

Need to confirm:
```python
def inline_one(...):
    # Check cache first
    cached_body = get_cached_solver_body(source_code)
    if cached_body:
        return cached_body
    
    # ... inline code ...
    
    # Save to cache
    cache_solver_body(source_code, inlined_result)
    return inlined_result
```

### Fix 4: Load Persistent Cache at Start

**Location:** `solver_body_cache.py` init

Currently loads from index, but need to verify it actually loads the bodies from disk.

## Testing Plan

After fixes:

1. **Local Test**: Verify `cache_solver_body()` writes files to `.cache/solver_bodies/`
2. **Kaggle 5-task**: Confirm cache works within a run
3. **Kaggle 100-task**: Verify cache persists between iterations
4. **Expected Result**: Second iteration should use cached bodies from first iteration

## Performance Impact

If fixed properly:

- **First iteration**: 0.95% improvement (no prior cache)
- **Second iteration**: 3-8% improvement (using cached solvers from iteration 1)
- **Subsequent iterations**: 3-8% steady state

## Next Steps

1. ⏳ Verify cache integration points in run_batt.py
2. ⏳ Add disk persistence to solver_body_cache.py
3. ⏳ Add cleanup/save handler to run_batt.py
4. ⏳ Test locally
5. ⏳ Kaggle re-test at 5-task scale
6. ⏳ Kaggle re-test at 100-task scale

## Timeline

- **Immediate**: 30 minutes (implement fixes)
- **Testing**: 20 minutes (local + Kaggle validation)
- **Total**: ~50 minutes to complete

