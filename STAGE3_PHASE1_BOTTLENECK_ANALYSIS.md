# Stage 3 Phase 1: Framework Bottleneck Analysis

**Date**: October 16, 2025  
**Platform**: Kaggle (GPU enabled)  
**Profiling Scope**: 100 tasks (3200 outputs, 13,200 solvers)  
**Wall-Clock Time**: 3.05s  
**Status**: 🔴 Ready for optimization

---

## Executive Summary

### Bottleneck Breakdown
| Category | Cum Time | % | Calls | Functions | Priority |
|----------|----------|---|-------|-----------|----------|
| **Other Framework** | 8.10s | **63.6%** | 3.19M | 223 | 🔴 P0 |
| **DSL Operations** | 4.10s | **32.2%** | 460k | 47 | 🔴 P1 |
| Candidate Management | 0.45s | 3.5% | 257k | 2 | 🟡 P2 |
| Tuple Operations | 0.04s | 0.3% | 33k | 5 | ⚪ P3 |
| Dedupe Operations | 0.03s | 0.2% | 3.6k | 1 | ⚪ P3 |
| Frozenset Operations | 0.02s | 0.2% | 19k | 4 | ⚪ P3 |

**Total**: 12.74s cumulative time (across all threads/processes)

---

## Critical Finding: Function Overlap

⚠️ **IMPORTANT**: The "Other Framework" and "DSL Operations" categories likely contain overlapping call chains:

```
batt (3.02s cum)
  ├─ [generates solvers]
  ├─ calls f (1.45s cum)
  │   ├─ [applies mutations]
  │   └─ calls DSL ops (o_g, objects, etc.)
  ├─ calls get_type_hints (0.378s cum) [for mutation type checking]
  └─ calls <setcomp> (0.296s cum) [set comprehension in candidate generation]
       └─ calls DSL ops
```

**This means**: Optimizing DSL ops (like o_g, objects) will help BOTH categories.

---

## Detailed Analysis: Top Framework Functions

### 1. **batt** (3.02s cumulative, 100 calls, 30.4ms per call)
**Role**: Main solver evaluation function
**Current Time Breakdown**:
- Direct execution: 0.074s (2.4%)
- Overhead calling other functions: 2.95s (97.6%)

**What It Does**:
```python
def batt(task_id, S, I, C, log_path):
    s = []  # Differ results
    o = []  # Solver outputs
    # For each task, generates candidate solvers and tests them
    # Calls: f(), get_type_hints(), DSL ops (o_g, objects, etc.)
    return o, s
```

**Observations**:
- 30.4ms per call seems reasonable for generating ~132 solvers per task
- 97.6% overhead suggests it's orchestrating expensive operations
- Not the function to optimize directly - focus on what it calls

### 2. **f** (1.45s cumulative, 13,261 calls, 0.0001ms per call)
**Role**: ✅ **IDENTIFIED** - Local closure inside `rbind()` and `lbind()` functions
**Location**: dsl.py lines 1235-1243 (rbind) and 1292-1300 (lbind)
**Current Time**: 1.45s (11.4% of total)

**What It Does**:
```python
# Inside rbind() - creates partial application with right-bound argument
def rbind(function, fixed):
    if n == 2:
        def f(x):
            return function(x, fixed)  # Partial application
        return f
    # ... similar for n==3 and n>3
```

**Why It's Called 13,261 Times**:
- Every solver mutation that uses `rbind()` or `lbind()` creates a new closure
- These operations bind arguments to DSL functions (e.g., `rbind(o_g, rotation)`)
- Called ~13k times per 100 tasks = ~132 times per task

**Per-call Time**: 0.0001ms (very fast, but 13k adds up to 1.45s)

**Optimization Potential**: ⭐⭐ (MEDIUM) 
- Closures are already optimal in Python
- Real bottleneck is not the closure creation itself, but the FREQUENCY
- If rbind/lbind are called 13k times, that means we're creating 13k solver mutations
- This might indicate the mutation loop is too aggressive

