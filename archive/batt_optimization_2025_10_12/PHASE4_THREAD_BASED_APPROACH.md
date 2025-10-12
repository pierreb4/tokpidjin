# Phase 4 Alternative: Thread-Based Parallelism (No asyncio)

## Strategy: Direct ThreadPoolExecutor Without asyncio

### Problem with Current Approach
- `batt()` is synchronous but wrapped in `run_with_timeout()` which uses asyncio
- `asyncio.gather()` schedules coroutines that compete for executor workers
- Mixing asyncio and threading creates complexity and deadlock

### Solution: Pure Threading
Use ThreadPoolExecutor directly with thread-based timeout handling (no asyncio needed!)

---

## Implementation

### 1. Thread-Based Timeout Function

Replace `run_with_timeout()` with pure threading approach:

```python
import threading
from queue import Queue, Empty

def call_with_timeout(func, args, timeout=5):
    """
    Call a function with a timeout using threads (no asyncio).
    
    Returns:
        (timed_out: bool, result: Any)
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
        # Thread still running after timeout
        return True, None  # (timed_out, result)
    
    # Check for exceptions
    try:
        exception = exception_queue.get_nowait()
        # Could log exception here if needed
        return True, None  # Treat exceptions as timeouts
    except Empty:
        pass
    
    # Get successful result
    try:
        result = result_queue.get_nowait()
        return False, result  # (timed_out, result)
    except Empty:
        return True, None
```

### 2. Synchronous Sample Scoring

Convert `check_batt` from async to sync:

```python
def check_batt(total_data, task_i, task_id, d_score, start_time, pile_log_path, timeout=1, prof=None):
    """Check batt - now synchronous (no async/await)"""
    
    demo_task, test_task = total_data
    
    o = {'demo': {}, 'test': {}}
    s = {'demo': {}, 'test': {}}
    all_o = set()
    S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in demo_task)

    print_l(f'-- {task_id} - {task_i} --') if DO_PRINT else None

    o_score = O_Score()
    s_score = {}
    
    # OPTION A: Sequential (current stable approach)
    for i, sample in enumerate(demo_task):
        I = sample['input']
        O = sample['output']
        
        prof_start = timer() if prof is not None else None
        solve_timed_out, solve_result = call_with_timeout(batt,
            [task_id, S, I, None, pile_log_path], timeout)
        if prof is not None:
            prof['batt.demo.call_with_timeout'] += timer() - prof_start

        if solve_timed_out and DO_PRINT:
            print_l(f'-- {task_id} - demo[{i}] timed out')

        # ... rest of scoring logic (unchanged)
```

### 3. Parallel Sample Scoring with ThreadPoolExecutor

Add parallel version that actually works:

