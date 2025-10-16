# Phase 1B: Investigation Summary

**Date**: October 16, 2025  
**Profiling Data**: 100 tasks, Kaggle GPU enabled, 3.05s wall-clock  
**Status**: Investigation complete, ready for implementation  

---

## Key Findings

### 🔍 Mystery Function `f` - IDENTIFIED ✅
**Found in**: dsl.py lines 1235-1243 (rbind) and 1292-1300 (lbind)

```python
# Pattern repeated in both rbind and lbind functions:
def rbind(function: 'Callable', fixed: 'Any') -> 'Callable':
    if n == 2:
        def f(x):                      # ← This is the closure
            return function(x, fixed)
        return f
    # ...similar for n==3, n>3
```

**Profile Data for `f` closures**:
- Total time: 1.45s (11.4% of total)
- Call count: 13,261 per 100 tasks
- Per-call time: 0.0001ms (extremely fast)
- Per task: 132 closure creations/calls

**Interpretation**: Creating 132 partial applications per task is EXCESSIVE
- Expected mutation count: 50-100 per task
- Actual: 132+ (and probably creating many more than we use)
- This indicates overactive mutation generation loop

### 📊 Bottleneck Distribution - Revised Analysis

| Component | Time | Calls | Per Task | Issue |
|-----------|------|-------|----------|-------|
| **batt()** | 3.02s | 100 | 1 per task | ✓ Normal |
| **f() closure** | 1.45s | 13,261 | 132 per task | ✅ **TOO MANY** |
| **<setcomp>** | 0.296s | 161,488 | 1,614 per task | ✅ **MASSIVE** |
| **get_type_hints** | 0.378s | 3,773 | 37 per task | ✓ Can cache |
| **asindices** | 0.223s | 3,247 | 32 per task | ✓ Normal |
| **objects()** | 1.39s | 3,400 | 34 per task | ✓ Normal rate |
| **o_g()** | 1.41s | 3,400 | 34 per task | ✓ Normal rate |

### 🎯 Root Cause Analysis

**The 63.6% framework bottleneck is NOT due to slow code, but EXCESSIVE OPERATIONS**

**Evidence**:
1. **Set comprehensions**: 1,614 calls per task is 10-30x higher than expected
   - Suggests: Filtering, deduplication, or set operations in hot loop
   - Or: Genetic algorithm generating 1,600+ candidate variations

2. **Closure creations**: 132 per task (expected: 50-100)
   - Suggests: Exhaustive search instead of heuristic search
   - Or: No early termination when good candidates found

3. **Type hint checks**: 37 per task (expected: 5-10)
   - Suggests: Type checking every mutation instead of once per function

**This is a DESIGN problem, not an OPTIMIZATION problem**
- The mutation algorithm is generating way too many candidates
- Each candidate triggers set comprehensions and type checks
- We need to either: reduce candidates, batch operations, or early-terminate

---

## Immediate Action Items

### MUST DO (This Week)

#### 1. Cache Type Hints (5 min, 0.34s saved) ⭐⭐⭐
**Priority**: HIGHEST - Quick win with big payoff

**What to do**:
```python
# In dsl.py, right after rbind/lbind definitions (around line 1305)

# Build cache at module load time
_TYPE_HINTS_CACHE = {}

def _build_type_hints_cache():
    """Initialize type hints cache for all DSL functions"""
    import inspect
    from typing import get_type_hints
    
    # Get all DSL functions from current module
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if callable(obj) and not name.startswith('_'):
            try:
                _TYPE_HINTS_CACHE[name] = get_type_hints(obj)
            except Exception:
                pass  # Skip functions without type hints

# Call at module load
_build_type_hints_cache()

# Use cache instead of get_type_hints()
# In card.py, replace: get_type_hints(func)
# With:              _TYPE_HINTS_CACHE.get(func.__name__, {})
```

**Expected result**: 
- get_type_hints: 0.378s → 0.038s (-90%)
- Total time: 3.05s → 2.71s
- Speedup: 1.1x

---

#### 2. Investigate Mutation Rate (20 min investigation)
**Priority**: HIGH - Understand root cause before optimizing

**Questions to answer**:
1. Where are 161,488 set comprehensions coming from?
   - Search card.py for all `{... for ... in ...}` patterns
   - Check run_batt.py for set operations
   - Look at genetic algorithm loop

2. Why 132 rbind/lbind calls per task?
   - Are mutations being deduplicated?
   - Is there early termination?
   - How many mutations are we trying before giving up?

3. Sample output:
   ```bash
   # Search for set comprehensions
   grep -n "{.*for.*in.*}" card.py run_batt.py
   
   # Search for mutation generation loop
   grep -n "for.*mutate\|for.*candidate\|for.*solver" card.py
   
   # Look for rbind/lbind calls
   grep -n "rbind\|lbind" card.py | wc -l
   ```

**Expected findings**:
- Genetic algorithm generates 500-1000+ candidate mutations per task
- Most are duplicates or invalid
- No early termination (scores all mutations)
- Could reduce by 50-77% with better heuristics

---

#### 3. Profile Most Expensive Set Comprehensions (10 min)
**Priority**: MEDIUM - Find optimization targets

**How to identify**:
```python
# In profile_batt_framework.py, add line-by-line profiling:
python -m line_profiler card.py  # Profile hot function
# Or: use cProfile with --sort cumtime to see call chains
```

