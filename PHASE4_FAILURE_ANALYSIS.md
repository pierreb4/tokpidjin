# Phase 4 Failure Analysis - Post-Mortem

## Date: October 12, 2025

## Summary
Phase 4 dual thread pool implementation **FAILED** on Kaggle with the same demo[4] timeout issue and worse performance (22.5s vs 16.8s baseline).

---

## What We Tried

### Hypothesis
- Thread pool exhaustion from nested usage was causing deadlock
- Solution: Separate high-level (sample scoring) and low-level (run_with_timeout) thread pools
- Expected: Eliminate deadlock, achieve 2-2.4x speedup

### Implementation
```python
# utils.py
_high_level_executor = ThreadPoolExecutor(max_workers=4)  # For sample scoring
_low_level_executor = ThreadPoolExecutor(max_workers=4)   # For run_with_timeout

# run_batt.py
async def score_demo_sample(i, sample):
    solve_result = await run_with_timeout(batt, ...)  # Uses low-level pool
    ...

demo_results = await asyncio.gather(*[
    score_demo_sample(i, sample) for i, sample in enumerate(demo_task)
])
```

---

## What Actually Happened

### Kaggle Test Results
```
✗ demo[4] STILL timed out
✗ Total time: 22.519s (34% SLOWER than 16.826s baseline!)
✗ Only 126 candidates scored (expected 149)
✗ Same failure mode as initial Phase 4 attempt
```

### Detailed Output
```
run_batt.py:414: demo[1] - 007bbfb7 - 32
run_batt.py:414: demo[2] - 007bbfb7 - 32
run_batt.py:414: demo[0] - 007bbfb7 - 32
run_batt.py:414: demo[3] - 007bbfb7 - 32
run_batt.py:408: -- 007bbfb7 - demo[4] timed out  ← FAILED!
run_batt.py:487: test[0] - 007bbfb7 - 32
run_batt.py:598: -- 007bbfb7 - 0 done - 126 candidates scored
```

---

## Root Cause Analysis

### Why Dual Thread Pools Didn't Help

**The Critical Misunderstanding:**

```
What we thought:
┌──────────────────────────────────────┐
│ High-Level Pool (4 workers)          │
│ ├─ demo[0] executing                 │
│ ├─ demo[1] executing                 │
│ ├─ demo[2] executing                 │
│ ├─ demo[3] executing                 │
│ └─ demo[4] waiting for worker ✓      │
└──────────────────────────────────────┘
         ↓ calls run_with_timeout
┌──────────────────────────────────────┐
│ Low-Level Pool (4 workers) SEPARATE  │
│ ├─ demo[0].batt() timeout wrapper    │
│ ├─ demo[1].batt() timeout wrapper    │
│ ├─ demo[2].batt() timeout wrapper    │
│ └─ demo[3].batt() timeout wrapper    │
└──────────────────────────────────────┘

Result: Should work! ✓
```

**What actually happens:**

```
Reality with asyncio.gather:
┌──────────────────────────────────────┐
│ Asyncio Event Loop                   │
│ ├─ demo[0] coroutine scheduled ✓     │
│ ├─ demo[1] coroutine scheduled ✓     │
│ ├─ demo[2] coroutine scheduled ✓     │
│ ├─ demo[3] coroutine scheduled ✓     │
│ └─ demo[4] coroutine scheduled ✓     │
└──────────────────────────────────────┘
   ALL 5 coroutines start immediately!
         ↓ all call run_with_timeout
         ↓ all request executor worker
┌──────────────────────────────────────┐
│ Low-Level Pool (4 workers) ONLY!     │
│ ├─ demo[0].batt() ← worker 1         │
│ ├─ demo[1].batt() ← worker 2         │
│ ├─ demo[2].batt() ← worker 3         │
│ ├─ demo[3].batt() ← worker 4         │
│ └─ demo[4].batt() ← NO WORKER! ✗     │
└──────────────────────────────────────┘

Result: DEADLOCK! demo[4] can't get worker ✗
```

### The Fundamental Problem

**`asyncio.gather()` does NOT use thread pools!**

- `asyncio.gather()` schedules coroutines on the event loop
- All 5 demo sample coroutines start **concurrently** (not limited to 4)
- Each coroutine calls `run_with_timeout()`
- `run_with_timeout()` uses `loop.run_in_executor(executor, func, *args)`
- **All 5 samples compete for the SAME 4 low-level workers!**
- 5th sample gets stuck → timeout after 5 seconds

**High-level pool was never used!** It sits idle while low-level pool is exhausted.

---

## Why This Approach Can't Work

### Architecture Mismatch