```python
def score_demo_sample(args):
    """Score a single demo sample (for ThreadPoolExecutor)"""
    i, sample, task_id, S, pile_log_path, timeout = args
    
    I = sample['input']
    O = sample['output']
    
    # Call batt with timeout
    solve_timed_out, solve_result = call_with_timeout(batt,
        [task_id, S, I, None, pile_log_path], timeout)
    
    demo_o = []
    demo_s = []
    
    if solve_result is not None:
        demo_o, _ = solve_result
        
        # Score outputs and run diff for this sample
        for t_n, evo, o_solver_id, okt in demo_o:
            C = okt
            match = C == O
            
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
        'timed_out': solve_timed_out,
        'sample_output': O  # For verification
    }

def check_batt_parallel(total_data, task_i, task_id, d_score, start_time, pile_log_path, timeout=1, prof=None):
    """Check batt with PARALLEL sample scoring using ThreadPoolExecutor"""
    
    demo_task, test_task = total_data
    
    o = {'demo': {}, 'test': {}}
    s = {'demo': {}, 'test': {}}
    all_o = set()
    S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in demo_task)

    print_l(f'-- {task_id} - {task_i} --') if DO_PRINT else None

    o_score = O_Score()
    s_score = {}
    
    # Phase 4 Alternative: Parallel demo scoring with ThreadPoolExecutor
    prof_start = timer() if prof is not None else None
    
    # Use separate executor for high-level parallelism (5 workers for 5 demo samples)
    with ThreadPoolExecutor(max_workers=5) as executor:
        # Prepare arguments for each demo sample
        demo_args = [
            (i, sample, task_id, S, pile_log_path, timeout)
            for i, sample in enumerate(demo_task)
        ]
        
        # Submit all demo samples for parallel execution
        demo_futures = {executor.submit(score_demo_sample, args): args[0] 
                       for args in demo_args}
        
        # Collect results as they complete
        demo_results = [None] * len(demo_task)
        for future in as_completed(demo_futures):
            try:
                result = future.result(timeout=timeout + 1)  # Extra second for safety
                demo_results[result['index']] = result
            except Exception as e:
                sample_idx = demo_futures[future]
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
            if match and DO_PRINT:
                print_l(f'- {o_solver_id = } - {match = }')
            o_score.update(o_solver_id, match)
        
        # Update solver scores
        for s_item in result['solver_scores']:
            # Extract o_solver_id from first output if available
            if result['outputs']:
                o_solver_id = result['outputs'][0][2]
                d_score.update(o_solver_id, s_item)
    
    # Process test samples (can keep sequential or parallelize similarly)
    for i, sample in enumerate(test_task):
        I = sample['input']
        O = sample['output']
        
        prof_start = timer() if prof is not None else None
        solve_timed_out, solve_result = call_with_timeout(batt,
            [task_id, S, I, None, pile_log_path], timeout)
        if prof is not None:
            prof['batt.test.call_with_timeout'] += timer() - prof_start

        if solve_timed_out and DO_PRINT:
            print_l(f'-- {task_id} - test[{i}] timed out')

        if solve_result is not None:
            o['test'][i], _ = solve_result
            print_l(f"test[{i}] - {task_id} - {len(o['test'][i])}") if DO_PRINT else None

            all_o = all_o.union(o['test'][i])
            for t_n, evo, o_solver_id, okt in o['test'][i]:
                C = okt
                if match := C == O:
                    print_l(f'- {o_solver_id = } - {match = }')
                o_score.update(o_solver_id, match)

                diff_timed_out, diff_result = call_with_timeout(batt,
                    [task_id, S, I, C, pile_log_path], timeout)

                if diff_result is not None:
                    _, s['test'][i] = diff_result
                    for s_item in s['test'][i]:
                        d_score.update(o_solver_id, s_item)
    
    # Calculate scores
    for o_solver_id in d_score.score.keys():
        for name in d_score.score[o_solver_id].keys():
            if name not in s_score:
                s_score[name] = {'iz': S_Score(), 'zo': S_Score()}
            for score_type in ['iz', 'zo']:
                s_score[name][score_type].update(o_solver_id, 
                    d_score.score[o_solver_id][name][score_type])

    len_task = len(demo_task) + len(test_task)
    elapsed = timer() - start_time
    return all_o, o_score, s_score
```

---

## Key Advantages

### 1. No asyncio/executor Mismatch
- **Before**: asyncio.gather → coroutines → run_with_timeout → executor (conflict!)
- **After**: ThreadPoolExecutor → threads → call_with_timeout (direct!)

### 2. Explicit Worker Control
```python
# 5 demo samples = 5 workers (perfect match!)
ThreadPoolExecutor(max_workers=5)

# Each worker calls batt() with thread-based timeout
# No competition for shared executor workers
```

### 3. Independent Timeout Handling
```python
# Each thread has its own timeout mechanism
thread.join(timeout=timeout)  # No executor involvement!

# Inside each thread, batt() can call anything it wants
# No interference with parent ThreadPoolExecutor
```

### 4. Simpler Architecture
```
ThreadPoolExecutor (5 workers)
├─ Thread 1: score_demo_sample(demo[0])
│  └─ call_with_timeout(batt, ...) → separate thread → joins with timeout
├─ Thread 2: score_demo_sample(demo[1])
│  └─ call_with_timeout(batt, ...) → separate thread → joins with timeout
├─ Thread 3: score_demo_sample(demo[2])
├─ Thread 4: score_demo_sample(demo[3])
└─ Thread 5: score_demo_sample(demo[4])  ← NO DEADLOCK!

Total threads: 5 (worker) + 5 (timeout) = 10 concurrent
But timeout threads are short-lived and independent!
```

---

## Expected Performance

### Current (Sequential with asyncio)
```
Demo samples: ~12s
├─ demo[0]: 2.4s
├─ demo[1]: 2.4s
├─ demo[2]: 2.4s
├─ demo[3]: 2.4s
└─ demo[4]: 2.4s (sequential)
```

### With ThreadPoolExecutor (5 workers)
```
Demo samples: ~3s (4x faster!)
├─ demo[0]: 2.4s ┐
├─ demo[1]: 2.4s ├─ All run in parallel
├─ demo[2]: 2.4s ├─ Max time = longest sample
├─ demo[3]: 2.4s ├─ ~2.4-3.0s total
└─ demo[4]: 2.4s ┘
```

### Total Impact
```
Operation         | Before  | After   | Speedup
------------------|---------|---------|--------
Demo scoring      | 12.0s   | 3.0s    | 4x
Test scoring      | 3.5s    | 3.5s    | 1x (only 1 sample)
Other             | 1.3s    | 1.3s    | 1x
------------------|---------|---------|--------
Total             | 16.8s   | 7.8s    | 2.15x ✓
```

