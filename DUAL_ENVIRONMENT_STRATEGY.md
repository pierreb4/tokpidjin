# Dual Environment Optimization Strategy

**Date**: October 13, 2025  
**Goal**: Optimize for BOTH CPU and GPU environments  
**Context**: Code runs in both environments, want best performance everywhere

## Current State

### Week 5 Achievement: GPU Works! ✅
- **GPU Performance**: 127ms average per batt() call
- **GPU Speedup**: ~3.3x faster than estimated baseline
- **GPU Component**: Only 9% of total time (0.379s / 4.35s)

### Real Bottlenecks (91% of Time)
1. **Variable Inlining**: 2.989s (69%) - Pure CPU/Python/AST
2. **Solver Validation**: 2.770s (64%) - CPU-bound checking
3. **Inline Batch**: 0.976s (22%) - More AST work

## The Dual Environment Reality

### GPU Environment (Kaggle Competition)
```
Hardware: 4x NVIDIA L4 (22.3GB each)
Use Case: Process 400 tasks × 5 samples = 2000 batt() calls
Current Performance: 0.379s batt + 3.971s other = 4.35s total
```

### CPU Environment (Future Scale/Cost Optimization)
```
Hardware: Multi-core CPUs (4-32 cores)
Use Case: Batch processing at scale, development, CI/CD
Current Performance: ~430ms batt (estimated) + unknown other
```

## Key Insight: Different Bottlenecks!

### On GPU (Current Kaggle)
```
Bottleneck Priority:
1. Variable Inlining (2.989s, 69%) ← PURE CPU WORK
2. Solver Validation (2.770s, 64%) ← PURE CPU WORK  
3. Inline Batch (0.976s, 22%)      ← PURE CPU WORK
4. Batt execution (0.379s, 9%)     ← GPU ACCELERATED ✓

Week 5 optimized #4 (only 9% of problem on GPU!)
Week 6+ must optimize #1-3 (91% of problem, CPU-bound)
```

### On CPU (When No GPU)
```
Bottleneck Priority (PREDICTED):
1. Batt execution (~1.2-1.8s, 30-40%) ← NEEDS OPTIMIZATION
2. Variable Inlining (~2.989s, 60%)   ← NEEDS OPTIMIZATION
3. Solver Validation (~2.770s, 55%)   ← NEEDS OPTIMIZATION
4. Inline Batch (~0.976s, 20%)        ← NEEDS OPTIMIZATION

Total: ~7.5-8.5s (2-3x slower than GPU environment)
All components need optimization on CPU!
```

## Optimization Strategy: Best of Both Worlds

### Phase 1: Make Batt Fast Everywhere (DONE for GPU) ✅
**Goal**: Batt should be fast with OR without GPU

**Already Implemented**:
```python
def batch_process_samples_gpu(S):
    """GPU acceleration with automatic CPU fallback"""
    if not USE_GPU or len(S) < 3:
        # CPU fallback - works but slower
        return cpu_version()
    
    # GPU path - 3.3x faster
    return gpu_version()
```

**Status**: ✅ GPU path optimized, CPU fallback works

**Next**: Optimize CPU fallback path too!
- Current CPU fallback: ~430ms (estimated)
- Target: ~200ms with vectorization/caching
- Benefit: 2x speedup on CPU, no GPU required

### Phase 2: Parallelize CPU-Bound Operations (Week 6 Priority)
**Goal**: Speed up the 91% that's pure Python/AST work

**Target #1: Variable Inlining (2.989s → 1.0s)**
```python
# Current: Single-threaded AST traversal
# Target: Multi-process or caching

Optimization Options:
1. Multiprocessing pool (4 workers) → 2.5x speedup → 1.2s
2. Cache inlined results → Skip repeat work → 0.8s  
3. Optimize AST library → Use ast_tools → 0.9s
4. **COMBINE ALL THREE** → 0.5-0.7s (4-5x speedup!)

Impact: Save 2.0-2.5s per task
ROI: 8x more important than further batt optimization
Works: CPU AND GPU environments equally
```

**Target #2: Solver Validation (2.770s → 0.7s)**
```python
# Current: Sequential validation (87ms × 32 solvers)
# Target: Parallel validation

Optimization Options:
1. Multiprocessing pool (8 workers) → 4x speedup → 0.7s
2. Cache validation results → Skip known-good → 0.3s
3. Skip validation for simple solvers → Save 50% → 1.4s
4. **COMBINE** → 0.2-0.4s (7-10x speedup!)

Impact: Save 2.3-2.5s per task
ROI: 7x more important than further batt optimization  
Works: CPU AND GPU environments equally
```

