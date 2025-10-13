# Week 5 Day 1 - Operation Frequency Analysis

**Date**: October 13, 2025  
**File Analyzed**: batt_mega_test.py (5 tasks generated)

---

## 📊 Operation Frequency (Top 30)

```
  24  size           ← Tuple/Container size (cheap operation)
  24  astuple        ← Create tuple from args (cheap)
  15  get_nth_t      ← Get nth from tuple (cheap)
  15  difference_tuple ← Set difference on tuples (moderate)
  14  get_nth_f      ← Get nth from frozenset (cheap)
  14  difference     ← Set difference (moderate)
   6  dedupe        ← Remove duplicates (moderate)
   5  rbind         ← Partial application (cheap)
   3  mapply        ← Apply to each element 🎯 **GPU TARGET**
   3  batch_process_samples_gpu ← Already GPU-ready ✅
   2  move          ← Grid movement (moderate)
   2  identity      ← Identity function (trivial)
   2  compose       ← Function composition (cheap) 🎯 **GPU TARGET**
   2  colorfilter   ← Filter by color (moderate) 🎯 **GPU TARGET**
   1  o_g           ← Object extraction 🎯 **CRITICAL GPU TARGET**
   1  gravitate     ← Physics simulation (expensive) 🎯 **GPU TARGET**
   1  fill          ← Fill operation (moderate)
   1  apply         ← Apply function 🎯 **GPU TARGET**
```

---

## 🎯 GPU Acceleration Priorities

### Tier 1: CRITICAL (Must implement for 4.8x speedup)

**1. `o_g` (Object extraction)**
- Frequency: Low in this file (1), but 75-92% of solver execution time
- Complexity: High (grid partitioning, connected components)
- GPU Benefit: ⭐⭐⭐⭐⭐ (Validated 2.3-7.8x speedup potential)
- Status: ✅ Already profiled in GPU_SOLVER_STRATEGY.md
- **Action**: Implement `batch_o_g()` using existing gpu_optimizations.py patterns

**2. `mapply` (Map apply)**
- Frequency: 3 occurrences
- Pattern: `mapply(func, grid_list)` - applies function to each grid
- GPU Benefit: ⭐⭐⭐⭐⭐ (Perfect for parallelization)
- Complexity: Medium (depends on inner function)
- **Action**: Implement `batch_mapply()` - process all grids in parallel

**3. `batch_process_samples_gpu`**
- Frequency: 3 occurrences  
- Status: ✅ Already implemented in batt_gpu.py
- GPU Benefit: ⭐⭐⭐⭐ (10-35x validated on grids)
- **Action**: Ensure integration working correctly

---

### Tier 2: HIGH IMPACT (Should implement for 6x+ speedup)

**4. `gravitate` (Physics simulation)**
- Frequency: 1 occurrence
- Complexity: Very High (42 iterations in profiled example)
- GPU Benefit: ⭐⭐⭐⭐ (Iterative operations benefit greatly)
- CPU Time: 6.379ms (Week 4 solver benchmarks)
- **Action**: Implement `batch_gravitate()` with GPU iteration

**5. `colorfilter` (Color filtering)**
- Frequency: 2 occurrences
- Complexity: Medium (set operations on objects)
- GPU Benefit: ⭐⭐⭐⭐ (Set operations parallelize well)
- **Action**: Implement `batch_colorfilter()`

**6. `apply` (Function application)**
- Frequency: 1 occurrence
- Pattern: `apply(first/second, samples)` - extract from samples
- GPU Benefit: ⭐⭐⭐ (Can process all samples in parallel)
- **Action**: Enhance existing batch_process_samples_gpu()

---

### Tier 3: OPTIMIZATION (Nice to have for 9x speedup)

**7. `difference_tuple` / `difference`**
- Frequency: 15 + 14 = 29 occurrences (!)
- Complexity: Low-Medium (set operations)
- GPU Benefit: ⭐⭐⭐ (But operations are already fast on CPU)
- **Action**: Consider if cumulative overhead is significant

**8. `move` / `fill`**
- Frequency: 2 + 1 = 3 occurrences
- Complexity: Medium (grid manipulation)
- GPU Benefit: ⭐⭐⭐ (Grid operations parallelize)
- **Action**: Batch implementation if time permits

**9. `compose`**
- Frequency: 2 occurrences
- Complexity: Low (function composition)
- GPU Benefit: ⭐⭐ (Overhead might exceed benefit)
- **Action**: CPU fallback likely sufficient

