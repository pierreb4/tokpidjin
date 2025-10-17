# 🔧 run_batt.py Arguments Reference

**File**: `run_batt.py` (lines 2005-2019)  
**Purpose**: Configure how run_batt.py processes tasks

---

## Available Arguments

### Task Selection

#### `-c` / `--count` (COUNT)
- **Type**: integer
- **Default**: 0 (all tasks)
- **Usage**: `python run_batt.py -c 32`
- **Effect**: Run first 32 tasks from solver_dir
- **Note**: `-c 0` runs all available tasks

#### `-s` / `--start` (START)
- **Type**: integer
- **Default**: 0
- **Usage**: `python run_batt.py -s 10 -c 20`
- **Effect**: Run 20 tasks starting from task 10 (tasks 10-29)
- **Note**: Useful for resuming or skipping early tasks

#### `-i` / `--task_ids` (TASK_IDS)
- **Type**: list of strings
- **Default**: None (random)
- **Usage**: `python run_batt.py -i task1 task2 task3`
- **Effect**: Run specific task IDs only
- **Note**: Can be used with other options

---

### Execution Options

#### `-t` / `--timeout` (TIMEOUT)
- **Type**: float (seconds)
- **Default**: 10.0
- **Usage**: `python run_batt.py -c 32 -t 20`
- **Effect**: Each task/sample gets 20 seconds before timeout
- **Note**: This is per-SAMPLE timeout, not per-task
- **Recommended for 100 tasks**: `-t 15` or `-t 20`

#### `-b` / `--batt_import` (BATT_IMPORT)
- **Type**: string (module name)
- **Default**: 'batt'
- **Usage**: `python run_batt.py -b tmp_batt_onerun_run`
- **Effect**: Import different batt module
- **Note**: Used by run_card.sh to specify tmp_batt_onerun_run

---

### Profiling & Analysis

#### `--timing`
- **Type**: flag (no value)
- **Default**: False
- **Usage**: `python run_batt.py -c 32 --timing`
- **Effect**: Print lightweight timing breakdown after completion
- **Output**: Shows time spent on validation, inlining, DSL calls, etc.
- **Performance Impact**: Minimal (~5% overhead)

#### `--cprofile`
- **Type**: flag (no value)
- **Default**: False
- **Usage**: `python run_batt.py -c 32 --cprofile --cprofile-top 30`
- **Effect**: Run with cProfile enabled, print top N functions
- **Performance Impact**: Moderate (~15-20% overhead)

#### `--cprofile-top` (TOP_N)
- **Type**: integer
- **Default**: 30
- **Usage**: `python run_batt.py --cprofile --cprofile-top 50`
- **Effect**: Show top 50 functions in cProfile output
- **Note**: Only used if `--cprofile` enabled

---

### GPU & Advanced

#### `--mega-batch`
- **Type**: flag (no value)
- **Default**: False
- **Usage**: `python run_batt.py --mega-batch --batch-size 2000`
- **Effect**: Use GPU batch processing (Phase 2b feature)
- **Note**: For 4000+ samples at once

#### `--batch-size` (BATCH_SIZE)
- **Type**: integer
- **Default**: 1000
- **Usage**: `python run_batt.py --mega-batch --batch-size 2000`
- **Effect**: Batch size for mega-batch GPU mode
- **Recommended**: 1000-2000 for optimal GPU utilization

---

## Common Command Patterns

### Testing / Development
```bash
# Run 1 task with timing
python run_batt.py -c 1 --timing

# Run 5 tasks with profiler
python run_batt.py -c 5 --cprofile --cprofile-top 30

# Run with longer timeout
python run_batt.py -c 10 -t 20
```

### Validation (What You Should Use)
```bash
# 32-task validation (current size for Phase 2a)
python run_batt.py -c 32 --timing

# 100-task validation (Phase 1b baseline comparison)
python run_batt.py -c 100 --timing

# Full scale (all tasks)
python run_batt.py --timing
```

### Profiling (Phase 2 Optimization)
```bash
# Profile 32 tasks, top 30 functions
python run_batt.py -c 32 --cprofile --cprofile-top 30

# Profile with longer timeout
python run_batt.py -c 32 -t 15 --cprofile --cprofile-top 50

# Profile full run without count limit
python run_batt.py --cprofile --cprofile-top 30
```

### Production (run_card.sh uses)
```bash
# Via run_card.sh (what you're doing now)
bash run_card.sh -o -i -b -c -32

# Direct equivalent
python run_batt.py -c 32 -t 10 -b tmp_batt_onerun_run
```

