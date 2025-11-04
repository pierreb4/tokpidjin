# Profiling inline_variables() Timeout

## Current Configuration

**Timeout Settings:**
- `utils.py:322`: `timeout_seconds=1` (default parameter)
- `run_batt.py:1560`: `timeout_per_item=1` (batch solver inlining)
- `run_batt.py:1808`: `timeout_per_item=1` (batch differ inlining)

**Performance Data:**
- Normal solvers inline in `<100ms`
- 1s timeout was reduced from 30s to catch infinite loops faster
- Need real-world data to optimize further

## Profiling Strategy

### 1. Collect Timing Data from Real Runs

**Command 1: Profile with 100 tasks (quick baseline)**
```bash
# Run 100 tasks and capture inline timing stats
timeout 600 bash run_card.sh -c -100 2>&1 | tee profile_inline_100.log
```

This will:
- Generate candidates and inline them
- Show cache statistics at end
- Output goes to both terminal and log file

**Command 2: Extract inline timing statistics**
```bash
# Parse log file for inline operation patterns
grep -E "(inline_one|inline_differ|Inlining|SKIP:|timeout|ERROR)" profile_inline_100.log | head -100
```

### 2. Detailed Profiling with Built-in Timers

**Command 3: Enable profiler output (requires PROFILE env var)**
```bash
# If profiling is enabled in run_batt.py, this captures detailed timing
PROFILE=1 timeout 300 bash run_card.sh -c -32 2>&1 | tee profile_inline_detailed.log
```

**Command 4: Look for profiling output**
```bash
# Search for timing breakdown (if profiler is enabled)
grep -A 20 "== Timing Breakdown ==" profile_inline_detailed.log
```

### 3. Manual Benchmark (Isolated Test)

**Command 5: Create isolated profiling script**

Create `profile_inline_isolated.py`:
```python
#!/usr/bin/env python3
import sys
import time
import random
from timeit import default_timer as timer
from utils import inline_variables

# Load some solver candidates
import batt
import importlib.util

# Get a sample batt module
spec = importlib.util.spec_from_file_location("tmp_batt", "tmp_batt_onerun_run.py")
if spec and spec.loader:
    batt_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(batt_module)
    
    # Extract solvers and differs
    solvers = [s for s in dir(batt_module) if s.startswith('solve_')]
    differs = [d for d in dir(batt_module) if d.startswith('differ_')]
    
    print(f"Found {len(solvers)} solvers and {len(differs)} differs")
    
    # Profile a sample of each
    times_solver = []
    times_differ = []
    
    for solver_name in random.sample(solvers, min(10, len(solvers))):
        solver = getattr(batt_module, solver_name)
        source = inspect.getsource(solver)
        
        t0 = timer()
        try:
            result = inline_variables(source, timeout_seconds=1)
            dt = timer() - t0
            times_solver.append(dt)
            print(f"{solver_name:20s}: {dt*1000:7.2f}ms")
        except Exception as e:
            dt = timer() - t0
            print(f"{solver_name:20s}: ERROR after {dt*1000:7.2f}ms - {type(e).__name__}: {str(e)[:50]}")
    
    print(f"\nSolver timing stats:")
    print(f"  Count: {len(times_solver)}")
    print(f"  Mean:  {sum(times_solver)/len(times_solver)*1000:.2f}ms" if times_solver else "  Mean: N/A")
    print(f"  Max:   {max(times_solver)*1000:.2f}ms" if times_solver else "  Max: N/A")
    print(f"  Min:   {min(times_solver)*1000:.2f}ms" if times_solver else "  Min: N/A")
```

Run it:
```bash
python profile_inline_isolated.py > profile_inline_isolated.log 2>&1
```

### 4. Stress Test with Different Timeouts

**Command 6: Test with different timeout values**

