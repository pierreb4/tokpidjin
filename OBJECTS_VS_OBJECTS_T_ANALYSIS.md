# 🔍 Analysis: objects() vs objects_t() - Which is More Efficient?

**Date**: October 16, 2025  
**Key Question**: Can we retire `objects()` and use `objects_t()` everywhere for better performance?

---

## The Functions Compared

### objects() - Returns frozenset of frozensets
```python
# dsl.py lines 3078-3122
def objects(grid, univalued, diagonal, without_bg) -> 'Objects':
    # ...
    objs = []  # Use list during construction
    occupied = set()
    # ...
    for loc in unvisited:
        # ...
        obj = [initial_cell]  # List
        obj_set = {initial_cell}  # Set for uniqueness
        cands = {loc}
        while cands:
            neighborhood = set()
            for cand in cands:
                # ...
                neighborhood |= {(i, j) for i, j in diagfun(cand) if 0 <= i < h and 0 <= j < w}
                # ^^^ SET COMPREHENSION - LINE 3117 (our bottleneck!)
            cands = neighborhood - occupied
        objs.append(frozenset(obj))  # Convert to frozenset
    return frozenset(objs)  # Return frozenset of frozensets
```

**Key operations**:
- Line 3117: `neighborhood |= {...set comprehension...}` - **EXPENSIVE** (234,539 calls!)
- Converts to frozenset at end: `frozenset(obj)`
- Returns: `frozenset(frozenset(...))`

---

### objects_t() - Returns tuple of tuples
```python
# dsl.py lines 3125-3155
def objects_t(grid, univalued, diagonal, without_bg) -> 'Tuple[Tuple[Tuple[int, int, int], ...], ...]':
    # ...
    objs = []
    occupied = set()
    # ...
    for loc in unvisited:
        # ...
        obj = []  # Direct list (no obj_set)
        cands = {loc}
        while cands:
            neighborhood = set()
            for cand in cands:
                # ...
                neighborhood |= {(i, j) for i, j in diagfun(cand) if 0 <= i < h and 0 <= j < w}
                # ^^^ SET COMPREHENSION - SAME LINE ISSUE!
            cands = neighborhood - occupied
        objs.append(tuple(obj))  # Convert to tuple
    return tuple(objs)  # Return tuple of tuples
```

**Key differences**:
- Line 3117: **SAME SET COMPREHENSION** as objects()!
- No `obj_set` tracking (slightly faster)
- Returns: `tuple(tuple(...))` instead of `frozenset(frozenset(...))`

---

## Performance Comparison

### Memory & Construction Costs

| Aspect | objects() | objects_t() | Winner |
|--------|-----------|-------------|--------|
| **Inner container type** | frozenset | tuple | **objects_t** (tuples faster to create) |
| **Outer container type** | frozenset | tuple | **objects_t** (tuples faster to create) |
| **obj_set tracking** | Yes (extra set) | No | **objects_t** (-overhead) |
| **Set comprehension** | Same as below | Same as below | TIED |
| **Frozenset final conversion** | frozenset(obj) | tuple(obj) | **objects_t** (tuple cheaper) |

**Memory estimate per 100 tasks**:
- frozenset overhead: ~10-15% higher than tuple
- obj_set tracking: +10% for objects()
- **Potential savings**: ~20-25% memory, 5-10% speed for objects_t

---

### The Real Bottleneck: Set Comprehension (Line 3117)

**BOTH functions use the SAME problematic code**:

```python
neighborhood |= {(i, j) for i, j in diagfun(cand) if 0 <= i < h and 0 <= j < w}
```

**Profiling data** (Kaggle, 100 tasks):
- 234,539 set comprehension calls per 100 tasks
- 0.384s cumulative time
- 0.002ms per call

**Problem**: Creating a set every iteration is expensive
- Set creation overhead
- Set union operation
- Repeated across 234,539 times

**This affects BOTH objects() and objects_t() equally**

---

## Optimization Strategy: Two-Pronged Approach

### 🎯 Priority 1: Fix the Set Comprehension (Affects BOTH)

**Current code** (line 3117, both functions):
```python
neighborhood |= {(i, j) for i, j in diagfun(cand) if 0 <= i < h and 0 <= j < w}
```

**Optimized code - Option A (Direct iteration)**:
```python
# Replace set comprehension with direct loop
for i, j in diagfun(cand):
    if 0 <= i < h and 0 <= j < w:
        neighborhood.add((i, j))
```

**Optimized code - Option B (List then update)**:
```python
# Accumulate in list, then update set
new_coords = [
    (i, j) for i, j in diagfun(cand) if 0 <= i < h and 0 <= j < w
]
neighborhood.update(new_coords)
```

**Expected savings**:
- 5-10% per comprehension call
- 0.02-0.04s savings per 100 tasks
- **This is THE critical optimization**

---

### 🎯 Priority 2: Choose Container Types

**Option 1: Keep both, optimize both**
```
✅ Pros: Backward compatible, serves different needs
✅ Pros: frozenset for mutation detection, tuple for speed
❌ Cons: Duplicates the set comprehension fix
❌ Cons: Adds code complexity
```

**Option 2: Retire objects(), use objects_t() everywhere**
```
✅ Pros: Single implementation to maintain
✅ Pros: Tuples are universally faster than frozensets
✅ Pros: No duplicate code
❌ Cons: Breaks API (frozenset → tuple)
❌ Cons: May break existing solvers
❌ Cons: Type checking would catch, but still refactoring work
```

