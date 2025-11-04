#!/usr/bin/env python3
"""
Phase 4 Framework Profiling - Identify Bottleneck Functions

Purpose: Use cProfile to understand where the 74% framework overhead comes from
Usage: python profile_framework.py -c 10 --timing
Output: Detailed function-level timing analysis

Analysis will show:
1. Which functions consume most CPU time
2. How many times functions are called
3. Cumulative time per function
4. Call chains and relationships
"""

import cProfile
import pstats
import io
import sys
import asyncio
from pathlib import Path

# Import the main run_batt module
sys.path.insert(0, str(Path(__file__).parent))

# We'll wrap run_batt to profile it
import run_batt as rb_module


def profile_run_batt_main(count=10, timeout=1):
    """
    Profile the main run_batt execution path.
    
    This captures the actual timing of the framework without GPU overhead.
    """
    # Create profiler
    pr = cProfile.Profile()
    
    # Start profiling
    pr.enable()
    
    try:
        # Run the main function with specified count
        sys.argv = ['run_batt.py', '-c', str(count), '--timing']
        asyncio.run(rb_module.main())
    finally:
        # Stop profiling
        pr.disable()
    
    return pr


def analyze_profile(pr, sort_by='cumulative', top_n=50):
    """
    Analyze profiling results and print in useful format.
    
    Args:
        pr: cProfile.Profile object
        sort_by: How to sort results ('cumulative', 'time', 'calls', etc.)
        top_n: Number of top functions to show
    """
    # Create string buffer for output
    s = io.StringIO()
    
    # Sort by cumulative time by default
    ps = pstats.Stats(pr, stream=s)
    ps.strip_dirs()
    ps.sort_stats(sort_by)
    
    # Print top N functions
    print(f"\n{'='*80}")
    print(f"FRAMEWORK PROFILING ANALYSIS - Top {top_n} Functions by {sort_by} Time")
    print(f"{'='*80}\n")
    
    ps.print_stats(top_n)
    
    # Print call chains for top functions
    print(f"\n{'='*80}")
    print("TOP FUNCTIONS CALL CHAINS")
    print(f"{'='*80}\n")
    
    # Get top 10 functions and show who calls them
    top_funcs = []
    for func, (cc, nc, tt, ct, callers) in ps.stats.items():
        if len(top_funcs) < 10:
            top_funcs.append((func, ct))  # ct = cumulative time
    
    top_funcs.sort(key=lambda x: x[1], reverse=True)
    
    for func, cum_time in top_funcs:
        print(f"\n{func[2]} (cumulative: {cum_time:.3f}s)")
        if func in ps.stats:
            _, _, _, _, callers = ps.stats[func]
            if callers:
                print("  Called by:")
                for caller_func, call_info in list(callers.items())[:3]:
                    print(f"    - {caller_func[2]}")
    
    print("\n" + s.getvalue())


def main():
    """Run profiling and analysis."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Profile run_batt framework')
    parser.add_argument('-c', '--count', type=int, default=10,
                       help='Number of tasks to profile (default: 10)')
    parser.add_argument('-t', '--timeout', type=float, default=1,
                       help='Timeout per task (default: 1)')
    parser.add_argument('--sort', type=str, default='cumulative',
                       choices=['cumulative', 'time', 'calls', 'name'],
                       help='Sort by (default: cumulative time)')
    parser.add_argument('--top', type=int, default=50,
                       help='Show top N functions (default: 50)')
    parser.add_argument('--output', type=str, default=None,
                       help='Save profile to file (for further analysis)')
    
    args = parser.parse_args()
    
    print(f"\nStarting profiling of {args.count} tasks...")
    print(f"This will run the full pipeline and capture CPU time by function.\n")
    
    # Run profiling
    pr = profile_run_batt_main(count=args.count, timeout=args.timeout)
    
    # Analyze and display results
    analyze_profile(pr, sort_by=args.sort, top_n=args.top)
    
    # Save profile if requested
    if args.output:
        pr.dump_stats(args.output)
        print(f"\nProfile saved to: {args.output}")
        print(f"Analyze with: python -m pstats {args.output}")


if __name__ == '__main__':
    main()
