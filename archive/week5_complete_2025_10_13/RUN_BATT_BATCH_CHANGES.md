# run_batt.py Changes for Batch Processing

**Date**: October 13, 2025  
**Context**: How to modify run_batt.py for true batch GPU acceleration  
**Status**: 🎯 Architecture changes needed

---

## Current Architecture (Individual Calls)

### How it Works Now

```python
# check_batt() - Lines 438-640
def check_batt(total_data, task_i, task_id, ...):
    demo_task = total_data['demo'][task_id]  # e.g., 5 samples
    S = tuple((inp, out) for inp, out in demo_task)
    
    # Process each demo sample INDIVIDUALLY
    for i, sample in enumerate(demo_task):
        I = sample['input']
        O = sample['output']
        
        # INDIVIDUAL batt() call
        result = batt(task_id, S, I, None, pile_log_path)
        
        # Process result...
        if result matches:
            # Another INDIVIDUAL batt() call for diff
            result = batt(task_id, S, I, O, pile_log_path)
```

**Key characteristics:**
- Each sample processed separately
- Each calls `batt(task_id, S, I, C, log)` individually
- S contains all demo samples (for context)
- I and C are for ONE specific sample
- Total calls per task: ~5-10 batt() calls

**Problem for GPU batching:**
- Can't batch DSL operations across samples
- Each batt() call is independent
- GPU sees one small workload at a time

---

## What Needs to Change for Batch Processing

### Strategy 1: Batch Within Task (Parallel Samples)

**Current (Sequential):**
```python
# Process samples one at a time
for sample in demo_task:
    result = batt(task_id, S, sample['input'], None, log)
    # Time: 5 × 0.3s = 1.5s
```

**Needed (Batch):**
```python
# Collect all sample inputs
all_I = [sample['input'] for sample in demo_task]
all_C = [None] * len(demo_task)  # No output for first pass

# SINGLE batch call
all_results = batt_batch(task_id, S, all_I, all_C, log)
# Time: 0.3s (if GPU can parallelize)
# Speedup: 5x per task
```

**Changes required:**
1. Create `batt_batch()` function that accepts lists
2. Modify DSL operations to handle batches of inputs
3. Return list of results (one per sample)

### Strategy 2: Batch Across Tasks (Mega-Batch)

**Current (Per-task):**
```python
# Process tasks one at a time
for task_id in all_tasks:
    result = check_batt(task_id, ...)
    # Time: 400 × 1.8s = 720s
```

**Needed (Mega-batch):**
```python
# Collect ALL inputs from ALL tasks
all_inputs = []
for task_id in all_tasks:
    demo_task = total_data['demo'][task_id]
    S = get_S(demo_task)
    for sample in demo_task:
        all_inputs.append({
            'task_id': task_id,
            'S': S,
            'I': sample['input'],
            'C': None
        })

# SINGLE mega-batch call
all_results = mega_batt_batch(all_inputs)
# Time: depends on GPU efficiency
# Expected: 720s / (4 GPUs × 0.8) = 225s
# Speedup: 3.2x
```

**Changes required:**
1. Collect inputs from all tasks before processing
2. Create `mega_batt_batch()` that processes 1000s of inputs
3. Split results back to per-task format
4. Handle task-specific S parameters

---

## Detailed Change Requirements

### Change 1: Modify batt() Signature

**Current:**
```python
def batt(task_id, S, I, C, log_path):
    """
    Process ONE sample
    
    Args:
        task_id: Task identifier
        S: Demo samples (for context)
        I: Input grid for THIS sample
        C: Output grid for THIS sample (or None)
        log_path: Log file path
    
    Returns:
        (outputs, solver_scores) for THIS sample
    """
    # 1076 operations...
    return o, s
```

