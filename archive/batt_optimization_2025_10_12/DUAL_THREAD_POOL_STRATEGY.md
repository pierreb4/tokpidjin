# Dual Thread Pool Strategy Analysis

## The Proposal

Use two separate thread pools to avoid nested usage conflicts:

```python
# High-level operations (sample scoring, batch processing)
_high_level_executor = ThreadPoolExecutor(max_workers=6)

# Low-level operations (run_with_timeout for individual batt calls)
_low_level_executor = ThreadPoolExecutor(max_workers=4)
```

## How It Would Work

### Current Problem (Single Pool)
```python
# Single global executor (4 workers)
_executor = ThreadPoolExecutor(max_workers=4)

# Phase 4 parallel scoring attempts:
for i in range(5):  # 5 demo samples
    # Uses _executor worker #1-4 (but we have 5 samples!)
    worker = _executor.submit(score_sample, sample[i])
    
    def score_sample(s):
        # Also needs _executor for run_with_timeout!
        # But all 4 workers are busy with score_sample calls!
        result = run_with_timeout(batt, ...)  # BLOCKED!

Result: Deadlock/starvation
```

### Proposed Solution (Dual Pool)
```python
# Two separate executors
_high_level_executor = ThreadPoolExecutor(max_workers=6)
_low_level_executor = ThreadPoolExecutor(max_workers=4)

# Phase 4 parallel scoring:
for i in range(5):  # 5 demo samples
    # Uses _high_level_executor workers
    worker = _high_level_executor.submit(score_sample, sample[i])
    
    def score_sample(s):
        # Uses _low_level_executor (separate pool!)
        result = run_with_timeout(batt, ...)  # NOT BLOCKED!

Result: No deadlock! ✅
```

## Implementation

### Option 1: Modify utils.py
```python
# utils.py

# Separate thread pools for different usage patterns
_high_level_executor = None
_low_level_executor = None
_executor_lock = threading.Lock()

def get_high_level_executor():
    """
    Get executor for high-level parallel operations (sample scoring, batch processing).
    Higher worker count since these operations don't nest.
    """
    global _high_level_executor
    if _high_level_executor is None:
        with _executor_lock:
            if _high_level_executor is None:
                # Can handle 6-8 parallel samples
                _high_level_executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)
    return _high_level_executor

def get_low_level_executor():
    """
    Get executor for low-level operations (run_with_timeout).
    Used by run_with_timeout to wrap batt() calls with timeouts.
    Limited to 4 workers to prevent resource contention.
    """
    global _low_level_executor
    if _low_level_executor is None:
        with _executor_lock:
            if _low_level_executor is None:
                # Conservative limit for nested operations
                _low_level_executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    return _low_level_executor

# Backward compatibility - default to low-level executor
def get_executor():
    """Get executor for legacy code (uses low-level executor)"""
    return get_low_level_executor()

async def run_with_timeout(func, args, timeout=5):
    """Uses low-level executor to avoid conflicts with high-level parallelism"""
    try:
        loop = asyncio.get_event_loop()
        executor = get_low_level_executor()  # ← Uses low-level pool
        result = await asyncio.wait_for(
            loop.run_in_executor(executor, func, *args), timeout
        )
        return False, result
    except asyncio.TimeoutError:
        return True, None
```

### Option 2: Modify run_batt.py Phase 4
```python
# run_batt.py

from utils import get_high_level_executor

async def check_batt(...):
    # Use high-level executor for sample parallelization
    loop = asyncio.get_event_loop()
    executor = get_high_level_executor()
    
    # Parallel demo scoring
    demo_futures = [
        loop.run_in_executor(executor, score_demo_sample, i, sample)
        for i, sample in enumerate(demo_task)
    ]
    demo_results = await asyncio.gather(*demo_futures)
    
    # Inside each score_demo_sample:
    # run_with_timeout uses low-level executor (separate pool)
```

## Expected Results

### Resource Allocation
```
High-level executor (8 workers):
├─ Worker 1: score_demo_sample(0) 
├─ Worker 2: score_demo_sample(1)
├─ Worker 3: score_demo_sample(2)
├─ Worker 4: score_demo_sample(3)
├─ Worker 5: score_demo_sample(4)
└─ Worker 6-8: Available for test samples

Low-level executor (4 workers):
├─ Worker 1: run_with_timeout for demo[0]'s batt()
├─ Worker 2: run_with_timeout for demo[1]'s batt()
├─ Worker 3: run_with_timeout for demo[2]'s batt()
└─ Worker 4: run_with_timeout for demo[3]'s batt()

Total: 12 threads, but no conflicts!
```

