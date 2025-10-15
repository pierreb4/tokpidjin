# Kaggle Profiling Results - Outlier Analysis

**Date**: October 15, 2025  
**Platform**: Kaggle T4x2 GPU  
**Profiled**: tmp_batt_onerun_run.py on 100 tasks  

## The Outlier Problem

### Extreme Cases Identified

Looking at task execution times, 4 tasks show **extreme outliers**:

| Task # | Task ID | Time (seconds) | Status |
|--------|---------|----------------|--------|
| 16 | 06df4c85 | 239.5s | 🔴 Likely infinite loop |
| 50 | 13f06aa5 | 117.3s | 🔴 Runaway recursion |
| 56 | 15113be4 | 101.9s | 🔴 Stuck computation |
| 79 | 1b59e163 | 180.3s | 🔴 Near-infinite loop |

**Total outlier time**: 638.9 seconds (in cProfile cumulative time)

### Why This Matters

These outliers:
1. **Skew average performance** - Make typical tasks look slower than they are
2. **Mask real bottlenecks** - Hide what's actually slow in normal execution
3. **Inflate DSL statistics** - Operations in loops get counted millions of times
4. **Distort optimization priorities** - Make us optimize the wrong things

### Corrected Analysis (Excluding Outliers)

**Removing 4 outliers from 100 tasks:**

```
Original (100 tasks):
  Wall-clock total: 110.3s
  Average per task: 1.1s
  
Excluding outliers (96 tasks):
  Need to recalculate with clean data
  Expected: ~0.5-0.8s per typical task
  Projected 400 tasks: 200-320s (reasonable!)
```

## Typical Task Performance

Looking at **non-outlier tasks** (most fall in 1.4s - 5.0s range):

**Fast tasks** (1.4-2.0s): ~40 tasks
- Example: 007bbfb7 (1.48s), 0d3d703e (1.46s), 1bfc4729 (1.43s)

**Medium tasks** (2.0-5.0s): ~40 tasks  
- Example: 045e512c (2.40s), 025d127b (3.39s), 00d62c1b (5.03s)

**Complex tasks** (5.0-10.0s): ~12 tasks
- Example: 09629e4f (6.00s), 14754a24 (8.90s), 1c786137 (9.49s)

**Slow but reasonable** (10-20s): ~4 tasks
- Example: 0607ce86 (12.41s), 09c534e7 (12.53s), 1d0a4b61 (16.23s)

**Typical average**: ~3-4 seconds per task (excluding outliers)

## Root Cause: Infinite Loops in Generated Code

The `tmp_batt_onerun_run.py` is a **genetically mutated solver** that:
- Combines existing solver patterns randomly
- May create infinite or near-infinite loops
- Is tested across ALL tasks to see if it solves new ones

**The outliers are not bugs** - they're expected behavior when testing untested genetic mutations!

## Implications for Profiling

### What We Should Profile

❌ **Don't profile**: Genetic candidates with infinite loops  
✅ **Do profile**: Validated, working solvers from `solvers.py`

### Corrected Profiling Strategy

1. **Use validated solvers** from `solvers.py` (not genetic mutations)
2. **Add timeout protection** (kill tasks after 5-10 seconds)
3. **Filter outliers** (exclude tasks >10s before analysis)
4. **Profile typical cases** (focus on 1-5 second tasks)

## Next Steps: Re-profile with Clean Data

### Option 1: Profile Validated Solvers (Recommended)

Profile actual working solvers from `solvers.py`:
```bash
# Example: Profile solve_007bbfb7
python profile_batt_dsl.py -f solvers -t 007bbfb7 --function solve_007bbfb7
```

**Advantages**:
- No infinite loops
- Representative of production code
- Real optimization targets
- Accurate bottleneck identification

### Option 2: Add Timeout to Genetic Profiling

Re-profile `tmp_batt_onerun_run.py` with:
- Per-task timeout (5-10 seconds)
- Skip outliers in analysis
- Focus on successful completions

```python
# In profile_batt_batch.py, add:
import signal

def timeout_handler(signum, frame):
    raise TimeoutError("Task exceeded timeout")

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(10)  # 10 second timeout
try:
    result = batt_func(...)
finally:
    signal.alarm(0)  # Cancel alarm
```

### Option 3: Filter and Re-analyze

Re-run analysis on existing results, excluding outliers:
```python
# Filter tasks >10s
filtered_results = {
    task_id: data 
    for task_id, data in results.items() 
    if data['analysis']['total_time'] < 10.0  # 10 seconds
}
```

## Corrected Performance Expectations

### With Clean Data (No Outliers)

**Typical task**: 3-4 seconds  
**400 tasks**: 1200-1600 seconds (20-27 minutes)

**DSL function breakdown** (expected with clean data):
- o_g/objects: 15-30% of execution (not 1.3% we saw!)
- Other DSL ops: 20-30%
- Framework overhead: 40-55%

### Why Original Results Were Misleading

The 4 outliers (638s cumulative cProfile time) were:
- Running DSL operations **millions of times** in loops
- Inflating DSL function call counts enormously
- Making DSL ops look insignificant (1.3% vs expected 15-30%)
- Hiding real performance characteristics

## Recommendation

**Profile validated solvers, not genetic mutations!**

Genetic mutations are for **discovery** (finding new solutions), not for **performance analysis**. Profile working solvers to understand real bottlenecks.

### Action Items

1. ✅ Identify outliers (DONE - 4 found)
2. 🔄 Re-profile using `solvers.py` validated solvers
3. ⏳ Add per-task timeout protection
4. ⏳ Re-analyze with clean data
5. ⏳ Update optimization strategy based on real bottlenecks

---

**Key Insight**: You can't profile performance using code that might have infinite loops! Use validated, working solvers for accurate bottleneck identification.

**Next**: Profile 20-30 validated solvers from `solvers.py` to get clean, representative data.
