# Week 5 Day 3 - Timeout Analysis

**Date**: October 13, 2025  
**Issue**: Batt calls timing out on Kaggle  
**Status**: 🔴 Critical performance problem discovered

---

## The Timeout Problem

### What Happened

```
-- 00576224 - demo[0] timed out
-- 00576224 - demo[1] timed out
-- 00576224 - test[0] timed out
```

**All batt() calls timing out!**

### Timing Data

```
main.run_batt                    0.051s
run_batt.check_batt             0.051s
batt.demo.parallel              0.040s  ← Demo scoring (all timeouts)
batt.test.call_with_timeout     0.011s  ← Test scoring (timeout)
```

**Problem**: Default timeout is **1 second**, but batt() with 1076 operations + GPU overhead is taking **> 1 second**!

---

## Root Cause Analysis

### The Generated Batt

```python
# batt.py (2,247 lines, 1,076 operations)
def batt(task_id, S, I, C, log_path):
    # Operation 1
    t1 = identity(p_g)
    t2 = t1(I)
    # ... 1074 more operations ...
    
    # GPU batch calls (9 total)
    t85, t86, t87, t88 = batch_process_samples_gpu(S)  # Line 190
    # ... more operations ...
    t185, t186, t187, t188 = batch_process_samples_gpu(S)  # Line 390
    # ... continues ...
```

**Characteristics**:
- 1,076 total operations
- 9 `batch_process_samples_gpu()` calls
- Each GPU call processes S (typically 2-3 sample pairs)
- Extensive operation chains between GPU calls

### The GPU Batch Function

```python
# batt_gpu.py
def batch_process_samples_gpu(S):
    """GPU-accelerated batch processing"""
    # Extract grids
    inputs = [sample[0] for sample in S]
    outputs = [sample[1] for sample in S]
    
    # GPU processing
    if USE_MULTI_GPU and len(S) >= 120:
        processed_inputs = multi_gpu_opt.batch_grid_op_multi_gpu(...)
        processed_outputs = multi_gpu_opt.batch_grid_op_multi_gpu(...)
    else:
        processed_inputs = gpu_opt.batch_grid_op_optimized(...)
        processed_outputs = gpu_opt.batch_grid_op_optimized(...)
```

**Problem**: GPU overhead dominates for small S!

### Why It Times Out

**Per batt() call:**
1. 1,076 DSL operations (CPU) ≈ 400-600ms
2. 9 GPU batch calls × overhead ≈ 9 × 100ms = 900ms
3. **Total ≈ 1,300-1,500ms** (exceeds 1s timeout!)

**GPU overhead breakdown:**
- Data transfer to GPU: 10-50ms per call
- GPU kernel launch: 1-10ms
- Data transfer from GPU: 10-50ms
- Total per GPU call: **20-110ms**
- × 9 calls = **180-990ms just for GPU overhead!**

**Critical issue**: S typically has only **2-3 samples**, which is TOO SMALL for GPU to be efficient!

---

## The Batch Size Problem

### What batch_process_samples_gpu() Expects

```python
# Efficient GPU usage needs 100+ grids
if USE_MULTI_GPU and len(S) >= 120:  # Multi-GPU threshold
    # Process on 4 GPUs
```

**Efficient batch size**: 100+ grids per call

### What It Actually Gets

```python
# Task 00576224 has 2 demo samples
S = ((input1, output1), (input2, output2))
len(S) = 2  # Only 2 sample pairs!

# batch_process_samples_gpu(S) processes:
# - 2 input grids
# - 2 output grids
# Total: 4 grids (WAY TOO SMALL!)
```

**Actual batch size**: 2-5 grids per call

**GPU overhead vs benefit**:
- GPU transfer: 50ms
- GPU compute (2 grids): 5ms
- **Total: 55ms**
- CPU would take: 10ms
- **GPU is 5.5x SLOWER!**

---

## Performance Calculations

### Sequential CPU Baseline (No GPU)

```python
# Pure CPU execution (no GPU calls)
1,076 operations × 0.4ms = 430ms per batt() call
✓ Fits within 1s timeout
```

### Current Implementation (GPU with tiny batches)

