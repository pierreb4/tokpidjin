# Phase 4: Parallel Scoring Implementation

## Overview

Phase 4 parallelizes the scoring loop in `check_batt` that runs `batt()` on demo and test samples. This addresses the real bottleneck identified in Phase 3.

## The Bottleneck (Phase 3 Discovery)

**Phase 3 profiling revealed:**
```
run_batt.check_batt:            15.494s  (92% of total time!)
  - Runs batt() on 5 demo samples sequentially
  - Runs batt() on 1 test sample sequentially
  - Each sample takes ~2-3s
  - Total: ~15s sequential execution
```

**Phase 3b and Phase 4 (differs) are NOT bottlenecks:**
- Phase 3b: 0.015s (solver file ops)
- Phase 4 (differs): 0.353s (differ processing)

## Phase 4 Strategy

Apply the same parallel approach that worked brilliantly in Phase 2:

### Phase 2 Success (Validation)
```python
# Before: Sequential validation (~7s)
for solver in solvers:
    validate(solver)  # 0.22s each

# After: Parallel validation (0.37s wall-clock)
results = await asyncio.gather(*[
    validate(solver) for solver in solvers
])

# Result: 19.4x speedup!
```

### Phase 4 Implementation (Scoring)
```python
# Before: Sequential scoring (~15s)
for sample in demo_samples:
    score_sample(sample)  # 2-3s each

for sample in test_samples:
    score_sample(sample)  # 2-3s each

# After: Parallel scoring (4-8s wall-clock expected)
demo_results = await asyncio.gather(*[
    score_demo_sample(i, sample) 
    for i, sample in enumerate(demo_samples)
])

test_results = await asyncio.gather(*[
    score_test_sample(i, sample)
    for i, sample in enumerate(test_samples)
])

# Expected: 2-4x speedup on scoring phase
```

## Implementation Details

### Demo Sample Parallelization

```python
async def score_demo_sample(i, sample):
    """Score a single demo sample in parallel"""
    I = sample['input']
    O = sample['output']
    sample_start = timer() if prof is not None else None
    
    # Run batt() on this sample
    solve_timed_out, solve_result = await run_with_timeout(batt,
        [task_id, S, I, None, pile_log_path], timeout)
    
    sample_time = timer() - sample_start if prof is not None else 0
    
    if solve_timed_out and DO_PRINT:
        print_l(f'-- {task_id} - demo[{i}] timed out')

    # Collect results for aggregation
    demo_o = set()
    demo_s = {}
    demo_o_updates = []
    demo_d_updates = []
    
    if solve_result is not None:
        o_result, _ = solve_result
        demo_o = o_result

        print_l(f"demo[{i}] - {task_id} - {len(o_result)}") if DO_PRINT else None

        for t_n, evo, o_solver_id, okt in o_result:
            # Compare candidate C with expected output O
            C = okt
            if match := C == O:
                print_l(f'- {o_solver_id = } - {match = }')
            demo_o_updates.append((o_solver_id, match))

            # Run differ scoring
            diff_timed_out, diff_result = await run_with_timeout(batt,
                [task_id, S, I, O, pile_log_path], timeout)

            if diff_result is not None:
                _, s_result = diff_result
                demo_s[i] = s_result

                for s_item in s_result:
                    demo_d_updates.append((o_solver_id, s_item))
    
    # Return structured result for aggregation
    return {
        'index': i,
        'type': 'demo',
        'o_result': demo_o,
        's_result': demo_s,
        'o_updates': demo_o_updates,
        'd_updates': demo_d_updates,
        'time': sample_time
    }
```

### Parallel Execution

```python
# Score all demo samples in parallel
import asyncio
demo_results = await asyncio.gather(*[
    score_demo_sample(i, sample) for i, sample in enumerate(demo_task)
])

# Aggregate results (maintain original data structure)
for result in demo_results:
    i = result['index']
    o['demo'][i] = result['o_result']
    all_o = all_o.union(result['o_result'])
    for o_solver_id, match in result['o_updates']:
        o_score.update(o_solver_id, match)
    for o_solver_id, s_item in result['d_updates']:
        d_score.update(o_solver_id, s_item)
    if result['s_result']:
        s['demo'].update(result['s_result'])
```

### Test Sample Parallelization

```python
async def score_test_sample(i, sample):
    """Score a single test sample in parallel"""
    # Similar structure to score_demo_sample
    # Key difference: uses C (candidate output) for differ scoring
    # instead of O (known correct output)
    
    diff_timed_out, diff_result = await run_with_timeout(batt,
        [task_id, S, I, C, pile_log_path], timeout)  # Note: C not O
```

### Profiling Instrumentation

```python
if prof is not None:
    phase4_demo_start = timer()

# ... parallel execution ...

if prof is not None:
    phase4_demo_time = timer() - phase4_demo_start  # Wall-clock
    phase4_demo_cpu = sum(r['time'] for r in demo_results)  # Total CPU
    prof['run_batt.phase4_demo_parallel'] = phase4_demo_time
    prof['run_batt.phase4_demo_cpu'] = phase4_demo_cpu
```

## Key Design Decisions

### 1. Separate Demo and Test Functions
- Demo samples use known output O for differ scoring
- Test samples use candidate output C for differ scoring
- This maintains the existing semantic difference

### 2. Result Aggregation Pattern
- Each parallel task returns a structured dictionary
- Aggregation phase updates shared data structures
- Maintains exact same final state as sequential version

