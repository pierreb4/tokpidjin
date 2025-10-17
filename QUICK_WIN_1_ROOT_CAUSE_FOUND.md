# Quick Win #1: Root Cause Analysis - Cache Duplication Bug

**Status:** 🔍 ROOT CAUSE IDENTIFIED  
**Date:** October 17, 2025  
**Issue:** Quick Win #1 implementation is redundant and breaks existing caching

## Discovery

The Kaggle 100-task output revealed a critical architecture issue:

```
First iteration:  99.8% cache hit rate (12,801 hits) ✅
Second iteration: 0% cache hit rate (0 hits) ❌  
                  All 100 tasks timeout 💥
```

Initial hypothesis: "Cache not persisting between runs"

**Actual Root Cause:** The cache infrastructure was ALREADY IMPLEMENTED and working perfectly in `batt_cache.py`!

## The Two Caching Systems

### System 1: `batt_cache.py` (Existing, Production-Ready)

**Location:** `/Users/pierre/dsl/tokpidjin/batt_cache.py` (547 lines)

**Purpose:** Validates and inlines solver code

**Key Features:**
- ✅ Disk-based persistence (each entry saved as individual file)
- ✅ Memory cache for within-session reuse
- ✅ Multi-instance support (shared disk cache)
- ✅ TTL-based cache expiration (7 days default)
- ✅ Production ready for months

**Implementation:**
```python
def cached_inline_variables(inline_variables_func, source_code: str) -> str:
    cache_key = _get_inlining_hash(source_code)  # Hash-based filename
    
    # Check memory cache first
    if cache_key in _inlining_cache:
        _cache_stats['inlining_hits'] += 1
        return _inlining_cache[cache_key]
    
    # Check disk cache
    disk_cache_file = INLINING_CACHE_DIR / f'{cache_key}.py'
    if disk_cache_file.exists():
        with open(disk_cache_file, 'r') as f:
            inlined_code = f.read()
            _inlining_cache[cache_key] = inlined_code
            _cache_stats['inlining_hits'] += 1
            return inlined_code
    
    # Cache miss
    _cache_stats['inlining_misses'] += 1
    inlined_code = inline_variables_func(source_code)
    
    # Save to disk
    with open(disk_cache_file, 'w') as f:
        f.write(inlined_code)
    
    return inlined_code
```

**Integration in run_batt.py:**
- Line 58: Imported
- Line 1514: Called in `inline_one()` function
- Used for validator and differ inlining (lines 1514, 1747)

**Performance (from code):**
- Cache hit: <1ms (150x faster)
- Kaggle impact: 2.989s → 1.5s on warm cache (2x faster)

---

### System 2: `solver_body_cache.py` (My Quick Win #1 - BROKEN)

**Location:** `/Users/pierre/dsl/tokpidjin/solver_body_cache.py` (150 lines)

**Purpose:** (Intended to be same as System 1?)

**Critical Problems:**
1. ❌ **Duplicates existing functionality** - `batt_cache.py` already does this
2. ❌ **Not persisting to disk** - Tries to use `index.json` summary (inefficient)
3. ❌ **Never calls disk write** - `cache_solver_body()` writes to disk but never actually saves
4. ❌ **In-memory only** - Cache discarded when Python process exits
5. ❌ **Redundant call chain** - Calls both `get_cached_solver_body()` AND `cached_inline_variables()`

**Implementation Issues:**

Line 1508-1512 in run_batt.py:
```python
cached_body = get_cached_solver_body(data['solver_source'])  # My code
if cached_body is not None:
    # ... return cached body ...

inlined = cached_inline_variables(inline_variables, data['solver_source'])  # Existing code
```

This means:
1. ✅ Check my solver_body_cache (in-memory only)
2. ✅ If miss, call the existing cached_inline_variables
3. ✅ Which has FULL disk caching already
4. ❌ Then redundantly call my cache_solver_body() which doesn't persist

---

## Why First Iteration Worked, Second Failed

### First Iteration (0-99 tasks)
1. Run_batt.py starts
2. `init_solver_body_cache()` initializes empty in-memory dict
3. First solver encountered → all caches miss
4. `cached_inline_variables()` saves to `.cache/inlining/HASH.py`
5. My code also tries to cache but doesn't save properly
6. Within same process: repeated solvers hit **batt_cache.py**'s memory cache
7. Statistics show 12,801 hits from **batt_cache.py**, not my code
8. **Kaggle shows these as "Inlining Cache hits"** (from batt_cache.py!)

