# Phase 4 Implementation Guide - Framework Optimization

**Date**: October 17, 2025  
**Focus**: Reduce 74% framework overhead through targeted optimizations  
**Target**: 1.8x - 2.7x overall speedup (24.8s → 12-14s)

---

## Quick Start

### Three Profiling Approaches (Pick One)

**Option 1: Light-weight DSL operation tracking** (RECOMMENDED - Start here)
```bash
python profile_dsl_usage.py -c 10 --top 20
```
Shows which DSL operations are called most and consume most time.

**Option 2: Enhanced timing analyzer**
```bash
python analyze_framework_timing.py -c 10
```
Breaks down framework overhead into components.

**Option 3: Full cProfile** (Most detailed but slower)
```bash
python profile_framework.py -c 10 --sort cumulative --top 50
```
Complete function-level profiling (takes longer).

---

## Known Optimization Opportunities

Based on Phase 2a success and Phase 3 analysis, here are high-ROI targets:

### 1. **Caching Opportunities** ⭐ HIGHEST PRIORITY

**Current success**: Inlining cache at 100%, validation cache at 18%

**Optimization targets**:
- Expand validation cache hit rate (currently only 15-18%)
- Add operation result caching
- Cache DSL operation outputs

**Estimated ROI**: 5-15% time savings

**Implementation**: 2-4 hours

---

### 2. **DSL Operation Optimization** ⭐ HIGH PRIORITY

**Known hot operations** (from Phase 2b analysis):
- `objects()` and `objects_t()` - Already cached diagonals, but room for more
- Pattern matching operations (`p_g`, `fgpartition`)
- Complex transformations (`o_g`, `gravitate`)

**Optimization targets**:
- Reduce redundant computations
- Use NumPy vectorization more
- Cache intermediate results

**Estimated ROI**: 10-30% time savings

**Implementation**: 4-6 hours

---

### 3. **Framework Pipeline Optimization** ⭐ MEDIUM PRIORITY

**Current pipeline**:
1. Generate candidates
2. Score demo samples
3. Score test samples
4. Filter/deduplicate
5. Validate
6. Build final solvers

**Optimization targets**:
- Batch operations more aggressively
- Reduce redundant scoring
- Optimize filter/deduplicate logic
- Parallelize where possible

**Estimated ROI**: 5-10% time savings

**Implementation**: 3-5 hours

---

### 4. **Memory/Allocation Optimization** ⭐ MEDIUM PRIORITY

**Current issues**:
- Possible unnecessary array allocations
- Grid copying could be optimized
- Object creation overhead

**Optimization targets**:
- Reduce allocations in hot loops
- Use views instead of copies
- Object pooling for grids

**Estimated ROI**: 3-8% time savings

**Implementation**: 2-4 hours

---

## Execution Plan

### Phase 4a: Profiling & Analysis (2-3 hours)

**Step 1: Run profiling**
```bash
# Run DSL profiling (fastest way to find hot spots)
python profile_dsl_usage.py -c 10

# Capture output for analysis
python profile_dsl_usage.py -c 10 > profile_results.txt 2>&1
```

**Step 2: Identify top bottlenecks**
- Look for operations with >1ms per call
- Look for operations called 1000+ times
- Calculate total time per operation (calls × avg_time)

**Step 3: Document findings**
- Create PHASE4_PROFILING_RESULTS.md
- List top 10 bottleneck functions
- Estimate potential ROI for each

**Step 4: Plan optimizations**
- Select top 3-5 optimization targets
- Estimate implementation time
- Plan attack order

---

### Phase 4b: Implementation (3-5 hours)

**Approach**: Implement optimizations one at a time, measure after each

**For each optimization**:
1. Implement the optimization
2. Run 10-task test locally to verify correctness
3. Measure wall-clock time (should decrease)
4. Commit with measured results
5. Move to next optimization

**Example workflow**:
```bash
# 1. Implement optimization
vim dsl.py  # or run_batt.py, etc.

# 2. Test locally (quick correctness check)
python run_batt.py -c 1 --timing

# 3. Measure on small sample
python run_batt.py -c 10 --timing

# 4. Commit with results
git add . && git commit -m "opt: Optimization X - measured Y% speedup"
```

---

### Phase 4c: Validation (1-2 hours)

**Step 1: Full Kaggle test**
```
Run 100-task test on Kaggle:
- Measure total wall-clock time
- Verify correctness (0 errors)
- Calculate total speedup vs baseline

Expected: 24.8s → 12-14s (2-2.7x speedup)
```

**Step 2: Document results**
- Create PHASE4_RESULTS.md
- Show before/after timings
- List all optimizations applied
- Calculate total speedup

**Step 3: Commit final results**
```bash
git commit -m "Phase 4 complete: Framework optimization achieved Xs speedup"
```

---

## Key Metrics to Track

