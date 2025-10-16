# Phase 2 Stage 2: Optimization Plan

**Date**: October 15, 2025  
**Current Baseline**: 5.24s for 100 tasks (after Stage 1)  
**Target**: 3.5-4.0s for 100 tasks (25-33% improvement)  
**Final Goal**: 9-11x total speedup (37.78s → 3.5-4.0s)

---

## Executive Summary

**Current Achievement**: 7.2x total speedup (37.78s → 5.24s)  
**Remaining Target**: 1.3-1.5x additional speedup to reach 9-11x goal  
**Strategy**: Focus on "Other Framework" category (79.3% of time) and remaining DSL bottlenecks

---

## Current Bottleneck Analysis

### Top Categories (from validation profiling)

| Category | Time | % Total | Calls | Status |
|----------|------|---------|-------|--------|
| **Other Framework** | 24.997s | **79.3%** | 6,961,742 | 🎯 **PRIMARY TARGET** |
| DSL Operations | 5.232s | 16.6% | 527,937 | 🟡 Secondary target |
| Candidate Management | 0.938s | 3.0% | 254,535 | 🟢 Lower priority |
| GPU Batch Processing | 0.246s | 0.8% | 1,967 | ✅ Already optimized |

### Top DSL Functions (Still Worth Optimizing)

| Function | Time | Calls | Per Call | Status |
|----------|------|-------|----------|--------|
| o_g | 1.163s | 3,400 | 0.342ms | 🟡 Improved but still #1 |
| objects | 1.140s | 3,400 | 0.335ms | 🟡 Improved but still #2 |
| apply | 0.688s | 5,400 | 0.127ms | 🎯 **Good memoization target** |
| o_g_t | 0.541s | 700 | 0.773ms | 🟡 Worth optimizing |
| objects_t | 0.534s | 700 | 0.762ms | 🟡 Worth optimizing |

### Top Framework Functions

| Function | Time | Calls | Per Call | Category |
|----------|------|-------|----------|----------|
| batt | 5.203s | 100 | 52.03ms | 🎯 **HUGE TARGET** |
| wrapper | 5.134s | 739,260 | 0.007ms | 🎯 Function call overhead |
| f | 1.713s | 55,487 | 0.031ms | 🎯 Unknown function |
| get_type_hints | 0.809s | 7,343 | 0.110ms | 🎯 **Type checking overhead** |
| _get_safe_default | 0.914s | 7,343 | 0.124ms | 🎯 **Candidate management** |

---

## Stage 2 Optimization Strategy

### Tier 1: High-Impact Framework Optimizations (3-4 days)

#### 1. **Optimize `wrapper` function** 🎯 **TOP PRIORITY**
- **Current**: 5.134s (739,260 calls, 0.007ms/call)
- **Issue**: Excessive function call overhead
- **Approach**: 
  - Investigate what wrapper does (likely timeout/decorator)
  - Consider inlining for hot paths
  - Reduce wrapping layers if possible
- **Expected**: -40-50% (2.0-2.5s saved) → **3.2-3.7s total**
- **Effort**: 2-3 days

#### 2. **Optimize `get_type_hints` and type checking** 🎯
- **Current**: 0.809s (7,343 calls, 0.110ms/call)
- **Issue**: Type checking on every function call
- **Approach**:
  - Cache type hints at module load time
  - Use `@lru_cache` on get_type_hints
  - Skip type checking for internal calls
- **Expected**: -60-80% (0.5-0.6s saved)
- **Effort**: 1 day

#### 3. **Optimize `_get_safe_default` candidate management** 🎯
- **Current**: 0.914s (7,343 calls, 0.124ms/call)
- **Issue**: Default value retrieval on every candidate
- **Approach**:
  - Cache safe defaults by type
  - Pre-compute common defaults
  - Reduce redundant lookups
- **Expected**: -50-60% (0.45-0.55s saved)
- **Effort**: 1 day

### Tier 2: DSL Memoization (2-3 days)

#### 4. **Memoize `apply` function**
- **Current**: 0.688s (5,400 calls, 0.127ms/call)
- **Approach**:
  - Add `@lru_cache` for pure function + hashable container combinations
  - Cache size: 256-512 entries
  - Monitor cache hit rate
- **Expected**: 20-30% improvement if high reuse (0.14-0.21s saved)
- **Effort**: 1 day

#### 5. **Optimize `o_g` and `objects` algorithms**
- **Current**: o_g (1.163s), objects (1.140s)
- **Approach**:
  - Pre-compute neighbor offsets (avoid recalculation)
  - Use spatial indexing for large grids
  - Optimize flood-fill in objects
- **Expected**: 10-15% improvement (0.23-0.35s saved)
- **Effort**: 2 days

### Tier 3: Framework Architecture (if needed)

#### 6. **Reduce function call overhead globally**
- **Current**: 739,260 wrapper calls = massive overhead
- **Approach**:
  - Profile exact call stack
  - Identify unnecessary wrapping layers
  - Consider JIT compilation for hot paths
- **Expected**: Additional 5-10% (0.3-0.5s saved)
- **Effort**: 2-3 days

---

## Implementation Plan

### Week 1 (Oct 15-22): Framework Optimizations