Create `profile_inline_stress.py`:
```python
#!/usr/bin/env python3
import sys
import os
from timeit import default_timer as timer
import random
import importlib.util

# Test different timeout values
TIMEOUTS = [0.1, 0.5, 1.0, 2.0, 5.0]

# Load sample batt
spec = importlib.util.spec_from_file_location("tmp_batt", "tmp_batt_onerun_run.py")
if spec and spec.loader:
    batt_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(batt_module)
    
    solvers = [s for s in dir(batt_module) if s.startswith('solve_')]
    sample_solvers = random.sample(solvers, min(20, len(solvers)))
    
    print("Testing different timeout values...")
    print(f"{'Timeout':>8s} | {'Success':>7s} | {'Timeout':>7s} | {'Error':>7s} | {'Avg Time':>10s}")
    print("-" * 60)
    
    for timeout_val in TIMEOUTS:
        success_count = 0
        timeout_count = 0
        error_count = 0
        total_time = 0
        
        from utils import inline_variables
        
        for solver_name in sample_solvers:
            solver = getattr(batt_module, solver_name)
            source = inspect.getsource(solver)
            
            t0 = timer()
            try:
                result = inline_variables(source, timeout_seconds=timeout_val)
                dt = timer() - t0
                total_time += dt
                success_count += 1
            except TimeoutError:
                total_time += timeout_val
                timeout_count += 1
            except Exception as e:
                dt = timer() - t0
                total_time += dt
                error_count += 1
        
        avg_time = total_time / len(sample_solvers)
        print(f"{timeout_val:7.1f}s | {success_count:7d} | {timeout_count:7d} | {error_count:7d} | {avg_time*1000:9.2f}ms")
```

Run it:
```bash
python profile_inline_stress.py > profile_inline_stress.log 2>&1
```

### 5. Production Profiling on Server

**Command 7: Quick 10-task run with full logging**
```bash
# On Simone server: Run 10 tasks and capture output
timeout 120 bash run_card.sh -c -10 2>&1 | tee profile_inline_server.log
grep -E "(inline|timeout|SKIP|ERROR)" profile_inline_server.log | head -50
```

**Command 8: Medium run for statistical significance**
```bash
# Run 50 tasks - larger sample for better statistics
timeout 300 bash run_card.sh -c -50 2>&1 | tee profile_inline_50.log
tail -50 profile_inline_50.log  # Show cache stats and summary
```

## Analysis Steps

### Step 1: Check for timeout occurrences
```bash
grep -i "timeout\|SKIP:" *.log | wc -l
grep -i "timeout\|SKIP:" *.log | head -20
```

### Step 2: Extract timing information
```bash
# If using profiler timings
grep "inline_variables" *.log | grep -E "[0-9]+\.[0-9]+ms"
```

### Step 3: Check error rates
```bash
# Count errors during inlining
grep -i "error.*inlin" *.log | wc -l
grep -i "error.*inlin" *.log | head -20
```

### Step 4: Analyze cache effectiveness
```bash
# Check cache hit rates
grep -A 5 "Inlining Cache:" *.log
```

## Decision Tree: Adjusting Timeouts

Based on profiling results:

```
If timeout_count > 0:
  ├─ Check if errors are AST-related:
  │  └─ "error return without exception set"? → Keep timeout, fix AST errors upstream
  │  └─ Other errors? → Increase timeout slightly (1s → 2s)
  │
  └─ Check if errors are legitimate infinite loops:
     └─ Yes → Keep or reduce timeout (0.5s-1s is good)
     └─ No → Increase timeout (1s → 2s)

If avg_time < 50ms:
  └─ Timeout is too generous, reduce to 0.5s to catch errors faster

If avg_time 50-100ms:
  └─ Timeout 1s is good, can reduce to 0.5s if no errors

If avg_time 100-500ms:
  └─ Timeout 1s is marginal, consider 2s for safety

If avg_time > 500ms:
  └─ Timeout 1s is too short, increase to 2-5s
  └─ Consider profiling why inlining is slow
```

## Recommendations

**Current Status (1s timeout):**
- ✅ Fast error detection for infinite loops
- ✅ Aggressive but reasonable for normal solvers (<100ms)
- ⚠️ May be cutting it close for edge cases

**If You See Many Timeouts:**
1. Profile with `profile_inline_stress.py` to get distribution
2. Increase timeout in steps: 1s → 2s → 5s
3. Check if timeouts are AST errors (need different fix) or legitimate slow inlining

**If You See No Timeouts:**
1. Profile shows all complete in <100ms? → Can reduce to 0.5s
2. Profile shows up to 200ms? → Keep 1s
3. Profile shows up to 500ms? → Keep 1s, consider 2s

## Key Files to Monitor

- `utils.py:322` - `inline_variables()` timeout_seconds parameter
- `run_batt.py:1560` - solver inlining timeout_per_item
- `run_batt.py:1808` - differ inlining timeout_per_item
- `.cache/` - cache hit rates show if inlining is being reused

## Example Output to Expect

Good profile run:
```
Found 50 solvers and 20 differs
solve_36d67576    :  120.34ms
solve_36fdfd69    :   58.31ms
solve_1a07d186    :   11.00ms
solve_09629e4f    :    6.38ms
...
Solver timing stats:
  Count: 50
  Mean:  45.23ms
  Max:   120.34ms
  Min:    0.98ms
```

If you see many timeouts or errors, post the log and we can analyze together!