**Needed for batching:**
```python
def batt_batch(task_id, S, I_list, C_list, log_path):
    """
    Process MULTIPLE samples at once
    
    Args:
        task_id: Task identifier
        S: Demo samples (for context)
        I_list: List of input grids [I1, I2, I3, ...]
        C_list: List of output grids [C1, C2, C3, ...] (or Nones)
        log_path: Log file path
    
    Returns:
        List of (outputs, solver_scores) - one per sample
    """
    # Batch operations across all samples
    # Returns: [(o1, s1), (o2, s2), (o3, s3), ...]
```

**OR create wrapper:**
```python
def batt_batch(task_id, S, I_list, C_list, log_path):
    """Wrapper that calls batt() in batch-friendly way"""
    # This is what GPU batch processing would accelerate
    results = []
    for I, C in zip(I_list, C_list):
        result = batt(task_id, S, I, C, log_path)
        results.append(result)
    return results
```

### Change 2: Modify DSL Operations for Batching

**Current DSL operations:**
```python
# From dsl.py - operates on single grid
def rot90(grid):
    return tuple(tuple(row) for row in zip(*grid[::-1]))

def apply(func, container):
    return frozenset(func(item) for item in container)

def o_g(grid, value):
    return frozenset((i, j) for i, row in enumerate(grid) 
                     for j, cell in enumerate(row) if cell == value)
```

**Needed for batching:**
```python
# Batch versions - operate on list of grids
def batch_rot90(grids):
    return [rot90(g) for g in grids]

def batch_apply(func, containers):
    return [apply(func, c) for c in containers]

def batch_o_g(grids, value):
    return [o_g(g, value) for g in grids]
```

**OR use GPU operations:**
```python
# gpu_dsl_operations.py already has these!
from gpu_dsl_operations import GPUDSLOperations

gpu_ops = GPUDSLOperations()
rotated_grids = gpu_ops.batch_rot90(grids)  # GPU accelerated
o_g_results = gpu_ops.batch_o_g(grids, value)  # GPU accelerated
```

### Change 3: Modify run_batt.py to Use Batching

**Option A: Batch within task (simpler)**

```python
# In check_batt() - Replace lines 457-520
def check_batt(total_data, task_i, task_id, d_score, start_time, pile_log_path, timeout=1, prof=None):
    demo_task = total_data['demo'][task_id]
    S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in demo_task)
    
    # Collect all demo inputs
    demo_I_list = [sample['input'] for sample in demo_task]
    demo_C_list = [None] * len(demo_task)
    
    # BATCH CALL for all demo samples at once
    demo_results = batt_batch(task_id, S, demo_I_list, demo_C_list, pile_log_path)
    
    # Process results
    for i, (demo_o, demo_s) in enumerate(demo_results):
        O = demo_task[i]['output']
        o['demo'][i] = demo_o
        
        # Check for matches
        for t_n, evo, o_solver_id, okt in demo_o:
            match = okt == O
            if match:
                # Run diff (can also batch these!)
                diff_result = batt(task_id, S, demo_I_list[i], O, pile_log_path)
                # Process diff...
```

**Option B: Mega-batch across tasks (more complex but better GPU utilization)**

