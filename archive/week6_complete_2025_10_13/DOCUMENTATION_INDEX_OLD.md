# Documentation Index - tokpidjin Project# TokPidjin Documentation Index



**Last Updated**: October 13, 2025  **Last Updated**: October 12, 2025

**Status**: Active - Week 6 Starting

This document provides a complete overview of all documentation in the tokpidjin project.

## 🎯 Quick Navigation

---

**New to the project?** Start with `README.md`

## 🚀 Quick Start (START HERE)

**Working on optimization?** See `DUAL_ENVIRONMENT_STRATEGY.md` ⭐

### For GPU Acceleration

**Need Week 5 summary?** See `WEEK5_GPU_SUCCESS.md`1. **[QUICK_START.md](QUICK_START.md)** - 25-minute introduction to GPU features

2. **[GPU_README.md](GPU_README.md)** - Quick start guide for GPU acceleration

**Looking for old docs?** Check `archive/week5_complete_2025_10_13/`3. **[GPU_WEEKS_1_2_3_COMPLETE.md](GPU_WEEKS_1_2_3_COMPLETE.md)** - Complete GPU project summary



---### For Batt Optimization

1. **[BATT_OPTIMIZATION_COMPLETE.md](BATT_OPTIMIZATION_COMPLETE.md)** - Complete optimization guide (4.06x speedup)

## 📚 Essential Documents (Read These First)

### For General Use

### Current Strategy1. **[README.md](README.md)** - Project overview and DSL introduction

1. **`DUAL_ENVIRONMENT_STRATEGY.md`** ⭐⭐⭐

   - Week 6+ optimization strategy for CPU AND GPU environments---

   - Shared optimization priorities (benefit both)

   - Expected performance targets (2-3x speedup)## 📚 Core Documentation



2. **`WEEK5_GPU_SUCCESS.md`** ⭐⭐### Project Overview

   - Week 5 GPU acceleration results (3.3x speedup)- **[README.md](README.md)** - Main project documentation with DSL examples

   - Key discovery: Batt is only 9% of problem- **[arc_dsl_writeup.pdf](arc_dsl_writeup.pdf)** - Detailed DSL description (academic paper)

   - Real bottlenecks identified

### GPU Acceleration

3. **`WEEK5_COMPLETE_STORY.md`** ⭐- **[GPU_DOCS_INDEX.md](GPU_DOCS_INDEX.md)** - Complete GPU documentation index

   - Full Week 5 journey with mistakes and breakthroughs- **[GPU_README.md](GPU_README.md)** - GPU quick start guide

   - Timeline and lessons learned- **[QUICK_START.md](QUICK_START.md)** - 25-minute GPU onboarding

- **[GPU_WEEKS_1_2_3_COMPLETE.md](GPU_WEEKS_1_2_3_COMPLETE.md)** - Complete GPU project (Weeks 1-3)

### Project Basics- **[COMPLETE_GPU_COMPARISON.md](COMPLETE_GPU_COMPARISON.md)** - GPU hardware comparison guide

4. **`README.md`** - Project overview and setup- **[INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md)** - How to integrate GPU code

5. **`.github/copilot-instructions.md`** - Development guidelines and GPU status- **[MULTI_GPU_SUPPORT.md](MULTI_GPU_SUPPORT.md)** - Multi-GPU usage guide

- **[FULL_ARC_ANALYSIS.md](FULL_ARC_ANALYSIS.md)** - Complete ARC problem analysis

---

### Performance Optimization

## 🖥️ GPU Documentation- **[BATT_OPTIMIZATION_COMPLETE.md](BATT_OPTIMIZATION_COMPLETE.md)** - Complete batt optimization (4.06x speedup)



### GPU System### Bug Fixes

- **`GPU_README.md`** - GPU architecture overview- **[BUS_ERROR_FIX.md](BUS_ERROR_FIX.md)** - Bus error resolution

- **`GPU_DOCS_INDEX.md`** - Complete GPU docs navigation

- **`COMPLETE_GPU_COMPARISON.md`** - GPU types (T4x2, P100, L4x4)---

- **`MULTI_GPU_SUPPORT.md`** - Multi-GPU usage

- **`GPU_INTEGRATION_QUICK_REFERENCE.md`** - API quick reference## 🔧 Core Source Files



### GPU Implementation Files### Primary DSL Implementation

- `batt_gpu.py` - GPU initialization and batch processing- **[dsl.py](dsl.py)** - Domain Specific Language (3725 lines, main implementation)

