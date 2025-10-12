# Phase 4 Root Cause Analysis - Thread Pool Exhaustion

## The Real Problem: Nested Thread Pool Usage

### Thread Pool Architecture
```python
# utils.py - Global thread pool
_executor = ThreadPoolExecutor(max_workers=4)

# Used by:
1. run_with_timeout() - wraps batt() calls
2. Phase 2 batch inline_variables() - processes 32 solvers
```

### The Parallel Scoring Problem

When we try to parallelize sample scoring:

```python
# Phase 4 attempted:
demo_results = await asyncio.gather(*[
    score_demo_sample(i, s) for i, s in enumerate(demo_task)  # 5 samples
])

# Each score_demo_sample() calls:
async def score_demo_sample(i, sample):
    # This uses the executor!
    solve_timed_out, solve_result = await run_with_timeout(batt, ...)
    
    # batt() internally generates many candidates
    # Each candidate evaluation might also use run_with_timeout
```

### Thread Pool Exhaustion

```
Thread Pool (4 workers):
┌─────────────────────────────────────────────────────────┐
│ Worker 1: score_demo_sample(0) → batt() → waiting...   │
│ Worker 2: score_demo_sample(1) → batt() → waiting...   │
│ Worker 3: score_demo_sample(2) → batt() → waiting...   │
│ Worker 4: score_demo_sample(3) → batt() → waiting...   │
└─────────────────────────────────────────────────────────┘

Queued (waiting for workers):
- score_demo_sample(4) ← STUCK! Needs a worker
- score_demo_sample(5) ← STUCK! 

Result: demo[4] times out after 22+ seconds waiting for a thread!
```

## Why Sequential Worked

```python
# Sequential version:
for sample in demo_task:
    run_with_timeout(batt, ...)  # Uses 1 worker at a time
    # Worker freed after each sample
    # Next sample gets a worker immediately
```

### Thread Usage Pattern (Sequential)
```
Time →
Worker 1: demo[0] ████ → demo[1] ████ → demo[2] ████ → demo[3] ████ → demo[4] ████
Worker 2: idle
Worker 3: idle  
Worker 4: idle

Result: Each demo completes, no thread starvation
```

### Thread Usage Pattern (Parallel)
```
Time →
Worker 1: demo[0] ████████████████████████ (stuck)
Worker 2: demo[1] ████████████████████████ (stuck)
Worker 3: demo[2] ████████████████████████ (stuck)
Worker 4: demo[3] ████████████████████████ (stuck)
Queue:    demo[4] ⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳ (waiting 22s → timeout!)

Result: demo[4] never gets a worker, times out
```

## The Metrics Confirm This

```
Phase 4 Results:
  phase4_demo_parallel:  22.259s ← Wall-clock (waiting for threads)
  phase4_demo_cpu:       3.178s  ← Actual work (only 3s!)
  
Ratio: 22.259 / 3.178 = 7x overhead from thread starvation!
```

## Why Increasing Thread Pool Won't Help

### Proposed Solution
```python
_executor = ThreadPoolExecutor(max_workers=10)  # More threads?
```

### Why It Fails

**Problem 1: Nested Usage**
- 10 parallel samples → 10 threads occupied
- Each sample's batt() needs threads for internal operations
- Still get thread pool exhaustion!

**Problem 2: Resource Contention**
- 10+ parallel batt() calls compete for:
  - GPU resources (only 4 GPUs)
  - Memory (each loads data)
  - CPU (Python GIL limits)
- Creates even MORE contention and slowdown!

**Problem 3: System Limits**
- Too many threads causes OS overhead
- Context switching degrades performance
- Diminishing returns after 8-16 threads

## The Real Solution

### Option 1: Don't Use Global Executor for Samples ✅
```python
# Create separate executor for sample-level parallelism
sample_executor = ThreadPoolExecutor(max_workers=6)

# Use for demo/test samples
demo_results = await asyncio.gather(*[
    loop.run_in_executor(sample_executor, score_sample, ...)
])

# run_with_timeout() still uses global executor (4 workers)
# No conflict!
```

### Option 2: Sequential Samples, Parallel Operations ✅✅
```python
# Keep samples sequential (current working version)
for sample in demo_task:
    # But parallelize operations within each sample
    # This is what Phase 2 validation does successfully!
    result = await score_sample(sample)
```

### Option 3: Limit Parallel Samples ✅
```python
# Only run 2-3 samples in parallel at once
async def batch_score_samples(samples, batch_size=3):
    for i in range(0, len(samples), batch_size):
        batch = samples[i:i+batch_size]
        results = await asyncio.gather(*[
            score_sample(s) for s in batch
        ])
```

## Why Phase 2 Validation Worked

Phase 2 parallelizes **validation**, not scoring:

```python
# Phase 2: Parallel validation (WORKS!)
validated_data = await asyncio.gather(*[
    check_one_solver(d) for d in inlined_data  # 32 solvers
])

async def check_one_solver(data):
    # check_solver_speed() is lightweight
    # Doesn't use run_with_timeout heavily
    # No nested thread pool usage!
```

### Key Difference
- **Validation**: Lightweight, independent operations
- **Scoring**: Heavy batt() calls with nested thread pool usage

## The Fundamental Issue

**You cannot efficiently parallelize operations that themselves use the same thread pool internally.**

This is a classic **thread pool deadlock** scenario:
1. Parent operation takes all workers
2. Child operations need workers from same pool
3. Child waits for parent to free worker
4. Parent waits for child to complete
5. Deadlock or extreme slowdown!

## Recommended Approach

### Keep Current Architecture (Sequential Samples)
```python
# What works (Phase 1-3):
for demo_sample in demo_task:        # Sequential
    run_with_timeout(batt, ...)      # Uses executor
for test_sample in test_task:        # Sequential
    run_with_timeout(batt, ...)      # Uses executor

# What works (Phase 2):
asyncio.gather(*validation_tasks)    # Parallel
  └─ check_solver_speed()            # Doesn't use executor heavily
```

### Future Optimization Target

Instead of parallelizing samples, optimize **inside batt()**:
- Parallelize candidate evaluation
- Optimize DSL operations (GPU acceleration already done!)
- Cache repeated computations
- Early termination strategies

## Conclusion

The thread pool size of 4 is **correct for the current architecture**. Increasing it would:
1. ❌ Not solve the nested usage problem
2. ❌ Create more resource contention
3. ❌ Degrade performance further

The real issue is trying to parallelize at the wrong level (samples instead of operations within samples).

**Current Status**: Reverted to sequential sample scoring (Phases 1-3), which achieves 23% speedup (21.8s → 16.8s).

**Next Steps**: Accept current performance or investigate batt() internals for optimization opportunities.
