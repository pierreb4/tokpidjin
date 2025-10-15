"""
Batch profile a batt file across multiple tasks to find DSL bottlenecks

Usage:
    python profile_batt_batch.py -f tmp_batt_onerun_run -n 20
    
Output:
    - Aggregate statistics across all tasks
    - Top DSL functions by total time
    - GPU acceleration recommendations
"""

import argparse
import json
import sys
from pathlib import Path
from collections import defaultdict
from timeit import default_timer as timer

# Import the profiler
from profile_batt_dsl import profile_batt_execution, analyze_dsl_calls


def aggregate_results(task_results):
    """
    Aggregate profiling results across multiple tasks
    
    Returns:
        Dict with:
        - total_execution_time: sum across all tasks
        - function_totals: {func_name: {total_calls, total_time, total_cumtime}}
        - per_task_stats: individual task breakdowns
        - recommendations: GPU acceleration priorities
    """
    
    # Aggregate function statistics
    func_totals = defaultdict(lambda: {
        'total_calls': 0,
        'total_time': 0.0,
        'total_cumtime': 0.0,
        'task_count': 0
    })
    
    total_execution_time = 0.0
    successful_tasks = 0
    failed_tasks = []
    
    for task_id, result in task_results.items():
        if not result['success']:
            failed_tasks.append(task_id)
            continue
        
        successful_tasks += 1
        analysis = result['analysis']
        total_execution_time += analysis['total_time']
        
        for func_name, stats in analysis['function_stats'].items():
            func_totals[func_name]['total_calls'] += stats['calls']
            func_totals[func_name]['total_time'] += stats['total_time']
            func_totals[func_name]['total_cumtime'] += stats['cumtime']
            func_totals[func_name]['task_count'] += 1
    
    # Calculate averages and sort by total cumulative time
    for func_name, data in func_totals.items():
        if data['total_calls'] > 0:
            data['avg_time_per_call'] = data['total_time'] / data['total_calls']
            data['avg_time_per_task'] = data['total_cumtime'] / data['task_count']
        else:
            data['avg_time_per_call'] = 0.0
            data['avg_time_per_task'] = 0.0
    
    sorted_funcs = sorted(func_totals.items(), 
                         key=lambda x: x[1]['total_cumtime'], 
                         reverse=True)
    
    # Generate recommendations based on aggregate data
    recommendations = []
    for func_name, data in sorted_funcs[:15]:  # Top 15
        pct_of_total = (data['total_cumtime'] / total_execution_time * 100) if total_execution_time > 0 else 0
        if pct_of_total > 0.1:  # More than 0.1% of total execution time (was 0.5)
            # GPU priority based on percentage AND call frequency
            if pct_of_total > 10:
                priority = 'HIGH'
            elif pct_of_total > 5:
                priority = 'MEDIUM'
            elif pct_of_total > 1:
                priority = 'LOW'
            else:
                priority = 'MINIMAL'
            
            recommendations.append({
                'function': func_name,
                'total_calls': data['total_calls'],
                'total_cumtime_ms': data['total_cumtime'] * 1000,
                'avg_time_per_call_ms': data['avg_time_per_call'] * 1000,
                'avg_time_per_task_ms': data['avg_time_per_task'] * 1000,
                'percent_of_total': pct_of_total,
                'task_count': data['task_count'],
                'gpu_priority': priority
            })
    
    return {
        'total_execution_time': total_execution_time,
        'successful_tasks': successful_tasks,
        'failed_tasks': failed_tasks,
        'function_totals': dict(sorted_funcs),
        'recommendations': recommendations
    }


