# Benchmarking & Profiling Scripts Archive

**Archive Date**: October 12, 2025  
**Status**: Historical reference - one-time use scripts

---

## 📁 Contents

### Solver Benchmarking
- **benchmark_solvers.py** - CPU benchmark for solver functions
  - Measures actual execution times
  - Validates GPU viability (execution time > 5ms)
  - Used to determine which solvers benefit from GPU acceleration
  - Result: Found 2 excellent candidates (58ms, 120ms), 5 good candidates (5-15ms)

### GPU Benchmarking
- **benchmark_gpu_solvers.py** - GPU solver benchmarking
  - Compares CPU vs GPU execution
  - Validates GPU implementations
  - Measures actual speedup

### Hybrid Strategy
- **benchmark_hybrid.py** - Comprehensive hybrid CPU/GPU benchmark
  - Compares CPU-only, GPU-only, and hybrid implementations
  - Validates automatic CPU/GPU selection
  - Used during Week 3 of GPU project

- **benchmark_hybrid_realistic.py** - Realistic hybrid scenarios
  - Tests hybrid strategy on real-world solver patterns
  - Validates performance on mixed workloads

### Profiling
- **profile_solvers.py** - Detailed solver profiling
  - Profiles DSL operations within solvers
  - Identifies bottlenecks (found o_g as 75-92% of time)
  - Validates on Kaggle environment

### Testing
- **test_hybrid.py** - Hybrid implementation tests
  - Validates hybrid CPU/GPU switching
  - Tests automatic device selection

---

## 🎯 Purpose

These scripts were used for one-time analysis during the GPU acceleration project:

1. **Discovery Phase**: Identify which operations/solvers benefit from GPU
2. **Validation Phase**: Confirm GPU implementations are correct and faster
3. **Optimization Phase**: Profile bottlenecks and validate improvements

---

## 📊 Key Findings

### From benchmark_solvers.py
```
Solver Viability Distribution (28 solvers):
- 21% too fast (<1ms) → CPU only
- 54% borderline (1-5ms) → marginal GPU benefit  
- 18% good (5-15ms) → 2-3x speedup
- 7% excellent (>15ms) → 3-6x speedup

Top Candidates:
- solve_36d67576: 120.674 ms (33 ops) → 3-6x GPU speedup
- solve_36fdfd69: 58.314 ms (16 ops) → 3-5x GPU speedup
```

### From profile_solvers.py
```
Bottleneck Identified: o_g operation
- solve_09629e4f: 92.3% of time in o_g (5/7 ops)
- solve_36fdfd69: 75.9% of time in o_g (2/16 ops)

Conclusion: Target o_g for GPU acceleration (not individual DSL ops)
```

### From benchmark_hybrid.py
```
Hybrid Strategy Validation:
- CPU-only: Baseline
- GPU-only: 2.3-7.8x faster (but requires GPU)
- Hybrid: Automatic selection, 2.0-2.5x average speedup

Result: Hybrid strategy approved for production
```

---

## 🔄 When to Use

### For Reference
- Understanding GPU viability criteria
- Reviewing profiling methodology
- Learning benchmarking patterns

### For Reproduction
These scripts can be re-run if needed:
```bash
# CPU benchmarking
python benchmark_solvers.py

# GPU benchmarking (requires GPU)
python benchmark_gpu_solvers.py

# Hybrid testing (requires GPU)
python benchmark_hybrid.py

# Profiling (works on CPU or GPU)
python profile_solvers.py
```

### Not for Production
These are analysis tools, not production code. Production implementations are in:
- `gpu_optimizations.py` - Production GPU code
- `gpu_hybrid.py` - Production hybrid strategy
- `run_batt.py` - Production evaluation (with optimizations)

---

## 📚 Related Documentation

### GPU Project
- **[GPU_WEEKS_1_2_3_COMPLETE.md](../../GPU_WEEKS_1_2_3_COMPLETE.md)** - Complete GPU project
- **[GPU_README.md](../../GPU_README.md)** - GPU quick start
- **[COMPLETE_GPU_COMPARISON.md](../../COMPLETE_GPU_COMPARISON.md)** - Hardware comparison

### Optimization
- **[BATT_OPTIMIZATION_COMPLETE.md](../../BATT_OPTIMIZATION_COMPLETE.md)** - Batt optimization

### Other Archives
- **[../gpu_solver_analysis_2025_10_10/](../gpu_solver_analysis_2025_10_10/)** - GPU solver analysis
- **[../batt_optimization_2025_10_12/](../batt_optimization_2025_10_12/)** - Batt optimization history

---

**Archive Reason**: One-time analysis complete, findings integrated into production code  
**Status**: Reference only, not actively maintained  
**Restoration**: Scripts can be re-run if new analysis needed