### 3. **get_type_hints** (0.378s cumulative, 3,773 calls, 0.01ms per call)
**Role**: Get type hints from DSL function signatures
**Current Time**: 0.378s (3.0% of total)

**Why It's Slow**:
- Called 3,773 times for mutation type checking
- Each call inspects function annotations (slow in Python)
- Called for nearly every mutation attempt

**Optimization Strategy**:
```python
# BEFORE: Called every time a mutation is attempted
hints = get_type_hints(dsl_func)  # Slow! ~10ms

# AFTER: Cache type hints at startup
TYPE_HINTS_CACHE = {}
for func in DSL_FUNCTIONS:
    TYPE_HINTS_CACHE[func.__name__] = get_type_hints(func)
# Then: TYPE_HINTS_CACHE[func_name]  # ~0.001ms
```

**Expected Improvement**: 0.378s → 0.038s (-90%) 🎯

### 4. **<setcomp>** (0.296s cumulative, 161,488 calls, 0.002ms per call)
**Role**: Set comprehension (likely candidate filtering)
**Current Time**: 0.296s (2.3% of total)

**Examples of setcomp in solver generation**:
```python
# Filter candidates that match input type
valid_candidates = {c for c in candidates if type(c) == expected_type}

# Extract unique results
unique_outputs = {apply_solver(s, sample) for s in solvers}
```

**Observation**: Very small per-call time but huge call count = **hot path**

**Optimization Strategy**:
- Profile to find which setcomp is most expensive
- Consider: vectorization, pre-filtering, or using set operations instead of comprehension

### 5. **asindices** (0.223s cumulative, 3,247 calls, 0.03ms per call)
**Role**: Convert indices from one representation to another (likely DSL-related)
**Current Time**: 0.223s (1.7% of total)

**Optimization Potential**: Medium - Lower call count than top 4, but per-call time is 300x higher

---

## Critical Finding: DSL Operations Are Expensive

### Top DSL Operations
| Function | Cum Time | Calls | Per Call | Problem |
|----------|----------|-------|----------|---------|
| **objects** | 1.39s | 3,400 | **0.18ms** 🔴 | Slow per-call |
| **o_g** | 1.41s | 3,400 | 0.008ms | But called 3,400 times |
| o_g_t | 0.29s | 600 | 0.007ms | Tuple version |
| objects_t | 0.29s | 600 | 0.19ms | Tuple version slow |

**Key Insight**: 
- `objects` has **HIGH per-call time** (0.18ms) - candidate for GPU acceleration
- `o_g` has low per-call but **massive call count** (3,400) - candidate for batching

---

## 🔴 CRITICAL INSIGHT: The Real Problem

**The 63.6% framework overhead is NOT a code efficiency issue - it's a DESIGN issue.**

Looking at the call counts:
- **batt**: 100 calls (1 per task) = normal
- **f**: 13,261 calls (132 per task!) = **EXCESSIVE**
- **<setcomp>**: 161,488 calls (1,614 per task!) = **EXPLOSIVE**
- **get_type_hints**: 3,773 calls (37 per task) = high

**This means the framework is generating 1,600+ set comprehensions per task**, which suggests:

### Root Cause 1: Overactive Mutation Loop
The solver mutation/candidate generation loop is running TOO MANY TIMES:
- Expected: 50-100 mutations per task
- Actual: 1,600+ operations per task (based on setcomp call count)

**This could mean**:
- ✅ Mutations aren't being deduplicated efficiently
- ✅ Candidates aren't being filtered early (wait until end to score)
- ✅ No early termination when good candidates are found
- ✅ Exhaustive search instead of heuristic search

### Root Cause 2: High Closure Creation Overhead
Creating 13,261 closures per 100 tasks means:
- Every mutation creates a new partial application (rbind/lbind)
- If we're generating 13k+ mutations, most must be bad

**Better approach**:
- Generate fewer mutations (smarter heuristics)
- Batch operations instead of per-mutation
- Use functools.partial (C-optimized) instead of manual closures