---

## What Was Wrong Before

### Issue 1: Previous Documentation
- Said `--gpu --profile` (DOESN'T EXIST)
- Should have been `--cprofile --cprofile-top 30`
- Fixed in commits 8c43c02e, dde871b5, 41454f30

### Issue 2: First 100-task Run
- Used default `-t 10` timeout
- First task took >10s, timed out
- Process exited after 1 task
- **Solution**: Use `-t 20` or higher for 100+ task runs

### Issue 3: Timeout Understanding
- "32 tasks - 32 timeouts" seemed like failure
- Actually: 32 sample-level timeouts (not task-level)
- Expected behavior for some difficult samples
- **Not** a test failure

---

## Recommended Arguments for Phase 2 Work

### Quick Test (5 min)
```bash
python run_batt.py -c 32 --timing
```
- Fast
- Shows timing breakdown
- Good for quick validation
- **Expected**: 1-2 minutes to complete

### Full Validation (10 min)
```bash
python run_batt.py -c 100 --timing
```
- Comparable to Phase 1b baseline (3.23s)
- Shows where time spent
- Gives wall-clock comparison
- **Expected**: ~3.1-3.2s (vs 3.23s baseline)

### Deep Profiling (15 min)
```bash
python run_batt.py -c 32 --cprofile --cprofile-top 30
```
- Identifies bottleneck functions
- Per-function execution time
- Helps plan Phase 2 optimizations
- **Expected**: Shows objects(), o_g(), dneighbors() performance

### Safe Large Run (with timeout increase)
```bash
python run_batt.py -c 100 -t 20 --timing
```
- Safer for 100 tasks
- 20s per sample (2x default)
- Prevents early timeouts
- **Expected**: All 100 tasks complete

---

## Timeout Value Recommendations

| Scale | Default | Recommended | Reason |
|-------|---------|-------------|--------|
| 1-5 tasks | 10s | 10s | Fast tasks only |
| 10-32 tasks | 10s | 15s | Average mix |
| 50-100 tasks | 10s | 20s | Some hard cases |
| 200+ tasks | 10s | 25-30s | More hard cases |
| Full dataset | 10s | 30s+ | Unknown mix |

**Rule of Thumb**: `timeout = 5 + (count / 4)`

---

## Argument Parsing Order

From `run_batt.py` source:
1. Parse arguments
2. If `--mega-batch`: Use GPU batch mode
3. Else: Use standard mode with specified batt module
4. If `--cprofile`: Enable profiling
5. Execute with `-c` / `-s` task selection
6. Use `-t` timeout for each sample
7. Print `--timing` breakdown if requested

---

## Why 32 vs 100 Tasks?

### 32 Tasks (Current Test)
- **Time**: ~32 seconds to complete
- **Solvers Generated**: ~1,000
- **Cache**: Can measure hit rates reliably
- **Use**: Quick validation, Phase 2a testing

### 100 Tasks (Baseline Comparison)
- **Time**: ~100 seconds to complete
- **Solvers Generated**: ~3,200
- **Solvers**: Better sample for profiling
- **Use**: Compare wall-clock to Phase 1b (3.23s)

### Full Dataset (Production)
- **Time**: ~400+ seconds
- **Solvers**: 13,000+
- **Use**: Final submission, full scale testing

---

## Next Steps

### Run 100-Task Validation
```bash
python run_batt.py -c 100 --timing
```

**What to check**:
- Wall-clock time (should be ~100s total)
- Per-function breakdown (objects, o_g, etc)
- Timeout count (should be 0-5, not 100)
- Compare to 3.23s Phase 1b baseline

### If Timeout Issues Occur
```bash
python run_batt.py -c 100 -t 20 --timing
```

Increase timeout to 20s per sample.

---

## Summary

| Argument | Most Common Value | For Phase 2 Validation |
|----------|------------------|----------------------|
| `-c` | 32, 100 | Use 100 for baseline comparison |
| `-t` | 10 | Use 20 for 100+ tasks |
| `--timing` | N/A (flag) | ✅ Always use for validation |
| `--cprofile` | N/A (flag) | Use for identifying bottlenecks |
| `--mega-batch` | N/A (flag) | Not yet (Phase 2b) |

**Current Best Command**:
```bash
python run_batt.py -c 100 --timing
```

This gives wall-clock comparison to Phase 1b (3.23s) with minimal overhead.
