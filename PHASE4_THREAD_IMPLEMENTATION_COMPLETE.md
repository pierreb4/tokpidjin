# Phase 4 Alternative: Thread-Based Parallelism - IMPLEMENTED ✅

## Status: Ready for Kaggle Testing

**Date**: October 12, 2025  
**Implementation**: Complete  
**Expected Performance**: 16.826s → 7-8s (2-2.5x speedup)

---

## What We Implemented

### 1. Thread-Based Timeout Function ✅
**File**: `utils.py`

```python
def call_with_timeout(func, args, timeout=5):
    """
    Call a function with a timeout using threads (no asyncio).
    Returns (timed_out: bool, result: Any)
    """
    result_queue = Queue()
    exception_queue = Queue()
    
    def worker():
        try:
            result = func(*args)
            result_queue.put(result)
        except Exception as e:
            exception_queue.put(e)
    
    thread = threading.Thread(target=worker)
    thread.daemon = True
    thread.start()
    thread.join(timeout=timeout)
    
    if thread.is_alive():
        return True, None  # Timed out
    
    # Check for exception
    try:
        exception = exception_queue.get_nowait()
        return True, None
    except Empty:
        pass
    
    # Get result
    try:
        result = result_queue.get_nowait()
        return False, result
    except Empty:
        return True, None
```

**Testing**: ✅ Tested locally with fast/slow functions - works perfectly!

### 2. Parallel Demo Sample Scoring ✅
**File**: `run_batt.py`

```python
def score_demo_sample(args):
    """Score a single demo sample (for parallel execution)"""
    i, sample, task_id, S, pile_log_path, timeout, DO_PRINT = args
    
    I = sample['input']
    O = sample['output']
    
    # Call batt with thread-based timeout (no asyncio!)
    solve_timed_out, solve_result = call_with_timeout(batt,
        [task_id, S, I, None, pile_log_path], timeout)
    
    if solve_timed_out and DO_PRINT:
        print_l(f'-- {task_id} - demo[{i}] timed out')
    
    demo_o = []
    demo_s = []
    
    if solve_result is not None:
        demo_o, _ = solve_result
        if DO_PRINT:
            print_l(f"demo[{i}] - {task_id} - {len(demo_o)}")
        
        # Score outputs and run diff
        for t_n, evo, o_solver_id, okt in demo_o:
            C = okt
            match = C == O
            if match and DO_PRINT:
                print_l(f'- {o_solver_id = } - {match = }')
            
            # Run diff to get solver-level scores
            diff_timed_out, diff_result = call_with_timeout(batt,
                [task_id, S, I, O, pile_log_path], timeout)
            
            if diff_result is not None:
                _, demo_s_result = diff_result
                demo_s.extend(demo_s_result)
    
    return {
        'index': i,
        'outputs': demo_o,
        'solver_scores': demo_s,
        'timed_out': solve_timed_out
    }
```

### 3. ThreadPoolExecutor with 5 Workers ✅
**File**: `run_batt.py` in `check_batt()`

```python
def check_batt(total_data, task_i, task_id, d_score, start_time, pile_log_path, timeout=1, prof=None):
    # ... setup ...
    
    # Phase 4 Alternative: Parallel demo scoring with ThreadPoolExecutor
    # Uses call_with_timeout (pure threading) instead of asyncio.gather
    prof_start = timer() if prof is not None else None
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        # Prepare arguments for each demo sample
        demo_args = [
            (i, sample, task_id, S, pile_log_path, timeout, DO_PRINT)
            for i, sample in enumerate(demo_task)
        ]
        
        # Submit all demo samples for parallel execution
        demo_futures = {executor.submit(score_demo_sample, args): args[0] 
                       for args in demo_args}
        
        # Collect results as they complete
        demo_results = [None] * len(demo_task)
        for future in as_completed(demo_futures):
            try:
                result = future.result(timeout=timeout + 1)
                demo_results[result['index']] = result
            except Exception as e:
                sample_idx = demo_futures[future]
                if DO_PRINT:
                    print_l(f"-- {task_id} - demo[{sample_idx}] failed: {e}")
                demo_results[sample_idx] = {
                    'index': sample_idx,
                    'outputs': [],
                    'solver_scores': [],
                    'timed_out': True
                }
    
    if prof is not None:
        prof['batt.demo.parallel'] = timer() - prof_start
    
    # Aggregate demo results
    for result in demo_results:
        if result is None:
            continue
        
        i = result['index']
        o['demo'][i] = result['outputs']
        s['demo'][i] = result['solver_scores']
        all_o = all_o.union(result['outputs'])
        
        # Update scores
        O = demo_task[i]['output']
        for t_n, evo, o_solver_id, okt in result['outputs']:
            C = okt
            match = C == O
            o_score.update(o_solver_id, match)
        
        # Update solver scores
        for s_item in result['solver_scores']:
            if result['outputs']:
                o_solver_id = result['outputs'][0][2]
                d_score.update(o_solver_id, s_item)
```

### 4. Test Sample Scoring Updated ✅
**File**: `run_batt.py` in `check_batt()`

