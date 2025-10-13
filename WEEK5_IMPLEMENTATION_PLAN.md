# Week 5 Implementation Plan - GPU Batch Operations

**Date**: October 13, 2025  
**Status**: 🚀 Starting Week 5  
**Goal**: Implement GPU batch processing for 4.8-9x speedup

---

## 🎯 Week 5 Overview

### Objective
Replace CPU sequential processing in `MegaBatchCoordinator` with GPU-accelerated batch operations.

### Target Performance
- **Current (CPU)**: 4.63ms per sample
- **Target (GPU)**: 0.77-0.96ms per sample
- **Speedup**: 4.8-6x minimum, 9x stretch goal

### Strategy
Focus on the highest-impact operations that appear most frequently in batt functions.

---

## 📊 Phase 1: Profiling & Analysis (Day 1)

### Goal
Identify which operations consume most time in batt execution.

### Tasks

#### 1.1 Profile Existing Batt Operations
```python
# Add profiling to mega_batch_batt.py
import cProfile
import pstats

def profile_batt_operations(batt_func, inputs):
    """Profile which DSL operations are called most"""
    pr = cProfile.Profile()
    pr.enable()
    
    for input in inputs[:100]:  # Profile first 100 samples
        batt_func(*input.to_args())
    
    pr.disable()
    stats = pstats.Stats(pr)
    stats.sort_stats('cumulative')
    stats.print_stats(50)
```

**Expected Top Operations** (based on GPU_SOLVER_STRATEGY.md):
1. `o_g` (object extraction) - 75-92% of solver time
2. `compose` / function application - High frequency
3. `mapply` / `apply` - Batch operations on samples
4. `colorfilter` / `colorcount` - Color operations
5. `rot90` / `flip` / `transpose` - Grid transformations

#### 1.2 Count Operation Frequency
```bash
# Analyze generated batt file
grep -o 't[0-9]* = [a-z_]*' batt_mega_test.py | \
    cut -d'=' -f2 | \
    sort | uniq -c | sort -rn | head -20
```

**Output format**:
```
  45 o_g
  32 compose
  28 mapply
  25 apply
  20 colorfilter
  ...
```

#### 1.3 Identify GPU Integration Points

**Target locations in code**:
1. `mega_batch_batt.py:180-210` - `process_batch()` method
2. `batt_gpu.py:33-93` - `batch_process_samples_gpu()` function
3. Generated batt operations (via wrapper functions)

---

## 🔧 Phase 2: GPU Operation Wrappers (Day 2)

### Goal
Create GPU-accelerated versions of top 5 operations.

### Architecture

```python
# gpu_dsl_operations.py (NEW FILE)

import cupy as cp
from gpu_optimizations import auto_select_optimizer

class GPUDSLOperations:
    """GPU-accelerated DSL operations for batch processing"""
    
    def __init__(self):
        self.gpu_opt = auto_select_optimizer()
        self.use_gpu = self.gpu_opt is not None
    
    def batch_compose(self, funcs_batch, args_batch):
        """
        GPU-accelerated batch composition.
        
        Args:
            funcs_batch: List of functions to compose
            args_batch: List of argument tuples
            
        Returns:
            List of composed results
        """
        if not self.use_gpu or len(args_batch) < 10:
            # CPU fallback for small batches
            return [f(*args) for f, args in zip(funcs_batch, args_batch)]
        
        # GPU batch processing
        # ... implementation ...
    
    def batch_o_g(self, grids_batch, rotations_batch):
        """
        GPU-accelerated batch object extraction.
        
        This is THE key operation (75-92% of solver time).
        Expected speedup: 3-8x
        """
        if not self.use_gpu:
            from dsl import o_g
            return [o_g(grid, rot) for grid, rot in zip(grids_batch, rotations_batch)]
        
        # GPU batch processing using existing gpu_optimizations.py
        # ... implementation ...
    
    def batch_mapply(self, func, grids_list):
        """GPU-accelerated mapply operation"""
        # ... implementation ...
    
    def batch_apply(self, func, samples_list):
        """GPU-accelerated apply operation"""
        # ... implementation ...
    
    def batch_colorfilter(self, objects_batch, colors_batch):
        """GPU-accelerated colorfilter"""
        # ... implementation ...
```

