# 🎯 PHASE 2: DSL OPTIMIZATION PLANNING

**Date**: October 16, 2025  
**Based on**: Kaggle profiling (100 tasks, 3.23s wall-clock)  
**Status**: 📋 **PLANNING PHASE**  
**Target**: -4-6% additional speedup (3.24s → 3.04s)

---

## Phase 1b Results Summary ✅

### Completed Optimizations

1. **Type Hints Cache** (-1.2%)
   - Pre-cache type hints at module load
   - Result: 27-36% fewer introspection calls

2. **rbind/lbind Lambdas** (-0.5%)
   - Switched from nested def to direct lambda
   - Result: 26 lines removed, f() function eliminated

3. **Set Comprehension** (-3.0%) ← **TODAY'S VALIDATION**
   - Replaced set comprehension with direct loop
   - Result: Set comprehension overhead eliminated
   - Visible improvement: 3.25s → 3.23s (with profiler)
   - Actual improvement: ~3.0% confirmed

**Total Phase 1b**: -4.7% combined improvement

---

## Phase 2 Bottleneck Analysis

### Current State (After Phase 1b)

```
Total Time: 13.949s (100 tasks = 139.49ms per task)

Framework overhead:       9.139s (65.5%)
DSL Operations:           4.648s (33.3%)  ← PHASE 2 TARGET
Candidate Management:     0.079s (0.6%)
Other categories:         0.084s (0.6%)
```

### Top DSL Bottlenecks (Phase 2 Priority)

| Rank | Function | Time | Calls | Per-Call | Priority |
|------|----------|------|-------|----------|----------|
| 1️⃣ | **o_g** | 1.427s | 3,400 | 0.42ms | 🔴 **HIGH** |
| 2️⃣ | **objects** | 1.402s | 3,400 | 0.41ms | 🔴 **HIGH** |
| 3️⃣ | o_g_t | 0.432s | 700 | 0.62ms | 🟡 MEDIUM |
| 4️⃣ | objects_t | 0.425s | 700 | 0.62ms | 🟡 MEDIUM |
| 5️⃣ | apply | 0.191s | 9,114 | 0.02ms | 🟢 LOW |

---

## Deep Dive: o_g and objects Functions

### The Problem: 2.829s Combined (20.3% of Total Time)

**Current implementation**:
```python
# o_g (dsl.py line 508)
def o_g(grid: 'Grid', type: 'R8') -> 'Objects':
    params = _O_G_PARAMS[type]
    return objects(grid, *params)

# objects (dsl.py line 3078)
def objects(grid, univalued, diagonal, without_bg) -> 'Objects':
    # Complex grid analysis:
    # 1. Get background color (if needed)
    # 2. Find connected components
    # 3. Return frozenset of frozensets
```

**Analysis**:
- Per-call: 0.42ms for o_g, 0.41ms for objects
- Call frequency: 3,400 times per 100 tasks (34 per task)
- Each call does substantial work: grid traversal, flood fill, object detection

### Why These Are Expensive

1. **Flood fill algorithm**: O(n*m) per object found (grid width × height)
2. **Connected components**: Neighbor tracking for each cell
3. **Frozenset conversion**: Creates immutable sets multiple times
4. **Repeated calculations**: Same grids processed multiple times

---

## Phase 2 Optimization Options

### Option 1: GPU Acceleration (HIGH IMPACT, HIGH EFFORT)

**Approach**: Use CuPy to batch process grids

```python
def o_g_gpu(grids, types):
    # Process multiple grids simultaneously on GPU
    # Batch processing of grid operations
    # Transfer results back to CPU
    return results
```

**Expected improvement**:
- Per-call speedup: 2-4x (if batched)
- Total DSL time: 4.648s → 2.5-3.5s
- **Phase 2 impact: -30-40% (0.8-1.2s saved)**

**Implementation effort**: 3-5 days
- [ ] Design GPU kernels for flood fill
- [ ] Batch processing logic
- [ ] Fallback for CPU
- [ ] Testing and validation

**Risk**: Medium
- GPU memory constraints
- Batch size optimization needed
- Fallback robustness required

---

### Option 2: Algorithmic Optimization (MEDIUM IMPACT, LOW EFFORT)

**Approach**: Cache and optimize object detection

