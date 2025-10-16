#!/usr/bin/env python3
"""
Profile generator expressions to find source of 161,146 calls

This script runs card.py with profiling and specifically looks for <genexpr> calls,
showing call stacks to identify where they're coming from.

Usage:
    python profile_genexpr.py
"""

import cProfile
import pstats
import io
import sys
import traceback

# Profile card.py execution
def profile_card():
    """Run card.py with profiling enabled"""
    import card
    
    # Simulate minimal card execution
    try:
        # This would normally be called by main:
        # card.gen(count=2)
        pass
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()


if __name__ == '__main__':
    profiler = cProfile.Profile()
    
    print("Profiling card.py for <genexpr> calls...")
    print()
    
    profiler.enable()
    
    # Import and run card.py
    import card
    
    profiler.disable()
    
    # Get stats
    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    
    # Find all <genexpr> calls
    print("=" * 80)
    print("GENERATOR EXPRESSION ANALYSIS")
    print("=" * 80)
    print()
    
    genexpr_functions = []
    genexpr_total_time = 0
    genexpr_total_calls = 0
    
    for func, (cc, nc, tt, ct, callers) in stats.stats.items():
        filename, line, func_name = func
        
        if '<genexpr>' in func_name:
            genexpr_functions.append({
                'func': func,
                'calls': nc,
                'total_time': tt,
                'cumulative_time': ct,
                'per_call': tt / nc if nc > 0 else 0,
                'callers': callers
            })
            genexpr_total_time += tt
            genexpr_total_calls += nc
    
    if genexpr_functions:
        print(f"Found {len(genexpr_functions)} <genexpr> occurrences")
        print(f"Total calls: {genexpr_total_calls}")
        print(f"Total time: {genexpr_total_time:.4f}s")
        print()
        
        print("TOP GENEXPR CALLERS (who is calling <genexpr>):")
        print("-" * 80)
        
        # Aggregate by caller
        caller_stats = {}
        for gexpr in genexpr_functions:
            for caller_func, (cc, nc, tt, ct) in gexpr['callers'].items():
                if caller_func not in caller_stats:
                    caller_stats[caller_func] = {'calls': 0, 'time': 0}
                caller_stats[caller_func]['calls'] += nc
                caller_stats[caller_func]['time'] += tt
        
        # Sort by most calls
        sorted_callers = sorted(caller_stats.items(), key=lambda x: x[1]['calls'], reverse=True)
        
        for caller_func, stats_data in sorted_callers[:20]:
            caller_file, caller_line, caller_name = caller_func
            print(f"{caller_name:<40} calls: {stats_data['calls']:>10}  time: {stats_data['time']:>10.4f}s")
            print(f"  Location: {caller_file}:{caller_line}")
            print()
    else:
        print("No <genexpr> functions found in this profiling run")
    
    # Show top functions overall
    print()
    print("=" * 80)
    print("TOP 20 FUNCTIONS OVERALL")
    print("=" * 80)
    stats.print_stats(20)

