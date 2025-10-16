# Phase 2: DSL Optimization Plan

## Executive Summary

**Goal**: Optimize DSL operations for 2-3x additional speedup
- **Current**: 6.64s for 100 tasks (after Phase 1 logging optimization)
- **Target**: 2-3s for 100 tasks (9-12x total speedup from 37.78s baseline)
- **Approach**: GPU acceleration + algorithmic improvements + caching

## Top DSL Bottlenecks (from Kaggle profiling)

Based on validated Kaggle profiling results:

| Function | Time (s) | % of Total | Calls | Per Call (ms) | Priority |
|----------|----------|------------|-------|---------------|----------|
| mapply_t | 2.148 | 4.0% | 700 | 3.07 | 🔴 HIGH |
| apply_t | 2.106 | 3.9% | 700 | 3.01 | 🔴 HIGH |
| o_g | 1.430 | 2.7% | 3,400 | 0.42 | 🟡 MEDIUM |
| objects | 1.374 | 2.6% | 3,400 | 0.40 | 🟡 MEDIUM |
| apply | 1.279 | 2.4% | 7,772 | 0.16 | 🟢 LOW |
| **Total Top 5** | **8.337s** | **15.6%** | **15,972** | | |

## Optimization Strategy

### 1. High Priority: mapply_t and apply_t (4.254s, 8%)

**Current behavior**:
- Apply functions to tuple/list elements
- 700 calls each, ~3ms per call
- Likely involves object conversion overhead

**Optimization approaches**:

A. **Vectorization** (Quick win, 1-2 days)
   - Batch multiple mapply/apply operations
   - Reduce Python call overhead
   - Expected: 1.5-2x speedup on these functions

B. **Caching results** (Medium effort, 2-3 days)
   - Memoize frequently called functions
   - Use LRU cache for pure functions
   - Expected: 2-3x speedup if high reuse

C. **GPU acceleration** (High effort, 1 week)
   - Implement GPU versions for array operations
   - Use hybrid strategy (GPU for bulk, CPU for small)
   - Expected: 2-4x speedup on large operations

**Recommendation**: Start with A (vectorization), then B (caching)

### 2. Medium Priority: o_g and objects (2.804s, 5.3%)

**Current behavior**:
- Object graph operations and object extraction
- 3,400 calls each, ~0.4ms per call
- Complex grid analysis operations

**Optimization approaches**:

A. **Algorithm optimization** (Medium effort, 3-4 days)
   - Review current implementation for inefficiencies
   - Reduce redundant computations
   - Use spatial indexing where possible
   - Expected: 1.5-2x speedup

B. **GPU acceleration** (High effort, 1-2 weeks)
   - Implement hybrid GPU strategy from GPU_O_G_IMPLEMENTATION.md
   - Arrays on GPU, frozenset at boundaries
   - Expected: 2-4x speedup based on benchmarks

**Recommendation**: Start with A (algorithm optimization), evaluate B based on results

### 3. Lower Priority: apply (1.279s, 2.4%)

**Current behavior**:
- Generic function application
- 7,772 calls, ~0.16ms per call
- High call count suggests frequent small operations

**Optimization approaches**:

A. **Inline frequently used operations** (Quick win, 1 day)
   - Identify most common apply patterns
   - Create specialized versions
   - Expected: 1.2-1.5x speedup

B. **Batch processing** (Medium effort, 2-3 days)
   - Group apply operations
   - Reduce function call overhead
   - Expected: 1.5-2x speedup

**Recommendation**: A (inlining) only if time permits after higher priorities

## Other Framework Overhead (not DSL)

From Kaggle results, remaining "Other Framework" is 75.1%:

- **get_type_hints** (2.657s, ~5%): Type checking overhead - hard to optimize without breaking safety
- **wrapper** (6.533s, ~12%): Safe_dsl rate-limited wrapper - acceptable overhead
- **f, <genexpr>** (~4.7s, ~9%): Generator/function overhead - part of functional style
- **batt** (6.603s, ~12%): Main entry point and orchestration

**Note**: These are harder to optimize without major architectural changes. Focus on DSL first.

## Implementation Plan

### Week 1: Vectorization + Caching (Quick Wins)

**Days 1-2**: Vectorize mapply_t and apply_t
- Identify vectorizable patterns
- Implement batch processing
- Test on Kaggle (expect 4.254s → 2-3s)