- `gpu_optimizations.py` - Core GPU acceleration (production ready)- **[arc_types.py](arc_types.py)** - Type definitions for ARC

- `gpu_dsl_operations.py` - GPU DSL operations- **[constants.py](constants.py)** - Constants (colors, directions, etc.)

- `gpu_env.py` - GPU environment config- **[utils.py](utils.py)** - Utility functions (async timeout handling, etc.)



---### GPU Implementations

- **[gpu_optimizations.py](gpu_optimizations.py)** - Production GPU code (530 lines)

## 🏗️ Core Files- **[gpu_dsl.py](gpu_dsl.py)** - GPU-accelerated DSL operations

- **[gpu_hybrid.py](gpu_hybrid.py)** - Hybrid CPU/GPU strategy

### Execution- **[gpu_solvers_hybrid.py](gpu_solvers_hybrid.py)** - Hybrid solver implementations

- **`run_batt.py`** - Main execution (timeout: 10s)- **[dsl_gpu.py](dsl_gpu.py)** - GPU DSL variants

- **`run_card.sh`** - Orchestration (-g GPU, -m CPU, -T timing)

- **`batt.py`** - Generated solver (2,247 lines, 32 solvers)### Solvers

- **`card.py`** - Batt generator (--vectorized for GPU)- **[solvers.py](solvers.py)** - Main solver implementations

- **[solvers_pre.py](solvers_pre.py)** - Pre-optimized solvers

### DSL- **[solvers_xxx.py](solvers_xxx.py)** - Experimental solvers

- `dsl.py` - Domain Specific Language (3,725 lines)- **[solvers_yyy.py](solvers_yyy.py)** - Additional solver variants

- `arc_types.py` - Type definitions

- `solvers.py` - Solver implementations### Evaluation & Testing

- `pile.py` - Helper functions- **[run_batt.py](run_batt.py)** - Batch solver evaluation (optimized, 4.06x speedup)

- **[run_test.py](run_test.py)** - DSL test runner

### Tools- **[main.py](main.py)** - Main execution entry point

- `utils.py` - Utilities (async, AST operations)- **[tests.py](tests.py)** - Test suite

- `batt_validation.py` - Validation functions

- `tests.py` - Test suite### Code Generation & Analysis

- **[expand_solver.py](expand_solver.py)** - Solver expansion utilities

---- **[inline_solver.py](inline_solver.py)** - Solver inlining

- **[regen.py](regen.py)** - Regeneration utilities

## 📦 Archives- **[optimize_solvers.py](optimize_solvers.py)** - Solver optimization



### **`archive/week5_complete_2025_10_13/`** ⭐### Utilities

All Week 5 documents, deployment guides, test scripts, and implementation strategies.- **[call.py](call.py)** - Function calling utilities

See `archive/week5_complete_2025_10_13/README.md` for complete index.- **[card.py](card.py)** - Card/catalog utilities

- **[differs.py](differs.py)** - Difference analysis

### Older Archives- **[grid.py](grid.py)** - Grid manipulation utilities

- `archive/gpu_docs_consolidated_2025_10_12/` - Earlier GPU docs- **[helpers.py](helpers.py)** - Helper functions

- `archive/gpu_solver_analysis_2025_10_10/` - Solver analysis

- `archive/gpu_weeks_1_2_3_2025_10_11/` - Weeks 1-3 work---

- `archive/gpu_docs_superseded/` - Very old docs

## 🧪 Testing & Benchmarking

---

### Production Testing

## 📊 Performance Status- **[test_kaggle_gpu_optimized.py](test_kaggle_gpu_optimized.py)** - Kaggle GPU validation

- **[test_multi_gpu.py](test_multi_gpu.py)** - Multi-GPU testing

### Current (Week 5 Complete)- **[tests.py](tests.py)** - Main test suite

```

Component           GPU      CPU (est)   Bottleneck?### Benchmarking (Archived)

────────────────────────────────────────────────────See `archive/benchmarking_scripts_2025_10_12/`:

Variable Inlining   2.989s   2.989s      69% ← Week 6- **benchmark_solvers.py** - Solver CPU benchmarking

Solver Validation   2.770s   2.770s      64% ← Week 6- **benchmark_gpu_solvers.py** - GPU solver benchmarking

Inline Batch        0.976s   0.976s      22% ← Week 6- **benchmark_hybrid.py** - Hybrid CPU/GPU benchmarking

Batt Execution      0.379s   ~1.8s       9%  ← Week 5 ✓- **benchmark_hybrid_realistic.py** - Realistic hybrid scenarios

────────────────────────────────────────────────────- **profile_solvers.py** - Solver profiling

TOTAL               4.35s    ~8.5s- **test_hybrid.py** - Hybrid implementation tests

```

