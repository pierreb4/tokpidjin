#!/usr/bin/env python3
"""
Stress test inline_variables() with different timeout values.
This tests the performance impact of different timeout settings.

Usage:
    python profile_inline_stress.py
    python profile_inline_stress.py > profile_inline_stress.log 2>&1
"""

import sys
import os
import random
import inspect
from timeit import default_timer as timer
from utils import inline_variables

def profile_inline_stress():
    """Test different timeout values on sample solvers"""
    
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
    
    # Extract and sample solvers
    solvers = [s for s in dir(batt_module) if s.startswith('solve_')]
    sample_solvers = random.sample(solvers, min(30, len(solvers)))
    
    print(f"Loading {len(sample_solvers)} solvers for stress testing...")
    
    # Pre-load all solver sources
    solver_sources = {}
    for solver_name in sample_solvers:
        try:
            solver = getattr(batt_module, solver_name)
            solver_sources[solver_name] = inspect.getsource(solver)
        except Exception as e:
            print(f"Warning: Could not get source for {solver_name}: {e}", file=sys.stderr)
    
    print(f"Successfully loaded {len(solver_sources)} solver sources")
    print()
    
    if not solver_sources:
        print("Error: No solver sources loaded", file=sys.stderr)
        return False
    
    # Test different timeout values
    TIMEOUTS = [0.1, 0.5, 1.0, 2.0, 5.0]
    
    print("=" * 80)
    print("TIMEOUT STRESS TEST")
    print("=" * 80)
    print(f"Testing {len(solver_sources)} solvers with different timeout values")
    print()
    print(f"{'Timeout':>8s} | {'Success':>7s} | {'Timeout':>7s} | {'Error':>7s} | "
          f"{'Success%':>8s} | {'Avg Time':>10s}")
    print("-" * 80)
    
    timeout_results = []
    
    for timeout_val in TIMEOUTS:
        success_count = 0
        timeout_count = 0
        error_count = 0
        total_time = 0
        times = []
        
        for solver_name, source in solver_sources.items():
            t0 = timer()
            try:
                result = inline_variables(source, timeout_seconds=timeout_val)
                dt = timer() - t0
                total_time += dt
                times.append(dt)
                success_count += 1
            except TimeoutError:
                dt = timer() - t0
                total_time += dt
                timeout_count += 1
            except Exception as e:
                dt = timer() - t0
                total_time += dt
                error_count += 1
        
        success_pct = 100 * success_count / len(solver_sources) if solver_sources else 0
        avg_time = total_time / len(solver_sources) if solver_sources else 0
        
        timeout_results.append({
            'timeout': timeout_val,
            'success': success_count,
            'timeout_count': timeout_count,
            'error_count': error_count,
            'avg_time': avg_time,
            'times': times
        })
        
        print(f"{timeout_val:7.1f}s | {success_count:7d} | {timeout_count:7d} | "
              f"{error_count:7d} | {success_pct:7.1f}% | {avg_time*1000:9.2f}ms")
    
    print()
    print("=" * 80)
    print("ANALYSIS")
    print("=" * 80)
    
    # Find best timeout (highest success with lowest overhead)
    best_result = max(timeout_results, key=lambda r: r['success'])
    print(f"\nHighest success rate: {best_result['timeout']}s with {best_result['success']} successes")
    
    # Show statistics for current timeout (1.0s)
    current = next((r for r in timeout_results if r['timeout'] == 1.0), None)
    if current:
        print(f"\nCurrent timeout (1.0s) statistics:")
        print(f"  Success count:  {current['success']}/{len(solver_sources)} ({100*current['success']/len(solver_sources):.1f}%)")
        print(f"  Timeout count:  {current['timeout_count']}")
        print(f"  Error count:    {current['error_count']}")
        print(f"  Average time:   {current['avg_time']*1000:.2f}ms")
        
        if current['times']:
            sorted_times = sorted(current['times'])
            p50 = sorted_times[len(sorted_times)//2]
            p95 = sorted_times[int(len(sorted_times)*0.95)]
            p99 = sorted_times[int(len(sorted_times)*0.99)]
            print(f"  Percentiles:    p50={p50*1000:.2f}ms, p95={p95*1000:.2f}ms, p99={p99*1000:.2f}ms")
    
    # Recommendations
    print("\n" + "=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)
    
    if current and current['timeout_count'] == 0 and current['error_count'] == 0:
        max_time = max(current['times'])*1000
        if max_time < 50:
            print(f"✓ 1.0s timeout is conservative (max observed: {max_time:.1f}ms)")
            print("  Recommendation: Can reduce to 0.5s for faster error detection")
        elif max_time < 100:
            print(f"✓ 1.0s timeout is reasonable (max observed: {max_time:.1f}ms)")
            print("  Recommendation: Keep at 1.0s or try 0.5s")
        elif max_time < 500:
            print(f"✓ 1.0s timeout is adequate (max observed: {max_time:.1f}ms)")
            print("  Recommendation: Keep at 1.0s")
        else:
            print(f"⚠ 1.0s timeout may be tight (max observed: {max_time:.1f}ms)")
            print("  Recommendation: Consider increasing to 2.0s")
    elif current and current['timeout_count'] > 0:
        print(f"⚠ {current['timeout_count']} timeouts with 1.0s timeout")
        print("  Check if these are:")
        print("  1. AST errors (need upstream fix)")
        print("  2. Legitimate slow inlining (increase timeout)")
        print("  3. Infinite loops (keep timeout to catch them)")
        
        # Check if increasing timeout helps
        two_sec = next((r for r in timeout_results if r['timeout'] == 2.0), None)
        if two_sec and two_sec['timeout_count'] < current['timeout_count']:
            reduced = current['timeout_count'] - two_sec['timeout_count']
            print(f"\n  2.0s timeout would catch {reduced} more cases")
            print("  Recommendation: Increase to 2.0s if these aren't AST errors")
    else:
        print("✓ 1.0s timeout is working well")
        print("  Recommendation: Keep at 1.0s unless profiling shows otherwise")
    
    return True

if __name__ == "__main__":
    try:
        success = profile_inline_stress()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"Fatal error: {type(e).__name__}: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
