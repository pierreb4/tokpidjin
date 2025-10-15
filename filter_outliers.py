#!/usr/bin/env python3
"""
Filter outlier tasks from Kaggle profiling results and re-analyze.

Removes 4 outlier tasks with infinite loops:
- Task 16 (06df4c85): 239.5s
- Task 50 (13f06aa5): 117.3s
- Task 56 (15113be4): 101.9s
- Task 79 (1b59e163): 180.3s

Re-calculates statistics for the remaining 96 tasks to get clean data.
"""

import json
import argparse
from pathlib import Path

# Outlier task IDs (from KAGGLE_PROFILING_OUTLIER_ANALYSIS.md)
OUTLIER_TASKS = {
    "06df4c85",  # Task 16: 239.5s - infinite loop
    "13f06aa5",  # Task 50: 117.3s - runaway recursion
    "15113be4",  # Task 56: 101.9s - stuck computation
    "1b59e163",  # Task 79: 180.3s - near-infinite loop
}

def load_profiling_results(input_file):
    """Load profiling results from JSON file."""
    if not Path(input_file).exists():
        print(f"❌ Error: {input_file} not found!")
        print("\nYou need the raw profiling output from Kaggle.")
        print("Expected format: profile_batt_batch output saved to JSON")
        return None
    
    with open(input_file, 'r') as f:
        return json.load(f)

def filter_outliers(results):
    """Remove outlier tasks from results."""
    if 'task_results' in results:
        original_count = len(results['task_results'])
        results['task_results'] = {
            task_id: data
            for task_id, data in results['task_results'].items()
            if task_id not in OUTLIER_TASKS
        }
        filtered_count = len(results['task_results'])
        removed = original_count - filtered_count
        print(f"✅ Filtered {removed} outliers ({filtered_count} tasks remaining)")
        return results
    else:
        print("⚠️  Warning: Unknown data format")
        return results

def recalculate_statistics(results):
    """Re-calculate aggregate statistics without outliers."""
    if 'task_results' not in results:
        print("❌ Cannot recalculate - no task_results found")
        return results
    
    # Aggregate DSL function statistics
    dsl_functions = {}
    total_time = 0.0
    task_count = len(results['task_results'])
    
    for task_id, task_data in results['task_results'].items():
        if 'dsl_functions' in task_data:
            for func_name, func_data in task_data['dsl_functions'].items():
                if func_name not in dsl_functions:
                    dsl_functions[func_name] = {
                        'total_time': 0.0,
                        'total_calls': 0,
                        'tasks_used': 0
                    }
                
                dsl_functions[func_name]['total_time'] += func_data.get('cumtime', 0.0)
                dsl_functions[func_name]['total_calls'] += func_data.get('ncalls', 0)
                dsl_functions[func_name]['tasks_used'] += 1
        
        # Add task execution time to total
        if 'analysis' in task_data:
            total_time += task_data['analysis'].get('total_time', 0.0)
    
    # Calculate percentages and averages
    for func_name, func_data in dsl_functions.items():
        func_data['avg_time_per_task'] = func_data['total_time'] / task_count
        func_data['avg_calls_per_task'] = func_data['total_calls'] / task_count
        func_data['avg_time_per_call'] = (
            func_data['total_time'] / func_data['total_calls']
            if func_data['total_calls'] > 0 else 0.0
        )
        if total_time > 0:
            func_data['percent_of_total'] = (func_data['total_time'] / total_time) * 100
        else:
            func_data['percent_of_total'] = 0.0
    
    # Sort by total time descending
    sorted_functions = sorted(
        dsl_functions.items(),
        key=lambda x: x[1]['total_time'],
        reverse=True
    )
    
    results['filtered_summary'] = {
        'task_count': task_count,
        'total_time': total_time,
        'avg_time_per_task': total_time / task_count if task_count > 0 else 0.0,
        'dsl_functions': dict(sorted_functions[:20])  # Top 20
    }
    
    return results