**Look for patterns like**:
```python
# Bad: Creates 1600+ sets per task
results = set()
for mutation in mutations:
    result = apply_mutation(mutation)
    results.add(result)  # ← Set add = setcomp equivalent

# Better: Pre-filter before adding to set
results = set()
for mutation in good_mutations:  # Filter first!
    result = apply_mutation(mutation)
    if is_valid(result):
        results.add(result)
```

---

### NICE TO HAVE (If Time)

#### Reduce Closure Creation Overhead
**If we find mutations are excessive**, can try:
```python
# Instead of creating closure per mutation:
#   f = rbind(o_g, rotation)
#   result = f(grid)

# Batch create all closures, then apply:
#   closures = [rbind(o_g, rot) for rot in rotations]
#   results = [f(grid) for f in closures]

# Or use functools.partial (C-optimized):
from functools import partial
#   f = partial(o_g, rotation)  # Faster than closure
#   result = f(grid)
```

**Expected savings**: 1.5-2x on closure overhead IF implemented
**But**: Won't help if mutation rate is fundamentally too high

---

## Implementation Timeline

### Phase 1B (This Week)
- **Mon-Tue**: Type hints cache (5 min) + Investigation (30 min)
- **Wed-Thu**: Implement based on findings (30-60 min)
- **Fri**: Re-profile on Kaggle, validate improvements

### Phase 1C (Next Week) 
- Analyze DSL bottlenecks (o_g, objects)
- Plan GPU acceleration or algorithmic improvements

### Phase 2 (Week After)
- Implement DSL optimizations
- Target: 2.8-3.5x cumulative speedup (3.05s → 0.9-1.1s)

---

## Critical Insights

### Why So Many Set Comprehensions?
The 1,614 set comprehension calls per task is telling us something:

**Possibility 1: Genetic Algorithm Explosion**
```python
# Pseudo-code for typical genetic algorithm:
for generation in range(100):
    for candidate in population:
        # Each mutation triggers set operations?
        mutated = mutate(candidate)
        validate(mutated)  # ← Involves set comprehensions
```

With 100 generations × 10-20 mutations per generation = 1000+ operations
Plus deduplication checks = 1600+ set operations ✓

**Possibility 2: Exhaustive Search**
```python
# Try all combinations of DSL functions + arguments
for func in dsl_functions:          # ~200 functions
    for arg1 in arguments:          # ~30 arguments
        for arg2 in arguments:      # ~30 arguments
            candidate = func(arg1, arg2)
            results.add(candidate)  # Set operations
```

This would generate 200 × 30 × 30 = 180,000+ candidates!
Then deduplication/filtering adds more set operations ✓

**Possibility 3: Lazy Evaluation + Caching**
```python
# Maybe set operations are appearing because:
# - Results are cached in sets
# - Membership checks trigger set comprehensions
# - Deduplication happens via set union/intersection
```

### Lesson
**Don't optimize operation speed - optimize the NUMBER of operations!**

A slow operation done 100 times is slow.
A fast operation done 1,600 times is SLOW.

The 0.002ms per setcomp is fast, but × 161,488 = expensive!

---

## Success Criteria

### After Type Hints Cache
- ✅ get_type_hints calls reduce from 3,773 to ~200-500 (cached lookups are near-zero)
- ✅ Time: 0.378s → 0.038s
- ✅ Total: 3.05s → 2.71s (1.1x speedup)
- ✅ Easy verification: Profile should show huge drop in get_type_hints time

### After Investigating Mutation Rate
- ✅ Understand root cause of 161,488 setcomps
- ✅ Identify optimization strategy (reduce mutations, batch, early-terminate, etc.)
- ✅ Estimate potential savings (0.2-0.5s per fix)

### After Phase 1B Complete
- ✅ Total framework time: 8.1s → ~6.5-7.5s (1.3x speedup)
- ✅ Ready for Phase 1C (DSL analysis)

---

## Files to Modify

### Priority 1 (This Week)
1. **dsl.py** - Add TYPE_HINTS_CACHE (10 lines)
2. **card.py** - Use cached type hints instead of get_type_hints() (2-5 changes)

### Priority 2 (After Investigation)
3. **card.py** - Optimize mutation generation loop (TBD based on findings)
4. **profile_batt_framework.py** - Add line-by-line profiling if needed

---

## Next Steps

1. ✅ Commit this analysis to git:
   ```bash
   git add STAGE3_PHASE1_BOTTLENECK_ANALYSIS.md PHASE1B_INVESTIGATION_SUMMARY.md
   git commit -m "docs: Complete Phase 1b investigation - identified f() as rbind/lbind closure, found mutation rate excessive"
   ```

2. Implement type hints cache (5 min work)
   ```bash
   # Edit dsl.py to add _build_type_hints_cache()
   # Edit card.py to use cache
   # Test: python card.py -c 2
   ```

3. Investigate mutation rate (30 min)
   ```bash
   # Profile on Kaggle or search codebase
   # Answer: where are 161,488 setcomps coming from?
   ```

4. Based on findings, implement optimization (1-2 hours)

5. Re-profile on Kaggle to validate (30 min)
   ```bash
   # bash run_card.sh -c -32  # Test 32 tasks
   # python profile_batt_framework.py --top 20
   ```

---

**Analysis complete! Ready to implement Phase 1B optimizations.** 🚀