---

### Week 6 Targets

```## 📦 Archive Structure

Variable Inlining: 2.989s → 1.0s (3x speedup, SHARED benefit)

Solver Validation: 2.770s → 0.7s (4x speedup, SHARED benefit)### Current Archives

Inline Batch:      0.976s → 0.5s (2x speedup, SHARED benefit)

Batt CPU Fallback: ~1.8s → 0.6s (3x speedup, CPU-specific)#### `archive/batt_optimization_2025_10_12/`

Complete history of batt optimization project (21.788s → 5.359s speedup):

Result: GPU 4.35s → 2.5s, CPU 8.5s → 2.8s (both 2-3x faster!)- Phase-by-phase documentation (Phase 1-4B)

```- Test scripts and temporary files

- Failure analyses and lessons learned

---- See [archive/batt_optimization_2025_10_12/README.md](archive/batt_optimization_2025_10_12/README.md)



## 🚀 Quick Commands#### `archive/benchmarking_scripts_2025_10_12/`

One-time benchmarking and profiling scripts:

```bash- benchmark_hybrid*.py

# GPU mode with timing- profile_solvers.py

bash run_card.sh -c 5 -T -g- test_hybrid.py



# CPU mode with timing  #### `archive/gpu_docs_superseded/`

bash run_card.sh -c 5 -T -mSuperseded GPU documentation (replaced by consolidated guides)



# Auto-detect (default)#### `archive/gpu_solver_analysis_2025_10_10/`

bash run_card.sh -c 5 -TIntermediate GPU solver analysis (o_g bottleneck discovery)



# Baseline CPU performance#### `archive/gpu_weeks_1_2_3_2025_10_11/`

bash run_card.sh -c 10 -T -mGPU project Weeks 1-3 detailed documentation

```

#### `archive/transient_tests_2025_10_12/`

---One-time GPU test scripts and experiments



## 🎯 Week 6 Focus#### `archive/bus_error_fix_2025_10_12/`

Bus error diagnosis and fix documentation

1. ✅ Documentation consolidated and archived

2. ⏳ **Baseline CPU-only performance** (next step)---

3. ⏳ Optimize variable inlining (benefits BOTH CPU and GPU)

4. ⏳ Optimize solver validation (benefits BOTH CPU and GPU)## 📊 Documentation by Topic

5. ⏳ Optimize inline batch (benefits BOTH CPU and GPU)

6. ⏳ Optimize CPU fallback paths (CPU-specific)### Performance Optimization

1. **Batt Optimization**: [BATT_OPTIMIZATION_COMPLETE.md](BATT_OPTIMIZATION_COMPLETE.md)

**Key Strategy**: Optimize the 91% that's pure Python (helps everywhere!), not just the 9% that needs GPU.2. **GPU Acceleration**: [GPU_README.md](GPU_README.md)

3. **Multi-GPU**: [MULTI_GPU_SUPPORT.md](MULTI_GPU_SUPPORT.md)

---

### GPU Development

## 📖 How to Find Things1. **Getting Started**: [QUICK_START.md](QUICK_START.md)

2. **Complete Guide**: [GPU_WEEKS_1_2_3_COMPLETE.md](GPU_WEEKS_1_2_3_COMPLETE.md)

**Week 5 work?** → `archive/week5_complete_2025_10_13/`  3. **Hardware Selection**: [COMPLETE_GPU_COMPARISON.md](COMPLETE_GPU_COMPARISON.md)

**GPU info?** → `GPU_*.md` files  4. **Integration**: [INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md)

**Strategy?** → `DUAL_ENVIRONMENT_STRATEGY.md`  

**Performance?** → `WEEK5_GPU_SUCCESS.md`  ### Problem Analysis

**Old docs?** → `archive/` subdirectories  1. **ARC Overview**: [FULL_ARC_ANALYSIS.md](FULL_ARC_ANALYSIS.md)

**Code?** → `.py` files in root  2. **DSL Design**: [arc_dsl_writeup.pdf](arc_dsl_writeup.pdf)

**Scripts?** → `.sh` files in root  

### Troubleshooting

---1. **Bus Errors**: [BUS_ERROR_FIX.md](BUS_ERROR_FIX.md)

2. **GPU Issues**: See [GPU_README.md](GPU_README.md) FAQ section

**Last Update**: October 13, 2025 - Week 5 complete, Week 6 starting with dual-environment focus

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
