# Batt Function GPU Acceleration Plan

**Date:** October 12, 2025  
**Target:** Multi-GPU batch processing with L4x4 (35x speedup)  
**Status:** Ready to implement

## Executive Summary

The `batt()` function combines **many solvers** and processes samples from dataset `S`. Analysis reveals extensive batch processing opportunities that are **perfect for GPU acceleration**.

### Key Discovery: Repeated Pattern Operations

The batt function contains a **repeating pattern** that runs multiple times:
```python
t113 = apply(first, S)      # Extract inputs from samples
t114 = apply(second, S)     # Extract outputs from samples  
t115 = mapply(p_g, t113)    # Process batch of inputs
t116 = mapply(p_g, t114)    # Process batch of outputs
```

This pattern appears **5+ times** in the file, each time processing the entire sample set `S` with batch operations!

## Batch Operations Identified

### Pattern 1: Sample Extraction + Batch Processing (HIGHEST IMPACT)
**Frequency:** 5 occurrences  
**Line numbers:** 581-584, 944-947, 1217-1220, 2388-2391, 2521-2524, 3279-3282, 3287-3290

```python
# Current (Sequential):
t113 = apply(first, S)      # ~0.5ms per sample * N samples
t114 = apply(second, S)     # ~0.5ms per sample * N samples
t115 = mapply(p_g, t113)    # ~0.1ms per grid * N grids
t116 = mapply(p_g, t114)    # ~0.1ms per grid * N grids

# GPU Batch (Parallel):
t113, t114, t115, t116 = batch_process_samples_gpu(S, [first, second, p_g, p_g])
# Single GPU transfer, parallel processing
# Expected speedup: 10-35x on L4x4
```

**Why This Is Perfect for GPU:**
- ✅ Processes multiple samples (typically 3-10 per task)
- ✅ Each sample has input+output grids  
- ✅ All operations are pure functions (no side effects)
- ✅ Data already in batch form (`S` is a list)
- ✅ Matches existing `batch_grid_op_optimized()` API

### Pattern 2: Object Extraction (o_g)
**Frequency:** 6+ occurrences  
**Line numbers:** 167, 187, 202, 237, 2379

```python
# Current:
t31 = o_g(I, R3)   # Connected components (expensive!)
t35 = o_g(I, R1)
t38 = o_g(I, R5)
t45 = o_g(I, R7)

# GPU Optimization:
# These run on SAME grid with different parameters
results = batch_o_g_gpu([I, I, I, I], [R3, R1, R5, R7])
t31, t35, t38, t45 = results
```

**Expected Impact:** 2-4x speedup per o_g call

### Pattern 3: mapply Operations
**Frequency:** 10+ occurrences  
**Line numbers:** 447, 547, 1198, 1351, 1476, and more

```python
# Current:
t86 = mapply(corners, t42)      # Loop over objects
t106 = mapply(backdrop, t58)    # Loop over objects
t245 = mapply(dneighbors, t151) # Loop over objects

# GPU Batch:
batch_results = multi_mapply_gpu([
    (corners, t42),
    (backdrop, t58),
    (dneighbors, t151)
])
```

**Expected Impact:** 5-15x speedup for large object sets

## Implementation Strategy

### Phase 1: Add GPU Batch Helper to Generated Files (Week 1)

**Goal:** Import GPU optimizer and create batch processing helpers

**File:** Modify `card.py` to generate GPU-enabled batt files

