#!/usr/bin/env python3
"""
Profile framework functions in batt (genetic mutation solver).

This script uses cProfile with detailed output to identify specific bottlenecks
within the 92.4% framework overhead. Focus areas:
1. batch_process_samples_gpu - GPU memory transfers
2. dedupe operations - Set deduplication
3. difference_tuple - Tuple difference operations
4. Candidate generation and validation
5. Result collection (o.append, s.append)

Usage:
    python profile_batt_framework.py [--tasks N]

Output: 
    - Console: Top framework functions by time
    - File: profile_batt_framework_TIMESTAMP.txt (detailed stats)
"""

import cProfile
import pstats
import io
import sys
import json
import time
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Import profiling target
try:
    from tmp_batt_onerun_run import batt
except ImportError as e:
    print(f"Import error: {e}")
    print("Make sure tmp_batt_onerun_run.py exists (generated solver)")
    sys.exit(1)


def load_tasks(data_path='../arc-prize-2025/arc-agi_training_challenges.json'):
    """Load tasks from JSON file."""
    try:
        with open(data_path) as f:
            data = json.load(f)
        
        tasks = []
        for task_id, task in data.items():
            tasks.append((task_id, task))
        
        return tasks
    except FileNotFoundError:
        print(f"Training data not found at {data_path}")
        print("Trying alternative path...")
        
        # Try alternative path
        alt_path = 'arc-agi_training_challenges.json'
        try:
            with open(alt_path) as f:
                data = json.load(f)
            
            tasks = []
            for task_id, task in data.items():
                tasks.append((task_id, task))
            
            return tasks
        except FileNotFoundError:
            print(f"Training data not found at {alt_path}")
            print("Please provide path to arc-agi_training_challenges.json")
            sys.exit(1)


def profile_framework_functions(num_tasks=100):
    """
    Profile batt execution with focus on framework functions.
    
    Args:
        num_tasks: Number of tasks to profile (default 100)
    
    Returns:
        dict: Profiling statistics organized by category
    """
    print(f"\n{'='*80}")
    print(f"FRAMEWORK PROFILING: {num_tasks} tasks")
    print(f"{'='*80}\n")
    
    # Get tasks
    all_tasks = load_tasks()
    tasks = all_tasks[:num_tasks]
    print(f"Loaded {len(tasks)} tasks for profiling\n")
    
    # Setup profiler
    profiler = cProfile.Profile()
    
    # Profile execution
    print("Starting profiling...")
    start_time = time.time()
    
    profiler.enable()
    
    results = []
    for task_id, task in tasks:
        try:
            I = tuple(map(tuple, task["train"][0]["input"]))
            C = tuple(map(tuple, task["train"][0]["output"]))
            S = tuple((tuple(map(tuple, sample['input'])), tuple(map(tuple, sample['output']))) 
                     for sample in task["train"])
            
            o, s = batt(task_id, S, I, C, "")
            results.append((task_id, len(o), len(s)))
        except Exception as e:
            print(f"Task {task_id} failed: {e}")
            results.append((task_id, 0, 0))
    
    profiler.disable()
    
    wall_time = time.time() - start_time
    print(f"Profiling complete: {wall_time:.2f}s wall-clock time\n")
    
    # Analyze results
    total_outputs = sum(r[1] for r in results)
    total_solvers = sum(r[2] for r in results)
    print(f"Results: {total_outputs} outputs, {total_solvers} solvers\n")
    
    # Get stats
    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    
    return stats, wall_time, results


def categorize_functions(stats):
    """
    Categorize profiled functions into framework components.
    
    Returns:
        dict: Functions grouped by category with timing data
    """
    categories = {
        'GPU Batch Processing': [],
        'Dedupe Operations': [],
        'Tuple Operations': [],
        'Frozenset Operations': [],
        'Candidate Management': [],
        'Result Collection': [],
        'Error Handling': [],
        'DSL Operations': [],
        'Other Framework': []
    }
    
    # Category patterns
    patterns = {
        'GPU Batch Processing': ['batch_process_samples_gpu', 'gpu_', 'cupy', 'transfer'],
        'Dedupe Operations': ['dedupe'],
        'Tuple Operations': ['difference_tuple', 'get_nth_t', 'astuple', 'remove_t', 'merge_t'],
        'Frozenset Operations': ['difference', 'union', 'intersection', 'get_nth_f'],
        'Candidate Management': ['_get_safe_default', 'append'],
        'Result Collection': ['append'],
        'Error Handling': ['except', 'TypeError', 'AttributeError', 'ValueError'],
        'DSL Operations': ['identity', 'p_g', 'o_g', 'objects', 'size', 'color', 'fill', 
                          'paint', 'move', 'shift', 'rotate', 'mirror', 'crop', 
                          'vconcat', 'hconcat', 'apply', 'mapply']
    }
    
    # Extract function stats
    function_stats = []
    for func, (cc, nc, tt, ct, callers) in stats.stats.items():
        filename, line, func_name = func
        
        # Skip built-in functions from other modules
        if filename.startswith('<'):
            continue
        
        function_stats.append({
            'name': func_name,
            'file': filename,
            'calls': nc,
            'total_time': tt,
            'cumulative_time': ct,
            'per_call': tt / nc if nc > 0 else 0
        })
    
    # Categorize functions
    for func_stat in function_stats:
        func_name = func_stat['name']
        categorized = False
        
        for category, keywords in patterns.items():
            for keyword in keywords:
                if keyword.lower() in func_name.lower():
                    categories[category].append(func_stat)
                    categorized = True
                    break
            if categorized:
                break
        
        if not categorized:
            categories['Other Framework'].append(func_stat)
    
    return categories


