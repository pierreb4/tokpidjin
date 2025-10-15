"""
Profile DSL function calls in generated batt() functions
Identifies which DSL operations are bottlenecks for GPU acceleration

Usage:
    python profile_batt_dsl.py -f batt.py -t <task_id>
    
Output:
    - Per-function call counts
    - Per-function cumulative times
    - Recommended GPU acceleration targets
"""

import argparse
import cProfile
import pstats
import io
import importlib
import sys
from pathlib import Path
from collections import defaultdict
import json


def profile_batt_execution(batt_module_name, task_id, training_data_path=None):
    """Profile a single batt() execution on a specific task"""
    
    # Load the training data
    if training_data_path is None:
        training_data_path = '../arc-prize-2025/arc-agi_training_challenges.json'
    
    with open(training_data_path) as f:
        data = json.load(f)
    
    if task_id not in data:
        print(f"Error: Task {task_id} not found in training data")
        return None
    
    task = data[task_id]
    demo_samples = task['train']
    
    # Prepare S (demo samples)
    S = tuple((tuple(map(tuple, sample['input'])), tuple(map(tuple, sample['output']))) 
              for sample in demo_samples)
    
    # Take first test input
    test_sample = task['test'][0]
    I = tuple(map(tuple, test_sample['input']))
    O = None  # For generation mode (not diff mode)
    
    # Import the batt module
    if batt_module_name in sys.modules:
        del sys.modules[batt_module_name]  # Force reload
    
    batt_module = importlib.import_module(batt_module_name)
    batt_func = batt_module.batt
    
    # Profile the execution
    profiler = cProfile.Profile()
    profiler.enable()
    
    try:
        # Try with log_path first (for card.py generated functions)
        try:
            result = batt_func(task_id, S, I, O, log_path=None)
        except TypeError:
            # Fall back to pile_log_path (for run_batt generated functions)
            try:
                result = batt_func(task_id, S, I, O, pile_log_path=None)
            except TypeError:
                # Fall back to simple signature
                result = batt_func(task_id, S, I, O)
        success = True
    except Exception as e:
        print(f"Error during execution: {e}")
        import traceback
        traceback.print_exc()
        result = None
        success = False
    
    profiler.disable()
    
    return profiler, success, result


def analyze_dsl_calls(profiler):
    """
    Analyze the profiler stats and extract DSL function calls
    
    Returns:
        Dict with:
        - function_stats: {func_name: {calls, total_time, avg_time}}
        - total_time: total execution time
        - recommendations: list of functions to GPU-accelerate
    """
    
    # Get stats
    stats = pstats.Stats(profiler)
    
    # DSL functions we care about
    # These are known to be computationally expensive
    target_functions = {
        'o_g', 'objects', 'objects_t',
        'gravitate', 'fgpartition', 'partition',
        'flood_fill', 'neighbors', 'dneighbors',
        'compress', 'upscale', 'downscale',
        'mapply', 'compose', 'chain',
        'hmirror', 'vmirror', 'rot90', 'rot180', 'rot270',
        'leftmost', 'rightmost', 'topmostobject', 'bottommostobject',
        'inbox', 'outbox', 'bordering',
        'asindices', 'ofcolor', 'colorfilter',
        'connect', 'hconcat', 'vconcat',
    }
    
    # Extract relevant stats
    function_stats = defaultdict(lambda: {'calls': 0, 'total_time': 0.0, 'cumtime': 0.0})
    
    for func_key, (cc, nc, tt, ct, callers) in stats.stats.items():
        filename, line, func_name = func_key
        
        # Filter for dsl.py functions
        if 'dsl.py' in filename and func_name in target_functions:
            function_stats[func_name]['calls'] += nc
            function_stats[func_name]['total_time'] += tt
            function_stats[func_name]['cumtime'] += ct
    
    # Calculate averages and sort by total time
    for func_name, data in function_stats.items():
        if data['calls'] > 0:
            data['avg_time'] = data['total_time'] / data['calls']
        else:
            data['avg_time'] = 0.0
    
    # Sort by cumulative time (most impactful first)
    sorted_funcs = sorted(function_stats.items(), 
                         key=lambda x: x[1]['cumtime'], 
                         reverse=True)
    
    # Get total profiled time
    total_time = sum(ct for (_, (_, _, _, ct, _)) in stats.stats.items())
    
    # Generate recommendations
    recommendations = []
    for func_name, data in sorted_funcs[:10]:  # Top 10
        pct_of_total = (data['cumtime'] / total_time * 100) if total_time > 0 else 0
        if pct_of_total > 1.0:  # More than 1% of execution time
            recommendations.append({
                'function': func_name,
                'calls': data['calls'],
                'total_time_ms': data['total_time'] * 1000,
                'cumtime_ms': data['cumtime'] * 1000,
                'avg_time_ms': data['avg_time'] * 1000,
                'percent_of_total': pct_of_total,
                'gpu_priority': 'HIGH' if pct_of_total > 10 else 'MEDIUM' if pct_of_total > 5 else 'LOW'
            })
    
    return {
        'function_stats': dict(sorted_funcs),
        'total_time': total_time,
        'recommendations': recommendations
    }