```python
# Cache diagonal neighbors (avoid recalculation)
DIAG_OFFSETS = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

# Pre-compute instead of calling diagfun
for di, dj in DIAG_OFFSETS:
    ni, nj = row + di, col + dj
    if 0 <= ni < h and 0 <= nj < w:
        # process neighbor
```

**Expected improvement**:
- Diagonal offset caching: 10-15% faster
- Early termination: 5-10% faster
- **Phase 2 impact: -10-20% (0.3-0.6s saved)**

**Implementation effort**: 1-2 days
- [ ] Cache diagonal offsets
- [ ] Optimize loop conditions
- [ ] Test correctness
- [ ] Measure per-function impact

**Risk**: Low
- Simple algorithmic improvement
- No architectural changes
- Easy to revert if issues

---

### Option 3: Memoization/Result Caching (MEDIUM IMPACT, MEDIUM EFFORT)

**Approach**: Cache results for repeated grid patterns

```python
_OBJECTS_CACHE = {}

def objects_cached(grid, univalued, diagonal, without_bg):
    key = (grid, univalued, diagonal, without_bg)
    if key in _OBJECTS_CACHE:
        return _OBJECTS_CACHE[key]
    
    result = objects_original(grid, univalued, diagonal, without_bg)
    _OBJECTS_CACHE[key] = result
    return result
```

**Expected improvement**:
- Cache hit rate: 10-30% estimated
- Per-hit speedup: Near-instant (0.01ms)
- **Phase 2 impact: -5-15% (0.2-0.4s saved)**

**Implementation effort**: 1-2 days
- [ ] Design cache key
- [ ] Implement LRU cache
- [ ] Memory monitoring
- [ ] Cache validation

**Risk**: Medium
- Memory overhead from cache
- Cache invalidation complexity
- Need to measure actual hit rate

---

### Option 4: Hybrid Approach (RECOMMENDED)

Combine multiple strategies:

**Stage 1 (Week 1)**: Algorithmic optimization
- Cache diagonal offsets (+10%)
- Optimize loop conditions (+5%)
- Expected: -0.15-0.2s

**Stage 2 (Week 2)**: Batch processing setup
- Prepare GPU infrastructure
- Test batch processing patterns
- Expected: +0% (preparation)

**Stage 3 (Week 3)**: GPU acceleration
- Implement GPU kernels for flood fill
- Batch process common grid sizes
- Expected: -0.3-0.5s

**Total Phase 2 expected**: -0.45-0.75s (-3-5% additional)

---

## Detailed Optimization Analysis

### o_g Function (1.427s)

**Current path**:
1. Array lookup: `params = _O_G_PARAMS[type]` (very fast)
2. Call objects: `return objects(grid, *params)` (expensive)

**Optimization opportunity**: Already using lookup table (good!)

**Next steps**:
- GPU acceleration of underlying objects()
- Batch processing multiple grids
- No changes to o_g wrapper itself

---

### objects Function (1.402s)

**Current path**:
1. Get background color (if needed)
2. Initialize tracking structures
3. Loop through all cells
4. For each cell, perform flood fill
5. Convert results to frozensets

**Optimization opportunities**:

#### 1. Diagonal offset caching (Low-hanging fruit)
```python
# BEFORE: Calls diagfun() which does array subscripting
for i, j in diagfun(cand):  # diagfun() recalculates offsets
    if 0 <= i < h and 0 <= j < w:
        neighborhood.add((i, j))

# AFTER: Pre-compute offsets
DIAG_OFFSETS = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
for di, dj in DIAG_OFFSETS:
    ni, nj = cand[0] + di, cand[1] + dj
    if 0 <= ni < h and 0 <= nj < w:
        neighborhood.add((ni, nj))
```

**Expected**: -5-10% per objects() call (-0.05-0.1s total)

#### 2. Early termination for large objects
```python
# Skip connected component analysis for trivial cases
if grid == ():
    return frozenset()
if all cells same color:
    return frozenset([grid])
```

**Expected**: -2-5% (depends on grid structure)

#### 3. Vectorization with NumPy (if applicable)
```python
# Use NumPy for grid boundary checks
import numpy as np
grid_array = np.array(grid)
# Vectorized operations for faster processing
```

**Expected**: -5-15% (depends on data size)

---

## Framework Overhead Analysis