def analyze_framework_bottlenecks(stats, wall_time):
    """
    Analyze profiling stats to identify framework bottlenecks.
    
    Returns:
        dict: Analysis results with top bottlenecks
    """
    print(f"\n{'='*80}")
    print("FRAMEWORK BOTTLENECK ANALYSIS")
    print(f"{'='*80}\n")
    
    # Categorize functions
    categories = categorize_functions(stats)
    
    # Calculate category totals
    category_totals = {}
    for category, functions in categories.items():
        if not functions:
            continue
        
        total_time = sum(f['total_time'] for f in functions)
        cumulative_time = sum(f['cumulative_time'] for f in functions)
        total_calls = sum(f['calls'] for f in functions)
        
        category_totals[category] = {
            'total_time': total_time,
            'cumulative_time': cumulative_time,
            'calls': total_calls,
            'functions': len(functions),
            'top_functions': sorted(functions, key=lambda x: x['cumulative_time'], reverse=True)[:5]
        }
    
    # Sort categories by cumulative time
    sorted_categories = sorted(
        category_totals.items(),
        key=lambda x: x[1]['cumulative_time'],
        reverse=True
    )
    
    # Print category summary
    print(f"Framework Bottlenecks by Category (Top 10):\n")
    print(f"{'Category':<30} {'Cum Time':<12} {'% Time':<10} {'Calls':<12} {'Functions':<10}")
    print(f"{'-'*80}")
    
    total_cum_time = sum(cat['cumulative_time'] for cat in category_totals.values())
    
    for i, (category, data) in enumerate(sorted_categories[:10], 1):
        cum_time = data['cumulative_time']
        pct_time = (cum_time / total_cum_time * 100) if total_cum_time > 0 else 0
        
        print(f"{category:<30} {cum_time:>10.3f}s  {pct_time:>8.1f}%  {data['calls']:>10}  {data['functions']:>8}")
    
    print(f"\n{'='*80}\n")
    
    # Print top functions in each major category
    print("Top Functions by Category:\n")
    
    for category, data in sorted_categories[:5]:  # Top 5 categories
        print(f"\n{category} (Top 5 functions):")
        print(f"{'Function':<40} {'Calls':<12} {'Total':<12} {'Cumulative':<12} {'Per Call':<12}")
        print(f"{'-'*80}")
        
        for func in data['top_functions']:
            print(f"{func['name'][:39]:<40} "
                  f"{func['calls']:>10}  "
                  f"{func['total_time']:>10.3f}s  "
                  f"{func['cumulative_time']:>10.3f}s  "
                  f"{func['per_call']*1000:>10.3f}ms")
    
    print(f"\n{'='*80}\n")
    
    return category_totals, sorted_categories


def save_detailed_report(stats, wall_time, category_totals, sorted_categories, output_file, top_n=100):
    """Save detailed profiling report to file.
    
    Args:
        stats: cProfile.Profile() object
        wall_time: Wall-clock time in seconds
        category_totals: Dictionary of category statistics
        sorted_categories: List of (category, data) tuples sorted by cumulative time
        output_file: Path to output file
        top_n: Number of top functions to include (default: 100, use None for all)
    """
    
    with open(output_file, 'w') as f:
        f.write(f"{'='*80}\n")
        f.write(f"FRAMEWORK PROFILING REPORT\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Wall-clock time: {wall_time:.2f}s\n")
        f.write(f"{'='*80}\n\n")
        
        # Category summary
        f.write("CATEGORY SUMMARY\n")
        f.write(f"{'='*80}\n\n")
        f.write(f"{'Category':<30} {'Cum Time':<12} {'% Time':<10} {'Calls':<12} {'Functions':<10}\n")
        f.write(f"{'-'*80}\n")
        
        total_cum_time = sum(cat['cumulative_time'] for cat in category_totals.values())
        
        for category, data in sorted_categories:
            cum_time = data['cumulative_time']
            pct_time = (cum_time / total_cum_time * 100) if total_cum_time > 0 else 0
            
            f.write(f"{category:<30} {cum_time:>10.3f}s  {pct_time:>8.1f}%  "
                   f"{data['calls']:>10}  {data['functions']:>8}\n")
        
        f.write(f"\n{'='*80}\n\n")
        
        # Detailed function listings
        f.write("DETAILED FUNCTION LISTINGS\n")
        f.write(f"{'='*80}\n\n")
        
        for category, data in sorted_categories:
            f.write(f"\n{category}\n")
            f.write(f"{'-'*80}\n")
            f.write(f"{'Function':<50} {'Calls':<12} {'Total':<12} {'Cumulative':<12} {'Per Call':<12}\n")
            f.write(f"{'-'*80}\n")
            
            for func in data['top_functions']:
                f.write(f"{func['name'][:49]:<50} "
                       f"{func['calls']:>10}  "
                       f"{func['total_time']:>10.3f}s  "
                       f"{func['cumulative_time']:>10.3f}s  "
                       f"{func['per_call']*1000:>10.3f}ms\n")
            
            f.write("\n")
        
        f.write(f"\n{'='*80}\n\n")
        
        # Full stats dump
        f.write(f"FULL PROFILING STATS (Top {top_n if top_n else 'ALL'})\n")
        f.write(f"{'='*80}\n\n")
        
        stream = io.StringIO()
        # stats is already a pstats.Stats object, just redirect its stream
        stats.stream = stream
        if top_n:
            stats.print_stats(top_n)
        else:
            stats.print_stats()
        
        f.write(stream.getvalue())
    
    print(f"Detailed report saved to: {output_file}")