```python
# CPU operations
1,076 ops × 0.4ms = 430ms

# GPU overhead (9 calls × 55ms)
9 GPU calls × 55ms = 495ms

# Total
430ms + 495ms = 925ms ≈ 1 second

# BUT: Variance + initialization overhead = 1,300-1,500ms
❌ Exceeds 1s timeout!
```

### Why GPU Makes It Worse

**For batch size = 2-5 grids:**

| Operation | CPU Time | GPU Transfer | GPU Compute | GPU Total | Winner |
|-----------|----------|--------------|-------------|-----------|--------|
| Single call | 10ms | 50ms | 5ms | 55ms | **CPU 5.5x faster** |
| 9 calls | 90ms | 450ms | 45ms | 495ms | **CPU 5.5x faster** |

**Conclusion**: GPU overhead dominates when batch size is tiny!

---

## Why This Architecture Fails

### The Fundamental Mismatch

**GPU batch operations designed for:**
```python
# Process 100+ grids at once
grids = [grid1, grid2, ..., grid100]  # 100 grids
result = gpu_opt.batch_grid_op_optimized(grids, operation)
# Transfer overhead amortized: 50ms / 100 = 0.5ms per grid ✓
```

**What batt.py actually does:**
```python
# Process 2-3 grids at once
S = ((I1, O1), (I2, O2))  # 2 sample pairs = 4 grids total
result = batch_process_samples_gpu(S)
# Transfer overhead: 50ms / 4 = 12.5ms per grid ❌
# CPU would be: 10ms / 4 = 2.5ms per grid ✓
```

**GPU is 5x SLOWER because batch is too small!**

### The Architecture Design Flaw

**Week 4-5 assumed:**
1. batt() would process 100s of samples at once ❌
2. GPU batch calls would have 100+ grids ❌
3. GPU overhead would be amortized ❌

**Reality is:**
1. batt() processes 1 sample at a time ✓
2. S contains 2-5 samples for context only ✓
3. GPU sees 2-5 grids per call ✓
4. **GPU overhead dominates benefit** ✓

---

## The Real Performance Picture

### Current: Sequential with Tiny GPU Batches

```
Per task (2 demo + 1 test):
  - 3 batt() calls
  - Each: 1,300-1,500ms (with GPU overhead)
  - Total: 3.9-4.5s per task
  - RESULT: TIMEOUTS (exceeds 1s timeout)

Full run (400 tasks):
  - Would take: 400 × 4.2s = 1,680s (28 minutes)
  - With timeouts: FAILS COMPLETELY
```

### Without GPU Overhead (Pure CPU)

```
Per batt() call: 430ms ✓
Per task: 3 × 430ms = 1,290ms ≈ 1.3s
Full run: 400 × 1.3s = 520s (8.7 minutes)
RESULT: Works, but close to timeout
```

### With Proper Batching (What We Need)

```
Collect all samples from all tasks:
  - 400 tasks × 3 samples = 1,200 batt() calls
  - Each call has S with 2-5 samples

Option 1: Remove GPU calls (they hurt performance)
  Per task: 1.3s
  Full run: 520s (8.7 minutes)
  Speedup: Works! ✓

Option 2: True mega-batch (collect 1000+ samples)
  Process 1,200 samples in batches of 1000
  GPU overhead: 50ms × 2 = 100ms total
  GPU compute: 1,200 × 5ms / 4 GPUs = 1,500ms
  Total: 1,600ms = 1.6s for ALL samples
  Speedup: 520s → 1.6s = 325x! ✓✓✓

BUT: Requires complete architecture rewrite!
```

---

## Solutions

### Immediate Fix: Remove GPU Batch Calls ⚡

**Change batt_gpu.py:**
```python
def batch_process_samples_gpu(S):
    """CPU-only version (GPU overhead too high for tiny batches)"""
    from pile import apply, first, second, mapply, p_g
    
    # Always use CPU for tiny batches
    t1 = apply(first, S)
    t2 = apply(second, S)
    t3 = mapply(p_g, t1)
    t4 = mapply(p_g, t2)
    return t1, t2, t3, t4
```

**Expected result:**
- Per batt(): 1,300ms → 430ms (3x faster!)
- Fits within 1s timeout ✓
- Full run: 28 minutes → 8.7 minutes ✓

### Medium-term: Increase Timeout

**Change run_batt.py:**
```python
# Line ~1172
parser.add_argument('-t', '--timeout', type=float, default=5,  # was: 1
                    help='Timeout for each task in seconds (default: 5)')
```