```python
# In main() - Replace task loop
def main(do_list, ...):
    # Phase 1: Collect ALL inputs from ALL tasks
    all_inputs = []
    task_metadata = []
    
    for task_id in do_list:
        demo_task = total_data['demo'][task_id]
        test_task = total_data['test'][task_id]
        S = get_S(demo_task)
        
        # Collect demo inputs
        for i, sample in enumerate(demo_task):
            all_inputs.append({
                'task_id': task_id,
                'S': S,
                'I': sample['input'],
                'C': None,
                'type': 'demo',
                'index': i
            })
            task_metadata.append((task_id, 'demo', i))
        
        # Collect test inputs
        for i, sample in enumerate(test_task):
            all_inputs.append({
                'task_id': task_id,
                'S': S,
                'I': sample['input'],
                'C': None,
                'type': 'test',
                'index': i
            })
            task_metadata.append((task_id, 'test', i))
    
    # Phase 2: Process ALL inputs in mega-batches
    print(f"Processing {len(all_inputs)} samples in mega-batches...")
    all_results = []
    
    for batch_start in range(0, len(all_inputs), 1000):
        batch = all_inputs[batch_start:batch_start+1000]
        
        # Extract batch data
        batch_task_ids = [inp['task_id'] for inp in batch]
        batch_S = [inp['S'] for inp in batch]
        batch_I = [inp['I'] for inp in batch]
        batch_C = [inp['C'] for inp in batch]
        
        # MEGA-BATCH CALL
        batch_results = mega_batt_batch(batch_task_ids, batch_S, batch_I, batch_C, pile_log_path)
        all_results.extend(batch_results)
    
    # Phase 3: Split results back to per-task format
    results_by_task = {}
    for (task_id, sample_type, index), result in zip(task_metadata, all_results):
        if task_id not in results_by_task:
            results_by_task[task_id] = {'demo': {}, 'test': {}}
        results_by_task[task_id][sample_type][index] = result
    
    # Phase 4: Post-process (scoring, diff, etc.)
    # ...
```

---

## Implementation Complexity Analysis

### Option A: Batch Within Task

**Pros:**
- ✅ Simpler to implement (minimal changes)
- ✅ Maintains task isolation
- ✅ Easy to debug
- ✅ Preserves existing error handling

**Cons:**
- ❌ Limited GPU utilization (only 5 samples at once)
- ❌ Can't amortize GPU transfer across many tasks
- ❌ Batch size too small (5 vs ideal 1000+)

**Expected speedup:**
- Per task: 1.8s → 0.36s (5x)
- Full run: 720s → 144s (5x)

**But**: GPU overhead might dominate for small batches!

### Option B: Mega-Batch Across Tasks

**Pros:**
- ✅ Maximum GPU utilization (1000+ samples per batch)
- ✅ Amortize GPU transfer cost
- ✅ True parallelism across independent tasks
- ✅ Best possible speedup

**Cons:**
- ❌ Complex restructuring of run_batt.py
- ❌ Need to handle heterogeneous S parameters
- ❌ Harder to debug failures
- ❌ More complex error handling

**Expected speedup:**
- Full run: 720s → 225s (3.2x realistic, up to 9x optimistic)

---

## Recommended Approach

### Phase 1: Test Feasibility First! 🎯

**Before changing anything, answer:**
1. Can Python even run 5 batt() calls in parallel without GIL blocking?
2. Does ThreadPoolExecutor help or hurt?
3. What is actual speedup of existing parallel demo code?

**Test script:**
```python
# test_parallel_feasibility.py
import time
from concurrent.futures import ThreadPoolExecutor

def test_sequential():
    start = time.time()
    for i in range(5):
        result = batt(task_id, S, demo_task[i]['input'], None, log)
    return time.time() - start

def test_parallel():
    start = time.time()
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [
            executor.submit(batt, task_id, S, demo_task[i]['input'], None, log)
            for i in range(5)
        ]
        results = [f.result() for f in futures]
    return time.time() - start

seq_time = test_sequential()
par_time = test_parallel()
print(f"Sequential: {seq_time:.3f}s")
print(f"Parallel: {par_time:.3f}s")
print(f"Speedup: {seq_time/par_time:.2f}x")
```

**Expected outcomes:**
- ✅ **Speedup > 1.5x**: Parallelism works! Proceed with Option A
- ⚠️ **Speedup 0.8-1.2x**: Marginal benefit, consider Option B (mega-batch)
- ❌ **Speedup < 0.8x**: GIL blocking, must use multiprocessing OR mega-batch GPU

### Phase 2A: If Parallelism Works (Speedup > 1.5x)

**Implement Option A: Batch within task**

1. Create `batt_batch()` wrapper (simple)
2. Modify `check_batt()` to use it
3. Test on 20 tasks
4. Deploy if successful

**Expected timeline:** 2-4 hours

### Phase 2B: If Parallelism Doesn't Work (Speedup < 1.5x)