**Target #3: Inline Batch (0.976s → 0.5s)**
```python
# Current: More sequential AST work
# Target: Same optimizations as variable inlining

Optimization Options:
1. Combine with variable inlining pass → Save overhead
2. Multiprocessing → 2x speedup → 0.5s
3. Caching → Additional 20% → 0.4s

Impact: Save 0.5s per task
Works: CPU AND GPU environments equally
```

### Phase 3: Optimize CPU Fallback Path (Week 6 Secondary)
**Goal**: Make batt fast even without GPU

```python
# Current CPU fallback in batch_process_samples_gpu
def batch_process_samples_gpu(S):
    if not USE_GPU or len(S) < 3:
        # CURRENT: Naive implementation
        t1 = apply(first, S)
        t2 = apply(second, S)
        t3 = mapply(p_g, t1)
        t4 = mapply(p_g, t2)
        return t1, t2, t3, t4

# OPTIMIZED: Vectorized CPU operations
def batch_process_samples_cpu_optimized(S):
    """Fast CPU path using NumPy/list comprehensions"""
    # Extract in one pass
    inputs = [s[0] for s in S]
    outputs = [s[1] for s in S]
    
    # Vectorized p_g using NumPy
    processed_inputs = [frozenset((r, c, color) 
                                  for r, row in enumerate(grid)
                                  for c, color in enumerate(row)
                                  if color != 0)
                       for grid in inputs]
    processed_outputs = [frozenset((r, c, color) 
                                   for r, row in enumerate(grid)
                                   for c, color in enumerate(row)
                                   if color != 0)
                        for grid in outputs]
    
    return tuple(inputs), tuple(outputs), \
           tuple(processed_inputs), tuple(processed_outputs)

# Expected: 430ms → 200ms (2x speedup on CPU)
```

## Implementation Priority

### Week 6A: CPU-Bound Optimization (HIGH IMPACT)
**Timeline**: 3-5 days  
**Impact**: 5-7s saved per task (60-80% speedup)  
**Benefits**: CPU AND GPU environments

1. **Variable Inlining Optimization** (Day 1-2)
   - Add multiprocessing pool
   - Implement caching for repeated patterns
   - Profile and optimize AST traversal
   - Target: 2.989s → 1.0s (3x speedup)

2. **Solver Validation Optimization** (Day 3-4)
   - Parallel validation with ProcessPoolExecutor
   - Cache validation results
   - Skip validation for known-good solvers
   - Target: 2.770s → 0.7s (4x speedup)

3. **Inline Batch Optimization** (Day 5)
   - Combine with variable inlining
   - Add caching
   - Target: 0.976s → 0.5s (2x speedup)

**Total Week 6A Impact**:
- GPU environment: 4.35s → ~1.5s (3x faster)
- CPU environment: ~8s → ~3s (2.7x faster)
- **Both environments benefit equally!**

### Week 6B: CPU Fallback Optimization (MEDIUM IMPACT)
**Timeline**: 2-3 days  
**Impact**: 1-2s saved per task on CPU-only  
**Benefits**: CPU environment only

1. **Optimize batch_process_samples CPU Path** (Day 1)
   - Replace naive apply/mapply with vectorized ops
   - Use NumPy for grid processing
   - Add list comprehension optimizations
   - Target: 430ms → 200ms (2x speedup)

2. **Vectorize Other Common Patterns** (Day 2-3)
   - Identify hot paths from profiling
   - Add CPU vectorization where beneficial
   - Maintain GPU compatibility

**Total Week 6B Impact**:
- GPU environment: No change (still 1.5s)
- CPU environment: 3s → 2.2s (1.4x faster)
- **Closes GPU/CPU performance gap**

## Expected Final Performance

### After Week 6A (CPU-Bound Optimization)
```
GPU Environment (Kaggle):
  Variable Inlining: 1.0s (was 2.989s) ← 3x faster
  Solver Validation: 0.7s (was 2.770s) ← 4x faster
  Inline Batch:      0.5s (was 0.976s) ← 2x faster
  Batt (GPU):        0.3s (was 0.379s) ← slightly faster
  TOTAL:            2.5s (was 4.35s)   ← 1.7x faster

CPU Environment (No GPU):
  Variable Inlining: 1.0s (was 2.989s) ← 3x faster
  Solver Validation: 0.7s (was 2.770s) ← 4x faster  
  Inline Batch:      0.5s (was 0.976s) ← 2x faster
  Batt (CPU):        1.2s (was ~1.8s)  ← slightly faster
  TOTAL:            3.4s (was ~8.5s)   ← 2.5x faster
```

