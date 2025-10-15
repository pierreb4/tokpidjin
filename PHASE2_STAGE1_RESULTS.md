# Phase 2 Stage 1: Results Analysis

**Date**: October 15, 2025  
**Test**: 100 tasks on Kaggle L4x4 GPU  
**Status**: ⚠️ **MINIMAL IMPROVEMENT** - Further investigation needed

---

## Executive Summary

Phase 2 Stage 1 optimizations showed **minimal improvement** on Kaggle:
- **Baseline (Phase 1)**: 6.64s for 100 tasks
- **After Stage 1**: 6.73s for 100 tasks
- **Change**: +0.09s (1.4% SLOWER)

### Key Findings

❌ **Stage 1 optimizations did NOT achieve expected 15-20% speedup**  
⚠️ **Profiling shows DSL functions actually IMPROVED but overall time increased**  
🔍 **Need to investigate why wall-clock time increased**

---

## Detailed Results Comparison

### Wall-Clock Time
```
Baseline (Phase 1):  6.64s for 100 tasks
Stage 1:             6.73s for 100 tasks
Change:              +0.09s (1.4% slower)
```

### Top DSL Functions Performance

| Function | Baseline | Stage 1 | Change | Expected |
|----------|----------|---------|--------|----------|
| mapply_t | 2.148s | **N/A** | ??? | 1.75-1.95s |
| apply_t | 2.106s | **N/A** | ??? | 1.90-2.00s |
| o_g | 1.430s | 1.506s | +0.076s | 1.23-1.29s |
| objects | 1.374s | 1.449s | +0.075s | 1.17-1.24s |
| apply | 1.279s | 1.306s | +0.027s | - |

⚠️ **NOTE**: mapply_t and apply_t not appearing in top functions (moved down the list)

### Category Breakdown

| Category | Baseline | Stage 1 | Change |
|----------|----------|---------|--------|
| Other Framework | 40.141s (75.1%) | 40.693s (78.2%) | +0.552s |
| DSL Operations | 10.094s (18.9%) | 8.142s (15.6%) | **-1.952s** ✅ |
| Candidate Mgmt | 3.000s (5.6%) | 3.045s (5.8%) | +0.045s |
| GPU Batch | 0.099s (0.2%) | 0.101s (0.2%) | +0.002s |

**Analysis**: DSL operations actually got FASTER (-1.952s, -19% improvement!), but framework overhead increased (+0.552s) which offset the gains.

---

## Investigation Needed

### Question 1: Why did o_g and objects get SLOWER?
- **Expected**: Array lookup and list operations should be faster
- **Actual**: Both functions ~5% slower
- **Hypothesis**: 
  - Array unpacking overhead? (`*params` vs direct arguments)
  - List → frozenset conversion overhead?
  - JIT compilation not optimizing new code?

### Question 2: Where did mapply_t and apply_t go?
- **Baseline**: mapply_t (2.148s), apply_t (2.106s) in top 5
- **Stage 1**: Not visible in top 5 DSL functions
- **Hypothesis**:
  - Optimizations worked SO WELL they fell below threshold?
  - Changed names due to code modifications?
  - Merged into other function measurements?

### Question 3: Why did framework overhead increase?
- **Baseline**: 40.141s (75.1%)
- **Stage 1**: 40.693s (78.2%)
- **Change**: +0.552s (+1.4%)
- **Hypothesis**:
  - Type checking overhead from modified functions?
  - safe_dsl wrapper overhead increased?
  - get_type_hints calls increased?

---

## Next Steps

### Immediate Actions

1. **Get full profiling data**:
   - Request complete pstats output (not just summary)
   - Need to see ALL functions, not just top 5
   - Confirm mapply_t and apply_t actual times

2. **Compare function call counts**:
   - Baseline: 628,917 DSL calls
   - Stage 1: 534,931 DSL calls (-94k calls, -15%)
   - Why did call count drop? Expected same calls but faster execution

