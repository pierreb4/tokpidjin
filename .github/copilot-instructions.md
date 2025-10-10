# Copilot Instructions for tokpidjin Project

## Project Overview

This is an ARC (Abstraction and Reasoning Corpus) solver project with GPU acceleration for Kaggle competition.

## GPU Optimization Status

**READ FIRST**: `GPU_PROJECT_SUMMARY.md` - Complete GPU optimization overview

### Key Achievement
- GPU acceleration is **COMPLETE and PRODUCTION READY** 🎉
- **10-35x speedup** vs CPU across all Kaggle GPU types
- Single-line integration: `auto_select_optimizer()`

### GPU Performance
| GPU Type | Single GPU | Multi-GPU | Recommendation |
|----------|------------|-----------|----------------|
| L4x4 🥇 | 9.35x | ~35x (4 GPUs) | Maximum performance |
| T4x2 🥈 | 9.69x | ~18x (2 GPUs) | Best availability ⭐ |
| P100 🥉 | 7.64x | N/A (1 GPU) | Fallback |

**All GPUs cost the same on Kaggle - choose based on availability!**

## Code Guidelines

### When Working with GPU Code

1. **GPU optimization is DONE** - Don't rewrite `gpu_optimizations.py` without good reason
2. **Use existing patterns** - See `INTEGRATION_GUIDE.md` for examples
3. **Test on Kaggle** - Always verify GPU code on actual Kaggle hardware
4. **Batch operations** - Optimal batch size is 200 grids
5. **Auto-detection** - Use `auto_select_optimizer()` for automatic GPU selection

### When Suggesting GPU Changes

**DON'T:**
- ❌ Suggest "simple" GPU acceleration without checking overhead analysis
- ❌ Propose per-element GPU transfers (use batch processing)
- ❌ Ignore JIT warmup (causes inconsistent performance)
- ❌ Hard-code GPU types (use auto-detection)
- ❌ Rewrite vectorized operations to use loops

**DO:**
- ✅ Check `GPU_PROJECT_SUMMARY.md` for proven patterns
- ✅ Use `KaggleGPUOptimizer` or `MultiGPUOptimizer` classes
- ✅ Maintain batch processing architecture
- ✅ Include JIT warmup in benchmarks
- ✅ Test on all GPU types (T4x2, P100, L4x4)

### Operation Complexity Guidelines

Based on extensive testing:

**❌ DON'T GPU Accelerate (Transfer overhead > Compute):**
- Simple ops: rot90, flip, transpose, shift, crop
- Scanning ops: fgpartition (even though it seems complex!)
- Operations < 10ms compute time per 100 grids
- Operations with < 10 iterations
- Operations requiring complex Python object conversion (frozensets, tuples)

**✅ DO GPU Accelerate (Compute >> Transfer):**
- Iterative ops: gravitate (42 iterations), flood_fill (100+ iterations)
- High arithmetic intensity: convolutions, matrix multiplications
- Operations > 50ms compute time per 100 grids
- Operations that naturally stay on GPU (numerical arrays)
- Operation pipelines (chain multiple ops on GPU without CPU transfer)

**Key Insight from Testing:**
- fgpartition: Expected 5-10x speedup, got 0.04x (23x slower!)
- Why: Per-grid GPU transfers (3000+ transfers), simple scan operations
- Lesson: Complexity alone doesn't guarantee GPU benefit - transfer overhead matters more!

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
2. **GPU_PROJECT_SUMMARY.md** - Overall status and results (START HERE)
3. **COMPLETE_GPU_COMPARISON.md** - Which GPU to use
4. **INTEGRATION_GUIDE.md** - How to integrate

### Technical Deep Dives
5. **GPU_OPTIMIZATION_SUCCESS.md** - Complete analysis
6. **MULTI_GPU_SUPPORT.md** - Multi-GPU details
7. **GPU_VECTORIZATION_UPDATE.md** - Vectorization patterns
8. **KAGGLE_GPU_OPTIMIZATION.md** - GPU specs
9. **GPU_TRANSFER_FIX.md** - Batch transfer details
10. **GPU_JIT_WARMUP.md** - JIT compilation handling
11. **GPU_FALLBACK_FIX.md** - Error handling patterns
12. **GPU_COMPARISON_P100_L4.md** - P100 vs L4 comparison
13. **GPU_BATCH_README.md** - Batch processing details

### Archived Documentation
- **archive/gpu_docs_superseded/** - Older docs replaced by comprehensive guides
  - QUICK_REF.md, SUMMARY.md, GPU_STRATEGY.md, GPU_OPTIMIZATION_APPLIED.md
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

✅ **GPU optimization**: Production ready, 10-35x speedup  
✅ **Multi-GPU support**: Working on T4x2 and L4x4  
✅ **Documentation**: Complete with 9 guides  
✅ **Testing**: Comprehensive test suites  
✅ **Integration**: One-line integration available  

**Next focus**: Integrating GPU acceleration into production solvers in `run_batt.py`

## Important Notes

1. **All Kaggle GPUs cost the same** - Choose based on availability, not cost
2. **T4x2 has best availability** - Recommended default choice
3. **L4x4 has best performance** - Try to get this allocation (35x speedup)
4. **Batch size 200 is optimal** - For single-GPU operations
5. **Multi-GPU auto-enabled** - When batch size >= 120 grids

## Quick Reference

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
