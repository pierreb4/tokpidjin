# Profiling Data Reference - Available Metrics

## Overview

The profiling system (`prof` dict) now tracks comprehensive timing and error data. Use this reference when analyzing performance.

## How to Enable Profiling

```python
from collections import defaultdict

prof = defaultdict(float)

# Pass prof to run_batt
timed_out = await run_batt(
    total_data, task_i, task_id, d_score,
    start_time, pile_log_path,
    timeout=20.0,
    prof=prof,  # ← Enable profiling
    batt_module_name='batt'
)

# After execution, prof contains all metrics
for key, value in sorted(prof.items()):
    print(f"{key}: {value:.4f}s")
```

## Available Metrics (as of Nov 2025)

### Phase Timing Metrics

| Metric | Description | Typical Value |
|--------|-------------|---------------|
| `run_batt.phase1_filter` | Filter solvers by validation | 0.05-0.15s |
| `run_batt.phase2_inline_batch` | Batch inline solvers | 0.001-0.005s |
| `run_batt.phase3a_validate_batch` | Validate solvers in parallel | 0.004-0.040s |
| `run_batt.phase3b_file_ops` | File operations (saving solvers) | 0.03-0.05s |
| `run_batt.phase3b_ensure_dir` | Directory creation | 0.0005-0.002s |
| `run_batt.phase3b_check_save` | Check if solver should be saved | 0.03-0.04s |
| `run_batt.phase3b_symlink` | Create symlinks | 0.001-0.003s |
| `run_batt.phase3b_score_calc` | Score calculation | <0.001s |
| `run_batt.phase3b_overhead` | Miscellaneous overhead | <0.001s |
| `run_batt.phase4_differs` | Total differ processing | 0.24-0.32s |
| `run_batt.phase4_build` | Build differ data structures | 0.003s |
| `run_batt.phase4_inline` | Inline differs | 0.002-0.003s |
| `run_batt.phase4_process` | Process inlined differs | 0.23-0.31s |

### Solver Execution Metrics

| Metric | Description | Typical Value |
|--------|-------------|---------------|
| `run_batt.check_solver` | Execute solvers on test cases | 0.004-1.0s |
| `run_batt.check_batt` | Aggregate solver checking | 0.3-1.2s |
| `batt.demo.parallel` | Parallel demo execution | 0.3-1.1s |

### Aggregation Metrics

| Metric | Description | Typical Value |
|--------|-------------|---------------|
| `batt.aggregation.total` | Total aggregation time | 0.002-0.017s |
| `batt.score.update` | Update scores | 0.001-0.017s |
| `batt.score.consolidate` | Consolidate scores | <0.001s |
| `batt.dscore.update` | Update D_Score object | <0.001s |
| `batt.result.union` | Union results | <0.001s |
| `run_batt.generate_expanded` | Generate expanded content | <0.001s |

### Error & Timeout Metrics (NEW)

| Metric | Description | When Present |
|--------|-------------|--------------|
| `run_batt.inline_errors` | Total inlining errors | When errors occur |
| `run_batt.inline_timeouts` | Inlining timeout count | When timeouts occur |
| `run_batt.inline_error.thread_error` | Thread exhaustion errors | When "can't start new thread" |
| `run_batt.inline_error.ast_error` | AST parsing errors | When AST fails |
| `run_batt.inline_error.other_value_error` | Other ValueError types | When other errors occur |
| `run_batt.inline_error.<type>` | Other error types | Dynamic based on exceptions |

## Telemetry Summary (Console Output)

In addition to `prof` dict, telemetry is printed to console:

```
=== INLINING TELEMETRY ===
Total attempts: 1280
Success (first try): 1280 (100.0%)
Timeouts: 0 (0.0%)
Other errors: 0 (0.0%)
==============================
```