```
asyncio.gather:
- Schedules ALL coroutines immediately on event loop
- No limit on number of concurrent coroutines
- Coroutines are NOT threads or workers
- They're lightweight tasks on single-threaded event loop

Thread Pool Executors:
- Limited number of workers (threads)
- One task per worker at a time
- Blocking operations run in executor threads
- asyncio event loop delegates to executor via run_in_executor()

Problem:
- 5 coroutines (unlimited) → all call run_with_timeout
- run_with_timeout needs executor worker (limited to 4)
- 5 tasks > 4 workers → deadlock
```

### What We Would Need

To make parallel sample scoring work, we'd need:

**Option 1: Increase Low-Level Pool**
```python
_low_level_executor = ThreadPoolExecutor(max_workers=6)  # or 8
```
- Allows 5+ concurrent batt() calls
- But: More threads = more memory, potential contention
- Risk: macOS file descriptor limits, resource exhaustion

**Option 2: Limit Concurrent Samples**
```python
semaphore = asyncio.Semaphore(4)

async def score_demo_sample(i, sample):
    async with semaphore:  # Only 4 samples at a time
        result = await run_with_timeout(batt, ...)
```
- Limits concurrent samples to 4
- demo[4] waits for earlier sample to finish
- Problem: Overhead from semaphore, no guaranteed speedup

**Option 3: ThreadPoolExecutor Directly**
```python
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(batt_sync, ...) for sample in demo_task]
    results = [f.result(timeout=5) for f in futures]
```
- No asyncio.gather (use thread pool directly)
- Problem: Loses async/await benefits, harder timeout handling

**Option 4: Restructure at Solver Level**
- Instead of parallelizing samples, parallelize solvers within batt()
- Each sample still sequential, but solvers run in parallel
- Problem: Major refactoring, different bottleneck

---

## Performance Impact

### Timing Breakdown (22.519s total)

```
Metric                     | Phase 3 Seq | Phase 4 Dual | Change
---------------------------|-------------|--------------|--------
Total time                 | 16.826s     | 22.519s      | +34% ✗
check_batt scoring         | 15.494s     | 21.236s      | +37% ✗
Demo sample scoring        | ~12s        | ~18s (est)   | +50% ✗
Test sample scoring        | ~3.5s       | ~3s          | -14% ✓
Validation (Phase 2)       | 0.366s      | 0.362s       | -1% ≈
Filter (Phase 1)           | 0.015s      | 0.013s       | -13% ✓
```

**Why SLOWER?**
1. **Timeout penalty**: demo[4] waits full 5s before timing out
2. **Overhead**: asyncio.gather + coroutine scheduling + aggregation
3. **No benefit**: Parallel scheduling doesn't help when workers are limited
4. **Wrong candidate count**: 126 instead of 149 (28 missing!)

---

## Lessons Learned

### 1. asyncio.gather ≠ Thread Pool Parallelism

**Key Insight:**
- `asyncio.gather()` provides **concurrency** (overlapping I/O waits)
- Not **parallelism** (simultaneous CPU work)
- Still limited by underlying executor workers

**When it works:**
- Phase 2 validation: Many quick tasks (0.362s total, 19.4x speedup)
- I/O-bound operations with waiting periods
- Tasks that don't block on limited resources

**When it fails:**
- Phase 4 sample scoring: Few long tasks competing for same workers
- CPU-bound operations requiring executor threads
- More tasks than available workers

### 2. Dual Thread Pools Require Different Architecture

**What we learned:**
- Can't just add second pool and expect asyncio.gather to use it
- Need explicit routing: which operations use which pool
- High-level pool needs to actually EXECUTE the coroutines, not just exist

**What would work:**
```python
# Execute coroutines IN high-level pool (not just schedule on event loop)
high_level = get_high_level_executor()
futures = [high_level.submit(run_sync_version, sample) for sample in demo_task]
results = [f.result(timeout=5) for f in futures]
```

But this loses async/await, needs synchronous wrappers, different trade-offs.

### 3. Know Your Bottleneck Type

**CPU-bound vs I/O-bound:**

Phase 2 (Validation): **I/O-bound**
- Quick syntax checks
- Lots of waiting for small operations
- asyncio.gather perfect fit → 19.4x speedup! ✓

Phase 4 (Sample Scoring): **CPU-bound**
- Long-running batt() execution (2-3s per sample)
- Heavy computation, not I/O waiting
- asyncio.gather wrong tool → 34% slower! ✗

**Rule of thumb:**
- Many quick tasks → asyncio.gather works
- Few long tasks → thread pool parallelism needed
- Need workers ≥ concurrent tasks

### 4. Thread Pool Sizing Matters

