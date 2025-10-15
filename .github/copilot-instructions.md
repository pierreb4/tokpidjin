# Copilot Instructions for tokpidjin Project

## Project Overview

This is an ARC (Abstraction and Reasoning Corpus) solver project with GPU acceleration for Kaggle competition.

## GPU Optimization Status

**READ FIRST**: `GPU_SOLVER_STRATEGY.md` - Complete solver GPU acceleration strategy

### Key Achievement - Strategy Pivot
- **Previous approach**: GPU-accelerate individual DSL operations → ❌ FAILED (p_g: GPU 3x slower)
- **New approach**: GPU-accelerate solver functions → ✅ VALIDATED (expect 2-6x speedup)
- **Discovery**: Solver functions are 10-1000x longer than DSL ops (1-120ms vs 0.1ms)
- **Result**: GPU overhead (0.2ms) becomes negligible for long solvers (0.2-2% vs 167%)

### Solver Benchmark Results (Kaggle L4 GPU)
| Solver | Operations | CPU Time | GPU Viability | Expected Speedup |
|--------|------------|----------|---------------|------------------|
| solve_36d67576 | 33 | 120.674 ms | ✅✅ Excellent | 3-6x (→20-40ms) |
| solve_36fdfd69 | 16 | 58.314 ms | ✅✅ Excellent | 3-5x (→12-19ms) |
| solve_1a07d186 | 16 | 11.004 ms | ✅ Good | 2-3x |
| solve_09629e4f | 7 | 6.379 ms | ✅ Good | 2-3x |

**Distribution (28 solvers tested)**:
- 21% too fast (<1ms) → CPU only
- 54% borderline (1-5ms) → marginal GPU benefit
- 18% good (5-15ms) → 2-3x speedup
- 7% excellent (>15ms) → 3-6x speedup

### Batch Operations (Previous Work)
| GPU Type | Single GPU | Multi-GPU | Recommendation |
|----------|------------|-----------|----------------|
| L4x4 🥇 | 9.35x | ~35x (4 GPUs) | Maximum performance |
| T4x2 🥈 | 9.69x | ~18x (2 GPUs) | Best availability ⭐ |
| P100 🥉 | 7.64x | N/A (1 GPU) | Fallback |

**All GPUs cost the same on Kaggle - choose based on availability!**

## Code Guidelines

### When Working with GPU Code

1. **Two GPU strategies**:
   - Batch operations (PRODUCTION): Use `auto_select_optimizer()` for batch grid processing
   - Solver acceleration (IN DEVELOPMENT): Hybrid GPU strategy for solver functions

2. **Hybrid GPU approach** (NEW STRATEGY):
   - GPU works with arrays/tuples internally (optimal performance)
   - Converts to frozensets only at boundaries (DSL compatibility)
   - No need to refactor dsl.py frozensets (80-90% speedup with 5% effort)
   - Target: `gpu_o_g` implementation for 2.3-7.8x speedup

3. **Implementation priority**: 
   - Week 1: Hybrid GPU o_g with frozenset return
   - Week 2: Validation on profiled solvers
   - Week 3: Add dual-return API (tuple for GPU-resident solvers)
   - Week 4: Convert 10-20 solvers to GPU-resident

4. **Test on Kaggle** - Always verify GPU code on actual Kaggle hardware
5. **Batch operations** - Optimal batch size is 200 grids (for batch processing)
6. **Auto-detection** - Use `auto_select_optimizer()` for automatic GPU selection

### When Suggesting GPU Changes

**DON'T:**
- ❌ Suggest GPU-accelerating individual DSL operations <1ms (proven ineffective)
- ❌ Propose per-element GPU transfers (use batch processing or solver-level transfer)
- ❌ Ignore JIT warmup (causes inconsistent performance)
- ❌ Hard-code GPU types (use auto-detection)
- ❌ Rewrite vectorized operations to use loops
- ❌ Suggest refactoring dsl.py frozensets to tuples (172 occurrences, high risk, low ROI)

**DO:**
- ✅ Focus on solver functions (>5ms execution time) for GPU acceleration
- ✅ Check `GPU_O_G_IMPLEMENTATION.md` for current implementation plan
- ✅ Use hybrid GPU strategy (arrays on GPU, frozenset at boundaries)
- ✅ Profile before implementing (use `profile_solvers.py`)
- ✅ Use `KaggleGPUOptimizer` or `MultiGPUOptimizer` for batch operations
- ✅ Maintain batch processing architecture
- ✅ Test on all GPU types (T4x2, P100, L4x4)