**Days 3-4**: Add caching layer
- Implement LRU cache for pure functions
- Add memoization to frequent operations
- Test on Kaggle (expect additional 20-30% reduction)

**Day 5**: Validation and profiling
- Run full 100-task profiling on Kaggle
- Measure actual speedup
- Document results

**Expected Week 1 results**: 6.64s → 4-5s (1.3-1.7x speedup)

### Week 2: Algorithm Optimization

**Days 1-3**: Optimize o_g and objects
- Review current implementations
- Identify inefficiencies
- Implement improvements
- Test on Kaggle (expect 2.804s → 1.5-2s)

**Days 4-5**: Integration and testing
- Combine all optimizations
- Run full profiling
- Validate correctness

**Expected Week 2 results**: 4-5s → 2.5-3.5s (1.4-2x additional speedup)

### Week 3+: GPU Acceleration (If Needed)

Only if Week 1-2 optimizations don't achieve 2-3x target:

**Implementation**:
- Hybrid GPU strategy for o_g (per GPU_O_G_IMPLEMENTATION.md)
- GPU versions of mapply_t/apply_t for large operations
- Batch GPU transfers

**Expected**: 2-4x speedup on GPU-accelerated operations

## Success Metrics

### Incremental Goals

After Week 1 (vectorization + caching):
- Target: 6.64s → 4-5s
- Success: ≥1.3x speedup

After Week 2 (algorithm optimization):
- Target: 4-5s → 2.5-3.5s
- Success: ≥2x total Phase 2 speedup

### Final Goals (Phase 1 + Phase 2)

100 tasks:
- Baseline: 37.78s
- Phase 1: 6.64s (5.7x)
- Phase 2 target: 2.5-3.5s (10-15x total)
- Success: ≥9x total speedup

400 tasks:
- Baseline: ~630s (10.5 min)
- Target: ~50-70s (0.8-1.2 min)
- Success: ≥9x speedup

### Correctness Validation

For each optimization:
1. Run `python run_batt.py --validate` on Kaggle
2. Compare outputs with baseline
3. Ensure no regressions in solve rate

## Risk Mitigation

### Risks

1. **Optimization doesn't transfer to Kaggle**: Local results may not scale
   - Mitigation: Test each optimization on Kaggle before proceeding
   
2. **Correctness issues**: Aggressive optimization may introduce bugs
   - Mitigation: Comprehensive validation after each change
   
3. **Diminishing returns**: Later optimizations may not compound
   - Mitigation: Profile after each step, adjust strategy as needed

4. **Time overrun**: Optimizations take longer than planned
   - Mitigation: Focus on high-priority items first, skip low-priority if needed

## Tools and Resources

### Profiling Tools
- `profile_batt_framework.py`: Framework profiling with categorization
- `benchmark_solvers.py`: Individual solver benchmarking
- Kaggle notebooks: For production profiling

### Documentation
- `GPU_O_G_IMPLEMENTATION.md`: Hybrid GPU strategy for o_g
- `KAGGLE_VALIDATION_RESULTS.md`: Phase 1 results and baseline
- `.github/copilot-instructions.md`: Project guidelines

### Testing
- `run_batt.py --validate`: Correctness validation
- `test_kaggle_gpu_optimized.py`: GPU optimization tests
- Kaggle notebooks: Production testing

## Next Steps

1. ✅ **Archive old documentation** (DONE)
2. 🔄 **Analyze mapply_t and apply_t implementations** (CURRENT)
3. ⏳ **Implement vectorization** (Week 1)
4. ⏳ **Add caching layer** (Week 1)
5. ⏳ **Optimize o_g and objects** (Week 2)
6. ⏳ **Validate and measure** (Ongoing)

## Conclusion

Phase 2 targets a realistic 2-3x additional speedup through:
1. **Quick wins**: Vectorization and caching (Week 1)
2. **Algorithm improvements**: Optimize core operations (Week 2)
3. **GPU acceleration**: Only if needed (Week 3+)

Combined with Phase 1's 5.7x speedup, this achieves 9-15x total improvement, bringing 100-task execution from 37.78s to 2.5-3.5s.

The strategy is incremental, validated at each step, and focuses on high-impact optimizations first.

---

**Status**: Ready to begin Phase 2  
**Next action**: Analyze mapply_t and apply_t implementations  
**Timeline**: 2-3 weeks to 2-3x speedup target
