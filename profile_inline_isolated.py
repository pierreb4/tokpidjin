#!/usr/bin/env python3
"""
Isolated profiling of inline_variables() performance.
This runs on generated solvers from a recent batt module.

Usage:
    python profile_inline_isolated.py
    python profile_inline_isolated.py > profile_inline_isolated.log 2>&1
"""

import sys
import os
import random
import inspect
from timeit import default_timer as timer
from utils import inline_variables

def profile_inline_isolated():
    """Profile inline_variables on isolated solvers"""
    
    # Try to load the most recent batt module
    batt_module = None
    batt_file = "tmp_batt_onerun_run.py"
    
    if os.path.exists(batt_file):
        try:
            import importlib.util
            spec = importlib.util.spec_from_file_location("tmp_batt", batt_file)
            if spec and spec.loader:
                batt_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(batt_module)
        except Exception as e:
            print(f"Error loading {batt_file}: {e}", file=sys.stderr)
            return False
    
    if not batt_module:
        print(f"Error: Could not find or load {batt_file}", file=sys.stderr)
        print("Please run 'bash run_card.sh -c -1' first to generate a batt module", file=sys.stderr)
        return False
    
    # Extract solvers
    solvers = [s for s in dir(batt_module) if s.startswith('solve_')]
    differs = [d for d in dir(batt_module) if d.startswith('differ_')]
    
    print(f"Found {len(solvers)} solvers and {len(differs)} differs")
    print()
    
    # Profile solvers
    print("=" * 60)
    print("SOLVER PROFILING")
    print("=" * 60)
    times_solver = []
    errors_solver = []
    timeouts_solver = []
    
    sample_solvers = random.sample(solvers, min(20, len(solvers)))
    print(f"Profiling {len(sample_solvers)} solvers...\n")
    
    for solver_name in sorted(sample_solvers):
        try:
            solver = getattr(batt_module, solver_name)
            source = inspect.getsource(solver)
            
            t0 = timer()
            try:
                result = inline_variables(source, timeout_seconds=1)
                dt = timer() - t0
                times_solver.append(dt)
                status = "OK"
                ms_str = f"{dt*1000:7.2f}ms"
            except TimeoutError as e:
                dt = timer() - t0
                timeouts_solver.append(dt)
                status = "TIMEOUT"
                ms_str = f">{dt*1000:6.2f}ms"
            except Exception as e:
                dt = timer() - t0
                errors_solver.append((solver_name, type(e).__name__, str(e)[:40]))
                status = type(e).__name__
                ms_str = f"{dt*1000:7.2f}ms"
            
            print(f"  {solver_name:25s}: {ms_str} - {status}")
        except Exception as e:
            print(f"  {solver_name:25s}: ERROR - {type(e).__name__}: {str(e)[:40]}")
            errors_solver.append((solver_name, type(e).__name__, str(e)[:40]))
    
    print()
    print("SOLVER STATISTICS:")
    if times_solver:
        print(f"  Completed:  {len(times_solver)}/{len(sample_solvers)}")
        print(f"  Mean time:  {sum(times_solver)/len(times_solver)*1000:.2f}ms")
        print(f"  Max time:   {max(times_solver)*1000:.2f}ms")
        print(f"  Min time:   {min(times_solver)*1000:.2f}ms")
    if timeouts_solver:
        print(f"  Timeouts:   {len(timeouts_solver)}")
    if errors_solver:
        print(f"  Errors:     {len(errors_solver)}")
        for name, err_type, msg in errors_solver[:3]:
            print(f"    - {name}: {err_type}: {msg}")
    
    # Profile differs
    print()
    print("=" * 60)
    print("DIFFER PROFILING")
    print("=" * 60)
    times_differ = []
    errors_differ = []
    timeouts_differ = []
    
    sample_differs = random.sample(differs, min(10, len(differs)))
    print(f"Profiling {len(sample_differs)} differs...\n")
    
    for differ_name in sorted(sample_differs):
        try:
            differ = getattr(batt_module, differ_name)
            source = inspect.getsource(differ)
            
            t0 = timer()
            try:
                result = inline_variables(source, timeout_seconds=1)
                dt = timer() - t0
                times_differ.append(dt)
                status = "OK"
                ms_str = f"{dt*1000:7.2f}ms"
            except TimeoutError as e:
                dt = timer() - t0
                timeouts_differ.append(dt)
                status = "TIMEOUT"
                ms_str = f">{dt*1000:6.2f}ms"
            except Exception as e:
                dt = timer() - t0
                errors_differ.append((differ_name, type(e).__name__, str(e)[:40]))
                status = type(e).__name__
                ms_str = f"{dt*1000:7.2f}ms"
            
            print(f"  {differ_name:25s}: {ms_str} - {status}")
        except Exception as e:
            print(f"  {differ_name:25s}: ERROR - {type(e).__name__}: {str(e)[:40]}")
            errors_differ.append((differ_name, type(e).__name__, str(e)[:40]))
    
    print()
    print("DIFFER STATISTICS:")
    if times_differ:
        print(f"  Completed:  {len(times_differ)}/{len(sample_differs)}")
        print(f"  Mean time:  {sum(times_differ)/len(times_differ)*1000:.2f}ms")
        print(f"  Max time:   {max(times_differ)*1000:.2f}ms")
        print(f"  Min time:   {min(times_differ)*1000:.2f}ms")
    if timeouts_differ:
        print(f"  Timeouts:   {len(timeouts_differ)}")
    if errors_differ:
        print(f"  Errors:     {len(errors_differ)}")
        for name, err_type, msg in errors_differ[:3]:
            print(f"    - {name}: {err_type}: {msg}")
    
    # Summary
    print()
    print("=" * 60)
    print("OVERALL SUMMARY")
    print("=" * 60)
    total_success = len(times_solver) + len(times_differ)
    total_timeouts = len(timeouts_solver) + len(timeouts_differ)
    total_errors = len(errors_solver) + len(errors_differ)
    total_tests = total_success + total_timeouts + total_errors
    
    print(f"Total tests:    {total_tests}")
    print(f"Success:        {total_success} ({100*total_success/total_tests:.1f}%)")
    if total_timeouts:
        print(f"Timeouts:       {total_timeouts} ({100*total_timeouts/total_tests:.1f}%)")
    if total_errors:
        print(f"Errors:         {total_errors} ({100*total_errors/total_tests:.1f}%)")
    
    all_times = times_solver + times_differ
    if all_times:
        print()
        print(f"Overall mean:   {sum(all_times)/len(all_times)*1000:.2f}ms")
        print(f"Overall max:    {max(all_times)*1000:.2f}ms")
        print(f"Overall min:    {min(all_times)*1000:.2f}ms")
    
    return True

if __name__ == "__main__":
    try:
        success = profile_inline_isolated()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"Fatal error: {type(e).__name__}: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
