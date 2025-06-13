"""
Comprehensive Solver Analysis Tool

This script combines the functionality of track_solver.py and trace_solver_calls.py
to provide complete analysis of DSL function usage across all solvers.

Usage:
    python analyze_all_solvers.py [-k KEY] [--top N]
"""
import os
import sys
import argparse
import json
import importlib
from collections import defaultdict

# Import functionality from both scripts
import track_solver
import trace_solver_calls
import solvers

def analyze_single_solver(solver_key):
    """Analyze a single solver's DSL function usage."""
    print(f"Analyzing solver: solve_{solver_key}")
    track_solver.track_solver(solver_key)
    
    # The track_solver function creates the stats file
    stats_file = f"{solver_key}_dsl_stats.json"
    if os.path.exists(stats_file):
        print("\nAnalyzing exported statistics:")
        trace_solver_calls.main([stats_file])

def analyze_top_solvers(n=10):
    """Analyze the top N most complex solvers based on code size."""
    # Get all solver functions
    solver_funcs = [f for f in dir(solvers) if f.startswith('solve_')]
    
    # Sort by code size (approximation of complexity)
    solver_complexity = []
    for func_name in solver_funcs:
        try:
            code = inspect.getsource(getattr(solvers, func_name))
            solver_complexity.append((func_name[6:], len(code.split('\n'))))
        except:
            continue
    
    # Sort by lines of code
    top_solvers = sorted(solver_complexity, key=lambda x: x[1], reverse=True)[:n]
    
    print(f"Analyzing top {n} most complex solvers:")
    for solver_key, lines in top_solvers:
        print(f"Solver {solver_key}: {lines} lines")
        analyze_single_solver(solver_key)

def main():
    parser = argparse.ArgumentParser(description="Analyze DSL function usage in solvers")
    parser.add_argument("-k", "--key", help="Analyze a specific solver key", type=str)
    parser.add_argument("--top", help="Analyze top N most complex solvers", type=int, default=5)
    
    args = parser.parse_args()
    
    if args.key:
        analyze_single_solver(args.key)
    else:
        analyze_top_solvers(args.top)

if __name__ == "__main__":
    main()