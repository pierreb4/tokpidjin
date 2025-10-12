# Transient Test Scripts Archive - October 12, 2025

This directory contains test scripts that were created during development and are no longer needed for production.

## Test Scripts Archived

### GPU Batch Operation Tests (Weeks 1-2)
- `test_gpu_batch.py` - Early GPU batch testing
- `test_gpu_batt.py` - GPU batt integration tests
- `test_gpu_batt_call.py` - Call pattern tests
- `test_gpu_batt_multi.py` - Multi-GPU batt tests
- `test_gpu_batt_multi_call.py` - Multi-GPU call tests
- `test_gpu_batt_v2.py` - Version 2 batt tests
- `test_gpu_batt_v2_call.py` - Version 2 call tests
- `test_batt_gpu_poc.py` - Proof of concept

### GPU DSL Tests
- `test_gpu_dsl_core.py` - Core DSL GPU tests
- `test_gpu_dsl_optimized.py` - Optimized DSL tests
- `test_gpu_env_basic.py` - Basic environment tests
- `test_gpu_fgpartition.py` - Specific operation tests
- `test_gpu_implementation.py` - Implementation validation

### Hybrid Strategy Tests (Week 3)
- `test_hybrid.py` - Hybrid CPU/GPU strategy tests
- `test_actual_scenario.py` - Real scenario testing

### Other Tests
- `test_kaggle_gpu_optimized.py` - Kaggle-specific tests (KEEP - still useful)
- `test_multi_gpu.py` - Multi-GPU validation (KEEP - still useful)
- `test_safe_default.py` - Safe default testing
- `test_generated_pattern.py` - Pattern generation tests

## Status

All archived tests were superseded by:
- Production code: `gpu_hybrid.py`, `gpu_solvers_hybrid.py`
- Benchmarks: `benchmark_hybrid_realistic.py`
- Validation: `test_hybrid.py` (kept for quick validation)

## Retention

These files are kept for historical reference but are not needed for:
- Production deployment
- Future development
- Kaggle submission