### Implementation Priority

**Tier 1 (Critical - Day 2)**: 
- `batch_o_g` - Biggest impact (75-92% of time)
- `batch_mapply` - High frequency, simple to parallelize

**Tier 2 (Important - Day 3)**:
- `batch_compose` - High frequency
- `batch_apply` - Sample extraction
- `batch_colorfilter` - Color operations

**Tier 3 (Nice to have - Day 4)**:
- Grid transformations (rot90, flip, transpose)
- Set operations (colorcount, difference_tuple)

---

## 🚀 Phase 3: Integrate GPU Operations (Day 3)

### Goal
Replace CPU sequential processing with GPU batch operations.

### 3.1 Modify MegaBatchCoordinator

**File**: `mega_batch_batt.py`

```python
from gpu_dsl_operations import GPUDSLOperations

class MegaBatchCoordinator:
    def __init__(self, batt_module_name='batt', batch_size=1000, use_gpu=True):
        self.batt_module_name = batt_module_name
        self.batch_size = batch_size
        self.batt = None
        
        # NEW: Initialize GPU operations
        self.gpu_ops = GPUDSLOperations() if use_gpu else None
        self.use_gpu = use_gpu and (self.gpu_ops.use_gpu if self.gpu_ops else False)
    
    def process_batch(self, batch, batch_idx):
        """Process batch with GPU acceleration"""
        
        if not self.use_gpu:
            # CPU fallback (Week 4 implementation)
            return self._process_batch_cpu(batch, batch_idx)
        
        # GPU batch processing (Week 5 NEW)
        return self._process_batch_gpu(batch, batch_idx)
    
    def _process_batch_gpu(self, batch, batch_idx):
        """
        GPU-accelerated batch processing.
        
        Strategy:
        1. Extract all inputs from batch
        2. Group operations by type
        3. Execute each operation type in GPU batch
        4. Reconstruct per-sample results
        """
        
        results = []
        
        # Pre-process: Extract common patterns
        # Example: All samples use same S (training samples)
        # Can process S operations once, reuse results
        
        for input_idx, batch_input in enumerate(batch):
            try:
                # Call batt with GPU operations injected
                o_result, s_result = self.batt(*batch_input.to_args())
                
                result = BatchResult(
                    batch_idx=input_idx,
                    o_result=o_result,
                    s_result=s_result
                )
                results.append(result)
            except Exception as e:
                logger.error(f"GPU batch {batch_idx}, input {input_idx} failed: {e}")
                # Fallback to CPU for this sample
                results.append(self._fallback_cpu_sample(batch_input))
        
        return results
```

### 3.2 Inject GPU Operations into Batt

Two approaches:

**Approach A: Monkey-patch DSL module** (Quick, Day 3)
```python
def load_batt_with_gpu(module_name, gpu_ops):
    """Load batt module and inject GPU operations"""
    import dsl
    
    # Replace DSL operations with GPU versions
    dsl.o_g = gpu_ops.batch_o_g_wrapper  # Wrapper that handles batching
    dsl.mapply = gpu_ops.batch_mapply_wrapper
    # ... other operations ...
    
    # Now import batt module
    batt_module = importlib.import_module(module_name)
    return batt_module.batt
```

**Approach B: Generate GPU-aware batt** (Better, Day 4)
```python
# card.py: Add --gpu flag
if args.gpu:
    print("from gpu_dsl_operations import gpu_ops", file=batt_file)
    print("o_g = gpu_ops.batch_o_g_wrapper", file=batt_file)
    # ... use GPU wrappers ...
```

**Decision**: Start with Approach A (faster), refine with B if needed.

---

## 🧪 Phase 4: Testing & Validation (Day 4)

### Goal
Validate correctness and measure actual speedup on Kaggle GPU.

### 4.1 Correctness Tests

```bash
# Generate test data
python card.py -c 20 -f batt_test_cpu.py
python card.py -c 20 -f batt_test_gpu.py --vectorized

# Test CPU baseline
python run_batt.py --mega-batch -c 20 -b batt_test_cpu --batch-size 100 > cpu_results.txt

# Test GPU version
python run_batt.py --mega-batch -c 20 -b batt_test_gpu --batch-size 100 --use-gpu > gpu_results.txt

# Compare results
diff cpu_results.txt gpu_results.txt
# Should be identical except timing!
```