### Operation Complexity Guidelines

Based on extensive testing:

**❌ DON'T GPU Accelerate (Transfer overhead > Compute):**
- Simple DSL ops: p_g, rot90, flip, transpose, shift, crop (all <0.5ms)
- Any operation with CPU time <1ms
- Operations requiring complex Python object conversion (frozensets, tuples)
- Operations in solver functions that execute <1ms

**✅ DO GPU Accelerate (Compute >> Transfer):**
- **Solver functions** with >5ms CPU time (PRIMARY FOCUS)
- Complex DSL operations within solvers: o_g, fgpartition, gravitate
- Iterative ops: flood_fill (100+ iterations), gravitate (42 iterations)
- Batch operations: processing 100+ grids simultaneously
- Operation pipelines (chain multiple ops on GPU without CPU transfer)

**Key Insight from Testing:**
- Individual DSL operation GPU acceleration: FAILED (p_g 3x slower)
- Solver function GPU acceleration: VALIDATED (expect 2-6x faster)
- Lesson: Target execution time matters more than operation complexity

### Code Quality Standards

1. **Async/Await**: Use `async`/`await` consistently for timeout handling
2. **Thread Management**: Use limited ThreadPoolExecutor (max_workers=4)
3. **Error Handling**: Always include CPU fallbacks for GPU operations
4. **Type Hints**: Use type hints from `arc_types.py`
5. **Documentation**: Update relevant .md files when changing GPU code

## File Organization

### GPU-Related Files
- **`gpu_optimizations.py`** - Main GPU implementation (530 lines, PRODUCTION READY)
- **`GPU_PROJECT_SUMMARY.md`** - Executive summary (READ THIS FIRST)
- **`COMPLETE_GPU_COMPARISON.md`** - GPU selection guide
- **`INTEGRATION_GUIDE.md`** - How to integrate GPU code
- **`MULTI_GPU_SUPPORT.md`** - Multi-GPU usage guide

### Core DSL Files
- **`dsl.py`** - Domain Specific Language functions (3725 lines)
- **`arc_types.py`** - Type definitions
- **`utils.py`** - Utility functions (async timeout handling)
- **`solvers.py`** - ARC solver implementations

### Testing & Validation
- **`run_batt.py`** - Batch solver evaluation (async)
- **`run_test.py`** - DSL test runner (async)
- **`test_kaggle_gpu_optimized.py`** - GPU test suite
- **`test_multi_gpu.py`** - Multi-GPU validation

## Common Tasks

### Adding a New DSL Function

1. Add function to `dsl.py` with proper type hints
2. If complex (compute > 20ms), consider GPU version in `gpu_optimizations.py`
3. Add tests to verify correctness
4. Update documentation if it's a major feature

### Optimizing Performance

1. **Profile first** - Use timing analysis to find hot paths
2. **Check GPU viability** - Is compute >> transfer time?
3. **Use existing patterns** - See `INTEGRATION_GUIDE.md`
4. **Test on Kaggle** - Verify actual speedup on real hardware
5. **Document results** - Update relevant .md files

### Fixing Errors

1. **Check async/await** - Most errors are missing `await` keywords
2. **Thread exhaustion** - Use the limited ThreadPoolExecutor
3. **GPU errors** - Verify CuPy is available and GPU is enabled
4. **Type errors** - Check `arc_types.py` for correct types

## Integration Patterns

### Using GPU Optimization

```python
from gpu_optimizations import auto_select_optimizer

# Automatic GPU selection (works on all Kaggle types)
optimizer = auto_select_optimizer()

# Process batch
results = optimizer.batch_grid_op_optimized(
    grids,
    operation_vectorized,
    vectorized=True,
    operation_single=operation_single
)
```

### Async Timeout Handling

```python
from utils import run_with_timeout

# Use async/await for timeout handling
result = await run_with_timeout(function, args, timeout=10.0)
```

## Key Insights

### GPU Optimization Journey
- **Started**: GPU 830x slower than CPU (broken)
- **Problem**: Per-element transfers, no warmup, wrong thresholds
- **Solution**: Batch processing, JIT warmup, vectorization
- **Result**: 10-35x faster than CPU (production ready)

### Lessons Learned
1. **Batch processing is critical** - Single transfer per batch, not per element
2. **JIT warmup matters** - Eliminates 800ms first-run overhead
3. **Not all operations benefit** - Simple ops stay on CPU
4. **Multi-GPU scales well** - 85-90% efficiency
5. **Automatic detection works** - One codebase for all GPUs