---

## Migration Steps

### Step 1: Add Thread-Based Timeout to utils.py
```python
# utils.py
import threading
from queue import Queue, Empty

def call_with_timeout(func, args, timeout=5):
    """Call function with timeout using threads (no asyncio)"""
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
        return True, None
    
    try:
        exception = exception_queue.get_nowait()
        return True, None
    except Empty:
        pass
    
    try:
        result = result_queue.get_nowait()
        return False, result
    except Empty:
        return True, None
```

### Step 2: Keep run_with_timeout for Backward Compatibility
```python
# Keep existing async version for other code
async def run_with_timeout(func, args, timeout=5):
    """Legacy async version (kept for backward compatibility)"""
    executor = get_low_level_executor()
    loop = asyncio.get_event_loop()
    try:
        result = await asyncio.wait_for(
            loop.run_in_executor(executor, func, *args), timeout
        )
        return False, result
    except asyncio.TimeoutError:
        return True, None
```

### Step 3: Make check_batt Synchronous
```python
# Change signature
def check_batt(total_data, task_i, task_id, d_score, start_time, pile_log_path, timeout=1, prof=None):
    # No async/await anymore!
    # Use call_with_timeout instead of run_with_timeout
    solve_timed_out, solve_result = call_with_timeout(batt, [...], timeout)
```

### Step 4: Add Parallel Version
```python
# Add new function (or replace check_batt)
def check_batt_parallel(total_data, ...):
    with ThreadPoolExecutor(max_workers=5) as executor:
        # Parallel demo scoring
        ...
```

### Step 5: Update Main Loop
```python
# main() or run_batt()
# Change from:
all_o, o_score, s_score = await check_batt(...)

# To:
all_o, o_score, s_score = check_batt_parallel(...)
```

---

## Testing Plan

### Phase 1: Local Testing
1. Add `call_with_timeout()` to utils.py
2. Test basic timeout functionality
3. Verify no regressions

### Phase 2: Sequential with New Timeout
1. Replace `run_with_timeout` with `call_with_timeout` in check_batt
2. Make check_batt synchronous (remove async/await)
3. Test on Kaggle - should match 16.8s baseline
4. Verify no timeouts, same results

### Phase 3: Parallel Implementation
1. Add `score_demo_sample()` function
2. Implement `check_batt_parallel()` with ThreadPoolExecutor(5)
3. Test on Kaggle
4. Expected: ~7-8s (2x faster!)

### Phase 4: Validation
1. Compare results with sequential version
2. Check for any new timeouts
3. Verify 149 candidates (not 126)
4. Confirm correctness

---

## Risk Assessment

### Low Risk
- ✅ Thread-based timeout is standard Python pattern
- ✅ ThreadPoolExecutor is well-tested and reliable
- ✅ No asyncio complexity or hidden interactions
- ✅ Easy to revert if issues occur

### Potential Issues
- ⚠️ **More threads** (5 workers + 5 timeout threads = 10 total)
  - Mitigation: Timeout threads are short-lived, minimal overhead
  
- ⚠️ **Thread safety** in batt()
  - Mitigation: Each thread processes different sample data
  
- ⚠️ **Resource usage** (memory, file descriptors)
  - Mitigation: Test on Kaggle, monitor resource usage

### Expected Outcome
- 🎯 **Success probability: HIGH**
- 🎯 **Expected speedup: 2-2.5x** (16.8s → 7-8s)
- 🎯 **Complexity: LOW** (simpler than asyncio approach!)

---

## Comparison with Previous Attempts

### Phase 4 Attempt 1 (asyncio.gather)
```
❌ FAILED: 26.2s (56% slower)
Problem: asyncio.gather + run_with_timeout → executor conflicts
```

### Phase 4 Attempt 2 (Dual pools with asyncio.gather)
```
❌ FAILED: 22.5s (34% slower)
Problem: High-level pool never used, still asyncio.gather conflicts
```

### Phase 4 Alternative (Direct ThreadPoolExecutor)
```
✓ EXPECTED SUCCESS: 7-8s (2x faster)
Solution: Pure threading, no asyncio, explicit control
```

---

## Conclusion

**Recommendation**: Implement thread-based approach (call_with_timeout + ThreadPoolExecutor)

**Why it will work**:
1. **No asyncio/executor mismatch** - direct threading all the way
2. **Independent timeout handling** - each thread self-manages timeout
3. **Explicit parallelism** - 5 workers for 5 samples (perfect match)
4. **Simpler architecture** - easier to understand and debug

**Expected result**: 16.8s → 7-8s (2-2.5x faster) with no deadlocks! 🚀

---

*Next Step: Implement call_with_timeout() in utils.py and test locally*
