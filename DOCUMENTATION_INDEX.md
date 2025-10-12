# TokPidjin Documentation Index

**Last Updated**: October 12, 2025

This document provides a complete overview of all documentation in the tokpidjin project.

---

## 🚀 Quick Start (START HERE)

### For GPU Acceleration
1. **[QUICK_START.md](QUICK_START.md)** - 25-minute introduction to GPU features
2. **[GPU_README.md](GPU_README.md)** - Quick start guide for GPU acceleration
3. **[GPU_WEEKS_1_2_3_COMPLETE.md](GPU_WEEKS_1_2_3_COMPLETE.md)** - Complete GPU project summary

### For Batt Optimization
1. **[BATT_OPTIMIZATION_COMPLETE.md](BATT_OPTIMIZATION_COMPLETE.md)** - Complete optimization guide (4.06x speedup)

### For General Use
1. **[README.md](README.md)** - Project overview and DSL introduction

---

## 📚 Core Documentation

### Project Overview
- **[README.md](README.md)** - Main project documentation with DSL examples
- **[arc_dsl_writeup.pdf](arc_dsl_writeup.pdf)** - Detailed DSL description (academic paper)

### GPU Acceleration
- **[GPU_DOCS_INDEX.md](GPU_DOCS_INDEX.md)** - Complete GPU documentation index
- **[GPU_README.md](GPU_README.md)** - GPU quick start guide
- **[QUICK_START.md](QUICK_START.md)** - 25-minute GPU onboarding
- **[GPU_WEEKS_1_2_3_COMPLETE.md](GPU_WEEKS_1_2_3_COMPLETE.md)** - Complete GPU project (Weeks 1-3)
- **[COMPLETE_GPU_COMPARISON.md](COMPLETE_GPU_COMPARISON.md)** - GPU hardware comparison guide
- **[INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md)** - How to integrate GPU code
- **[MULTI_GPU_SUPPORT.md](MULTI_GPU_SUPPORT.md)** - Multi-GPU usage guide
- **[FULL_ARC_ANALYSIS.md](FULL_ARC_ANALYSIS.md)** - Complete ARC problem analysis

### Performance Optimization
- **[BATT_OPTIMIZATION_COMPLETE.md](BATT_OPTIMIZATION_COMPLETE.md)** - Complete batt optimization (4.06x speedup)

### Bug Fixes
- **[BUS_ERROR_FIX.md](BUS_ERROR_FIX.md)** - Bus error resolution

---

## 🔧 Core Source Files

### Primary DSL Implementation
- **[dsl.py](dsl.py)** - Domain Specific Language (3725 lines, main implementation)
- **[arc_types.py](arc_types.py)** - Type definitions for ARC
- **[constants.py](constants.py)** - Constants (colors, directions, etc.)
- **[utils.py](utils.py)** - Utility functions (async timeout handling, etc.)

### GPU Implementations
- **[gpu_optimizations.py](gpu_optimizations.py)** - Production GPU code (530 lines)
- **[gpu_dsl.py](gpu_dsl.py)** - GPU-accelerated DSL operations
- **[gpu_hybrid.py](gpu_hybrid.py)** - Hybrid CPU/GPU strategy
- **[gpu_solvers_hybrid.py](gpu_solvers_hybrid.py)** - Hybrid solver implementations
- **[dsl_gpu.py](dsl_gpu.py)** - GPU DSL variants

### Solvers
- **[solvers.py](solvers.py)** - Main solver implementations
- **[solvers_pre.py](solvers_pre.py)** - Pre-optimized solvers
- **[solvers_xxx.py](solvers_xxx.py)** - Experimental solvers
- **[solvers_yyy.py](solvers_yyy.py)** - Additional solver variants

### Evaluation & Testing
- **[run_batt.py](run_batt.py)** - Batch solver evaluation (optimized, 4.06x speedup)
- **[run_test.py](run_test.py)** - DSL test runner
- **[main.py](main.py)** - Main execution entry point
- **[tests.py](tests.py)** - Test suite

### Code Generation & Analysis
- **[expand_solver.py](expand_solver.py)** - Solver expansion utilities
- **[inline_solver.py](inline_solver.py)** - Solver inlining
- **[regen.py](regen.py)** - Regeneration utilities
- **[optimize_solvers.py](optimize_solvers.py)** - Solver optimization

### Utilities
- **[call.py](call.py)** - Function calling utilities
- **[card.py](card.py)** - Card/catalog utilities
- **[differs.py](differs.py)** - Difference analysis
- **[grid.py](grid.py)** - Grid manipulation utilities
- **[helpers.py](helpers.py)** - Helper functions

---

## 🧪 Testing & Benchmarking

### Production Testing
- **[test_kaggle_gpu_optimized.py](test_kaggle_gpu_optimized.py)** - Kaggle GPU validation
- **[test_multi_gpu.py](test_multi_gpu.py)** - Multi-GPU testing
- **[tests.py](tests.py)** - Main test suite

### Benchmarking (Archived)
See `archive/benchmarking_scripts_2025_10_12/`:
- **benchmark_solvers.py** - Solver CPU benchmarking
- **benchmark_gpu_solvers.py** - GPU solver benchmarking
- **benchmark_hybrid.py** - Hybrid CPU/GPU benchmarking
- **benchmark_hybrid_realistic.py** - Realistic hybrid scenarios
- **profile_solvers.py** - Solver profiling
- **test_hybrid.py** - Hybrid implementation tests

---

## 📦 Archive Structure

### Current Archives

#### `archive/batt_optimization_2025_10_12/`
Complete history of batt optimization project (21.788s → 5.359s speedup):
- Phase-by-phase documentation (Phase 1-4B)
- Test scripts and temporary files
- Failure analyses and lessons learned
- See [archive/batt_optimization_2025_10_12/README.md](archive/batt_optimization_2025_10_12/README.md)

