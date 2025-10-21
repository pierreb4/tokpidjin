#!/usr/bin/env python3
"""
Simple profiling of inline_variables() using solvers from solvers.py

This is much simpler than the previous approach - it loads actual solver
functions from the main solvers module and profiles them directly.

Usage:
    python profile_inline_simple.py
    python profile_inline_simple.py > profile.log 2>&1
"""

import sys
import os
import random
from timeit import default_timer as timer
from utils import inline_variables

def profile_inline_simple():
    """Profile inline_variables on real solvers from solvers.py"""
    
    try:
        import solvers
    except ImportError as e:
        print(f"\nError: Could not import solvers module: {e}", file=sys.stderr)
        print(f"Make sure solvers.py exists in the current directory", file=sys.stderr)
        return False
    
    # Get all solver functions (solve_*)
    import inspect
    solvers_list = []
    for name, obj in inspect.getmembers(solvers):
        if name.startswith('solve_') and callable(obj):
            try:
                source = inspect.getsource(obj)
                solvers_list.append((name, source))
            except Exception:
                pass
    
    if not solvers_list:
        print(f"\nError: No solvers found in solvers.py", file=sys.stderr)
        print(f"Available items starting with 'solve_': {[name for name, _ in inspect.getmembers(solvers) if name.startswith('solve_')]}", file=sys.stderr)
        return False
    
    print(f"Found {len(solvers_list)} solvers to profile\n")
    
    # Profile a sample
    sample_size = min(30, len(solvers_list))
    sample = random.sample(solvers_list, sample_size)
    
    print("=" * 70)
    print("INLINE_VARIABLES PROFILING (from solvers.py)")
    print("=" * 70)
    print(f"\nProfiling {sample_size} solvers with timeout_seconds=1.0\n")
    print(f"{'Solver Name':30s} | {'Time (ms)':>10s} | Status")
    print("-" * 70)
    
    times = []
    timeouts = []
    errors = []
    
    for solver_name, source_code in sample:
        t0 = timer()
        try:
            result = inline_variables(source_code, timeout_seconds=1.0)
            dt = timer() - t0
            times.append(dt)
            print(f"{solver_name:30s} | {dt*1000:10.2f}ms | OK")
        except TimeoutError as e:
            dt = timer() - t0
            timeouts.append(solver_name)
            print(f"{solver_name:30s} | >{dt*1000:9.2f}ms | TIMEOUT")
        except Exception as e:
            dt = timer() - t0
            errors.append((solver_name, type(e).__name__))
            print(f"{solver_name:30s} | {dt*1000:10.2f}ms | {type(e).__name__}")
    
    # Statistics
    print("\n" + "=" * 70)
    print("STATISTICS")
    print("=" * 70)
    
    total = len(sample)
    success = len(times)
    print(f"\nTotal solvers tested:  {total}")
    print(f"Successful:            {success} ({100*success/total:.1f}%)")
    
    if timeouts:
        print(f"Timeouts:              {len(timeouts)} ({100*len(timeouts)/total:.1f}%)")
    if errors:
        print(f"Errors:                {len(errors)} ({100*len(errors)/total:.1f}%)")
    
    if times:
        print(f"\nTiming Statistics (successful runs):")
        print(f"  Mean:                {sum(times)/len(times)*1000:.2f}ms")
        print(f"  Min:                 {min(times)*1000:.2f}ms")
        print(f"  Max:                 {max(times)*1000:.2f}ms")
        
        sorted_times = sorted(times)
        if len(sorted_times) > 1:
            p50 = sorted_times[len(sorted_times)//2]
            p95 = sorted_times[max(0, int(len(sorted_times)*0.95-1))]
            p99 = sorted_times[max(0, int(len(sorted_times)*0.99-1))]
            print(f"  Percentiles:")
            print(f"    p50:               {p50*1000:.2f}ms")
            print(f"    p95:               {p95*1000:.2f}ms")
            print(f"    p99:               {p99*1000:.2f}ms")
    
    # Recommendations
    print("\n" + "=" * 70)
    print("RECOMMENDATIONS")
    print("=" * 70)
    
    if len(timeouts) > 0:
        print(f"\n⚠️  Found {len(timeouts)} timeouts with current 1.0s timeout")
        print(f"    Consider increasing timeout to 2.0s")
        print(f"    Or investigate if these are AST errors")
    elif times and max(times)*1000 < 50:
        print(f"\n✓  All solvers inline very fast (max {max(times)*1000:.0f}ms)")
        print(f"    Can safely reduce timeout to 0.5s for faster error detection")
    elif times and max(times)*1000 < 100:
        print(f"\n✓  All solvers inline quickly (max {max(times)*1000:.0f}ms)")
        print(f"    Current 1.0s timeout is good")
    elif times and max(times)*1000 < 500:
        print(f"\n✓  Solvers inline in reasonable time (max {max(times)*1000:.0f}ms)")
        print(f"    Current 1.0s timeout is adequate")
    else:
        print(f"\n⚠️  Some solvers are slow (max {max(times)*1000:.0f}ms)")
        print(f"    May need to increase timeout to 2.0s or investigate")
    
    return True

if __name__ == "__main__":
    try:
        success = profile_inline_simple()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\nFatal error: {type(e).__name__}: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
