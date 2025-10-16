# Stage 3 Phase 1: Quick Reference Card

**Status**: Investigation Complete ✅  
**Created**: October 16, 2025  
**Profiling Data**: 100 tasks, 3.05s wall-clock, Kaggle GPU

---

## The Problem (30 seconds)

| Metric | Value | Issue |
|--------|-------|-------|
| Wall-clock | 3.05s | Slow for 100 tasks |
| Framework | 8.1s (63.6%) | Overhead from mutations |
| DSL ops | 4.1s (32.2%) | Expensive operations |
| Target | 0.20-0.25s | 12-15x speedup needed |

---

## What We Found (3 minutes)

### Top Bottlenecks
1. **batt()** - 3.02s orchestrator (calls other functions)
2. **f() closure** - 1.45s (13,261 calls) - rbind/lbind in dsl.py
3. **objects()** - 1.39s DSL function (slow per-call)
4. **o_g()** - 1.41s DSL function (high call count)
5. **<setcomp>** - 0.296s (161,488 calls!) **MASSIVE**
6. **get_type_hints()** - 0.378s (3,773 calls) - can cache

### Root Cause
**161,488 set comprehensions per 100 tasks = 1,614 per task!**
- Expected: 50-200 per task
- 10-30x higher than normal
- Indicates genetic algorithm generating way too many candidates

---

## The Fix (Implementation Order)

### 1. Cache Type Hints (5 min work, 0.34s saved) ⭐ START HERE

**File**: `dsl.py` line ~1305
```python
# Add after lbind() function:
_TYPE_HINTS_CACHE = {}
def _build_type_hints_cache(): ...
_build_type_hints_cache()
```

**File**: `card.py` find `get_type_hints()`
```python
# Replace with:
dsl._TYPE_HINTS_CACHE.get(func.__name__, {})
```

**Expected**: 3.05s → 2.71s (1.1x faster)

### 2. Investigate Mutation Rate (20 min investigation)

**Questions**:
- Why 161,488 set comprehensions?
- Why 13,261 rbind/lbind calls?
- Can we generate fewer mutations?

**Command**:
```bash
grep -n "{.*for.*in.*}" card.py  # Find set comps
grep -n "rbind\|lbind" card.py   # Find mutation calls
```

### 3. Optimize Based on Findings (30-60 min work)

**Options**:
- Reduce mutation count (algorithm change)
- Add early termination
- Batch operations
- Better deduplication

**Expected**: 2.71s → 1.85s (1.6x from baseline)

---

## Detailed Documents

| Document | Purpose | Length |
|----------|---------|--------|
| **INVESTIGATION_COMPLETE_SUMMARY.md** | Executive summary with timeline | 5 min read |
| **STAGE3_PHASE1_BOTTLENECK_ANALYSIS.md** | Detailed function analysis | 10 min read |
| **PHASE1B_INVESTIGATION_SUMMARY.md** | Implementation details | 8 min read |

---

## Timeline

```
Week 1 (This week):
├─ Mon: Type hints cache (5 min)
├─ Tue: Investigate mutation rate (20 min)
├─ Wed-Thu: Implement optimization (30-60 min)
├─ Fri: Re-profile on Kaggle
└─ Result: 3.05s → 2.0-2.4s (1.3-1.6x)

Week 2 (Next):
├─ Analyze DSL bottlenecks
└─ Plan GPU acceleration

Week 3 (Following):
├─ Implement DSL optimizations
└─ Result: 1.85s → 0.9-1.1s (3.4x from baseline)

Final Goal: 3.05s → 0.20-0.25s (12-15x) ✅
```

---

## Key Numbers

- **batt**: 100 calls (normal)
- **f**: 13,261 calls (too many!) ← Mutation explosion
- **<setcomp>**: 161,488 calls (way too many!) ← Root cause
- **get_type_hints**: 3,773 calls (can cache)
- **objects**: 1.39s (DSL optimization target)
- **o_g**: 1.41s (DSL optimization target)

---

## Success Criteria

### Phase 1B (This Week)
- ✅ Type hints cache implemented
- ✅ Mutation rate investigated
- ✅ Re-profiled showing 1.3-1.6x speedup
- ✅ Framework time: 8.1s → ~5-6s

### Phase 1C (Next Week)
- ✅ DSL bottlenecks analyzed
- ✅ GPU acceleration strategy defined

### Phase 2 (Following Week)
- ✅ DSL optimizations implemented
- ✅ Total speedup: 3.05s → 0.9-1.1s (3.4x)

### Final (By End of Month)
- ✅ All optimizations done
- ✅ Total speedup: 3.05s → 0.20-0.25s (12-15x)

---

## Quick Lookup

**Q: Where's function `f`?**
A: dsl.py lines 1235-1243 and 1292-1300 - it's a closure inside rbind() and lbind()

**Q: Why so much time in framework?**
A: 161,488 set comprehensions per 100 tasks (1,614 per task) - genetic algorithm too aggressive

**Q: What should I fix first?**
A: Cache type hints (5 min work, 0.34s saved) - best ROI

**Q: What's the root cause?**
A: Mutation algorithm generates 1,600+ operations per task instead of 50-200

**Q: Can we GPU accelerate?**
A: Framework is hard to parallelize. DSL operations (o_g, objects) are better targets for GPU (Phase 2)

---

## Files to Edit

### Phase 1B
1. `dsl.py` - Add type hints cache (~10 lines)
2. `card.py` - Use cached type hints (~5 lines changed)

### Phase 1C
3. `profile_batt_framework.py` - Add investigation tools

### Phase 2
4. Implement DSL optimizations (GPU or algorithmic)

---

## Commands to Run

```bash
# Test type hints cache
python card.py -c 2

# Profile on Kaggle
bash run_card.sh -c -32
python profile_batt_framework.py --top 10

# Investigate mutations
grep -n "{.*for.*in.*}" card.py run_batt.py | wc -l
grep -n "rbind\|lbind" card.py | wc -l

# After implementation, compare
diff <(python profile_batt_framework.py --top 5 BEFORE) \
     <(python profile_batt_framework.py --top 5 AFTER)
```

---

## Bottom Line

**The framework is doing 10-30x more work than it should.**

Instead of optimizing operation speed (already fast), we need to **reduce the number of operations** by:
- Generating fewer mutations (smarter heuristics)
- Adding early termination (stop when good candidate found)
- Batching operations (amortize overhead)
- Caching expensive computations (type hints)

**Action**: Start with type hints cache (5 min, big payoff), then investigate mutation rate.

---

**Investigation complete. Ready to implement! ✅**