def main():
    parser = argparse.ArgumentParser(description='Profile DSL function calls in batt()')
    parser.add_argument('-f', '--file', default='batt', 
                       help='Batt module name (without .py)')
    parser.add_argument('-t', '--task', required=True,
                       help='Task ID to test (e.g., 007bbfb7)')
    parser.add_argument('-d', '--data', default='../arc-prize-2025/arc-agi_training_challenges.json',
                       help='Path to training data JSON')
    parser.add_argument('-o', '--output', help='Output JSON file for results')
    
    args = parser.parse_args()
    
    print(f"Profiling {args.file}.batt() on task {args.task}...")
    print("=" * 70)
    
    # Run profiling
    profiler, success, result = profile_batt_execution(args.file, args.task, args.data)
    
    if not success:
        print("❌ Execution failed, results may be incomplete")
    else:
        print("✅ Execution successful")
        if result:
            o_list, s_list = result
            print(f"   Generated {len(o_list)} output candidates")
    
    print()
    
    # Analyze DSL calls
    analysis = analyze_dsl_calls(profiler)
    
    print("DSL Function Call Analysis")
    print("=" * 70)
    print(f"Total execution time: {analysis['total_time']*1000:.2f} ms")
    print()
    
    if analysis['recommendations']:
        print("Top DSL Functions (by cumulative time):")
        print()
        print(f"{'Function':<20} {'Calls':>8} {'Total(ms)':>12} {'Cum(ms)':>12} {'Avg(ms)':>10} {'% Total':>8} {'GPU':>6}")
        print("-" * 90)
        
        for rec in analysis['recommendations']:
            print(f"{rec['function']:<20} {rec['calls']:>8} "
                  f"{rec['total_time_ms']:>12.2f} {rec['cumtime_ms']:>12.2f} "
                  f"{rec['avg_time_ms']:>10.4f} {rec['percent_of_total']:>7.1f}% "
                  f"{rec['gpu_priority']:>6}")
        
        print()
        print("GPU Acceleration Recommendations:")
        print()
        
        high_priority = [r for r in analysis['recommendations'] if r['gpu_priority'] == 'HIGH']
        medium_priority = [r for r in analysis['recommendations'] if r['gpu_priority'] == 'MEDIUM']
        
        if high_priority:
            print("🔴 HIGH PRIORITY (>10% of execution):")
            for rec in high_priority:
                print(f"   - {rec['function']}: {rec['cumtime_ms']:.2f}ms ({rec['percent_of_total']:.1f}%), {rec['calls']} calls")
        
        if medium_priority:
            print()
            print("🟡 MEDIUM PRIORITY (5-10% of execution):")
            for rec in medium_priority:
                print(f"   - {rec['function']}: {rec['cumtime_ms']:.2f}ms ({rec['percent_of_total']:.1f}%), {rec['calls']} calls")
        
        print()
        print(f"Expected GPU speedup: 2-6x for HIGH priority functions")
        print(f"Target speedup: {analysis['total_time']*1000:.1f}ms → {analysis['total_time']*1000/3:.1f}-{analysis['total_time']*1000/6:.1f}ms")
    else:
        print("No significant DSL function calls detected (all <1% of execution)")
    
    # Save to JSON if requested
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(analysis, f, indent=2)
        print()
        print(f"Results saved to {args.output}")


if __name__ == '__main__':
    main()