**Conservative (4 workers):**
- ✓ Safe: No resource exhaustion
- ✓ Proven: Phase 1-3 stable at 16.8s
- ✗ Limited: Can't run 5 samples in parallel

**Aggressive (6-8 workers):**
- ✓ Parallelism: Could handle 5+ samples
- ✗ Risk: Memory, file descriptors, contention
- ? Unknown: Would it actually be faster?

**Optimal?**
- Need to test with increased worker count
- But: May not be worth the risk/complexity
- Current 16.8s is 23% better than baseline (21.8s)

---

## Decision: REVERT to Phase 1-3

### Why Revert?

1. **Phase 3 is stable**: 16.826s consistently
2. **Phase 4 is broken**: 22.519s with timeouts and wrong results
3. **No clear path forward**: Would need major refactoring
4. **Diminishing returns**: 16.8s → 7-8s target might not be achievable
5. **Current is good enough**: 23% speedup over baseline is solid win

### What We Keep

**Phase 1 (Filter + Batch):**
- ✓ Body-hash deduplication: 149→32 candidates
- ✓ Batch inline with ThreadPoolExecutor (max_workers=4)
- ✓ 22.5% speedup: 21.8s → 16.9s

**Phase 2 (Parallel Validation):**
- ✓ asyncio.gather for validation: 19.4x faster
- ✓ 7.096s CPU → 0.366s wall-clock
- ✓ Works perfectly for I/O-bound quick tasks

**Phase 3 (Profiling):**
- ✓ Identified scoring bottleneck (92% of time)
- ✓ Confirmed file ops are fast (0.1%)
- ✓ Validated optimization priorities

**Dual Thread Pools (Keep in utils.py):**
- Keep implementation for future use
- Might help with other operations
- Low risk to leave in place

### What We Abandon

**Phase 4 (Parallel Sample Scoring):**
- ✗ asyncio.gather approach doesn't work
- ✗ Dual pools don't help without proper architecture
- ✗ Would need major refactoring or increased worker count
- ✗ Risk/reward not favorable

---

## Final Results

### Overall Performance

```
Baseline:   21.788s (100%)
Phase 1-2:  16.826s (77%)  ← STABLE ✓
Phase 4:    22.519s (103%) ← FAILED ✗

Net improvement: 23% faster (21.8s → 16.8s)
```

### Breakdown

```
Operation              | Original | Optimized | Speedup
-----------------------|----------|-----------|--------
Filter candidates      | 0.015s   | 0.015s    | 1x
Inline variables       | 3.645s   | 0.609s    | 6x ✓
Validate solvers       | 7.096s   | 0.362s    | 19.4x ✓
Sample scoring         | ~15s     | ~15s      | 1x
File operations        | 0.015s   | 0.014s    | 1x
```

### Remaining Bottleneck

**Sample Scoring: 15.494s (92% of total time)**

- 5 demo samples + 1 test sample
- Each calls batt() which generates ~32 candidates
- Each candidate runs solver
- **Cannot parallelize** with current architecture

**Options for future:**
1. Accept current performance (16.8s is good!)
2. Optimize batt() internals (solver execution)
3. GPU acceleration for grid operations
4. Smarter candidate filtering (fewer solvers to test)
5. Caching/memoization of repeated work

---

## Conclusion

Phase 4 dual thread pool approach **failed** because:

1. **asyncio.gather doesn't use thread pools** - schedules all coroutines immediately
2. **All coroutines compete for same executor** - low-level pool exhausted by 5 samples
3. **High-level pool never used** - architecture doesn't route work correctly
4. **Wrong tool for the job** - CPU-bound long tasks ≠ I/O-bound quick tasks

**The dual thread pool concept is sound**, but requires different implementation:
- Use thread pool directly (not asyncio.gather)
- Or increase low-level workers to 6-8
- Or restructure to parallelize at different level

**For now, reverting to stable Phase 1-3** (16.8s, 23% speedup):
- ✓ Proven performance
- ✓ No timeouts or errors
- ✓ Solid improvement over baseline
- ✓ Low risk, high reliability

**Key lesson**: Understand your parallelism model (asyncio vs threads vs multiprocessing) before implementing complex optimizations.

---

## Acknowledgments

User's critical observations led to understanding the problem:
1. "demo task didn't timeout" in sequential → identified NEW timeout
2. "4 threads" limit question → investigated thread pool architecture
3. "2 separate thread pools" suggestion → explored dual pool approach

Even though Phase 4 failed, the investigation was valuable for understanding asyncio/threading interaction and knowing when NOT to parallelize.

---

*Last Updated: October 12, 2025*
*Status: Phase 4 FAILED and REVERTED*
*Final: Phase 1-3 STABLE at 16.826s (23% speedup)*