### 4.2 Performance Benchmarks

**Small batch** (10 tasks, ~30 samples):
```bash
time python run_batt.py --mega-batch -c 10 -b batt_test --batch-size 50
```

**Medium batch** (50 tasks, ~150 samples):
```bash
time python run_batt.py --mega-batch -c 50 -b batt_test --batch-size 200
```

**Large batch** (200 tasks, ~600 samples):
```bash
time python run_batt.py --mega-batch -c 200 -b batt_test --batch-size 1000
```

### 4.3 Success Criteria

✅ **Correctness**: 100% match with CPU results  
✅ **Performance**: 4.8-6x speedup minimum  
🎯 **Stretch**: 9x speedup (best case)  
✅ **Fallback**: CPU fallback works when GPU unavailable  
✅ **Stability**: No crashes or memory errors

---

## 📝 Implementation Checklist

### Day 1: Profiling (4 hours)
- [ ] Add profiling to mega_batch_batt.py
- [ ] Profile batt_mega_test operations
- [ ] Count operation frequencies
- [ ] Identify top 5 operations
- [ ] Document baseline performance

### Day 2: GPU Wrappers - Tier 1 (8 hours)
- [ ] Create gpu_dsl_operations.py
- [ ] Implement batch_o_g (THE key operation)
- [ ] Implement batch_mapply
- [ ] Add CPU fallbacks
- [ ] Unit test each operation

### Day 3: Integration (8 hours)
- [ ] Modify MegaBatchCoordinator for GPU
- [ ] Implement _process_batch_gpu()
- [ ] Add GPU operation injection
- [ ] Test on small dataset (10 tasks)
- [ ] Fix any integration issues

### Day 4: Testing & Optimization (8 hours)
- [ ] Correctness validation (CPU vs GPU)
- [ ] Performance benchmarks (small/medium/large)
- [ ] Measure actual speedup
- [ ] Optimize batch sizes
- [ ] Document results

### Day 5: Polish & Documentation (4 hours)
- [ ] Add error handling
- [ ] Improve logging
- [ ] Update documentation
- [ ] Create usage guide
- [ ] Prepare for Week 6

---

## 🎯 Expected Outcomes

### Performance Targets

**Conservative** (4.8x speedup):
```
CPU baseline:  4.63ms/sample
GPU target:    0.96ms/sample
4000 samples:  18.5s → 3.8s
```

**Likely** (6x speedup):
```
CPU baseline:  4.63ms/sample
GPU target:    0.77ms/sample
4000 samples:  18.5s → 3.1s
```

**Optimistic** (9x speedup):
```
CPU baseline:  4.63ms/sample
GPU target:    0.51ms/sample
4000 samples:  18.5s → 2.0s
```

### What Could Go Wrong

**Risk 1**: GPU memory limits
- Mitigation: Adaptive batch sizing based on available VRAM

**Risk 2**: Some operations not GPU-friendly
- Mitigation: CPU fallback per operation

**Risk 3**: Transfer overhead dominates
- Mitigation: Keep data on GPU between operations

**Risk 4**: Correctness issues
- Mitigation: Extensive testing, compare with CPU

---

## 📚 Resources

**Existing GPU Code**:
- `gpu_optimizations.py` - Batch grid operations (validated, 10-35x speedup)
- `GPU_SOLVER_STRATEGY.md` - o_g bottleneck analysis
- `GPU_PROJECT_SUMMARY.md` - Batch processing patterns

**Key Insights**:
- Batch size 200 optimal for single GPU
- Multi-GPU for batches >120
- JIT warmup critical (800ms first run)
- Transfer overhead amortized over batch

**Kaggle GPU Specs**:
- L4x4: 4 GPUs, 22.3GB VRAM each (best performance)
- T4x2: 2 GPUs, 15GB VRAM each (best availability)
- P100: 1 GPU, 16GB VRAM (fallback)

---

## 🚀 Let's Begin!

**Starting Point**: Week 4 complete, CPU baseline working  
**Next Step**: Day 1 profiling to find bottlenecks  
**End Goal**: 4.8-9x speedup with GPU batch processing

Ready to start Week 5 Day 1? 🎯