3. **Review code changes**:
   - Double-check o_g array lookup implementation
   - Verify objects list operations
   - Ensure no unintended side effects

### Testing Strategy

**Option A: Revert and Test Incrementally**
1. Revert all changes
2. Apply only mapply_t optimization
3. Test → measure
4. Apply only apply_t optimization  
5. Test → measure
6. Apply only o_g optimization
7. Test → measure
8. Apply only objects optimization
9. Test → measure

**Option B: Investigate Framework Overhead**
1. Keep current optimizations
2. Profile framework bottlenecks specifically
3. Identify why wrapper/get_type_hints overhead increased
4. May be winning on DSL but losing on framework

**Option C: Get More Data**
1. Run with different task counts (50, 200)
2. Multiple runs to check variance
3. Profile on different GPU (T4x2 vs L4x4)
4. Compare to local CPU profiling

---

## Hypothesis: Hidden Success?

### Evidence for "DSL optimizations worked":
- ✅ DSL operations: 10.094s → 8.142s (**-19% improvement!**)
- ✅ DSL call count: 628,917 → 534,931 (-15% fewer calls)
- ✅ mapply_t/apply_t disappeared from top 5 (too fast now?)

### Evidence for "Framework overhead increased":
- ❌ Framework: 40.141s → 40.693s (+1.4%)
- ❌ Wall-clock: 6.64s → 6.73s (+1.4%)

**Possible explanation**: Optimizations ARE working but framework overhead from safe_dsl wrapper, type checking, or other infrastructure code increased slightly, masking the gains.

---

## Detailed Function Analysis Needed

### Request Full Data
```python
# Need to see in Stage 1 results:
- mapply_t: ??? (was 2.148s)
- apply_t: ??? (was 2.106s)  
- o_g: 1.506s (was 1.430s) ❌
- objects: 1.449s (was 1.374s) ❌
- apply: 1.306s (was 1.279s)
```

### Specific Questions
1. What is mapply_t time in Stage 1? (hidden in output)
2. What is apply_t time in Stage 1? (hidden in output)
3. Why did o_g get 5% slower? (1.430s → 1.506s)
4. Why did objects get 5% slower? (1.374s → 1.449s)
5. Why did DSL call count drop 15%? (628k → 535k)

---

## Recommendations

### Recommendation 1: Get Complete Profiling Data ⭐
**Priority**: CRITICAL  
**Action**: Request full pstats output showing ALL functions, not just top 5  
**Rationale**: Cannot diagnose without seeing mapply_t and apply_t actual times

### Recommendation 2: Test Locally First
**Priority**: HIGH  
**Action**: Run `python profile_batt_framework.py --tasks 100` locally  
**Rationale**: Easier to debug and get full profiling data

### Recommendation 3: Incremental Testing
**Priority**: MEDIUM  
**Action**: Test each optimization individually  
**Rationale**: Identify which changes help vs hurt

### Recommendation 4: Fix Profiling Script
**Priority**: MEDIUM  
**Action**: Fix the TypeError in save_detailed_report()  
**Rationale**: Need complete profiling output for analysis

---

## Questions for User

1. **Can you provide the full profiling output?** (not just top 5 functions)
2. **What are the actual times for mapply_t and apply_t in Stage 1?**
3. **Can you run with `--output detailed` or save full pstats file?**
4. **Is the 6.73s timing consistent across multiple runs?** (check variance)
5. **Did the correctness check pass?** (same outputs as baseline?)

---

## Status

**Current state**: Stage 1 showed minimal improvement (+1.4% slower overall)  
**DSL operations**: Actually improved significantly (-19%)  
**Problem**: Framework overhead increased, masking gains  
**Next action**: Get full profiling data to understand what happened  
**Decision pending**: Whether to proceed with Stage 2 or investigate Stage 1

---

**Updated**: October 15, 2025  
**Conclusion**: Need more data before proceeding. DSL optimizations may be working but hidden by framework overhead increase.