### Baseline Measurements
```
Phase 2a: 24.813s (100 tasks)
- Inlining cache: 100% hit rate
- Validation cache: 18% hit rate
- Solvers generated: 13,200
- Errors: 0
```

### Target Measurements for Phase 4
```
Goal: 12-14s (100 tasks) = 2-2.7x speedup

If we achieve:
- 50% framework reduction: 18.7s / 2 = 9.35s total (2.7x speedup) ✅
- 40% framework reduction: 18.7s * 0.6 = 11.2s total (2.2x speedup) ✅
- 30% framework reduction: 18.7s * 0.7 = 13.1s total (1.9x speedup) ✅
- 20% framework reduction: 18.7s * 0.8 = 14.8s total (1.7x speedup) ✅
```

---

## Common Optimization Patterns

### Pattern 1: Reduce Cache Lookups
```python
# Bad: Check cache multiple times
if key in cache:
    value = cache[key]
    if check_validity(value):
        if process_value(value):
            ...

# Good: Cache the result
cached_value = cache.get(key)
if cached_value and check_validity(cached_value) and process_value(cached_value):
    ...
```

### Pattern 2: Batch Operations
```python
# Bad: Process one at a time
results = []
for grid in grids:
    results.append(transform(grid))

# Good: Batch process if possible
results = batch_transform(grids)
```

### Pattern 3: Avoid Redundant Computations
```python
# Bad: Compute same thing multiple times
result = expensive_operation(x)
check_result(result)
use_result(result)
verify_result(result)

# Good: Compute once, reuse
result = expensive_operation(x)
check_result(result)  # Uses computed result
use_result(result)    # Uses computed result
verify_result(result) # Uses computed result
```

### Pattern 4: Use Vectorization
```python
# Bad: Loop-based operations
for i in range(len(array)):
    array[i] = array[i] * 2

# Good: Vectorized operations
array = array * 2  # Or: np.array(array) * 2
```

---

## Potential Quick Wins

### 1. Validation Cache Expansion
**Opportunity**: Validation cache at 18%, could target 25-30%

**Implementation**: 
- Analyze what causes misses
- Expand cache key generation
- Add pre-population logic

**Time**: 1-2 hours  
**Expected ROI**: 5-10% time savings

---

### 2. DSL Operation Memoization
**Opportunity**: Expensive DSL operations called repeatedly with same inputs

**Implementation**:
- Add `@lru_cache` to pure DSL functions
- Careful with side effects
- Monitor memory usage

**Time**: 1-2 hours  
**Expected ROI**: 10-20% time savings

---

### 3. Grid Copying Reduction
**Opportunity**: grids may be copied unnecessarily

**Implementation**:
- Use numpy views instead of copies
- Pass by reference where safe
- Profile memory allocations

**Time**: 2-3 hours  
**Expected ROI**: 5-15% time savings

---

### 4. Parallel Scoring Optimization
**Opportunity**: Demo/test scoring might be parallelizable further

**Implementation**:
- Increase thread pool size (if safe)
- Reduce GIL contention
- Batch operations per thread

**Time**: 2-4 hours  
**Expected ROI**: 5-15% time savings

---

## Tools Available

### Built Profilers
- `profile_dsl_usage.py` - Track DSL operation calls
- `analyze_framework_timing.py` - Component timing breakdown
- `profile_framework.py` - Full cProfile analysis

### Kaggle Testing
- `run_batt.py -c 10 --timing` - Quick 10-task test
- `run_batt.py -c 100 --timing` - Full 100-task validation

### Local Testing
- `python run_test.py` - DSL functionality tests
- `python tests.py` - Unit tests

---

## Success Criteria

Phase 4 is successful if:
- ✅ Profiling identifies top 5-10 bottleneck functions
- ✅ At least 3 optimization targets identified with ROI
- ✅ Implementation achieves 1.8x minimum speedup
- ✅ Correctness maintained (all solvers correct)
- ✅ All optimizations validated on Kaggle

---

## Timeline

```
Today (Oct 17):
  - Create profiling infrastructure ✓
  - Document optimization opportunities ✓
  - Plan execution sequence ✓

Tomorrow (Oct 18):
  - Run profiling and analysis
  - Identify specific optimization targets
  - Begin implementation

Day 3 (Oct 19):
  - Complete optimizations
  - Validate on 100-task
  - Document results
```

---

## Success Looks Like

**If Phase 4 succeeds**, we'll have:

1. **Documented bottlenecks** - Know exactly where time is spent
2. **Successful optimizations** - 1.8-2.7x speedup achieved
3. **Replicable improvements** - Specific changes made, measured impact
4. **Optimization template** - Framework for future improvements
5. **Combined speedup** - Phase 1b + 2a + 4 = 50-75% total

**Overall optimization from baseline**: -60% to -75% ✅

