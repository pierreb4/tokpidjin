# run_batt.py Performance Optimizations

**Date:** October 12, 2025  
**Goal:** Speed up batt execution by reducing candidate processing overhead

## Problem Analysis

From Kaggle L4x4 GPU profiling:
```
Total time:     21.788s
Actual batt:     0.468s (2%)
Overhead:       21.320s (98%)  ← THE PROBLEM!

Breakdown of overhead:
- check_batt:    15.426s (processing 149 candidates)
- inline_variables: 3.645s (called 149 times!)
- expand_solver: 0.169s
```

**Key insight:** We process **149 candidates** sequentially, calling expensive AST operations on each one.

## Optimizations Implemented

### 1. **Early Duplicate Filtering** (Phase 1)
**Before:** Build solver body → inline → compute md5 → check if duplicate  
**After:** Build solver body → compute body hash → filter duplicates early

```python
# Quick dedup check using body hash before expensive inline_variables
body_hash = hashlib.md5(solver_body.encode()).hexdigest()
if body_hash in seen_bodies:
    continue  # Skip before expensive operations!
```

**Expected impact:** Reduces candidates from ~149 to ~50-100 unique ones

### 2. **Batch Inline Variables** (Phase 2)
**Before:** `for candidate in all_o: inline_variables(candidate)` (sequential)  
**After:** Batch all candidates and process in parallel with ThreadPoolExecutor

```python
def inline_one(data):
    inlined = inline_variables(data['solver_source'])
    md5 = hashlib.md5(inlined.encode()).hexdigest()
    return {**data, 'inlined_source': inlined, 'md5_hash': md5}

with ThreadPoolExecutor(max_workers=4) as executor:
    inlined_data = list(executor.map(inline_one, candidate_data))
```

**Expected impact:** 
- 4x parallelism = ~3.645s → ~1s (with 4 cores)
- Reduced candidates = even faster

### 3. **Batch Differ Processing** (Phase 4)
**Before:** Process differs sequentially inside main loop  
**After:** Collect all differs, batch inline them in parallel

```python
# Collect all differ data first
differ_data_list = []
for name, last_t in d_score.last_t.items():
    # Build differ bodies...
    differ_data_list.append(differ_data)

# Batch inline differs
with ThreadPoolExecutor(max_workers=4) as executor:
    inlined_differs = list(executor.map(inline_differ, differ_data_list))
```

**Expected impact:** Additional 20-30% speedup on differ processing

### 4. **Enhanced Profiling**
Added phase timing to measure impact:
- `run_batt.phase1_filter` - Early filtering and body building
- `run_batt.phase2_inline_batch` - Batch inlining of solvers
- `run_batt.phase3_process` - File I/O and symlinks
- `run_batt.phase4_differs` - Batch inlining of differs

## Expected Performance Improvement

### Before Optimization:
```
Total:          21.788s
├─ check_batt:  15.426s
│  ├─ inline:    3.645s (149 calls)
│  ├─ process:  ~11s (file I/O, tracking)
│  └─ expand:    0.169s
└─ batt exec:    0.468s
```

### After Optimization (Expected):
```
Total:          ~8-10s (2-3x faster!)
├─ check_batt:   5-7s
│  ├─ phase1:    ~1s (filter 149→50 candidates)
│  ├─ phase2:    ~0.9s (batch inline 50 solvers, 4x parallel)
│  ├─ phase3:    ~3s (process 50 candidates)
│  └─ phase4:    ~0.5s (batch inline differs, parallel)
└─ batt exec:    0.468s (unchanged)
```

**Expected speedup: 2-3x overall, 4x on inline_variables specifically**

## Key Architectural Changes

### Old Flow:
```
for candidate in all_o:  # 149 candidates
    build_body()
    inline_variables()    # ← Sequential, slow!
    compute_md5()
    check_duplicate()     # ← Too late!
    check_solver_speed()
    generate_expanded()
    save_files()
```

### New Flow:
```
# Phase 1: Fast filter (no AST parsing)
for candidate in all_o:
    build_body()
    body_hash = md5(body)
    if duplicate: skip     # ← Early exit!

# Phase 2: Batch expensive operations
parallel_inline_all_candidates()  # ← 4x parallelism!

# Phase 3: Process results
for result in inlined_data:
    check_solver_speed()
    generate_expanded()
    save_files()

# Phase 4: Batch differs
parallel_inline_all_differs()     # ← Bonus speedup!
```

## Testing

### On Local Machine:
```bash
chmod +x test_run_batt_speed.sh
./test_run_batt_speed.sh
```

### On Kaggle:
Upload optimized `run_batt.py` and run with `--timing` flag:
```bash
python run_batt.py --timing -i 007bbfb7 -b tmp_batt_onerun_run
```

Look for these new metrics:
- `run_batt.phase1_filter`
- `run_batt.phase2_inline_batch`
- `run_batt.phase3_process`
- `run_batt.phase4_differs`
- "Filtered to X unique candidates (from Y)"

### Expected Results:
- Total time: **21.788s → 8-10s** (2-3x faster)
- inline_variables: **3.645s → 0.9s** (4x faster)
- Candidates processed: **149 → 50-100** (fewer duplicates)

## Additional Optimization Opportunities

If needed, further improvements:

1. **Cache track_solution results** - Many candidates share solution paths
2. **Parallelize generate_expanded_content** - Currently sequential
3. **Batch file I/O** - Write multiple files at once
4. **GPU-accelerate AST parsing** - If becomes bottleneck again
5. **Lazy evaluation** - Only inline/expand when actually needed

## Files Modified

- `run_batt.py` - Main optimization implementation
- `test_run_batt_speed.sh` - Testing script

## Backward Compatibility

✅ **100% compatible** - No changes to:
- Function signatures
- Return values
- File formats
- Command-line arguments

The only visible changes:
- New profiling metrics (phase1-4)
- Debug message: "Filtered to X unique candidates"
- Faster execution!

## Status

✅ **Code complete** - Ready for testing  
⏳ **Performance validation** - Need to test on Kaggle L4x4  
📊 **Profiling data** - Will update after Kaggle run  

---

## Quick Reference

**Problem:** 98% overhead processing 149 candidates  
**Solution:** Filter early + batch parallelize inline_variables  
**Expected:** 2-3x speedup (21s → 8s)  
**Risk:** Low (no API changes, parallel-safe operations)  
**Testing:** `./test_run_batt_speed.sh` or on Kaggle with `--timing`