### Performance Estimate
```
Current (Sequential):
  Demo scoring: ~12s (sequential)
  Test scoring: ~3s (sequential)
  Total: ~15s

With Dual Pool (Parallel):
  Demo scoring: ~3-4s (5 samples parallel, no blocking)
  Test scoring: ~1-2s (parallel with demos)
  Total: ~4-5s (3-4x speedup!)
  
Overall: 16.8s → 7-8s (2-2.4x faster)
```

## Advantages ✅

1. **No Thread Pool Deadlock**: Separate pools eliminate nested usage conflicts
2. **Better Resource Utilization**: 12 total threads vs 4 (but no contention)
3. **Scalability**: Can tune each pool independently
4. **Backward Compatible**: Keep get_executor() for existing code
5. **Clear Separation**: High-level vs low-level operations explicit

## Potential Issues ⚠️

### 1. Resource Contention (Still Possible)
Even with separate thread pools, we still have:
- 5-8 parallel batt() calls competing for:
  - 4 GPUs (bottleneck!)
  - Memory (each loads data)
  - Python GIL (CPU-bound operations)

**Mitigation**: Limit high-level executor to 4-6 workers (not 8)

### 2. System Thread Limits
- Total threads: 12 (8 high + 4 low)
- macOS default limit: ~2048 threads per process
- Should be fine, but monitor

**Mitigation**: Start conservative (4 high + 4 low = 8 total)

### 3. Complexity
- Two executors to manage
- Need to choose correct executor for each operation
- More complex debugging

**Mitigation**: Good documentation and clear naming

## Recommended Implementation

### Phase 1: Add Dual Pool Support
```python
# utils.py - Add new executors
_high_level_executor = ThreadPoolExecutor(max_workers=4)  # Start conservative
_low_level_executor = ThreadPoolExecutor(max_workers=4)
```

### Phase 2: Test with Batch Operations
```python
# run_batt.py Phase 2 - Already uses explicit ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=4) as executor:
    inlined_data = list(executor.map(inline_one, candidate_data))

# Change to use high-level executor:
executor = get_high_level_executor()
inlined_data = list(executor.map(inline_one, candidate_data))
```

### Phase 3: Re-attempt Parallel Scoring
```python
# run_batt.py Phase 4 - Use high-level executor
async def check_batt(...):
    loop = asyncio.get_event_loop()
    executor = get_high_level_executor()  # ← New!
    
    # Parallel demo scoring
    demo_results = await asyncio.gather(*[
        loop.run_in_executor(executor, score_demo_sample, i, s)
        for i, s in enumerate(demo_task)
    ])
    
    # run_with_timeout inside still uses low-level executor
    # No conflicts!
```

### Phase 4: Gradually Increase High-Level Workers
```python
# Start: 4 high + 4 low = 8 total
# If stable, try: 6 high + 4 low = 10 total
# If still stable, try: 8 high + 4 low = 12 total

# Monitor for:
# - Timeouts (too much contention)
# - Memory usage (GPU memory especially)
# - Overall performance
```

## Testing Strategy

1. **Verify No Deadlock**: 
   - Run with 5-6 parallel samples
   - Ensure no timeouts that didn't exist before

2. **Measure Performance**:
   - Baseline: 16.8s (current)
   - Target: 8-10s (2x speedup)
   - Minimum acceptable: 12s (1.4x speedup)

3. **Check Resource Usage**:
   - GPU utilization
   - Memory consumption
   - Thread count

4. **Validate Correctness**:
   - Same candidate count (149 → 32)
   - Same solver scores
   - Same files created

## Risk Assessment

### Low Risk ✅
- Implementation is straightforward
- Easy to revert if problems occur
- Backward compatible with existing code

### Medium Risk ⚠️
- Still might hit resource contention (GPU, memory)
- May need tuning of worker counts
- Requires testing on Kaggle to validate

### High Risk ❌
- None identified

## Recommendation

**YES, implement dual thread pools!** This is a promising approach that:
- ✅ Addresses the root cause (nested usage)
- ✅ Low implementation complexity
- ✅ Easy to test incrementally
- ✅ Backward compatible
- ✅ Likely to succeed where Phase 4 failed

**Start conservative**:
- 4 high-level workers + 4 low-level workers = 8 total
- Test on Kaggle with Phase 4 parallel scoring
- Gradually increase if stable

**Expected outcome**: 2-2.5x overall speedup (16.8s → 7-8s)