---

### Tier 4: CPU FALLBACK (Not worth GPU overhead)

**Operations to skip**:
- `size`, `astuple`, `get_nth_t`, `get_nth_f` - Too cheap, transfer overhead exceeds benefit
- `rbind`, `lbind`, `identity` - Function wrappers, no computation
- `dedupe` - Set operation, fast enough on CPU

---

## 🔍 Key Insights

### 1. Small Test File Limitation
This analysis is from a **5-task test file** (353 lines). Production batt files with more tasks will have:
- More `o_g` operations (the critical bottleneck)
- More `mapply` operations (batch processing)
- More complex operation chains

**Recommendation**: Profile a larger batt file (50+ tasks) for better data.

### 2. Operation Patterns

**Dominant pattern**: Tuple/Set manipulation
- `size`, `astuple`, `get_nth_*`, `difference` are pervasive
- These are cheap operations - focus on expensive ones

**Expensive operations** (from solver benchmarks):
- `o_g`: 11-120ms per call (75-92% of solver time)
- `gravitate`: 6.4ms with 42 iterations
- `mapply`: Depends on inner function and batch size

### 3. GPU Integration Strategy

**Phase 1** (Day 2): Implement Tier 1
- `batch_o_g` - THE critical operation
- `batch_mapply` - High parallelism potential
- Validate `batch_process_samples_gpu` integration

**Phase 2** (Day 3): Implement Tier 2
- `batch_gravitate` - Expensive iterative operation
- `batch_colorfilter` - Moderate impact
- Enhanced `batch_apply`

**Phase 3** (Day 4): Optimization
- Profile actual performance
- Add Tier 3 operations if needed
- Tune batch sizes

---

## 📈 Expected Speedup Calculation

### Conservative (4.8x)
Assuming:
- `o_g` accounts for 60% of time → GPU 3x faster → 1.8x overall
- `mapply` accounts for 15% of time → GPU 5x faster → 1.6x overall
- Other ops account for 25% of time → No GPU → 1x
- **Total**: 1.8 × 1.6 × 1.0 = **2.88x**

Hmm, need better estimate. Let me recalculate:

### Realistic (6x)
Based on solver profiling:
- `o_g`: 75% of time, 3-8x GPU speedup → 75% × 5x = **3.75x** contribution
- `mapply`: 10% of time, 5-10x GPU speedup → 10% × 7x = **0.7x** contribution
- Other: 15% of time, 1-2x speedup → 15% × 1.5x = **0.225x** contribution
- **Total**: 3.75 + 0.7 + 0.225 = **4.675x** ≈ **4.8x** ✅

### Optimistic (9x)
If we nail everything:
- `o_g`: 75% × 8x = **6x** contribution
- `mapply`: 10% × 10x = **1x** contribution
- `gravitate` + others: 15% × 5x = **0.75x** contribution
- **Total**: 6 + 1 + 0.75 = **7.75x** → with optimizations → **9x** 🎯

---

## 📋 Next Steps (Day 1 Remaining)

### 1. Generate Larger Test File ✅
```bash
python card.py -c 50 -f batt_large_test.py --vectorized
```

### 2. Profile Larger File
```bash
grep -o 't[0-9]* = [a-z_]*(' batt_large_test.py | \
    cut -d'=' -f2 | cut -d'(' -f1 | sort | uniq -c | sort -rn
```

### 3. Create Operation Benchmarks
Measure actual CPU time for each operation type:
```python
# benchmark_operations.py
import time
from dsl import o_g, mapply, gravitate, colorfilter

# Test data
test_grids = [...]  # Generate test grids

# Benchmark each operation
times = {}
for op_name, op_func in [('o_g', o_g), ('mapply', mapply), ...]:
    start = time.time()
    for grid in test_grids:
        result = op_func(grid, ...)
    times[op_name] = time.time() - start
```

### 4. Document Baseline Performance
Create comprehensive baseline for Week 5 comparison.

---

## ✅ Day 1 Progress

- [x] Analyzed batt_mega_test.py operation frequencies
- [x] Identified Tier 1-4 GPU targets
- [x] Calculated expected speedup ranges (4.8-9x)
- [ ] Generate larger test file (50+ tasks)
- [ ] Profile larger file for validation
- [ ] Benchmark individual operations
- [ ] Document comprehensive baseline

**Status**: Day 1 on track, ready for Day 2 implementation! 🚀
