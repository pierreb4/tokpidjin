# ✅ CORRECTED KAGGLE VALIDATION INSTRUCTIONS

**Date**: October 17, 2025, 09:28 CEST  
**Status**: ✅ **DOCUMENTATION CORRECTED**  
**Latest Commit**: 8c43c02e

---

## Corrected Kaggle Validation Command

### Option 1: Full Profiling with cProfile (Recommended for detailed analysis)

```bash
cd /Users/pierre/dsl/tokpidjin
git pull origin main
python run_batt.py -c 100 --cprofile --cprofile-top 30
```

**What this does**:
- Runs 100 tasks
- Enables cProfile (detailed function profiling)
- Shows top 30 functions by cumulative time
- GPU auto-enabled if available
- Generates 13,200 solvers

**Expected output**:
- Wall-clock time: 3.08-3.15s (target) vs 3.23s baseline
- Top 30 functions list (look for objects, o_g timing)
- Solver count: 13,200
- Errors: 0
- Success rate: 100%

---

### Option 2: Quick Wall-Clock Only (Faster, less overhead)

```bash
cd /Users/pierre/dsl/tokpidjin
git pull origin main
python run_batt.py -c 100 --timing
```

**What this does**:
- Runs 100 tasks
- Enables lightweight timing breakdown
- GPU auto-enabled if available
- Less profiling overhead

**Expected output**:
- Wall-clock time: 3.08-3.15s (target)
- Lightweight timing breakdown
- Solver count: 13,200
- Errors: 0
- Success rate: 100%

---

## Why These Commands?

### About `--gpu --profile`
- ❌ These arguments don't exist in run_batt.py
- GPU is **automatically detected and enabled** if available
- No need for explicit flag

### About `--cprofile`
- ✅ Enables cProfile profiling (built-in Python tool)
- ✅ Shows function-level performance data
- Shows which functions take the most time
- Perfect for validating that objects() and o_g() improved

### About `--timing`
- ✅ Lightweight timing breakdown
- ✅ Less overhead than cProfile
- Good for quick wall-clock measurements
- Still shows main categories (framework, DSL, etc.)

---

## What to Expect in Output

### With `--cprofile`:

```
Kaggle GPU Support: True (1 devices)
  GPU 0: Compute 7.5, Memory: 24.0GB
✓ Kaggle GPU Optimizer initialized

... (solver generation output) ...

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 234539    0.015    0.000    0.232    0.000 dsl.py:XXXX(dneighbors)
  13200    0.005    0.000    0.385    0.000 dsl.py:YYYY(objects)
  ...

Wall-clock: 3.10s
```

### With `--timing`:

```
Kaggle GPU Support: True (1 devices)
  GPU 0: Compute 7.5, Memory: 24.0GB

... (solver generation output) ...

Timing Breakdown:
  Framework: 2.12s (68.5%)
  DSL: 0.98s (31.5%)

Wall-clock: 3.10s
```

---

## Success Criteria (Same as Before)

✅ **PASS** if:
- Wall-clock < 3.23s (any improvement counts)
- Solvers generated = 13,200
- Errors = 0
- Success rate = 100%

⚠️ **EXCELLENT** if:
- Wall-clock < 3.15s (good improvement)
- All other metrics same

🎉 **OUTSTANDING** if:
- Wall-clock < 3.10s (excellent improvement)
- All other metrics same

---

## After You Run the Test

### 1. Capture the Output

Save or note:
- Wall-clock time
- objects() time (if visible in profiler output)
- o_g() time (if visible)
- Solver count
- Error count
- Success rate

### 2. Compare with Phase 1b Baseline

```
Phase 1b (Oct 16):  3.23s (with profiler overhead)
Phase 2a expected:  3.08-3.15s
Your measurement:   _______ s

Improvement:        _______ s (-_____%)
```

### 3. Document Results

Create `PHASE2A_VALIDATION_RESULTS.md` with:
- Command used
- Full output (or key metrics)
- Wall-clock comparison
- Per-function improvements (if visible)
- Assessment: Good/Excellent/Outstanding

### 4. Next Steps Decision

Based on results:
- If improvement ≥ 0.05s: Continue with Phase 2a Step 2
- If improvement < 0.05s: Debug or try alternative approach
- If excellent (≥ 0.15s): Decide on Phase 2b (GPU acceleration)

---

## Available run_batt.py Arguments (Reference)

```
-c, --count             Number of tasks to process
-i, --task_ids          Specific task IDs
-s, --start             Start task index
-t, --timeout           Timeout per solver (seconds)
-b, --batt_import       Which batt module to import
--timing                Print lightweight timing breakdown
--cprofile              Run with cProfile profiling
--cprofile-top N        Number of top functions to show
--mega-batch            Use mega-batch GPU processing
--batch-size N          Batch size for mega-batch mode
```

**Note**: GPU is auto-detected and enabled if available. No explicit `--gpu` flag needed.

---

## Quick Reference

| Scenario | Command | When to Use |
|----------|---------|-----------|
| Full profiling | `python run_batt.py -c 100 --cprofile --cprofile-top 30` | Deep analysis needed |
| Quick test | `python run_batt.py -c 100 --timing` | Just need wall-clock |
| Production run | `python run_batt.py -c 100` | No output overhead |

---

## Troubleshooting

### If you get command errors:

```bash
# Check available arguments
python run_batt.py -h

# Run with minimal args
python run_batt.py -c 100
```

### If GPU not detected:

- No problem! Script falls back to CPU
- GPU auto-enables if available
- Output will show: "Kaggle GPU Support: True/False"

### If measurement seems inconsistent:

- Profiler overhead can vary (-0.3 to 0.5s)
- Run multiple times if unsure
- Compare with and without `--cprofile` for clearer result

---

## Next Steps

1. ✅ Pull latest (commit 8c43c02e)
2. ⏳ **Run validation** using corrected command
3. ⏳ **Capture results** (wall-clock, solver count, errors)
4. ⏳ **Compare** with Phase 1b baseline (3.23s)
5. ⏳ **Document** results in PHASE2A_VALIDATION_RESULTS.md
6. ⏳ **Decide** on Phase 2a Step 2 or Phase 2b

---

**Status**: ✅ **READY FOR CORRECTED KAGGLE VALIDATION**

**Try Option 1 (full profiling) first** for detailed data about the improvements!