#### `archive/benchmarking_scripts_2025_10_12/`
One-time benchmarking and profiling scripts:
- benchmark_hybrid*.py
- profile_solvers.py
- test_hybrid.py

#### `archive/gpu_docs_superseded/`
Superseded GPU documentation (replaced by consolidated guides)

#### `archive/gpu_solver_analysis_2025_10_10/`
Intermediate GPU solver analysis (o_g bottleneck discovery)

#### `archive/gpu_weeks_1_2_3_2025_10_11/`
GPU project Weeks 1-3 detailed documentation

#### `archive/transient_tests_2025_10_12/`
One-time GPU test scripts and experiments

#### `archive/bus_error_fix_2025_10_12/`
Bus error diagnosis and fix documentation

---

## 📊 Documentation by Topic

### Performance Optimization
1. **Batt Optimization**: [BATT_OPTIMIZATION_COMPLETE.md](BATT_OPTIMIZATION_COMPLETE.md)
2. **GPU Acceleration**: [GPU_README.md](GPU_README.md)
3. **Multi-GPU**: [MULTI_GPU_SUPPORT.md](MULTI_GPU_SUPPORT.md)

### GPU Development
1. **Getting Started**: [QUICK_START.md](QUICK_START.md)
2. **Complete Guide**: [GPU_WEEKS_1_2_3_COMPLETE.md](GPU_WEEKS_1_2_3_COMPLETE.md)
3. **Hardware Selection**: [COMPLETE_GPU_COMPARISON.md](COMPLETE_GPU_COMPARISON.md)
4. **Integration**: [INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md)

### Problem Analysis
1. **ARC Overview**: [FULL_ARC_ANALYSIS.md](FULL_ARC_ANALYSIS.md)
2. **DSL Design**: [arc_dsl_writeup.pdf](arc_dsl_writeup.pdf)

### Troubleshooting
1. **Bus Errors**: [BUS_ERROR_FIX.md](BUS_ERROR_FIX.md)
2. **GPU Issues**: See [GPU_README.md](GPU_README.md) FAQ section

---

## 🗂️ File Organization

### By Purpose

**Core DSL**:
- dsl.py, arc_types.py, constants.py, utils.py

**GPU Acceleration**:
- gpu_optimizations.py, gpu_dsl.py, gpu_hybrid.py, gpu_solvers_hybrid.py

**Evaluation**:
- run_batt.py, run_test.py, main.py

**Solvers**:
- solvers.py, solvers_pre.py, solvers_*.py

**Testing**:
- tests.py, test_kaggle_gpu_optimized.py, test_multi_gpu.py

**Documentation**:
- README.md, *.md files in root

**Archives**:
- archive/ directory with dated subdirectories

---

## 🎯 Navigation Guide

### "I want to..."

#### Use GPU acceleration
→ Start: [QUICK_START.md](QUICK_START.md)  
→ Deep dive: [GPU_WEEKS_1_2_3_COMPLETE.md](GPU_WEEKS_1_2_3_COMPLETE.md)  
→ Integration: [INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md)

#### Understand batt optimization
→ [BATT_OPTIMIZATION_COMPLETE.md](BATT_OPTIMIZATION_COMPLETE.md)

#### Learn the DSL
→ Start: [README.md](README.md)  
→ Deep dive: [arc_dsl_writeup.pdf](arc_dsl_writeup.pdf)  
→ Code: [dsl.py](dsl.py)

#### Contribute to the project
→ Read: [README.md](README.md)  
→ Check: [GPU_README.md](GPU_README.md) for GPU features  
→ Review: [BATT_OPTIMIZATION_COMPLETE.md](BATT_OPTIMIZATION_COMPLETE.md) for optimization patterns

#### Debug issues
→ Bus errors: [BUS_ERROR_FIX.md](BUS_ERROR_FIX.md)  
→ GPU issues: [GPU_README.md](GPU_README.md)  
→ Performance: [BATT_OPTIMIZATION_COMPLETE.md](BATT_OPTIMIZATION_COMPLETE.md)

---

## 📈 Project History

### GPU Acceleration Project (Weeks 1-3)
- **Week 1**: Batch processing - 9.35x speedup
- **Week 2**: Multi-GPU support - 35x speedup (L4x4)
- **Week 3**: Hybrid strategy - 2.0-2.5x expected speedup
- **Status**: ✅ Complete (validated on 8,616 grids)

### Batt Optimization Project (Oct 7-12, 2025)
- **Phase 1**: Body hash deduplication - 1.29x speedup
- **Phase 2**: Parallel inline processing - 1.30x speedup
- **Phase 3**: Parallel validation - maintained performance, added profiling
- **Phase 4B**: Match-only diff calls - 4.06x overall speedup
- **Status**: ✅ Complete

### Bug Fixes
- **Bus Error Fix** (Oct 12, 2025): Resolved malloc_zone_malloc crash
- **Status**: ✅ Fixed

---

## 🔄 Documentation Maintenance

### When to Update This Index
- New documentation files added
- Major features implemented
- Archives created
- Project structure changes

### Archive Policy
Move to `archive/` when:
- Documentation is superseded by newer versions
- Feature is complete and documentation is reference-only
- Test scripts are one-time use only
- Detailed phase documentation after project completion

### Keep in Root
- Current project README
- Active feature documentation
- Integration guides
- Quick start guides
- Production code documentation

---

**Index Maintained By**: Documentation consolidation process  
**Last Consolidation**: October 12, 2025  
**Next Review**: As needed for major changes