### After Week 6B (CPU Fallback Optimization)
```
GPU Environment: 2.5s (no change)

CPU Environment:
  Variable Inlining: 1.0s ← optimized
  Solver Validation: 0.7s ← optimized
  Inline Batch:      0.5s ← optimized
  Batt (CPU):        0.6s ← 2x faster with vectorization
  TOTAL:            2.8s (was 3.4s) ← 1.2x faster
  
CPU now only 12% slower than GPU! (was 95% slower)
```

## Key Architectural Decisions

### 1. Keep Dual Code Paths
```python
# GOOD: Automatic fallback
if USE_GPU:
    return gpu_accelerated_version()
else:
    return cpu_optimized_version()  # Also optimize this!

# BAD: Only optimize GPU path
if USE_GPU:
    return super_fast_gpu()
else:
    return slow_naive_cpu()  # Don't leave this slow!
```

### 2. Optimize Shared Bottlenecks First
- Variable inlining, validation, etc. are pure Python
- **Same code runs on both CPU and GPU machines**
- Optimizing these helps BOTH environments
- **Higher ROI than environment-specific optimizations**

### 3. Use Multiprocessing for CPU-Bound Work
- Python's GIL limits threading for CPU work
- Multiprocessing bypasses GIL
- Works great for:
  - AST traversal (embarrassingly parallel)
  - Solver validation (independent checks)
  - Batch operations (process multiple tasks)

### 4. Cache Expensive Operations
- Variable inlining results (same patterns repeat)
- Solver validation results (solvers don't change)
- AST transformations (common code patterns)
- Works equally well on CPU and GPU machines

## Testing Strategy

### Dual Environment Testing
```bash
# Test on GPU (Kaggle)
bash run_card.sh -c 10 -T -g

# Test on CPU (local)
bash run_card.sh -c 10 -T -m

# Compare results
python analyze_dual_performance.py
```

### Performance Targets
```
Metric                  GPU Target    CPU Target
--------------------------------------------------
Variable Inlining       < 1.0s        < 1.0s
Solver Validation       < 0.7s        < 0.7s
Inline Batch            < 0.5s        < 0.5s
Batt Execution          < 0.3s        < 0.6s
--------------------------------------------------
Total per Task          < 2.5s        < 2.8s
```

## Next Steps

### Immediate (This Week)
1. ✅ Fix run_card.sh for proper GPU/CPU mode selection
2. ✅ Add timing output (-T flag)
3. ⏳ Baseline CPU-only performance (force -m mode)
4. ⏳ Document CPU vs GPU actual timings

### Week 6A: Shared Optimizations (HIGH ROI)
1. Profile variable inlining (utils.inline_variables)
2. Implement multiprocessing pool
3. Add caching for repeated patterns
4. Test on BOTH GPU and CPU environments
5. Parallelize solver validation
6. Optimize inline batch operations

### Week 6B: CPU-Specific Optimizations
1. Vectorize batch_process_samples CPU fallback
2. Add NumPy operations where beneficial
3. Profile and optimize other CPU hot paths
4. Validate GPU path still works
5. Measure CPU/GPU performance gap

### Documentation
1. Create performance comparison table
2. Document optimization techniques used
3. Guide for adding new dual-environment code
4. Best practices for CPU vs GPU selection

## Success Metrics

### Week 6A Success (Shared Optimizations)
- ✅ GPU environment: 4.35s → 2.5s (1.7x faster)
- ✅ CPU environment: 8.5s → 3.4s (2.5x faster)  
- ✅ Both environments benefit
- ✅ Code runs correctly in both modes

### Week 6B Success (CPU Optimization)
- ✅ CPU environment: 3.4s → 2.8s (1.2x faster)
- ✅ CPU only 12% slower than GPU (was 95%)
- ✅ Cost-effective fallback for non-GPU compute
- ✅ Development/CI can use CPU mode

### Overall Success
- ✅ Best performance in each environment
- ✅ Graceful degradation when GPU unavailable
- ✅ Single codebase handles both modes
- ✅ Easy to switch between CPU and GPU (-g/-m flags)

## Key Takeaway

**Week 5 taught us**: GPU acceleration works great for batt! (3.3x speedup)

**Week 6 strategy**: 
1. Optimize the 91% that's pure Python (benefits BOTH)
2. Then optimize CPU fallback paths (benefits CPU)
3. Result: Fast code everywhere, not just on GPU

**Philosophy**: 
- Don't just make GPU code fast
- Make ALL code fast, regardless of environment
- Best of both worlds!