## Documentation Structure

### Quick Start (Read These First)
1. **GPU_DOCS_INDEX.md** - Complete documentation index and navigation
2. **GPU_SOLVER_STRATEGY.md** - Solver GPU acceleration strategy (START HERE FOR NEW WORK)
3. **GPU_PROJECT_SUMMARY.md** - Batch operations status and results
4. **COMPLETE_GPU_COMPARISON.md** - Which GPU to use
5. **INTEGRATION_GUIDE.md** - How to integrate batch operations

### Implementation Guide (CURRENT WORK)
6. **GPU_O_G_IMPLEMENTATION.md** - Complete implementation guide for GPU o_g (START HERE) ⭐
7. **benchmark_solvers.py** - Benchmarks solver execution times (validated on Kaggle)
8. **profile_solvers.py** - Profiles DSL operations within solvers (validated, found o_g bottleneck)

### Technical Deep Dives (Batch Operations)
9. **GPU_OPTIMIZATION_SUCCESS.md** - Complete batch operations analysis
10. **MULTI_GPU_SUPPORT.md** - Multi-GPU details
11. **GPU_VECTORIZATION_UPDATE.md** - Vectorization patterns
12. **KAGGLE_GPU_OPTIMIZATION.md** - GPU specs
13. **GPU_TRANSFER_FIX.md** - Batch transfer details
14. **GPU_JIT_WARMUP.md** - JIT compilation handling
15. **GPU_FALLBACK_FIX.md** - Error handling patterns
16. **GPU_COMPARISON_P100_L4.md** - P100 vs L4 comparison
17. **GPU_BATCH_README.md** - Batch processing details