**Option 3: Hybrid approach (RECOMMENDED)**
```
✅ Pros: Keep backward compatibility
✅ Pros: Single optimized implementation shared via wrapper
✅ Pros: Easy to measure impact
❌ Cons: Small wrapper overhead

Pattern:
# Shared optimized implementation
def _objects_internal(grid, univalued, diagonal, without_bg):
    # ... optimized code ...
    return list_of_tuples  # Return raw tuples

def objects(grid, univalued, diagonal, without_bg):
    result = _objects_internal(...)
    return frozenset(frozenset(obj) for obj in result)  # Wrap for API

def objects_t(grid, univalued, diagonal, without_bg):
    result = _objects_internal(...)
    return tuple(obj for obj in result)  # Minimal wrap
```

---

## Current Usage Analysis

### Where objects() is used:
```python
# solvers_ref_*.py - Generated solvers use objects()
def solve_e8593010(I):
    x1 = objects(I, T, F, T)  # <-- USED HERE
    x2 = sizefilter(x1, ONE)
    # ...

def solve_6d75e8bb(I):
    x1 = objects(I, T, F, T)  # <-- USED HERE
    # ...
```

**Count**: Hundreds of generated solvers use `objects()`

### Where objects_t() is used:
```python
# o_g_t() uses it
def o_g_t(grid, type):
    params = _O_G_PARAMS[type]
    return objects_t(grid, *params)  # <-- LIMITED USE

# Directly in some solvers (fewer)
```

**Count**: Limited direct usage (mostly via o_g_t)

---

## Decision Matrix

| Scenario | Action | Rationale |
|----------|--------|-----------|
| **Short-term (Now)** | Fix set comprehension in BOTH | 0.02-0.04s gain, minimal risk |
| **Medium-term (Phase 2)** | Measure objects_t adoption impact | Understand if tuple variant is worth pushing |
| **Long-term (Future)** | Decide: keep both or choose one | Depends on mutation detection needs |

---

## Recommendation: Three-Step Plan

### Step 1: Fix Set Comprehension (TODAY - 10 minutes)
**Impact**: -0.02-0.04s per 100 tasks (0.7-1.4% speedup)

Optimize line 3117-3119 in BOTH functions:
```python
# OLD (both functions)
neighborhood |= {(i, j) for i, j in diagfun(cand) if 0 <= i < h and 0 <= j < w}

# NEW (both functions)
for i, j in diagfun(cand):
    if 0 <= i < h and 0 <= j < w:
        neighborhood.add((i, j))
```

**Changes needed**: 2 locations
- Line 3117 in objects()
- Line 3155 in objects_t()

---

### Step 2: Validate Locally (5 minutes)
```bash
# Test both variants
python card.py -c 2
```

---

### Step 3: Measure on Kaggle (30 minutes)
```bash
# Profile to see actual impact
bash run_card.sh -c -32
```

**Success criteria**:
- Wall-clock time: < 3.0s (down from 3.25s)
- Correctness: All solvers still work
- Profiler: <setcomp> calls reduced or time reduced

---

## Why NOT Retire objects() Yet

1. **Risk**: 12,000+ generated solvers use objects()
2. **Unknown**: Haven't measured if tuple swap breaks anything
3. **Type system**: frozenset provides immutability guarantee
4. **Backward compat**: Many examples depend on frozenset return
5. **Better strategy**: Fix the real bottleneck (set comprehension) first

---

## Why objects_t is NOT Automatically Better

**Common misconception**: "Tuples are faster than frozensets"

**Reality**:
- Tuple creation: ~0.5-1ns per element
- Frozenset creation: ~2-3ns per element
- **BUT**: Set operations (union, difference, membership) are WAY faster for frozensets!

**In objects()**:
- `obj_set` membership test: O(1) with frozenset (hashed)
- `occupied` set operations: O(1) with set
- `cands = neighborhood - occupied`: Set difference is optimized

**If we switched to tuple**:
- Membership tests become O(n) scans
- Set difference becomes list comprehension
- Could actually be SLOWER for large objects!

---

## The Real Insight

### Set Comprehension is the Problem, Not Container Types

The performance issue is:
```python
neighborhood |= {(i, j) for i, j in diagfun(cand) if 0 <= i < h and 0 <= j < w}
```

This creates a NEW set 234,539 times per 100 tasks.

**Solution**: Don't create a new set, just add to existing:
```python
for i, j in diagfun(cand):
    if 0 <= i < h and 0 <= j < w:
        neighborhood.add((i, j))
```

**This fix helps BOTH objects() and objects_t()** equally!

---

## Conclusion

### ✅ YES to: Fix set comprehension in both functions
- **Why**: Real bottleneck identified
- **Impact**: 0.7-1.4% speedup expected
- **Risk**: Very low (simple loop replacement)
- **Time**: 10 minutes

### ⏳ MAYBE to: Retire objects() in favor of objects_t()
- **Need**: Real measurement on Kaggle
- **Risk**: High (changes 12,000+ solvers)
- **Benefit**: Unclear (tuple not automatically faster)
- **Time**: After Phase 1b complete (Phase 2 optimization)

### ❌ NO to: Replace objects_t with objects_t due to container type
- **Why**: Isn't the problem
- **Real issue**: Set comprehension overhead
- **Same fix applies to both**

---

## Next Action

**Immediate**: Fix set comprehension (line 3117-3119 in both functions)

```python
# BEFORE (objects, line 3114-3119)
neighborhood |= {
    (i, j) for i, j in diagfun(cand) if 0 <= i < h and 0 <= j < w
}

# AFTER (objects, line 3114-3119)
for i, j in diagfun(cand):
    if 0 <= i < h and 0 <= j < w:
        neighborhood.add((i, j))
```

Same change for objects_t() at line 3152-3157.