Replaced `await run_with_timeout()` with `call_with_timeout()`:

```python
# Test sample scoring (sequential - typically only 1 test sample)
for i, sample in enumerate(test_task):
    I = sample['input']
    O = sample['output']
    
    solve_timed_out, solve_result = call_with_timeout(batt,
        [task_id, S, I, None, pile_log_path], timeout)
    
    # ... rest of scoring logic (unchanged) ...
```

---

## Architecture Changes

### Before (Sequential with asyncio)
```
check_batt (async)
  ├─ for each demo sample (sequential):
  │  ├─ await run_with_timeout(batt, ...)
  │  │  └─ asyncio.wait_for + loop.run_in_executor
  │  └─ await run_with_timeout(batt, ...) [diff]
  └─ for each test sample (sequential):
     └─ await run_with_timeout(batt, ...)

Total time: ~12s for 5 demo samples (sequential)
```

### After (Parallel with ThreadPoolExecutor)
```
check_batt (sync)
  ├─ ThreadPoolExecutor(max_workers=5):
  │  ├─ Thread 1: score_demo_sample(demo[0])
  │  │  ├─ call_with_timeout(batt, ...) → separate thread
  │  │  └─ call_with_timeout(batt, ...) [diff] → separate thread
  │  ├─ Thread 2: score_demo_sample(demo[1])
  │  ├─ Thread 3: score_demo_sample(demo[2])
  │  ├─ Thread 4: score_demo_sample(demo[3])
  │  └─ Thread 5: score_demo_sample(demo[4]) ✓ NO DEADLOCK!
  └─ for each test sample (sequential):
     └─ call_with_timeout(batt, ...)

Expected time: ~3s for 5 demo samples (4x speedup!)
```

---

## Key Differences from Failed Attempts

### Phase 4 Attempt 1 (asyncio.gather) ❌
```python
async def score_demo_sample(i, sample):
    result = await run_with_timeout(batt, ...)
    
demo_results = await asyncio.gather(*[
    score_demo_sample(i, s) for i, s in enumerate(demo_task)
])
```

**Problem**: 
- asyncio.gather schedules 5 coroutines immediately
- All 5 call run_with_timeout → executor (4 workers)
- 5 > 4 → deadlock!

### Phase 4 Attempt 2 (Dual pools with asyncio.gather) ❌
```python
_high_level_executor = ThreadPoolExecutor(max_workers=4)
_low_level_executor = ThreadPoolExecutor(max_workers=4)

async def run_with_timeout(func, args, timeout):
    executor = get_low_level_executor()  # Uses low-level
    ...

demo_results = await asyncio.gather(*[...])  # Still uses gather!
```

**Problem**:
- High-level pool never used
- asyncio.gather still schedules all coroutines
- Still compete for low-level executor
- Same deadlock!

### Phase 4 Alternative (Direct ThreadPoolExecutor) ✅
```python
def score_demo_sample(args):
    # Synchronous function (no async/await)
    result = call_with_timeout(batt, ...)  # Pure threading
    return result

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(score_demo_sample, args) for args in demo_args]
    results = [f.result() for f in as_completed(futures)]
```

**Solution**:
- No asyncio.gather (uses ThreadPoolExecutor directly!)
- 5 workers for 5 samples (perfect match)
- call_with_timeout uses independent threads
- No executor conflicts!

---

## Expected Performance

### Current Baseline (Phase 1-3)
```
Total: 16.826s
├─ Demo scoring: ~12.0s (71%) ← TARGET FOR OPTIMIZATION
│  ├─ demo[0]: 2.4s ┐
│  ├─ demo[1]: 2.4s │ Sequential
│  ├─ demo[2]: 2.4s │ (one after another)
│  ├─ demo[3]: 2.4s │
│  └─ demo[4]: 2.4s ┘
├─ Test scoring: ~3.5s (21%)
└─ Other: ~1.3s (8%)
```

### Expected with Phase 4 Alternative
```
Total: 7-8s (2.1-2.4x faster!) 🚀
├─ Demo scoring: ~3.0s (38%) ← 4x FASTER!
│  ├─ demo[0]: 2.4s ┐
│  ├─ demo[1]: 2.4s │
│  ├─ demo[2]: 2.4s │ All run in parallel
│  ├─ demo[3]: 2.4s │ Max time = slowest sample
│  └─ demo[4]: 2.4s ┘ ~2.4-3.0s total
├─ Test scoring: ~3.5s (44%)
└─ Other: ~1.3s (18%)
```

**Why not 5x speedup?**
- 5 samples on 5 workers, but samples have varying execution times
- Overhead from ThreadPoolExecutor and result aggregation
- Test scoring still sequential (only 1 test sample)
- Expected practical speedup: 3-4x for demo scoring

---

## Testing Plan

### Step 1: Local Smoke Test
```bash
cd /Users/pierre/dsl/tokpidjin
python run_batt.py --timing -i 007bbfb7 -b tmp_batt_onerun_run
```

**Expected**:
- ✓ No Python errors
- ✓ Code runs to completion
- ✓ Results look reasonable