**Day 1-2**: Investigate and optimize `wrapper` function
- Profile exact call stack
- Identify wrapping layers
- Implement inline optimizations
- Test and validate

**Day 3**: Optimize type checking (`get_type_hints`)
- Cache type hints at module level
- Add `@lru_cache` decorator
- Test performance impact

**Day 4**: Optimize candidate management (`_get_safe_default`)
- Cache safe defaults by type
- Pre-compute common values
- Validate correctness

**Day 5**: Test and validate all framework optimizations
- Run on Kaggle with 100 tasks
- Verify correctness
- Measure speedup
- **Expected**: 3.0-3.5s (vs 5.24s baseline)

### Week 2 (Oct 23-29): DSL Optimizations (if needed)

**Day 6-7**: Memoization for DSL functions
- Add `@lru_cache` to `apply`, `merge`
- Monitor cache hit rates
- Optimize cache sizes

**Day 8-9**: Algorithm optimizations
- Optimize `o_g` and `objects`
- Pre-compute neighbor offsets
- Spatial indexing for large grids

**Day 10**: Final validation
- Full Kaggle run (100 tasks)
- Correctness verification
- Performance measurement
- **Target**: 3.5-4.0s total

---

## Expected Results

### Conservative Estimate
- wrapper optimization: -2.0s (5.24s → 3.24s)
- Type checking: -0.5s (3.24s → 2.74s)
- Candidate mgmt: -0.45s (2.74s → 2.29s)
- DSL memoization: -0.15s (2.29s → 2.14s)
- **Total**: 5.24s → **2.14s** (2.45x from Stage 2)
- **Combined**: 37.78s → 2.14s (**17.7x total!**)

### Realistic Estimate
- wrapper optimization: -2.5s (5.24s → 2.74s)
- Type checking: -0.6s (2.74s → 2.14s)
- Candidate mgmt: -0.5s (2.14s → 1.64s)
- DSL optimizations: -0.3s (1.64s → 1.34s)
- **Total**: 5.24s → **1.34s** (3.9x from Stage 2)
- **Combined**: 37.78s → 1.34s (**28.2x total!**)

### Target Range
- **Stage 2**: 5.24s → 3.5-4.0s (1.3-1.5x)
- **Total**: 37.78s → 3.5-4.0s (9.4-10.8x)

---

## Priority Order

### MUST DO (To reach 9-11x goal):
1. ✅ **wrapper optimization** (biggest single opportunity: 2-2.5s)
2. ✅ **get_type_hints caching** (easy win: 0.5-0.6s)
3. ✅ **_get_safe_default caching** (easy win: 0.45-0.55s)

### SHOULD DO (To exceed goal):
4. 🟡 **apply memoization** (moderate win if high reuse: 0.15-0.2s)
5. 🟡 **o_g/objects algorithm optimization** (moderate effort: 0.2-0.35s)

### COULD DO (If time permits):
6. 🟢 **Global call overhead reduction** (complex but powerful: 0.3-0.5s)
7. 🟢 **Additional DSL memoization** (diminishing returns)

---

## Success Criteria

### Minimum Success (Tier 1 only):
- ✅ Wall-clock: <4.0s (from 5.24s, 31% improvement)
- ✅ Total speedup: >9.4x (37.78s → <4.0s)
- ✅ Correctness maintained (all outputs match)

### Target Success (Tier 1 + some Tier 2):
- ✅ Wall-clock: 3.5-4.0s (from 5.24s, 31-40% improvement)
- ✅ Total speedup: 9.4-10.8x (37.78s → 3.5-4.0s)
- ✅ Correctness maintained

### Stretch Success (All tiers):
- 🎯 Wall-clock: <3.0s (from 5.24s, >43% improvement)
- 🎯 Total speedup: >12x (37.78s → <3.0s)
- 🎯 Correctness maintained

---

## Risk Assessment

### Low Risk (Quick wins):
- Type hint caching: Just add `@lru_cache`
- Safe default caching: Simple dict caching

### Medium Risk (Requires investigation):
- wrapper optimization: Need to understand call stack
- apply memoization: Must handle non-hashable inputs

### High Risk (Complex changes):
- Global call overhead: May require architecture changes
- Algorithm optimizations: Risk breaking correctness

**Strategy**: Start with low-risk, high-impact optimizations first!

---

## Next Steps

**Immediate** (tonight):
1. 🔍 Profile `wrapper` function to understand what it does
2. 🔍 Profile `batt` function call stack
3. 🔍 Investigate `get_type_hints` usage patterns
4. 📝 Create detailed implementation plan for wrapper optimization

**Tomorrow**:
1. Implement wrapper optimization
2. Test locally
3. Deploy to Kaggle
4. Measure improvement

**This Week**:
- Focus on Tier 1 (framework optimizations)
- Target: 5.24s → 3.0-3.5s
- Validate correctness at each step

---

**STATUS**: Planning Complete ✅  
**READY TO START**: Investigating framework bottlenecks  
**FIRST TARGET**: wrapper function (5.134s, 739K calls)  
**EXPECTED STAGE 2 RESULT**: 1.3-1.5x additional (9-11x total)
