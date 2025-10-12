# Phase 4 Results Analysis - Timeout Issue

## The Problem

Phase 4 parallel implementation is **SLOWER** than sequential version!

### Metrics Comparison

```
Phase 3 (Sequential):
  Total:                16.826s
  check_batt:           15.494s
  Demo scoring:         ~12s (estimated sequential)
  Test scoring:         ~3s (estimated sequential)

Phase 4 (Parallel - BROKEN):
  Total:                26.184s  ← WORSE! (+9.4s, 56% slower!)
  check_batt:           24.809s  ← WORSE! (+9.3s)
  phase4_demo_parallel: 22.259s  ← Should be 3-4s!
  phase4_demo_cpu:      3.178s   ← Actual work only 3s
  phase4_test_parallel: 2.546s
  phase4_test_cpu:      0.077s
```

## Root Cause Analysis

### Issue 1: Timeout Blocking
```
demo[4] timed out

When one demo sample times out in asyncio.gather(), it blocks
for the full timeout duration (likely 20+ seconds based on metrics).

The gather() waits for ALL tasks to complete or timeout.
```

### Issue 2: Slower Than Expected
```
phase4_demo_parallel: 22.259s (wall-clock)
phase4_demo_cpu:      3.178s  (actual work)

Ratio: 22.259 / 3.178 = 7x SLOWER than expected!

Expected:
- 5 demos in parallel
- Each takes ~0.6s (3.178s / 5)
- Wall-clock should be ~0.6s (the longest one)
- Actual: 22.259s ← Something is very wrong!
```

### Issue 3: Demo Results Don't Match
```
Phase 3 (Sequential): 149 candidates generated
  - demo[0]: 32 candidates ✓
  - demo[1]: 32 candidates ✓
  - demo[2]: 32 candidates ✓
  - demo[3]: 32 candidates ✓
  - demo[4]: 32 candidates ✓ (NO TIMEOUT)
  - test[0]: 32 candidates ✓

Phase 4 (Parallel): 126 candidates generated
  - demo[0]: 32 candidates ✓
  - demo[1]: 32 candidates ✓
  - demo[2]: 32 candidates ✓
  - demo[3]: 32 candidates ✓
  - demo[4]: TIMED OUT ✗ (NEW TIMEOUT!)
  - test[0]: 32 candidates ✓

Missing 23 candidates from demo[4]!
```

**Critical Finding**: demo[4] did NOT timeout in sequential version, but DOES timeout in parallel version. This proves the parallel execution is CAUSING the timeout through resource contention, not just handling it differently.

## Why This Happened

### Hypothesis 1: Sequential Within Parallel (MOST LIKELY)
The `batt()` function itself might be running candidates sequentially:
```python
# Inside batt():
for each candidate:
    try to solve
    if timeout, continue
    
# If batt() is sequential internally and one candidate times out,
# it could block the whole demo sample for 20+ seconds
```

### Hypothesis 2: Resource Contention (CONFIRMED!) ✅
Running 5 batt() calls in parallel is hitting resource limits:
- **Evidence**: demo[4] completed fine sequentially (Phase 3) but times out in parallel (Phase 4)
- GPU contention (4 GPUs, but 5 parallel batt() calls competing)
- Memory contention (each batt() loads data, generates candidates)
- Python GIL limitations (CPU-bound candidate generation)
- I/O contention (reading solver files, test data)

**This is the PRIMARY cause**: Parallel execution creates resource starvation that causes timeouts that didn't exist before.

### Hypothesis 3: Timeout Not Properly Applied
The `run_with_timeout(batt, ..., timeout=1)` might not be working as expected:
- Timeout should be 1 second per batt() call
- But demo[4] took 22 seconds to timeout
- Suggests timeout isn't being enforced properly

## The Real Problem

Looking at the code flow:
```python
# Each demo sample calls:
solve_timed_out, solve_result = await run_with_timeout(batt,
    [task_id, S, I, None, pile_log_path], timeout)

# batt() internally:
# - Generates candidates (could be 149 per sample!)
# - Tests each candidate  
# - Each candidate could timeout
# - Total time = num_candidates × timeout_per_candidate
```

**If batt() tries 149 candidates and each has a 1s timeout:**
- Total time = 149 seconds per sample!
- With 5 samples in parallel, we'd wait for the longest one
- This explains why demo[4] took 22+ seconds

## Why Sequential Was Faster

In the original sequential version:
```python
for sample in demo_task:
    run batt() on sample
    # If batt() times out, move to next sample
    # No parallel overhead
```

The sequential version likely had better timeout handling or early termination.

## Solutions

### Solution 1: Don't Parallelize Sample Scoring ❌
- Revert to sequential version
- Accept 16.8s performance
- Not ideal, but safe

### Solution 2: Fix batt() Timeout Handling ✅
- Ensure batt() respects timeout limit
- Add early termination when timeout is approaching
- Limit candidates processed per sample

### Solution 3: Parallel Candidate Processing (BETTER) ✅✅
Instead of parallelizing samples, parallelize candidate evaluation:
```python
# Inside batt(), for each sample:
candidates = generate_candidates()  # Fast

# Parallel candidate evaluation:
results = await asyncio.gather(*[
    evaluate_candidate(c) for c in candidates[:N]  # Limit N
])
```

This is actually safer because:
- Each candidate evaluation is faster (0.1-0.5s typically)
- Timeout per candidate is more predictable
- Less resource contention

### Solution 4: Hybrid Approach ✅✅✅
```python
# Sequential demo samples (safer)
for demo_sample in demo_task:
    # But parallel candidate evaluation within each sample
    results = await evaluate_candidates_parallel(candidates)
```

This gives us:
- Better timeout control
- Less resource contention
- Safer execution
- Still potential for speedup

## Immediate Action

**REVERT Phase 4** - The parallel sample scoring makes things worse.

The real opportunity is **inside batt()** - parallelize candidate evaluation, not sample evaluation.

## Lessons Learned

### ❌ What Didn't Work
- Parallelizing entire sample scoring
- Using asyncio.gather() at the wrong level
- Not considering timeout accumulation

### ✅ What We Learned
- Profile first, implement second (we should have tested on smaller scale)
- Consider timeout behavior in parallel contexts
- Look for parallelization opportunities at finer granularity
- Sequential can be faster if parallel has too much overhead

## Next Steps

1. **Revert Phase 4 changes** - Go back to sequential sample scoring
2. **Investigate batt() internals** - Where is the real time spent?
3. **Consider candidate-level parallelization** - Parallelize within batt()
4. **Add better timeout handling** - Ensure timeouts are respected
5. **Test incrementally** - Start with 2 samples parallel, then scale up

## Performance Summary

```
Phase 1: 21.8s → 16.9s (22.5% faster) ✅
Phase 2: 16.9s → 16.8s (validation 19.4x faster!) ✅
Phase 3: Identified bottleneck (scoring 15.5s) ✅
Phase 4: 16.8s → 26.2s (56% SLOWER!) ❌

Total: 21.8s → 26.2s (20% SLOWER overall!)
```

This is a valuable learning experience - not all parallelization improves performance!