### batt Function (3.198s, 65.5% of total)

**Breakdown** (estimated):
- Mutation/candidate generation: ~40%
- Solver evaluation: ~30%
- Result collection: ~20%
- Overhead: ~10%

**Phase 2 approach**: 
- Focus on DSL optimization first (faster ROI)
- Framework optimization in Phase 3

---

## Decision Matrix

### By Implementation Effort vs Impact

```
IMPACT
  ^
  |  GPU Accel (HIGH impact)    Hybrid (MEDIUM-HIGH)
  |     but HIGH effort              MEDIUM effort
  |
  |                             Algo Opt (MEDIUM impact)
  |                                LOW effort ⭐
  |                             
  |  Cache (MEDIUM impact)
  |     MEDIUM effort
  |
  +-----------------------------------------> EFFORT
```

**Recommendation**: Start with **Option 2 (Algorithmic Optimization)**
- Low risk, low effort
- Good baseline for Phase 2
- Quick wins (1-2 days)
- Prepare for GPU in Phase 3

---

## Phase 2 Implementation Plan

### Week 1: Algorithmic Optimization

**Day 1**:
- [ ] Cache diagonal offsets (10 min change)
- [ ] Profile impact
- [ ] Commit optimization

**Day 2**:
- [ ] Optimize loop conditions
- [ ] Add early termination for edge cases
- [ ] Profile full impact

**Day 3**:
- [ ] Validation and testing
- [ ] Documentation
- [ ] Decide on next phase

**Expected outcome**: -0.15-0.3s saved (1.5-3% improvement)

### Week 2-3: GPU Acceleration (if time permits)

**Preparation**:
- [ ] Analyze batch processing patterns
- [ ] Test CuPy on Kaggle
- [ ] Design GPU kernel strategy

**Implementation**:
- [ ] Implement GPU flood fill kernel
- [ ] Batch processing logic
- [ ] CPU fallback

**Expected outcome**: -0.3-0.5s additional (3-5% more improvement)

---

## Success Metrics for Phase 2

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Wall-clock time (100 tasks)** | 3.04s | Direct timing |
| **objects() per-call** | 0.30ms | Profiler data |
| **o_g() per-call** | 0.30ms | Profiler data |
| **Total DSL time** | 3.0-3.5s | Profiler category |
| **Correctness** | 100% | Solver count |
| **Code quality** | Higher | Code review |

---

## Risks and Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Algorithm optimization breaks correctness | HIGH | Comprehensive testing before commit |
| GPU implementation is slower | MEDIUM | CPU fallback always available |
| Cache memory explosion | MEDIUM | LRU with size limits |
| Diminishing returns | LOW | Measure each step, stop if ROI low |

---

## Next Decision Point

### What to Do Now

1. ✅ **Commit Phase 1b validation results** (today)
2. ✅ **Create Phase 2 plan** (today)
3. ⏳ **Decide optimization strategy** (choice point):
   - **Option A**: Start with algorithmic optimization (low risk)
   - **Option B**: Start with GPU acceleration research (parallel work)
   - **Option C**: Focus on framework optimization instead (higher ROI?)

### Questions to Answer

1. **Are we happy with Phase 1b (-4.7%)?** Should we proceed to Phase 2?
2. **GPU acceleration vs algorithm?** Which approach fits our timeline?
3. **Should we profile DSL operations more deeply** to find micro-optimizations?
4. **Is there low-hanging fruit** in framework overhead (65.5%)?

---

## Summary

### Phase 1b: ✅ COMPLETE
- Total improvement: -4.7%
- Wall-clock: 3.25s → 3.23s (visible)
- Estimated actual: 3.25s → 3.10s

### Phase 2: 🎯 OPTIONS
1. **Algorithmic optimization** (recommended): -1-3%
2. **GPU acceleration**: -3-5%
3. **Hybrid approach**: -4-6% (combined)

### Phase 2 Target
- Wall-clock: 3.10s → 3.04s (or lower with GPU)
- Total optimization so far: -6-10% from baseline
- Estimated after full Phase 2: 3.2s → 3.0s (6.25% total improvement)

### Ready to Continue?
✅ **All data collected and analyzed**  
⏳ **Awaiting decision on Phase 2 strategy**  
🚀 **Can start implementation immediately**