def main():
    parser = argparse.ArgumentParser(description='Batch profile batt across multiple tasks')
    parser.add_argument('-f', '--file', default='tmp_batt_onerun_run', 
                       help='Batt module name (without .py)')
    parser.add_argument('-n', '--num-tasks', type=int, default=20,
                       help='Number of tasks to profile')
    parser.add_argument('-d', '--data', default='../arc-prize-2025/arc-agi_training_challenges.json',
                       help='Path to training data JSON')
    parser.add_argument('-o', '--output', help='Output JSON file for results')
    parser.add_argument('--start', type=int, default=0,
                       help='Start index in task list')
    
    args = parser.parse_args()
    
    # Load task list
    with open(args.data) as f:
        data = json.load(f)
    
    task_ids = list(data.keys())
    
    # Select tasks to profile
    end_idx = min(args.start + args.num_tasks, len(task_ids))
    selected_tasks = task_ids[args.start:end_idx]
    
    print(f"Batch Profiling: {args.file}.batt()")
    print(f"Tasks: {len(selected_tasks)} (indices {args.start}-{end_idx-1})")
    print("=" * 70)
    print()
    
    # Profile each task
    task_results = {}
    start_time = timer()
    
    for i, task_id in enumerate(selected_tasks):
        print(f"[{i+1}/{len(selected_tasks)}] Profiling task {task_id}...", end=' ', flush=True)
        
        try:
            profiler, success, result = profile_batt_execution(args.file, task_id, args.data)
            
            if success:
                analysis = analyze_dsl_calls(profiler)
                task_results[task_id] = {
                    'success': True,
                    'analysis': analysis,
                    'output_count': len(result[0]) if result else 0
                }
                print(f"✅ {analysis['total_time']*1000:.1f}ms, {task_results[task_id]['output_count']} outputs")
            else:
                task_results[task_id] = {
                    'success': False,
                    'analysis': None
                }
                print(f"❌ Failed")
        except Exception as e:
            task_results[task_id] = {
                'success': False,
                'analysis': None,
                'error': str(e)
            }
            print(f"❌ Error: {e}")
    
    elapsed = timer() - start_time
    
    print()
    print("=" * 70)
    print(f"Profiling complete in {elapsed:.2f}s")
    print()
    
    # Aggregate results
    aggregate = aggregate_results(task_results)
    
    print("Aggregate DSL Function Analysis")
    print("=" * 70)
    print(f"Successful tasks: {aggregate['successful_tasks']}/{len(selected_tasks)}")
    print(f"Total execution time: {aggregate['total_execution_time']*1000:.2f}ms")
    print(f"Average per task: {aggregate['total_execution_time']*1000/aggregate['successful_tasks']:.2f}ms" if aggregate['successful_tasks'] > 0 else "N/A")
    
    if aggregate['failed_tasks']:
        print(f"Failed tasks: {', '.join(aggregate['failed_tasks'])}")
    
    print()
    
    if aggregate['recommendations']:
        print("Top DSL Functions (aggregate across all tasks):")
        print()
        print(f"{'Function':<20} {'Calls':>8} {'Total(ms)':>12} {'Per-Call':>10} {'Per-Task':>10} {'% Total':>8} {'Tasks':>6} {'GPU':>8}")
        print("-" * 100)
        
        for rec in aggregate['recommendations']:
            print(f"{rec['function']:<20} {rec['total_calls']:>8} "
                  f"{rec['total_cumtime_ms']:>12.2f} "
                  f"{rec['avg_time_per_call_ms']:>10.4f} "
                  f"{rec['avg_time_per_task_ms']:>10.2f} "
                  f"{rec['percent_of_total']:>7.1f}% "
                  f"{rec['task_count']:>6} "
                  f"{rec['gpu_priority']:>8}")
        
        print()
        print("GPU Acceleration Recommendations (Aggregate Data):")
        print()
        
        high_priority = [r for r in aggregate['recommendations'] if r['gpu_priority'] == 'HIGH']
        medium_priority = [r for r in aggregate['recommendations'] if r['gpu_priority'] == 'MEDIUM']
        low_priority = [r for r in aggregate['recommendations'] if r['gpu_priority'] == 'LOW']
        
        if high_priority:
            print("🔴 HIGH PRIORITY (>10% of execution):")
            for rec in high_priority:
                print(f"   - {rec['function']}: {rec['total_cumtime_ms']:.2f}ms total ({rec['percent_of_total']:.1f}%), "
                      f"{rec['total_calls']} calls across {rec['task_count']} tasks")
                print(f"     • Avg {rec['avg_time_per_call_ms']:.4f}ms per call, {rec['avg_time_per_task_ms']:.2f}ms per task")
        
        if medium_priority:
            print()
            print("🟡 MEDIUM PRIORITY (5-10% of execution):")
            for rec in medium_priority:
                print(f"   - {rec['function']}: {rec['total_cumtime_ms']:.2f}ms total ({rec['percent_of_total']:.1f}%), "
                      f"{rec['total_calls']} calls across {rec['task_count']} tasks")
        
        if low_priority:
            print()
            print("🟢 LOW PRIORITY (1-5% of execution):")
            for rec in low_priority:
                print(f"   - {rec['function']}: {rec['total_cumtime_ms']:.2f}ms ({rec['percent_of_total']:.1f}%)")
        
        print()
        print("Expected Impact of GPU Acceleration:")
        print()
        
        high_total = sum(r['total_cumtime_ms'] for r in high_priority)
        medium_total = sum(r['total_cumtime_ms'] for r in medium_priority)
        
        if high_priority:
            print(f"  HIGH priority functions: {high_total:.2f}ms")
            print(f"    → With 3-6x GPU speedup: {high_total/6:.2f}-{high_total/3:.2f}ms")
            print(f"    → Potential savings: {high_total - high_total/6:.2f}-{high_total - high_total/3:.2f}ms ({high_total * 5/6:.0f}-{high_total * 2/3:.0f}ms)")
        
        if medium_priority:
            print(f"  MEDIUM priority functions: {medium_total:.2f}ms")
            print(f"    → With 2-4x GPU speedup: {medium_total/4:.2f}-{medium_total/2:.2f}ms")
            print(f"    → Potential savings: {medium_total - medium_total/4:.2f}-{medium_total - medium_total/2:.2f}ms")
        
        total_time = aggregate['total_execution_time'] * 1000
        if high_priority or medium_priority:
            best_case_savings = (high_total * 5/6 if high_priority else 0) + (medium_total * 3/4 if medium_priority else 0)
            worst_case_savings = (high_total * 2/3 if high_priority else 0) + (medium_total * 1/2 if medium_priority else 0)
            print()
            print(f"  Total execution time: {total_time:.2f}ms")
            print(f"  Expected after GPU: {total_time - best_case_savings:.2f}-{total_time - worst_case_savings:.2f}ms")
            print(f"  Overall speedup: {total_time/(total_time - best_case_savings):.2f}-{total_time/(total_time - worst_case_savings):.2f}x")
    else:
        print("No significant DSL function calls detected")
    
    # Save to JSON if requested
    if args.output:
        output_data = {
            'aggregate': aggregate,
            'task_results': task_results,
            'metadata': {
                'batt_file': args.file,
                'num_tasks': len(selected_tasks),
                'successful': aggregate['successful_tasks'],
                'failed': len(aggregate['failed_tasks']),
                'total_time_ms': aggregate['total_execution_time'] * 1000
            }
        }
        with open(args.output, 'w') as f:
            json.dump(output_data, f, indent=2)
        print()
        print(f"Results saved to {args.output}")


if __name__ == '__main__':
    main()