**Implement Option B: Mega-batch across tasks**

1. Create `mega_batt_batch()` with GPU support
2. Restructure run_batt.py for batch collection
3. Implement result splitting
4. Extensive testing

**Expected timeline:** 1-2 days

### Phase 3: GPU Integration (Either Option)

**Once batching works, add GPU acceleration:**

```python
def mega_batt_batch(task_ids, S_list, I_list, C_list, log_path):
    # Use GPU operations for batch processing
    from gpu_dsl_operations import get_gpu_ops
    
    gpu_ops = get_gpu_ops()
    
    # GPU-accelerated batch operations
    # (This is what provides the actual speedup!)
    results = []
    for task_id, S, I, C in zip(task_ids, S_list, I_list, C_list):
        # Process with GPU batch operations
        result = batt_with_gpu(task_id, S, I, C, gpu_ops)
        results.append(result)
    
    return results
```

---

## Critical Insight: Architecture Mismatch!

### The Real Problem

**Current batt() signature:**
```python
def batt(task_id, S, I, C, log_path):
    # S already contains multiple demo samples!
    # I and C are for ONE specific sample
    # Operations use S for context, I/C for this sample
```

**S parameter structure:**
```python
S = tuple((sample1_input, sample1_output),
          (sample2_input, sample2_output),
          (sample3_input, sample3_output),
          ...)
# S = all demo samples (for learning)
# I = specific input to transform
# C = specific output to match (or None)
```

**This means:**
- S is ALREADY a batch of samples (for context)
- I is the ONE sample we're processing
- Batching needs to handle multiple (S, I, C) tuples
- Can't just pass list of I's - each might have different S!

### The Heterogeneity Problem

**Different tasks have different S:**
```python
# Task 1: 3 demo samples
S1 = ((I1a, O1a), (I1b, O1b), (I1c, O1c))

# Task 2: 5 demo samples  
S2 = ((I2a, O2a), (I2b, O2b), (I2c, O2c), (I2d, O2d), (I2e, O2e))

# Can't easily batch these together!
```

**This is why mega-batch is complex:**
- Each batt() call has task-specific S
- Can't just concatenate inputs
- Need to handle variable-length S parameters

**Solutions:**
1. **Pad S to same length** (wasteful)
2. **Group by S size** (limits batching)
3. **Process within-task only** (Option A - simpler!)

---

## Final Recommendation

### Start with Feasibility Test (30 minutes)

**Create and run:**
```bash
# test_parallel_feasibility.py
python test_parallel_feasibility.py -c 1 -b batt
```

**Measure:**
- Sequential: ? seconds
- Parallel (ThreadPoolExecutor): ? seconds
- Speedup: ? x

### Then Choose Path

**IF speedup > 1.5x:**
→ **Implement Option A** (batch within task)
→ Simple, effective, works now!

**IF speedup < 1.5x:**
→ **Implement multiprocessing** OR **mega-batch GPU**
→ More complex but necessary to bypass GIL

---

## Summary

**Current architecture:**
- ❌ Calls batt() individually for each sample
- ❌ Can't batch DSL operations across samples
- ❌ GPU sees tiny workloads (one sample at a time)

**Needed changes:**
- ✅ Batch samples within task (Option A) OR
- ✅ Mega-batch across tasks (Option B)
- ✅ Use GPU batch operations
- ✅ Handle heterogeneous S parameters

**First step:**
- 🎯 **TEST feasibility of parallel execution!**
- 🎯 Measure actual speedup before implementing
- 🎯 Let data drive the decision!

**Expected outcome:**
- Best case: 3-5x speedup (if parallelism works)
- Realistic: 2-3x speedup (with GIL limits)
- Worst case: Need multiprocessing (more complex)

---

**Status**: Need to test feasibility FIRST before implementing! 🎯  
**Next action**: Create test_parallel_feasibility.py and measure actual speedup  
**Priority**: HIGH - This determines which implementation path to take!