### 3. Profiling Strategy
- Track both wall-clock time (actual speedup)
- Track total CPU time (sum of parallel tasks)
- Enables calculation of speedup ratio

### 4. Error Handling
- Timeout handling preserved (async run_with_timeout)
- Print statements preserved for debugging
- Result validation maintained

## Expected Performance

### Current (Phase 3)
```
Total time:              16.826s
  check_batt (scoring):  15.494s  (92%)
    - 5 demo samples:    ~12s sequential
    - 1 test sample:     ~3s sequential
```

### After Phase 4 (Expected)
```
Total time:              6-10s
  check_batt (scoring):  4-8s  (60-80%)
    - 5 demo samples:    ~3-4s parallel (3-4x speedup)
    - 1 test sample:     ~1s (single sample, no speedup)
  
Speedup calculation:
  Demo: 12s → 3-4s (3-4x on 5 parallel samples)
  Test: 3s → 1s (limited by single sample)
  Total scoring: 15s → 4-5s (3-4x overall)
```

### Overall Journey
```
Original:    21.788s
Phase 1:     16.884s  (22.5% faster)
Phase 2:     16.826s  (validation 19.4x faster)
Phase 4:     6-10s    (2.2-3.6x faster overall!)
```

## Testing Strategy

### Validation Checklist
1. **Correctness**: Results must match sequential version exactly
2. **Performance**: Measure actual speedup on Kaggle L4x4
3. **Profiling**: Verify new metrics show expected times
4. **Edge cases**: Test with timeouts, empty results

### Test Command
```bash
python run_batt.py --timing -i 007bbfb7 -b tmp_batt_onerun_run
```

### Expected Metrics
```
New profiling output:
  run_batt.phase4_demo_parallel:  3-4s    (wall-clock)
  run_batt.phase4_demo_cpu:       12-15s  (total CPU)
  run_batt.phase4_test_parallel:  1-2s    (wall-clock)
  run_batt.phase4_test_cpu:       3s      (total CPU)
  
Speedup ratios:
  Demo: phase4_demo_cpu / phase4_demo_parallel = 3-4x
  Test: phase4_test_cpu / phase4_test_parallel = 1-2x (limited by 1 sample)
```

## Potential Issues and Solutions

### Issue 1: Less Speedup Than Expected
**Symptom**: Only 1.5-2x speedup instead of 3-4x  
**Possible causes**:
- Shared resource contention (I/O, memory)
- GIL limitations (Python global interpreter lock)
- Overhead from asyncio.gather

**Solutions**:
- Profile individual sample times
- Check if CPU-bound vs I/O-bound
- Consider ProcessPoolExecutor if GIL is limiting

### Issue 2: Incorrect Results
**Symptom**: Different solver counts or scores  
**Possible causes**:
- Race condition in shared data structures
- Incorrect result aggregation order

**Solutions**:
- Verify o_score, d_score, s_score updates are order-independent
- Add assertions to check result consistency
- Compare output files between sequential and parallel versions

### Issue 3: Memory Issues
**Symptom**: Out of memory errors  
**Possible causes**:
- All 6 samples loading data simultaneously
- Large intermediate results

**Solutions**:
- Batch scoring (e.g., 3 samples at a time)
- Monitor memory usage during execution
- Add memory profiling

## Success Criteria

✅ **Functional Requirements:**
- Same number of candidates generated
- Same solver scores (o_score)
- Same differ scores (d_score, s_score)
- Same files created in solver_md5, differ_md5

✅ **Performance Requirements:**
- Total time: 16.8s → 6-10s (target 2.2-3.6x speedup)
- Scoring time: 15.5s → 4-8s (target 2-4x speedup)
- New profiling metrics show expected speedups

✅ **Code Quality:**
- Syntax compiles correctly
- No breaking changes to existing functionality
- Profiling infrastructure maintained

## Files Modified

- **run_batt.py**: 
  - Lines ~390-450: Added `score_demo_sample()` function
  - Lines ~450-520: Added `score_test_sample()` function
  - Replaced sequential loops with `asyncio.gather()`
  - Added Phase 4 profiling instrumentation

## Next Steps

1. **Test on Kaggle** (5 minutes)
   - Upload updated run_batt.py
   - Run with --timing flag
   - Check correctness and performance

2. **Analyze Results** (5 minutes)
   - Compare solver counts (should be same)
   - Check new profiling metrics
   - Calculate actual speedup achieved

3. **Iterate if Needed** (30-60 minutes)
   - If speedup < 2x: investigate bottlenecks
   - If incorrect results: fix aggregation logic
   - If memory issues: add batching

4. **Document Final Results** (15 minutes)
   - Update all optimization documents
   - Create final performance summary
   - Document complete optimization journey

## Status

✅ **Implementation**: Complete  
✅ **Syntax check**: Passed  
⏳ **Kaggle testing**: Pending  
⏳ **Performance validation**: Pending  
⏳ **Documentation**: Pending  

## Context

This is Phase 4 of a multi-phase optimization journey:

- **Phase 1**: Filtering + batching (21.8s → 16.9s) ✅
- **Phase 2**: Parallel validation (19.4x speedup on validation) ✅
- **Phase 3**: Identified real bottleneck (scoring: 15.5s) ✅
- **Phase 4**: Parallelize scoring (16.8s → 6-10s target) 🔄
