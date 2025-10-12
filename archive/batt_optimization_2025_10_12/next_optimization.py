#!/usr/bin/env python3
"""
Next optimization: Parallelize check_solver_speed() calls

Current bottleneck: ~14s validating 32 solvers sequentially
Target: ~3.5s with 4-way parallelism

Usage:
1. Apply the optimization below to run_batt.py
2. Test on Kaggle with --timing flag
3. Expect 3-4x speedup on validation phase
"""

# BEFORE (current code in run_batt.py Phase 3):
"""
for data in inlined_data:
    ...
    check_start = timer()
    timed_out = await check_solver_speed(total_data, solver_source, task_id, sol_solver_id, timeout)
    check_time = timer() - check_start
    ...
"""

# AFTER (optimized version):
"""
# Phase 3a: Batch validate all solvers in parallel
if prof is not None:
    phase3a_start = timer()

async def check_one_solver(data):
    solver_source = data['solver_source']
    sol_solver_id = data['sol_solver_id']
    check_start = timer()
    timed_out = await check_solver_speed(total_data, solver_source, task_id, sol_solver_id, timeout)
    check_time = timer() - check_start
    t_log = 11 - int(math.log(check_time))
    return {**data, 'timed_out': timed_out, 't_log': t_log, 'check_time': check_time}

# Validate all solvers in parallel (async)
import asyncio
validated_data = await asyncio.gather(*[check_one_solver(d) for d in inlined_data])

if prof is not None:
    prof['run_batt.phase3a_validate_batch'] = timer() - phase3a_start
    prof['run_batt.check_solver_speed'] = sum(d['check_time'] for d in validated_data)

# Phase 3b: Process validated results
if prof is not None:
    phase3b_start = timer()

for data in validated_data:
    sol_solver_id = data['sol_solver_id']
    inlined_source = data['inlined_source']
    md5_hash = data['md5_hash']
    t_log = data['t_log']
    
    # Prepare storage folder
    ensure_dir('solver_md5')
    solver_md5_path = f'solver_md5/{md5_hash}.py'
    
    # Expand to .py file (only if doesn't exist)
    expand_start = timer()
    if not Path(solver_md5_path).exists():
        generate_expanded_content(inlined_source, solver_md5_path)
    if prof is not None:
        prof['run_batt.generate_expanded'] += timer() - expand_start
    
    task_o_score = o_score.get(sol_solver_id)
    solver_score = f'solver_dir/solve_{task_id}/{task_o_score}/{t_log}'
    
    ensure_dir(solver_score)
    solver_link = f'{solver_score}/{md5_hash}.py'
    
    symlink(solver_md5_path, solver_link)
    
    # ... rest of processing (differs)

if prof is not None:
    prof['run_batt.phase3b_file_ops'] = timer() - phase3b_start
"""

print("""
Expected results after applying this optimization:

BEFORE:
  run_batt.check_solver_speed    ~14.0s  (32 solvers × 0.4s, sequential)
  run_batt.phase3_process         0.633s

AFTER:
  run_batt.phase3a_validate_batch ~3.5s  (32 solvers × 0.4s, 4-way parallel)
  run_batt.check_solver_speed    ~14.0s  (sum of all checks, for comparison)
  run_batt.phase3b_file_ops       0.633s

TOTAL SPEEDUP: 16.9s → ~6-8s (2-3x overall improvement)

Note: check_solver_speed will show the same total time (sum of all checks),
but phase3a_validate_batch shows the actual wall-clock time due to parallelism.
""")
