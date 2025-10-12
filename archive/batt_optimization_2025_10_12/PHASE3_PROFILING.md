# Phase 3: Granular Profiling Implementation

## Overview

Phase 3 adds detailed timing instrumentation to identify the ~5-6s mystery overhead exposed by Phase 2's validation optimization.

## The Mystery

**Phase 2 Results Puzzle:**
- Validation improved 37.7x: 14s → 0.371s (stunning success!)
- Total time barely changed: 16.884s → 17.043s (expected ~3s reduction)
- **Missing time**: ~5-6s unaccounted overhead

**Where is the time going?**
```
Phase 2 breakdown (17.043s total):
- phase1_filter:        0.015s
- phase2_inline_batch:  0.599s  
- phase3a_validate:     0.371s  ← 37.7x faster!
- generate_expanded:    0.000s  ← clearly wrong!
- Everything else:      ~16s    ← THE MYSTERY
```

## Profiling Strategy

Break down the mystery overhead into measurable components:

### Phase 3b: Solver File Operations
Track time spent in:
- **ensure_dir**: Directory creation (called 32+ times)
- **check_save**: Checking existing files (called 32+ times)
- **symlink**: Creating symlinks (called 32+ times)
- **score_calc**: o_score.get() calls (called 32+ times)
- **overhead**: Residual unaccounted time

### Phase 4: Differ Processing
Track time spent in:
- **build**: Constructing differ source code
- **inline**: Batch inline_variables for differs
- **process**: File operations (ensure_dir, generate_expanded_content, symlink)

## Implementation

### Phase 3b Instrumentation

```python
# Initialize profiling counters
if prof is not None:
    phase3b_ensure_dir_time = 0
    phase3b_check_save_time = 0
    phase3b_symlink_time = 0
    phase3b_score_calc_time = 0

# Track each operation category in the loop
for data in validated_data:
    # Track ensure_dir
    if prof is not None:
        dir_start = timer()
    ensure_dir('solver_md5')
    if prof is not None:
        phase3b_ensure_dir_time += timer() - dir_start
    
    # Track check_save
    if prof is not None:
        save_start = timer()
    should_skip = check_save(solver_task, task_s_score, max_files)
    if prof is not None:
        phase3b_check_save_time += timer() - save_start
    
    # Track symlink
    if prof is not None:
        link_start = timer()
    symlink(solver_md5_path, solver_link)
    if prof is not None:
        phase3b_symlink_time += timer() - link_start
    
    # Track score calculations
    if prof is not None:
        score_start = timer()
    task_o_score = o_score.get(sol_solver_id, {}).get(name)
    if prof is not None:
        phase3b_score_calc_time += timer() - score_start

# Calculate residual overhead
if prof is not None:
    phase3b_total = timer() - phase3b_start
    tracked_time = (phase3b_ensure_dir_time + phase3b_check_save_time + 
                   phase3b_symlink_time + phase3b_score_calc_time)
    phase3b_overhead = phase3b_total - tracked_time
    
    prof['run_batt.phase3b_ensure_dir'] = phase3b_ensure_dir_time
    prof['run_batt.phase3b_check_save'] = phase3b_check_save_time
    prof['run_batt.phase3b_symlink'] = phase3b_symlink_time
    prof['run_batt.phase3b_score_calc'] = phase3b_score_calc_time
    prof['run_batt.phase3b_overhead'] = phase3b_overhead
```

### Phase 4 Instrumentation