### Step 2: Kaggle Performance Test
Upload code to Kaggle L4x4 and run:
```bash
python run_batt.py --timing -i 007bbfb7 -b tmp_batt_onerun_run
```

**Look for**:
1. **No timeouts**: All 5 demo samples complete (especially demo[4]!)
2. **Total time**: 7-10s (vs 16.8s baseline)
3. **Demo scoring**: 3-5s (vs 12s sequential)
4. **Candidate count**: 149 (not 126)
5. **Correctness**: Same results as Phase 3

### Step 3: Validation
- Compare output files with Phase 3
- Check timing breakdown: `prof['batt.demo.parallel']`
- Verify no new errors in logs

---

## Success Criteria

### Must Have ✅
- [x] Code compiles without errors
- [ ] ⏳ No new timeouts (especially demo[4])
- [ ] ⏳ Total time: 7-10s (2-2.5x faster)
- [ ] ⏳ Demo scoring: 3-5s (3-4x faster)
- [ ] ⏳ Same correctness: 149 candidates, matching results

### Nice to Have
- [ ] ⏳ Profiling shows parallel speedup
- [ ] ⏳ Memory usage acceptable (<80% VRAM)
- [ ] ⏳ No resource contention issues

---

## Why This Will Work

### 1. No asyncio/executor Mismatch
- **Before**: asyncio.gather → coroutines → run_with_timeout → executor (conflict!)
- **After**: ThreadPoolExecutor → threads → call_with_timeout (independent!)

### 2. Explicit Worker Control
```python
ThreadPoolExecutor(max_workers=5)  # Explicit: 5 workers for 5 samples
├─ Worker 1: demo[0]
├─ Worker 2: demo[1]
├─ Worker 3: demo[2]
├─ Worker 4: demo[3]
└─ Worker 5: demo[4]  ← Gets its own worker! No deadlock!
```

### 3. Independent Timeout Handling
```python
# Each demo sample's batt() call has its own timeout thread
call_with_timeout(batt, ...)
  └─ Creates daemon thread
  └─ thread.join(timeout=5)
  └─ Independent from ThreadPoolExecutor!
  
# No interference with executor workers
# No shared resource conflicts
```

### 4. Simpler Architecture
- No async/await complexity
- Direct threading (well-understood pattern)
- Easy to debug (standard Python threading)
- Clear separation of concerns

---

## Risk Assessment

### Low Risk ✅
- Thread-based timeout is standard Python pattern
- ThreadPoolExecutor is well-tested and reliable
- No complex asyncio interactions
- Easy to revert if issues

### Potential Issues
1. **More threads** (5 workers + 5 timeout threads = 10 total)
   - Mitigation: Timeout threads are short-lived, minimal overhead
   
2. **Thread safety in batt()**
   - Mitigation: Each thread processes different sample data
   - Should be safe if batt() doesn't use global state
   
3. **Resource usage** (memory, file descriptors)
   - Mitigation: Test on Kaggle, monitor resources
   - Can reduce workers if needed (e.g., 4 instead of 5)

---

## Next Steps

### Immediate
1. ⏳ Test locally (smoke test)
2. ⏳ Upload to Kaggle
3. ⏳ Run performance test
4. ⏳ Compare results with Phase 3

### If Successful
1. ⏳ Document actual results in PHASE4_THREAD_RESULTS.md
2. ⏳ Update BATT_OPTIMIZATION_FINAL.md
3. ⏳ Commit with message: "feat: Phase 4 thread-based parallel scoring (2.5x speedup)"
4. ⏳ Celebrate! 🎉

### If Failed
1. ⏳ Analyze logs and timing
2. ⏳ Check for timeouts or errors
3. ⏳ Consider fallback options:
   - Reduce workers to 4
   - Increase timeout
   - Revert to Phase 3 if persistent issues

---

## Comparison Summary

| Approach | Method | Workers | Result |
|----------|--------|---------|---------|
| Phase 3 (Baseline) | Sequential | N/A | 16.8s ✅ Stable |
| Phase 4 Attempt 1 | asyncio.gather | 4 (executor) | 26.2s ❌ Deadlock |
| Phase 4 Attempt 2 | Dual pools + gather | 4+4 | 22.5s ❌ Still deadlock |
| **Phase 4 Alternative** | **ThreadPoolExecutor** | **5** | **7-8s** ✅ **Expected** |

---

## Conclusion

Implemented Phase 4 Alternative using **pure threading** approach:

- ✅ Thread-based timeout (`call_with_timeout`)
- ✅ Direct ThreadPoolExecutor(max_workers=5)
- ✅ Parallel demo sample scoring
- ✅ Code compiles successfully
- ✅ Ready for Kaggle testing

**Expected result**: 16.8s → 7-8s (2-2.5x faster) 🚀

**Key innovation**: Eliminated asyncio/executor mismatch by using ThreadPoolExecutor directly with independent thread-based timeouts. Simple, clean, and should actually work!

---

*Last Updated: October 12, 2025*  
*Status: IMPLEMENTED - Ready for Kaggle Testing*  
*Expected: 2-2.5x speedup (16.8s → 7-8s)*