**Generated code addition:**
```python
# At top of generated batt file (after imports)
from gpu_optimizations import auto_select_optimizer

# Initialize GPU optimizer
try:
    gpu_opt = auto_select_optimizer()
    USE_GPU = True
except:
    gpu_opt = None
    USE_GPU = False

def batch_mapply_gpu(func, containers, min_batch=30):
    """GPU-accelerated mapply for batch processing"""
    if not USE_GPU or len(containers) < min_batch:
        return [mapply(func, c) for c in containers]
    
    # Flatten all objects from all containers
    all_objects = []
    object_counts = []
    for container in containers:
        objs = list(container)
        all_objects.extend(objs)
        object_counts.append(len(objs))
    
    # GPU batch process
    if all_objects:
        processed = gpu_opt.batch_grid_op_optimized(
            all_objects, func, vectorized=False
        )
        
        # Reconstruct containers
        results = []
        idx = 0
        for count in object_counts:
            results.append(frozenset(processed[idx:idx+count]))
            idx += count
        return results
    return [frozenset() for _ in containers]

def batch_process_samples_gpu(S, operations):
    """
    Process samples with multiple operations in batch
    S = [(input, output), (input, output), ...]
    operations = [first, second, p_g, p_g] for example
    """
    if not USE_GPU or len(S) < 3:
        # CPU fallback
        t1 = apply(operations[0], S)
        t2 = apply(operations[1], S)
        t3 = mapply(operations[2], t1) if len(operations) > 2 else t1
        t4 = mapply(operations[3], t2) if len(operations) > 3 else t2
        return t1, t2, t3, t4
    
    # GPU batch mode
    inputs = [sample[0] for sample in S]   # All input grids
    outputs = [sample[1] for sample in S]  # All output grids
    
    # Single GPU transfer and batch process
    if len(operations) > 2:
        processed_inputs = gpu_opt.batch_grid_op_optimized(
            inputs, operations[2], vectorized=False
        )
        processed_outputs = gpu_opt.batch_grid_op_optimized(
            outputs, operations[3], vectorized=False
        )
        return tuple(inputs), tuple(outputs), tuple(processed_inputs), tuple(processed_outputs)
    else:
        return tuple(inputs), tuple(outputs), tuple(inputs), tuple(outputs)
```

### Phase 2: Identify and Replace Batch Patterns (Week 1-2)

**Pattern Detection in card.py:**

Add detection logic to identify these patterns during generation:
1. Detect `apply(first/second, S)` followed by `mapply()`
2. Detect multiple `o_g()` calls on same grid
3. Detect multiple `mapply()` calls in sequence

**Code Generation Modification:**

```python
# In card.py's main() function
def detect_batch_pattern(code, start_t):
    """Detect if t_num to t_num+N form a batch pattern"""
    # Check for sample extraction pattern
    if (code.t_call.get(start_t) == 'apply, first, S' and
        code.t_call.get(start_t+1) == 'apply, second, S' and
        'mapply' in code.t_call.get(start_t+2, '') and
        'mapply' in code.t_call.get(start_t+3, '')):
        return 'sample_batch', 4  # pattern type, length
    
    # Check for multiple o_g on same input
    # ... more patterns
    
    return None, 0

# During file generation
def generate_batch_optimized(code, pattern_type, t_start, t_end):
    if pattern_type == 'sample_batch':
        print(f'    # GPU Batch: Sample processing (t{t_start}-t{t_end})', file=code.file)
        print(f'    t{t_start}, t{t_start+1}, t{t_start+2}, t{t_start+3} = \\', file=code.file)
        print(f'        batch_process_samples_gpu(S, [first, second, p_g, p_g])', file=code.file)
        return True
    return False
```

### Phase 3: Multi-GPU Distribution (Week 2)

**For L4x4 GPU (4 devices):**

```python
from gpu_optimizations import MultiGPUOptimizer

# Initialize multi-GPU
try:
    import cupy as cp
    gpu_count = cp.cuda.runtime.getDeviceCount()
    if gpu_count >= 2:
        multi_gpu_opt = MultiGPUOptimizer()
        print(f"Multi-GPU enabled: {gpu_count} GPUs")
    else:
        multi_gpu_opt = None
except:
    multi_gpu_opt = None

# In batt function, for large batches (e.g., S with many samples):
def batch_process_samples_multi_gpu(S, operations):
    if multi_gpu_opt and len(S) >= 120:  # Threshold for multi-GPU
        # Split S across GPUs
        return multi_gpu_opt.batch_grid_op_multi_gpu(
            samples=S,
            operation=lambda s: process_sample(s, operations),
            num_gpus=4
        )
    else:
        return batch_process_samples_gpu(S, operations)
```