def print_summary(results):
    """Print summary of filtered results."""
    if 'filtered_summary' not in results:
        print("⚠️  No filtered summary available")
        return
    
    summary = results['filtered_summary']
    
    print("\n" + "="*80)
    print("FILTERED PROFILING RESULTS (Outliers Removed)")
    print("="*80)
    
    print(f"\n📊 Overall Statistics:")
    print(f"  Tasks analyzed: {summary['task_count']}")
    print(f"  Total time: {summary['total_time']:.2f}s")
    print(f"  Average per task: {summary['avg_time_per_task']:.2f}s")
    
    print(f"\n🔝 Top DSL Functions (by total time):\n")
    print(f"{'Function':<20} {'Time (s)':<12} {'Calls':<12} {'Per-Call (ms)':<15} {'% Total':<10}")
    print("-" * 80)
    
    for func_name, func_data in list(summary['dsl_functions'].items())[:10]:
        time_s = func_data['total_time']
        calls = func_data['total_calls']
        per_call_ms = func_data['avg_time_per_call'] * 1000
        percent = func_data['percent_of_total']
        
        print(f"{func_name:<20} {time_s:<12.2f} {calls:<12,} {per_call_ms:<15.3f} {percent:<10.1f}%")
    
    # Calculate total DSL time
    total_dsl_time = sum(f['total_time'] for f in summary['dsl_functions'].values())
    dsl_percent = (total_dsl_time / summary['total_time']) * 100 if summary['total_time'] > 0 else 0
    
    print("\n" + "-" * 80)
    print(f"{'ALL DSL FUNCTIONS':<20} {total_dsl_time:<12.2f} {'':<12} {'':<15} {dsl_percent:<10.1f}%")
    print("-" * 80)
    
    framework_time = summary['total_time'] - total_dsl_time
    framework_percent = 100 - dsl_percent
    print(f"Framework overhead: {framework_time:.2f}s ({framework_percent:.1f}%)")
    
    # Projected to 400 tasks
    print(f"\n📈 Projected to 400 tasks:")
    print(f"  Total time: {summary['avg_time_per_task'] * 400:.2f}s ({summary['avg_time_per_task'] * 400 / 60:.1f} minutes)")
    print(f"  DSL time: {total_dsl_time / summary['task_count'] * 400:.2f}s")
    print(f"  Framework time: {framework_time / summary['task_count'] * 400:.2f}s")
    
    # GPU optimization potential
    print(f"\n🎯 Optimization Potential:")
    
    # Find o_g and objects
    o_g_data = summary['dsl_functions'].get('o_g', {})
    objects_data = summary['dsl_functions'].get('objects', {})
    
    if o_g_data and objects_data:
        og_time = o_g_data['total_time']
        obj_time = objects_data['total_time']
        combined_time = og_time + obj_time
        combined_avg = combined_time / summary['task_count']
        projected_400 = combined_avg * 400
        
        print(f"  o_g + objects current: {combined_time:.2f}s ({combined_time/summary['total_time']*100:.1f}%)")
        print(f"  Projected to 400 tasks: {projected_400:.2f}s")
        print(f"  GPU 3x speedup saves: {projected_400 * 2/3:.2f}s")
        print(f"  GPU 6x speedup saves: {projected_400 * 5/6:.2f}s")
    
    print("\n" + "="*80)

def save_filtered_results(results, output_file):
    """Save filtered results to JSON file."""
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\n✅ Filtered results saved to: {output_file}")

def main():
    parser = argparse.ArgumentParser(
        description="Filter outliers from Kaggle profiling results"
    )
    parser.add_argument(
        '-i', '--input',
        default='kaggle_profiling_results.json',
        help='Input JSON file with profiling results'
    )
    parser.add_argument(
        '-o', '--output',
        default='kaggle_profiling_filtered.json',
        help='Output JSON file for filtered results'
    )
    
    args = parser.parse_args()
    
    print("🔍 Filtering Kaggle profiling outliers...")
    print(f"   Input: {args.input}")
    print(f"   Output: {args.output}")
    print(f"   Removing {len(OUTLIER_TASKS)} outliers: {', '.join(OUTLIER_TASKS)}")
    
    # Load results
    results = load_profiling_results(args.input)
    if results is None:
        print("\n💡 To use this script:")
        print("   1. Save the raw JSON output from profile_batt_batch.py")
        print("   2. Run: python filter_outliers.py -i <input_file>")
        return 1
    
    # Filter outliers
    results = filter_outliers(results)
    
    # Re-calculate statistics
    results = recalculate_statistics(results)
    
    # Print summary
    print_summary(results)
    
    # Save filtered results
    save_filtered_results(results, args.output)
    
    print("\n✅ Done! Outliers filtered and statistics recalculated.")
    print("\n📝 Key insights:")
    print("   - Check if DSL percentages increased (expected 15-30% for o_g/objects)")
    print("   - Compare with original results in KAGGLE_PROFILING_ANALYSIS.md")
    print("   - If still low, framework overhead is the real bottleneck")
    
    return 0

if __name__ == '__main__':
    exit(main())
