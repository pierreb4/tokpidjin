# Archived GPU Implementations - October 13, 2025

## Why Archived

These files represent **outdated GPU implementation attempts** that were **superseded** by the current Week 5 approach.

**Problem with old implementations:**
- Used `batch_process_samples_gpu()` from `batt_gpu.py` 
- Different GPU system that doesn't integrate with current DSL operations
- Generated batt files that call old GPU functions instead of new GPU operations
- Caused confusion when benchmarking (no speedup because wrong code was being called)

**Current working approach (Week 5):**
- `gpu_dsl_operations.py` - Batch GPU operations (batch_o_g, batch_mapply, batch_apply)
- `mega_batch_batt.py` - Coordinator that uses GPUDSLOperations
- `gpu_optimizations.py` - Core GPU optimizer (MultiGPUOptimizer)
- Integrates directly with DSL functions via vectorized operations

## Archived Files

### Old GPU Batch Processing
- `batt_gpu.py` - Old GPU batch processing system
- `batt_gpu_large.py` - Large batch GPU processing
- `batt_gpu_large_call.py` - Call script for large batches

### Old GPU DSL Attempts
- `gpu_dsl.py` - Early GPU DSL implementation
- `dsl_gpu.py` - Alternative GPU DSL approach
- `safe_dsl.py` - Safe DSL wrapper attempt
- `gpu_env.py` - GPU environment setup
- `gpu_hybrid.py` - Hybrid GPU/CPU approach
- `gpu_solvers_hybrid.py` - Hybrid solver approach
- `gpu_solvers_pre.py` - Pre-processed solvers

### Old Test Files
- `test_batt_standard.py` - Standard batt tests
- `test_batt_standard_call.py` - Call script
- `test_batt_vectorized.py` - Vectorized tests
- `test_batt_vectorized_call.py` - Call script
- `test_refactored.py` - Refactored tests
- `test_refactored_call.py` - Call script

## Timeline

- **Weeks 1-3**: GPU optimization work on `gpu_optimizations.py` (batch operations)
  - Result: 10-35x speedup for batch grid processing ✅
  - Status: PRODUCTION READY

- **Week 4**: Batt optimization and mega-batch coordinator
  - Result: 3.78x speedup locally ✅
  - Status: VALIDATED

- **Week 5 Day 1-2**: Created GPU DSL operations (batch_o_g, batch_mapply, batch_apply)
  - Integrated with mega_batch_batt.py
  - Fixed to actually use GPU optimizer (not CPU DSL functions)
  - Status: VALIDATED LOCALLY ✅

- **Week 5 Day 3**: Kaggle deployment discovered issue
  - Problem: `batt_mega_test.py` uses OLD `batch_process_samples_gpu()` system
  - Result: No GPU speedup (0.96x) because wrong code was being called
  - Solution: Archive old GPU implementations to prevent confusion

## What NOT to Use

❌ **Don't use** `batch_process_samples_gpu()` from `batt_gpu.py`
❌ **Don't generate** batt files that call old GPU functions
❌ **Don't reference** these archived implementations in new code

## What TO Use

✅ **Use** `gpu_dsl_operations.py` - Current GPU operations
✅ **Use** `mega_batch_batt.py` - Current batch coordinator
✅ **Use** `gpu_optimizations.py` - Core GPU optimizer
✅ **Generate** batt files that use standard DSL (mapply, o_g, apply)
✅ **Let** GPUDSLOperations intercept and batch these operations

## Key Insight

The current approach works by:
1. Batt code calls normal DSL functions (mapply, o_g, apply)
2. GPUDSLOperations intercepts these calls
3. Batches them together
4. Processes batch on GPU using gpu_optimizations.py
5. Returns results

This is **much cleaner** than having batt code explicitly call GPU functions!

## If You Need These Files

These files are kept for historical reference. If you need to understand the evolution of the GPU implementation, they're here. But **do not use them in new code**.

## Related Documentation

See current GPU documentation:
- `GPU_DOCS_INDEX.md` - Complete documentation index
- `GPU_SOLVER_STRATEGY.md` - Current strategy (solver-level GPU acceleration)
- `WEEK5_IMPLEMENTATION_PLAN.md` - Week 5 plan
- `WEEK5_DAY3_GPU_DIAGNOSIS.md` - The bug that led to archiving these files

---

**Archived**: October 13, 2025  
**Reason**: Superseded by Week 5 GPU operations approach  
**Status**: Historical reference only - DO NOT USE