def search_functions(stats, patterns):
    """Search for functions matching patterns in profiling stats.
    
    Args:
        stats: cProfile.Profile() object
        patterns: List of function name patterns to search for
        
    Returns:
        Dictionary mapping pattern to list of matching functions with stats
    """
    results = {pattern: [] for pattern in patterns}
    
    for func_key, (cc, nc, tt, ct, callers) in stats.stats.items():
        filename, line, func_name = func_key
        
        # Search for patterns in function name
        for pattern in patterns:
            if pattern.lower() in func_name.lower():
                results[pattern].append({
                    'name': func_name,
                    'file': filename,
                    'line': line,
                    'calls': nc,
                    'total_time': tt,
                    'cumulative_time': ct,
                    'per_call': ct / nc if nc > 0 else 0
                })
    
    return results


def print_search_results(search_results):
    """Print search results in a readable format."""
    print(f"\n{'='*80}")
    print("FUNCTION SEARCH RESULTS")
    print(f"{'='*80}\n")
    
    for pattern, matches in search_results.items():
        if matches:
            print(f"\nPattern: '{pattern}' ({len(matches)} matches)")
            print(f"{'-'*80}")
            print(f"{'Function':<40} {'Calls':>10}  {'Cum Time':>10}  {'Per Call':>10}")
            print(f"{'-'*80}")
            
            # Sort by cumulative time
            matches.sort(key=lambda x: x['cumulative_time'], reverse=True)
            
            for match in matches:
                print(f"{match['name'][:39]:<40} "
                      f"{match['calls']:>10}  "
                      f"{match['cumulative_time']:>10.3f}s  "
                      f"{match['per_call']*1000:>10.3f}ms")
        else:
            print(f"\nPattern: '{pattern}' - NO MATCHES FOUND")
    
    print(f"\n{'='*80}\n")


def main():
    """Main profiling entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Profile batt framework functions')
    parser.add_argument('--tasks', type=int, default=100,
                       help='Number of tasks to profile (default: 100)')
    parser.add_argument('--all', action='store_true',
                       help='Include ALL functions in report (not just top 100)')
    parser.add_argument('--top', type=int, default=100,
                       help='Number of top functions to include (default: 100, ignored if --all is set)')
    parser.add_argument('--search', nargs='+', 
                       help='Search for functions matching these patterns (e.g., --search mapply_t apply_t)')
    
    args = parser.parse_args()
    
    # Run profiling
    stats, wall_time, results = profile_framework_functions(args.tasks)
    
    # Analyze bottlenecks
    category_totals, sorted_categories = analyze_framework_bottlenecks(stats, wall_time)
    
    # Search for specific functions if requested
    if args.search:
        search_results = search_functions(stats, args.search)
        print_search_results(search_results)
    
    # Determine how many functions to include
    top_n = None if args.all else args.top
    
    # Save detailed report
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = f"profile_batt_framework_{timestamp}.txt"
    save_detailed_report(stats, wall_time, category_totals, sorted_categories, output_file, top_n)
    
    print(f"\n{'='*80}")
    print("PROFILING COMPLETE")
    print(f"{'='*80}\n")
    print(f"Wall-clock time: {wall_time:.2f}s")
    print(f"Report saved to: {output_file}")
    print("\nNext steps:")
    print("1. Review top categories to identify main bottlenecks")
    print("2. Focus on categories with >10% of total time")
    print("3. Implement targeted optimizations for top functions")
    print("4. Re-profile to validate improvements")
    print()


if __name__ == '__main__':
    main()