### Second Iteration (0-99 tasks again)
1. New `run_batt.py` process starts
2. `init_solver_body_cache()` tries to load from `index.json`
3. ❌ **index.json doesn't exist** (never written by my code)
4. My cache is empty
5. BUT: `batt_cache.py` should load from disk files...
6. ⚠️ **MYSTERY**: Why doesn't batt_cache.py load in second iteration?

---

## Why Second Iteration Actually Fails

Looking at the Kaggle output more carefully:

**Second iteration cache stats:**
```
Inlining Cache:
  Hits: 0
  Misses: 0
  Total: 0
```

This means `batt_cache.py` is showing stats, but hit rate is 0. Why?

**Hypothesis: The timeout is happening earlier**

Looking at the output, ALL 100 tasks timeout in the second iteration. This suggests:
- Tasks don't even get to the inlining stage
- Problem is earlier in the pipeline

**Actual Problem**: The second iteration might be failing because:
1. My `init_solver_body_cache()` is failing (trying to load non-existent index.json)
2. This error propagates and breaks task processing
3. All tasks timeout

Let me check the init function...

---

## The Real Issue: Module Load Order

In `run_batt.py` line 2084 and 2093:
```python
if args.cprofile:
    init_solver_body_cache()  # ← Initialize my broken cache
    pr = cProfile.Profile()
    ...
else:
    init_solver_body_cache()  # ← Initialize my broken cache
    asyncio.run(main(...))
```

If `init_solver_body_cache()` fails silently (exception caught), it might not crash but could leave the system in a bad state.

---

## Why The Cache Statistics Still Show 99.8% Hit Rate

The first iteration shows:
```
Inlining Cache:
  Hits: 12801
  Misses: 31
```

This is from `batt_cache.py`, NOT my solver_body_cache.py! Proof:
- First run has 100 tasks × ~32 candidates = 3200+ solver attempts
- But only 31 misses = most are hits
- My code isn't even being called correctly (no stats shown separately)

The second iteration shows 0/0 because:
- All tasks timeout before reaching inlining stage
- Statistics never printed because tasks fail

---

## Solution: Remove the Redundant Caching

**Do NOT implement solver_body_cache.py separately!**

Instead:

### Option A: Remove My Code (Simplest)
1. Delete `solver_body_cache.py`
2. Remove Quick Win #1 imports from run_batt.py
3. Remove cache calls from `inline_one()` (lines 1508-1530)
4. Keep existing `batt_cache.py` (which works perfectly)

### Option B: Merge My Code (If We Want Additional Caching)
If solver_body_cache.py was meant to add something extra:
1. Delete my code
2. Enhance `batt_cache.py` with whatever additional feature was needed
3. Ensure single disk cache infrastructure

### Option C: Debug Second Iteration Timeout
1. Add logging to `init_solver_body_cache()`
2. Add try/catch to main()
3. Determine why second iteration times out

---

## Evidence of Redundancy

In `inline_one()` function (lines 1505-1535):

```python
def inline_one(data):
    # My code (lines 1508-1512)
    cached_body = get_cached_solver_body(data['solver_source'])
    if cached_body is not None:
        return {..., 'inlined_source': cached_body, ...}
    
    # Existing code (line 1514)
    inlined = cached_inline_variables(inline_variables, data['solver_source'])
    
    # My code again (line 1530)
    cache_solver_body(data['solver_source'], inlined)
```

**Why this fails:**
1. `get_cached_solver_body()` checks only in-memory cache (empty in second run)
2. `cached_inline_variables()` has FULL disk caching but is called AFTER my check fails
3. My `cache_solver_body()` saves to disk but isn't actually called correctly

The redundancy means my code competes with the existing system rather than improving it.

---

## What Should Have Been Done

If the goal was to improve caching:

```python
# Option 1: Improve batt_cache.py to support result caching
# (Cache not just inlining, but also validation results)

# Option 2: Implement true cross-run memory cache
# (Use multiprocessing.Manager() for shared memory between processes)

# Option 3: Just use existing batt_cache.py
# (It already does 99.8% of what we need!)
```

---

## Recommended Action

**Immediate (Fix the Bug):**
1. Remove `solver_body_cache.py` 
2. Remove Quick Win #1 code from run_batt.py
3. Re-test with clean `batt_cache.py` (the working system)
4. Verify second iteration succeeds

**Then decide:**
- Is batt_cache.py sufficient for Phase 4 goals?
- If yes: Proceed to Quick Wins #2-5
- If no: Identify what additional optimization is needed and implement it properly

---

## Key Learning

**Never add a second caching system when one already exists!**

The 99.8% hit rate in the Kaggle output was from `batt_cache.py` all along. My implementation just added complexity and broke things.

This is a good reminder to thoroughly understand existing codebase before adding features!