```python
# Track Phase 4 subsections
if prof is not None:
    phase4_start = timer()
    phase4_build_time = 0
    phase4_inline_time = 0
    phase4_process_time = 0

# Track differ construction
if prof is not None:
    build_start = timer()
# ... build differ_data_list ...
if prof is not None:
    phase4_build_time = timer() - build_start

# Track batch inline
if prof is not None:
    inline_start = timer()
# ... ThreadPoolExecutor inline ...
if prof is not None:
    phase4_inline_time = timer() - inline_start

# Track file processing
if prof is not None:
    process_start = timer()
# ... differ file operations ...
if prof is not None:
    phase4_process_time = timer() - process_start

# Record totals
if prof is not None:
    phase4_total = timer() - phase4_start
    prof['run_batt.phase4_differs'] = phase4_total
    prof['run_batt.phase4_build'] = phase4_build_time
    prof['run_batt.phase4_inline'] = phase4_inline_time
    prof['run_batt.phase4_process'] = phase4_process_time
```

## Expected Output

When running on Kaggle with `--timing` flag, you'll see:

```
=== PROFILING RESULTS ===
run_batt.phase1_filter:         0.015
run_batt.phase2_inline_batch:   0.599
run_batt.phase3a_validate:      0.371
run_batt.phase3b_ensure_dir:    ?.???  ← NEW
run_batt.phase3b_check_save:    ?.???  ← NEW
run_batt.phase3b_symlink:       ?.???  ← NEW
run_batt.phase3b_score_calc:    ?.???  ← NEW
run_batt.phase3b_overhead:      ?.???  ← NEW
run_batt.phase4_differs:        ?.???
run_batt.phase4_build:          ?.???  ← NEW
run_batt.phase4_inline:         ?.???  ← NEW
run_batt.phase4_process:        ?.???  ← NEW
```

## Hypotheses

**Likely culprits for ~5-6s overhead:**

1. **ensure_dir (High probability)**
   - Called 32+ times for solvers
   - Called 2-3 times per differ (potentially hundreds)
   - Each call checks directory existence
   - Solution: Cache directory existence

2. **symlink (Medium probability)**
   - Called 32+ times for solvers
   - Called many times for differs
   - Filesystem operations can be slow
   - Solution: Batch or optimize creation

3. **generate_expanded_content (Medium probability)**
   - Currently shows 0.000s (measurement bug?)
   - Could be hiding significant time
   - Solution: Fix measurement, optimize if needed

4. **Loop overhead (Low probability)**
   - Pure Python iteration over 32 items
   - Unlikely to be 5s+
   - Solution: Add more granular profiling

## Next Steps

1. **Test on Kaggle** (5 minutes)
   ```bash
   python run_batt.py --timing -i 007bbfb7 -b tmp_batt_onerun_run
   ```

2. **Analyze results** (5 minutes)
   - Which metric shows the highest time?
   - Does phase3b_overhead remain large?
   - Does phase4_process dominate?

3. **Implement optimization** (30-60 minutes)
   - If ensure_dir: Cache directory checks
   - If symlink: Batch operations
   - If generate_expanded: Fix measurement and optimize
   - If overhead: Add more granular profiling

4. **Validate** (10 minutes)
   - Test on Kaggle again
   - Verify correctness
   - Measure actual speedup

## Success Criteria

- **Target**: 17s → 12-14s (1.2-1.4x improvement)
- **Overall**: 21.788s → 12-14s (1.6-1.8x total improvement)
- **Identification**: Know which operation causes overhead
- **Optimization**: Implement targeted fix with measurable impact

## Status

✅ **Phase 3b profiling**: Complete  
✅ **Phase 4 profiling**: Complete  
⏳ **Kaggle testing**: Pending  
⏳ **Optimization**: Pending (depends on test results)  
⏳ **Validation**: Pending  

## Files Modified

- **run_batt.py**: Added granular profiling to Phase 3b and Phase 4
  - Lines ~658-760: Phase 3b instrumentation
  - Lines ~755-835: Phase 4 instrumentation
  - No functional changes, only timing measurement

## Context

This is Phase 3 of a three-phase optimization:
- **Phase 1**: Filtering + batching (21.8s → 16.9s, ✅ complete)
- **Phase 2**: Parallel validation (16.9s → 17.0s, ✅ complete, exposed bottleneck)
- **Phase 3**: Find and fix overhead (17.0s → 12-14s target, 🔄 in progress)
