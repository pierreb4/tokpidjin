#!/usr/bin/env python3
"""
Profile outlier tasks to understand why they take 3-10x longer than median.

Based on timing analysis showing:
- Median task: 4.60s
- P95: 19.30s (4.2x slower)
- Max: 44.82s (9.7x slower)

Outlier tasks (≥15s):
  4f537728: 44.82s
  a64e4611: 31.43s
  446ef5d2: 21.79s
  b2862040: 20.96s
  7837ac64: 20.86s
  73ccf9c2: 19.30s
  b74ca5d1: 17.29s
  c9f8e694: 15.66s
  e84fef15: 15.39s
  c7f57c3e: 15.12s
  639f5a19: 15.10s
"""

import json
import sys
import time
from pathlib import Path
from collections import defaultdict
from timeit import default_timer as timer

# Import from run_batt for profiling
import run_batt
from run_batt import get_data, run_batt as run_batt_func, D_Score
from tmp_batt_onerun_run_call import t_call


# Outlier tasks to profile
OUTLIER_TASKS = [
    '4f537728',  # 44.82s - worst case
    'a64e4611',  # 31.43s
    '446ef5d2',  # 21.79s
    'b2862040',  # 20.96s
    '7837ac64',  # 20.86s
]

# Reference tasks (fast, for comparison)
REFERENCE_TASKS = [
    # Will be populated from timing logs - tasks in 3-5s range (around median)
]


def load_timing_data():
    """Load timing statistics to find reference tasks."""
    timing_file = Path('logs/run_batt_timing_stats.jsonl')
    if not timing_file.exists():
        return []
    
    with open(timing_file) as f:
        lines = [json.loads(line) for line in f]
    
    # Filter completed tasks with execution time
    completed = [t for t in lines if t.get('execution_time') is not None]
    
    # Find tasks in 3-5s range (around median of 4.60s)
    reference = [
        t['task_id'] for t in completed 
        if 3.0 <= t['execution_time'] <= 5.0
    ]
    
    return reference[:5]  # Take 5 reference tasks


def profile_task(task_id, total_data, timeout=60.0):
    """
    Profile a single task with detailed timing breakdowns.
    
    Returns dict with:
    - total_time: Total execution time
    - phase_times: Dict of phase timing (if profiling enabled)
    - solver_count: Number of solvers checked
    - differ_count: Number of differs generated
    - success: Whether task completed without timeout
    """
    print(f"\n{'='*70}")
    print(f"Profiling task: {task_id}")
    print(f"{'='*70}")
    
    # Enable profiling in run_batt
    prof = defaultdict(float)
    
    d_score = D_Score()
    start_time = timer()
    
    try:
        # Run with profiling enabled
        timed_out = run_batt.asyncio.run(
            run_batt_func(
                total_data,
                task_i=0,
                task_id=task_id,
                d_score=d_score,
                start_time=start_time,
                pile_log_path='pile.log',
                timeout=timeout,
                prof=prof,
                batt_module_name='tmp_batt_onerun_run',
                batch_accumulator=None
            )
        )
        
        total_time = timer() - start_time
        
        result = {
            'task_id': task_id,
            'total_time': total_time,
            'timed_out': timed_out,
            'success': not timed_out,
            'phase_times': dict(prof),
        }
        
        # Analyze phase breakdown
        print(f"\nTotal time: {total_time:.2f}s")
        print(f"Timed out: {timed_out}")
        
        if prof:
            print(f"\nPhase breakdown:")
            for phase, phase_time in sorted(prof.items(), key=lambda x: -x[1]):
                pct = 100 * phase_time / total_time if total_time > 0 else 0
                print(f"  {phase:40s} {phase_time:8.3f}s ({pct:5.1f}%)")
        
        return result
        
    except Exception as e:
        print(f"ERROR profiling {task_id}: {e}")
        import traceback
        traceback.print_exc()
        return {
            'task_id': task_id,
            'error': str(e),
            'success': False
        }