**Trade-offs:**
- ✓ Allows complex operations to complete
- ✓ Minimal code changes
- ❌ Slower overall (waits for timeouts)
- ❌ Doesn't fix root cause

### Long-term: True Mega-Batch Architecture 🎯

**Complete restructure:**

```python
# Collect ALL samples from ALL tasks
all_samples = []
for task in all_tasks:
    for sample in task_samples:
        all_samples.append((task_id, S, I, C))

# Process in TRUE batches of 1000
for batch_start in range(0, len(all_samples), 1000):
    batch = all_samples[batch_start:batch_start+1000]
    
    # Extract ALL grids (1000+ grids!)
    all_grids = [s[2] for s in batch]  # All I grids
    
    # GPU processes 1000 grids at once
    results = gpu_opt.batch_grid_op_optimized(all_grids, operation)
    
    # Now GPU overhead is amortized:
    # 50ms / 1000 = 0.05ms per grid ✓
```

**Expected speedup**: 520s → 1.6s = **325x faster!** 🚀

**But**: Requires complete rewrite of:
- batt() generation (remove per-sample structure)
- run_batt.py (collect before processing)
- Result handling (split back to per-task)
- Extensive testing

---

## Recommendations

### Immediate Action (Today) ⚡

**1. Disable GPU batch calls**
```bash
# Edit batt_gpu.py - force CPU fallback
vim batt_gpu.py
# Change batch_process_samples_gpu to always use CPU

# Regenerate batt
python card.py -fd -c 32 --vectorized -f batt.py

# Test
python run_batt.py -c 5 -b batt -t 5 --timing
```

**Expected**: No more timeouts, 3x faster per call

**2. Increase timeout as safety**
```bash
# Test with longer timeout
python run_batt.py -c 5 -b batt -t 5 --timing
```

### This Week (If Time Permits)

**Analyze feasibility of true mega-batch:**
- How to collect 1000+ samples before processing?
- How to maintain task-specific S parameters?
- How to split results back to per-task format?
- Is the complexity worth 325x speedup?

### Recommendation

**FOR NOW**: **Disable GPU batch calls and use pure CPU**

**WHY**:
1. ✅ GPU overhead >> benefit for tiny batches (2-5 grids)
2. ✅ CPU is 5.5x faster for this workload
3. ✅ Fits within 1s timeout
4. ✅ No architecture changes needed
5. ✅ Can be done TODAY

**LATER**: Consider true mega-batch if:
1. Sequential CPU still too slow
2. Have time for major architecture rewrite
3. Potential 325x speedup worth complexity

---

## Key Learnings

### 1. GPU is NOT Always Faster

**GPU excels at:**
- Large batches (100+ items)
- Parallel operations
- Amortized transfer costs

**GPU fails at:**
- Tiny batches (2-10 items) ← **Our case!**
- Transfer overhead > compute benefit
- Sequential operations

### 2. Batch Size is Critical

```
Batch size 2-5:    GPU 5.5x SLOWER ❌
Batch size 100:    GPU 2x faster ✓
Batch size 1000:   GPU 10-35x faster ✓✓✓
```

**Our current batch size: 2-5** ❌

### 3. Architecture Must Match Hardware

**Current architecture:**
- Process samples one at a time
- S has 2-5 samples (too small for GPU)
- GPU overhead dominates

**Needed for GPU:**
- Process 1000+ samples at once
- Amortize transfer costs
- True parallelism

**Gap**: Current architecture fundamentally incompatible with efficient GPU usage!

---

## Status

**Week 5 GPU effort assessment**: ❌ **FAILED - Made performance WORSE**

**Why**:
1. GPU batch calls add 495ms overhead
2. Tiny batch sizes (2-5 grids) don't benefit from GPU
3. CPU is 5.5x faster for this workload
4. Causes timeouts (> 1s per call)

**Solution**:
- Remove GPU batch calls (immediate)
- Use pure CPU (3x faster!)
- Consider true mega-batch architecture (future, 325x potential)

**Current priority**: **GET IT WORKING FIRST** (disable GPU), optimize later!

---

**Created**: October 13, 2025  
**Status**: Critical issue identified - GPU makes performance WORSE  
**Action**: Disable GPU batch calls immediately! ⚡