**With errors (NEW format):**
```
=== INLINING TELEMETRY ===
Total attempts: 2048
Success (first try): 2010 (98.1%)
Timeouts: 15 (0.7%)
  → Retry success (raw source): 15 (100.0% of timeouts)
  → Retry fail: 0 (0.0% of timeouts)
  → Total retry time: 450.2ms (avg 30.01ms per retry)
Other errors: 23 (1.1%)
Error breakdown:
  → thread_error: 18 (78.3% of errors)
  → ast_error: 3 (13.0% of errors)
  → other_value_error: 2 (8.7% of errors)
==============================
```

## Usage Examples

### 1. Identify Slowest Phase

```python
import json

with open('logs/outlier_profiling_results.json') as f:
    data = json.load(f)

for task in data['outlier_tasks']:
    phases = task.get('phase_times', {})
    slowest = max(phases.items(), key=lambda x: x[1])
    print(f"{task['task_id']}: Slowest = {slowest[0]} ({slowest[1]:.2f}s)")
```

### 2. Calculate Thread Error Rate

```python
for task in data['outlier_tasks']:
    phases = task.get('phase_times', {})
    thread_errors = phases.get('run_batt.inline_error.thread_error', 0)
    total_errors = phases.get('run_batt.inline_errors', 0)
    
    if total_errors > 0:
        rate = 100 * thread_errors / total_errors
        print(f"{task['task_id']}: {thread_errors}/{total_errors} thread errors ({rate:.1f}%)")
```

### 3. Find Phase Taking >25% of Total Time

```python
for task in data['outlier_tasks']:
    total = task['total_time']
    phases = task.get('phase_times', {})
    
    bottlenecks = [(k, v) for k, v in phases.items() if v > 0.25 * total]
    if bottlenecks:
        print(f"{task['task_id']} bottlenecks:")
        for phase, time in sorted(bottlenecks, key=lambda x: -x[1]):
            pct = 100 * time / total
            print(f"  {phase}: {time:.2f}s ({pct:.1f}%)")
```

### 4. Compare Outlier vs Reference Tasks

```python
def avg_phase_time(tasks, phase):
    times = [t.get('phase_times', {}).get(phase, 0) for t in tasks]
    return sum(times) / len(times) if times else 0

phase = 'run_batt.check_solver'
outlier_avg = avg_phase_time(data['outlier_tasks'], phase)
ref_avg = avg_phase_time(data['reference_tasks'], phase)

if ref_avg > 0:
    ratio = outlier_avg / ref_avg
    print(f"{phase}: Outlier {outlier_avg:.3f}s vs Ref {ref_avg:.3f}s ({ratio:.1f}x)")
```

## Error Tracking Benefits

### Before (No Error Tracking)
- Errors logged to console only
- No quantitative measure of error rate
- Hard to correlate errors with timeouts
- No visibility in profiling analysis

### After (With Error Tracking)
- ✅ Error counts in `prof` dict
- ✅ Error breakdown by type
- ✅ Can measure thread error rate
- ✅ Visible in profiling JSON output
- ✅ Can correlate errors with task timeouts
- ✅ Error telemetry in console summary

## Profiling Overhead

**Minimal overhead when profiling enabled:**
- Timer calls: ~0.1-0.5µs each
- Dict updates: ~0.05µs each
- Total overhead: <1ms per task (<0.1% of total time)

**Recommended:** Always enable profiling in production for visibility.

## Next Steps

1. **Run profiler with error tracking:**
   ```bash
   python profile_outlier_tasks.py
   ```

2. **Check for thread errors in results:**
   ```bash
   python3 -c "
   import json
   d = json.load(open('logs/outlier_profiling_results.json'))
   for t in d['outlier_tasks'] + d['reference_tasks']:
       if 'run_batt.inline_error.thread_error' in t.get('phase_times', {}):
           print(f\"{t['task_id']}: {t['phase_times']['run_batt.inline_error.thread_error']} thread errors\")
   "
   ```

3. **Monitor thread error rate over time:**
   ```bash
   grep "thread_error:" logs/*.log | tail -20
   ```

## See Also

- `THREAD_EXHAUSTION_ANALYSIS.md` - Thread error root cause and solutions
- `CACHE_CLEANUP_RESULTS.md` - Cache cleanup verification results
- `profile_outlier_tasks.py` - Profiling tool implementation