---

## 🎯 Recommended Prioritization (Not Implementation Order!)

Based on impact and effort, here's the best sequence to maximize speedup:

### PHASE 1 (This Week) - Quick Wins
1. **Cache Type Hints** (5 min work, 0.34s saved) - ⭐ DO THIS FIRST
2. **Investigate setcomp call count** (5 min investigation) - Understand root cause
3. **Reduce mutation rate** (20-60 min, depends on findings) - Could save 0.5-1.0s

### PHASE 2 (Next Week) - Design Changes  
4. **Optimize objects() DSL** (30-60 min, 0.7-1.4s saved)
5. **Batch o_g() calls** (60-120 min, 0.7s saved)

### PHASE 3 (Week After) - Advanced
6. **Profile DSL hot paths** (o_g, objects improvements)
7. **Consider GPU acceleration for DSL**

---

## Success Targets

### Realistic Speedup Path (15-20x Goal)
| Phase | Work | Wall-Clock | Cumulative | Notes |
|-------|------|-----------|------------|-------|
| **Current** | Baseline | 3.05s | 1.0x | 100 tasks on Kaggle GPU |
| **1: Caching** | Type hints cache | 2.71s | 1.1x | Quick win |
| **1: Investigation** | Reduce setcomps | 2.30s | 1.3x | If design change works |
| **1: Mutation** | Cut rbind calls | 1.85s | 1.6x | -50% mutation overhead |
| **2: DSL** | Optimize objects+o_g | 1.10s | 2.8x | GPU or algorithm improvements |
| **3: Framework** | Profile + optimize framework | 0.60s | 5.1x | Fine-tuning |
| **Goal** | All optimizations | 0.20-0.25s | **12-15x** | ✅ Achievable |

**Key insight**: Reducing mutation rate (Phase 1) is the biggest lever for quick speedup.

---

### PHASE 1B: Quick Wins (Easy, Low Risk)

#### 1️⃣ **Cache Type Hints** (0.34s speedup expected) 🎯
**Effort**: 5 minutes  
**Expected Impact**: -90% on get_type_hints (3.73ms → 0.37ms)
**ROI**: 0.34s saved for 5 min work = **4x time multiplier**

**Implementation**:
```python
# In card.py or utils.py - Build cache at startup
TYPE_HINTS_CACHE = {}

def build_type_hints_cache(dsl_functions):
    """Cache type hints for all DSL functions at startup"""
    from typing import get_type_hints
    for func_name, func in dsl_functions.items():
        try:
            TYPE_HINTS_CACHE[func_name] = get_type_hints(func)
        except Exception:
            TYPE_HINTS_CACHE[func_name] = {}

# Use cached version in mutations (3,773 calls/runs)
def get_hints_cached(func_name):
    return TYPE_HINTS_CACHE.get(func_name, {})
```

**Why This Works**:
- Type hints inspection is O(n) for each call (introspects all annotations)
- 3,773 calls × 0.01ms per call = expensive!
- Cache built once = O(1) lookups afterwards
- Mutations need type hints for candidate generation

#### 2️⃣ **Analyze Closure Frequency** (1.45s → investigate root cause)
**Effort**: 20 minutes (investigation)
**Expected Impact**: 0.3-0.7s (if we reduce rbind/lbind call count)
**Root Cause**: 13,261 rbind/lbind calls = ~132 per task = excessive mutation rate

**Investigation Steps**:
```bash
# Profile batt.py to find who's calling rbind/lbind so much
# Check if mutation rate can be reduced:
1. How many mutations per task? (expected: 50-100)
2. Are we generating duplicates? (check for early termination logic)
3. Is there a way to batch-bind arguments instead of per-mutation?
```

**Optimization Strategies**:
- ✅ **Strategy A (Quick)**: Check if mutations are being deduplicated early
  - If we generate 1,000 mutations but 900 are duplicates, stop earlier
  - Could reduce rbind calls from 13,261 to 3,000 (-77%)
  - Time saved: 1.1s