def analyze_profiles(outlier_profiles, reference_profiles):
    """Compare outlier and reference task profiles."""
    print(f"\n{'='*70}")
    print(f"COMPARATIVE ANALYSIS")
    print(f"{'='*70}")
    
    # Calculate average times for each phase
    outlier_phases = defaultdict(list)
    reference_phases = defaultdict(list)
    
    for profile in outlier_profiles:
        if 'phase_times' in profile:
            for phase, time_val in profile['phase_times'].items():
                outlier_phases[phase].append(time_val)
    
    for profile in reference_profiles:
        if 'phase_times' in profile:
            for phase, time_val in profile['phase_times'].items():
                reference_phases[phase].append(time_val)
    
    # Find phases with biggest differences
    print(f"\nPhase comparison (outlier avg vs reference avg):")
    print(f"{'Phase':<40s} {'Outlier':>10s} {'Reference':>10s} {'Ratio':>8s}")
    print("-" * 70)
    
    all_phases = set(outlier_phases.keys()) | set(reference_phases.keys())
    phase_ratios = []
    
    for phase in sorted(all_phases):
        outlier_avg = sum(outlier_phases[phase]) / len(outlier_phases[phase]) if phase in outlier_phases else 0
        ref_avg = sum(reference_phases[phase]) / len(reference_phases[phase]) if phase in reference_phases else 0
        
        if ref_avg > 0:
            ratio = outlier_avg / ref_avg
            phase_ratios.append((phase, outlier_avg, ref_avg, ratio))
            print(f"{phase:<40s} {outlier_avg:10.3f}s {ref_avg:10.3f}s {ratio:8.2f}x")
    
    # Highlight biggest bottlenecks
    print(f"\n{'='*70}")
    print(f"BOTTLENECK IDENTIFICATION")
    print(f"{'='*70}")
    
    # Sort by ratio (biggest difference first)
    phase_ratios.sort(key=lambda x: -x[3])
    
    print(f"\nTop phases causing slowdown (ratio > 2.0x):")
    for phase, outlier_avg, ref_avg, ratio in phase_ratios[:10]:
        if ratio > 2.0:
            diff = outlier_avg - ref_avg
            print(f"  {phase}")
            print(f"    Outlier: {outlier_avg:.3f}s, Reference: {ref_avg:.3f}s")
            print(f"    {ratio:.1f}x slower (adds {diff:.3f}s)")
    
    # Overall statistics
    outlier_total = sum(p['total_time'] for p in outlier_profiles if 'total_time' in p)
    reference_total = sum(p['total_time'] for p in reference_profiles if 'total_time' in p)
    
    n_outliers = len([p for p in outlier_profiles if 'total_time' in p])
    n_reference = len([p for p in reference_profiles if 'total_time' in p])
    
    if n_outliers > 0 and n_reference > 0:
        outlier_avg_total = outlier_total / n_outliers
        reference_avg_total = reference_total / n_reference
        total_ratio = outlier_avg_total / reference_avg_total if reference_avg_total > 0 else 0
        
        print(f"\nOverall comparison:")
        print(f"  Outlier tasks avg: {outlier_avg_total:.2f}s")
        print(f"  Reference tasks avg: {reference_avg_total:.2f}s")
        print(f"  Ratio: {total_ratio:.2f}x slower")


def main():
    print("="*70)
    print("OUTLIER TASK PROFILER")
    print("="*70)
    print()
    print("This script profiles slow tasks (≥15s) to identify bottlenecks.")
    print("Results will show which phases take disproportionately long.")
    print()
    
    # Load reference tasks from timing logs
    reference_tasks = load_timing_data()
    if reference_tasks:
        REFERENCE_TASKS.extend(reference_tasks)
        print(f"Loaded {len(reference_tasks)} reference tasks (3-5s range)")
    
    # Load data
    print("Loading ARC data...")
    total_data = get_data(train=True, sort_by_size=True)
    
    # Profile outlier tasks
    print(f"\nProfiling {len(OUTLIER_TASKS)} outlier tasks...")
    outlier_profiles = []
    for task_id in OUTLIER_TASKS:
        profile = profile_task(task_id, total_data, timeout=60.0)
        outlier_profiles.append(profile)
        time.sleep(0.5)  # Brief pause between tasks
    
    # Profile reference tasks (if available)
    reference_profiles = []
    if REFERENCE_TASKS:
        print(f"\nProfiling {len(REFERENCE_TASKS)} reference tasks (for comparison)...")
        for task_id in REFERENCE_TASKS:
            profile = profile_task(task_id, total_data, timeout=30.0)
            reference_profiles.append(profile)
            time.sleep(0.5)
    
    # Analyze results
    if outlier_profiles and reference_profiles:
        analyze_profiles(outlier_profiles, reference_profiles)
    
    # Save results
    output_file = Path('logs/outlier_profiling_results.json')
    output_file.parent.mkdir(exist_ok=True)
    
    results = {
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'outlier_tasks': outlier_profiles,
        'reference_tasks': reference_profiles,
    }
    
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n{'='*70}")
    print(f"Results saved to: {output_file}")
    print(f"{'='*70}")


if __name__ == '__main__':
    main()