### Archived Documentation
- **archive/gpu_docs_superseded/** - Older docs replaced by comprehensive guides
- **archive/gpu_solver_analysis_2025_10_10/** - Intermediate analysis (o_g bottleneck discovery)
  - Kept for historical reference only

## Testing Requirements

### Before Committing GPU Changes

1. **Correctness**: Results must match CPU version exactly
2. **Performance**: Must show >= 2x speedup on Kaggle
3. **All GPUs**: Test on T4x2, P100, and L4x4
4. **Fallback**: CPU fallback must work when GPU unavailable
5. **Documentation**: Update relevant .md files

### Test Commands

```bash
# Local testing (CPU fallback)
python gpu_optimizations.py

# Kaggle testing (with GPU)
python test_kaggle_gpu_optimized.py
python test_multi_gpu.py
```

## Version Control

### Commit Message Format
- **feat**: New feature (e.g., "feat: add multi-GPU support")
- **fix**: Bug fix (e.g., "fix: async timeout handling")
- **perf**: Performance improvement (e.g., "perf: optimize batch transfers")
- **docs**: Documentation (e.g., "docs: update GPU comparison")
- **test**: Tests (e.g., "test: add L4x4 GPU tests")

### Branch Strategy
- **main**: Production-ready code only
- **feature/**: New features in development
- **fix/**: Bug fixes
- **perf/**: Performance optimizations

## Support & Resources

### When Stuck
1. Check **GPU_PROJECT_SUMMARY.md** for overview
2. Read **INTEGRATION_GUIDE.md** for patterns
3. Look at **test_kaggle_gpu_optimized.py** for examples
4. Review **gpu_optimizations.py** for implementation details

### Kaggle-Specific Issues
- **GPU not available**: Check kernel GPU is enabled
- **Memory errors**: Reduce batch size (try 100 instead of 200)
- **Slow performance**: Ensure JIT warmup is included
- **Wrong results**: Verify vectorized operation correctness

## Current Status (October 2025)

✅ **GPU optimization for batch operations**: Production ready, 10-35x speedup  
✅ **Multi-GPU support**: Working on T4x2 and L4x4  
✅ **Strategy pivot**: Discovered solver functions are perfect GPU target (not individual DSL ops)  
✅ **Solver benchmarks**: Validated 28 solvers, found 2 excellent candidates (58ms, 120ms)  
✅ **Scale analysis complete**: GPU optimization ROI increases 25x from testing (32 tasks) to production (400 tasks)  
✅ **Kaggle profiling complete**: 100 tasks profiled, discovered 4 outliers (infinite loops), validated framework is 92.4% bottleneck  
✅ **Filtered analysis**: Removed outliers, confirmed priorities unchanged (framework 92.4%, DSL 7.6%)  
🔄 **In progress**: Framework bottleneck profiling with cProfile to identify specific functions (batch_process_samples_gpu, dedupe, etc.)  
⏳ **Next**: Implement framework optimizations (2-5x speedup target) based on detailed profiling data  

**Current focus**: Using profile_batt_framework.py to identify specific bottlenecks within 92.4% framework overhead

## Competition Resources

**Kaggle ARC Competition Allocation:**
- **Compute**: 8 hours of L4x4 GPU time (28,800 seconds)
- **Hardware**: 4× NVIDIA L4 GPUs, 24GB each (best available)
- **Philosophy**: With abundant compute, ALL GPU optimizations are worthwhile
- **Strategy**: Multi-week optimization efforts justified for even small improvements

**Scale Impact:**
- Testing at 32 tasks: Solver time 0.7s (GPU saves 0.6s)
- Production at 400 tasks: Solver time 15.9s (GPU saves 15.5s)
- **ROI increases 25x with scale!**

**After optimization:**
- Solver time: 0.3-0.5s at 400 tasks (30-50x faster)
- Total pipeline: 4.3-4.5s vs 42.5s baseline (9-10x faster)
- Result: Can run pipeline **thousands of times** in 8hr budget

## Profiling Workflow

### Local Development (Laptop)
- ❌ **Don't profile on local laptop** - Threading/multiprocessing obscures DSL function times
- ❌ **Don't trust local timing data** - No GPU, different threading model than production
- ✅ **Do develop profiling tools locally** - Create and test profilers on small examples
- ✅ **Do commit profilers to repo** - Deploy to Kaggle for real data collection

### Kaggle Profiling (Production Environment)
- ✅ **Run profile_batt_batch.py on Kaggle** - With GPU enabled, across 50-100 tasks
- ✅ **Profile generated batt functions** - Use tmp_batt_onerun_run.py or similar
- ✅ **Collect aggregate statistics** - Which DSL ops are bottlenecks across all tasks
- ✅ **Prioritize by % of execution time** - Target ops with >5% total time
- ✅ **Validate with multiple runs** - Ensure consistent bottleneck identification

### Development Cycle
1. **Local**: Create profiling tools, test on small examples
2. **Kaggle**: Deploy profilers, collect real data with GPU
3. **Local**: Implement GPU DSL operations based on Kaggle data
4. **Kaggle**: Test GPU ops, measure actual speedup, validate correctness
5. **Local**: Document results, iterate on implementation

## Important Notes

1. **All Kaggle GPUs cost the same** - Choose based on availability, not cost
2. **T4x2 has best availability** - Recommended default choice
3. **L4x4 has best performance** - Try to get this allocation (35x speedup for batch ops)
4. **Batch size 200 is optimal** - For batch grid operations
5. **Multi-GPU auto-enabled** - When batch size >= 120 grids
6. **Profile on Kaggle, not locally** - Threading obscures DSL function times on local machines

## Quick Reference

### Scale Analysis Decision Tree
```
Testing scale (32 tasks, 0.7s solver)?
  → GPU optimization ROI: Low (saves 0.6s)
  → Still develop tools for production scale

Production scale (400 tasks, 15.9s solver)?
  → GPU optimization ROI: HIGH (saves 15.5s = 97% faster)
  → Batch ops: ESSENTIAL (14-15s saved, 1-2 days effort)
  → GPU DSL: HIGH VALUE (2-4s saved, 4-6 weeks effort)
  
Full scale (1000 tasks, 39.7s solver)?
  → GPU optimization ROI: CRITICAL (saves 39s)
  → Both optimizations mandatory for production

With 8 hours L4x4 GPU:
  → Every optimization is worthwhile
  → Multi-week efforts justified
  → Optimize aggressively
```

### GPU Selection Decision Tree
```
Need maximum performance? → Try L4x4 (35x with 4 GPUs)
  ├─ Available? → Use L4x4 ✓
  └─ Not available? → Use T4x2 (18x with 2 GPUs) ✓

Want reliable availability? → Use T4x2 (9.69x single, 18x dual)

Only P100 available? → Use P100 (7.64x speedup) ✓

No GPU available? → CPU fallback works automatically ✓
```

### Integration Checklist
- [ ] Import `auto_select_optimizer()`
- [ ] Replace loops with batch processing
- [ ] Include JIT warmup in benchmarks
- [ ] Test on Kaggle with GPU enabled
- [ ] Verify correctness matches CPU
- [ ] Measure actual speedup
- [ ] Document results

---

**Remember**: The GPU optimization work is complete and production-ready. Focus on integrating it into your ARC solver workflow to achieve 10-35x speedup!