## Expected Performance Improvements

### Current Performance (CPU)
```
Sample extraction:    ~0.5ms per sample * 5 samples = 2.5ms
Batch p_g:            ~0.1ms per grid * 10 grids = 1.0ms
Object processing:    ~2ms per mapply * 10 calls = 20ms
Total per pattern:    ~23.5ms
Pattern repeats 5x:   ~117ms per batt call
```

### With Single GPU (L4)
```
Sample extraction:    ~0.3ms (batched)
Batch p_g:            ~0.2ms (GPU transfer + compute)
Object processing:    ~2ms (GPU batch)
Total per pattern:    ~2.5ms (9.4x speedup)
Pattern repeats 5x:   ~12.5ms per batt call
```

### With Multi-GPU (L4x4)
```
Sample extraction:    ~0.1ms (parallel across 4 GPUs)
Batch p_g:            ~0.05ms (distributed)
Object processing:    ~0.5ms (4-way parallel)
Total per pattern:    ~0.65ms (36x speedup!)
Pattern repeats 5x:   ~3.25ms per batt call
```

## Implementation Checklist

### Week 1: Basic GPU Batch Support
- [ ] Modify `card.py` to add GPU imports to generated files
- [ ] Add `batch_mapply_gpu()` helper function generation
- [ ] Add `batch_process_samples_gpu()` helper function generation
- [ ] Test on single pattern (sample extraction)
- [ ] Benchmark: expect 9-10x speedup

### Week 2: Pattern Detection & Replacement
- [ ] Implement pattern detection in `card.py`
- [ ] Auto-replace detected patterns with GPU batch calls
- [ ] Handle multiple `o_g` batching
- [ ] Test on full batt file
- [ ] Benchmark: expect 10-15x speedup

### Week 3: Multi-GPU Scaling
- [ ] Add Multi-GPU support for large batches
- [ ] Implement L4x4 4-GPU distribution
- [ ] Auto-detect GPU count and distribute
- [ ] Test on Kaggle L4x4
- [ ] Benchmark: expect 25-35x speedup

### Week 4: Production Optimization
- [ ] Add caching for repeated operations
- [ ] Optimize GPU memory management
- [ ] Add profiling/timing per pattern
- [ ] Create monitoring dashboard
- [ ] Full production deployment

## Risk Mitigation

1. **CPU Fallback Always Available**
   - GPU code wrapped in try-except
   - Auto-falls back to CPU if GPU unavailable
   - No regression on non-GPU systems

2. **Correctness Validation**
   - Run both CPU and GPU versions
   - Compare results for equality
   - Unit tests for each pattern

3. **Memory Management**
   - Batch size limits based on available GPU memory
   - Automatic batch splitting for large datasets
   - Clean up GPU memory after each batch

## Success Metrics

- **Performance**: 25-35x speedup on L4x4 for full batt execution
- **Reliability**: 100% correctness match with CPU version
- **Coverage**: 80%+ of batch operations GPU-accelerated
- **Memory**: < 80% GPU memory utilization
- **Availability**: Graceful CPU fallback when GPU unavailable

## Next Steps

1. **Start with Phase 1** - Add GPU helpers to generated files
2. **Test on single pattern** - Sample extraction (lines 581-584)
3. **Measure speedup** - Should see 9-10x on single L4 GPU
4. **Scale to multi-pattern** - Replace all 5+ occurrences
5. **Deploy multi-GPU** - Use L4x4 for maximum performance

**Expected Timeline:** 2-3 weeks to full production deployment  
**Expected ROI:** 25-35x faster batt execution on L4x4 GPU