- ✅ **Strategy B (Medium)**: Batch rbind operations
  - Instead of: `rbind(func, arg1), rbind(func, arg2), ...`
  - Do: `batch_rbind(func, [arg1, arg2, ...])` to create all at once
  - Could achieve 2-3x speedup on rbind overhead

- ⏳ **Strategy C (Advanced)**: Use functools.partial instead of closures
  - `functools.partial` is C-optimized, faster than Python closures
  - Could achieve 1.5-2x speedup on individual closure calls
  - But won't help if call count is fundamentally high

#### 3️⃣ **Investigate <setcomp>** (0.10-0.30s speedup possible) 
**Effort**: 20 minutes  
**Expected Impact**: 10-30% reduction if we optimize the most expensive comprehensions  
**Details**: 161,488 calls @ 0.002ms each = 0.296s total
- This is a **hot path** - called 1,600+ times per task
- Likely candidate filtering in mutation loop

**Implementation**:
- Profile to find which setcomps are slowest
- Replace comprehension with set operations or pre-filtering
- Consider vectorization for batch operations

### PHASE 1C: Medium Impact (Moderate Effort, Higher Risk)

#### 4️⃣ **Optimize objects() DSL Function** (0.70-1.40s speedup)
**Effort**: 30-60 minutes  
**Expected Impact**: -50% to -100% (GPU acceleration or algorithmic improvement)  
**Options**:
- a) GPU acceleration (if not already active)
- b) Vectorize the inner loops
- c) Memoize results
- d) Reduce redundant object construction

#### 5️⃣ **Batch o_g() Calls** (0.70s speedup possible)
**Effort**: 60-120 minutes  
**Expected Impact**: -50% by batching 3,400 calls into 17-34 GPU batches  
**Strategy**:
- Collect o_g() calls in codegen phase
- Process all grids for a rotation together
- Return batched results

---

## Success Criteria

### Target for 15-20x Speedup
**Current State**:
- Wall-clock: 3.05s (100 tasks)
- Total cumulative: 12.74s
- Speedup needed: 15-20x

**Phased Targets**:
1. **Phase 1B (Quick Wins)**: 3.05s → 2.70s (-11%) [cache hints + optimize f + setcomp]
2. **Phase 1C (DSL)**: 2.70s → 2.00s (-26%) [optimize objects + batch o_g]
3. **Phase 2 (GPU)**: 2.00s → 1.20s (-40%) [GPU acceleration of long-running ops]
4. **Phase 3 (Full Scale)**: 1.20s → 0.60s (-50%) [advanced caching + algorithmic]

**Final Expected**: ~0.6s for 100 tasks = **5x faster than current** ✅

---

## Immediate Action Items

### TODAY
1. ✅ Identify function `f` - search code
2. ✅ Create patches for type hints caching
3. ✅ Run profiling with `--search` flag for `f`

### THIS WEEK
1. Implement type hints caching
2. Identify slow setcomps
3. Analyze objects() function
4. Plan o_g() batching

### NEXT WEEK
1. Implement optimizations
2. Re-profile to validate speedups
3. Plan Phase 2 optimizations

---

## Notes

### Why `batt` Shows 3.02s Cumulative
The 3.02s cumulative time for `batt` includes ALL functions called within it. The 0.074s "Total" is just the direct execution time of `batt` itself (the loop and orchestration logic).

### GPU Status Check
Current profiling shows no obvious GPU batch operations in the top functions. Need to verify:
- Is GPU being used?
- Are there GPU batch calls that aren't showing up?
- Is GPU overhead masked by CPU time?

### Call Count Interpretation
- **batt: 100 calls** = one per task (expected)
- **f: 13,261 calls** = ~132 per task = candidates generated/evaluated
- **get_type_hints: 3,773 calls** = ~37 per task = type checks during mutations
- **<setcomp>: 161,488 calls** = ~1,614 per task = heavy filtering/deduplication

This suggests the mutation loop is very active and could benefit from caching/optimization.

