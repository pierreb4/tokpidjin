#!/usr/bin/env python3
"""
Pipeline Performance Profiler

Profiles the full ARC pipeline to identify bottlenecks:
1. Data loading
2. Code generation (card.py)
3. Solver execution (run_batt.py)
4. Validation
5. Result processing

Usage:
    python profile_pipeline.py --tasks 10
    python profile_pipeline.py --tasks 32  # Full test set
"""

import time
import sys
import argparse
from pathlib import Path
from utils import print_l, get_data

def profile_data_loading():
    """Profile data loading time"""
    print_l("\n" + "="*100)
    print_l("PHASE 1: DATA LOADING")
    print_l("="*100)
    
    start = time.perf_counter()
    train_data = get_data(train=True)
    elapsed = time.perf_counter() - start
    
    task_count = len(train_data.get('demo', {}))
    
    print_l(f"✅ Data loaded in {elapsed:.3f}s")
    print_l(f"   Tasks: {task_count}")
    
    return elapsed, train_data


def profile_code_generation(task_count):
    """Profile code generation (card.py) time"""
    print_l("\n" + "="*100)
    print_l("PHASE 2: CODE GENERATION (card.py)")
    print_l("="*100)
    
    import subprocess
    
    # Generate batt code
    # card.py expects: -c COUNT (not -i -b -c)
    # Generates tmp_batt_onerun_run.py by default (or use -f to specify)
    start = time.perf_counter()
    
    result = subprocess.run(
        ['python', 'card.py', '-c', str(task_count), '-f', 'tmp_batt_onerun_run.py'],
        capture_output=True,
        text=True,
        timeout=300
    )
    
    elapsed = time.perf_counter() - start
    
    if result.returncode == 0:
        print_l(f"✅ Code generated in {elapsed:.3f}s")
        print_l(f"   Tasks: {task_count}")
        print_l(f"   Rate: {elapsed/task_count*1000:.1f}ms per task")
    else:
        print_l(f"❌ Code generation failed")
        print_l(f"   Error: {result.stderr[:500]}")
        print_l(f"   Output: {result.stdout[:500]}")
        return None
    
    return elapsed


def profile_solver_execution(task_ids, train_data):
    """Profile solver execution time"""
    print_l("\n" + "="*100)
    print_l("PHASE 3: SOLVER EXECUTION")
    print_l("="*100)
    
    # Import generated batt module
    try:
        import tmp_batt_onerun_run as batt_module
        from importlib import reload
        reload(batt_module)
    except ImportError as e:
        print_l(f"❌ Cannot import batt module - generate code first: {e}")
        return None
    
    total_time = 0
    sample_count = 0
    task_times = []
    
    for task_id in task_ids:
        if task_id not in train_data['demo']:
            continue
        
        task = train_data['demo'][task_id]
        S = tuple((tuple(s['input']), tuple(s['output'])) for s in task)
        
        task_start = time.perf_counter()
        
        for sample in task:
            I = sample['input']
            
            try:
                start = time.perf_counter()
                result = batt_module.batt(task_id, S, I, None, None)
                elapsed = time.perf_counter() - start
                
                total_time += elapsed
                sample_count += 1
            except Exception as e:
                print_l(f"   {task_id}: Sample failed: {e}")
        
        task_elapsed = time.perf_counter() - task_start
        task_times.append((task_id, task_elapsed, len(task)))
    
    avg_per_sample = (total_time / sample_count * 1000) if sample_count > 0 else 0
    
    print_l(f"✅ Solvers executed in {total_time:.3f}s")
    print_l(f"   Samples: {sample_count}")
    print_l(f"   Average: {avg_per_sample:.3f}ms per sample")
    print_l(f"   Rate: {total_time/len(task_ids)*1000:.1f}ms per task")
    
    # Show slowest tasks
    task_times.sort(key=lambda x: x[1], reverse=True)
    print_l(f"\n   Slowest tasks:")
    for task_id, task_time, sample_count in task_times[:5]:
        print_l(f"     {task_id}: {task_time*1000:.1f}ms ({sample_count} samples)")
    
    return total_time, sample_count, avg_per_sample


def profile_validation(task_ids, train_data):
    """Profile validation time"""
    print_l("\n" + "="*100)
    print_l("PHASE 4: VALIDATION")
    print_l("="*100)
    
    try:
        import tmp_batt_onerun_run as batt_module
        from importlib import reload
        reload(batt_module)
    except ImportError as e:
        print_l(f"❌ Cannot import batt module: {e}")
        return None
    
    total_time = 0
    correct = 0
    total = 0
    
    for task_id in task_ids:
        if task_id not in train_data['demo']:
            continue
        
        task = train_data['demo'][task_id]
        S = tuple((tuple(s['input']), tuple(s['output'])) for s in task)
        
        for sample in task:
            I = sample['input']
            expected = sample['output']
            
            try:
                result = batt_module.batt(task_id, S, I, None, None)
                
                start = time.perf_counter()
                is_correct = (result == expected)
                elapsed = time.perf_counter() - start
                
                total_time += elapsed
                total += 1
                if is_correct:
                    correct += 1
            except Exception:
                total += 1
    
    avg_per_validation = (total_time / total * 1000) if total > 0 else 0
    accuracy = (correct / total * 100) if total > 0 else 0
    
    print_l(f"✅ Validation completed in {total_time:.3f}s")
    print_l(f"   Validations: {total}")
    print_l(f"   Average: {avg_per_validation:.3f}ms per validation")
    print_l(f"   Accuracy: {correct}/{total} ({accuracy:.1f}%)")
    
    return total_time, accuracy


def project_to_scale(results, scale_factor):
    """Project current results to production scale"""
    print_l("\n" + "="*100)
    print_l(f"PROJECTION TO PRODUCTION SCALE (×{scale_factor:.1f})")
    print_l("="*100)
    
    data_load_time = results['data_loading']
    gen_time = results['code_generation']
    solver_time = results['solver_execution'][0]
    validation_time = results['validation'][0]
    
    # Data loading doesn't scale (same dataset)
    projected_data = data_load_time
    
    # Generation scales with task count
    projected_gen = gen_time * scale_factor
    
    # Solver execution scales with sample count
    projected_solver = solver_time * scale_factor
    
    # Validation scales with sample count
    projected_validation = validation_time * scale_factor
    
    total_current = data_load_time + gen_time + solver_time + validation_time
    total_projected = projected_data + projected_gen + projected_solver + projected_validation
    
    print_l(f"\nCurrent scale ({results['task_count']} tasks):")
    print_l(f"  Data loading:     {data_load_time:8.3f}s ({data_load_time/total_current*100:5.1f}%)")
    print_l(f"  Code generation:  {gen_time:8.3f}s ({gen_time/total_current*100:5.1f}%)")
    print_l(f"  Solver execution: {solver_time:8.3f}s ({solver_time/total_current*100:5.1f}%)")
    print_l(f"  Validation:       {validation_time:8.3f}s ({validation_time/total_current*100:5.1f}%)")
    print_l(f"  TOTAL:           {total_current:8.3f}s")
    
    print_l(f"\nProjected scale ({results['task_count']*scale_factor:.0f} tasks, {results['sample_count']*scale_factor:.0f} samples):")
    print_l(f"  Data loading:     {projected_data:8.3f}s ({projected_data/total_projected*100:5.1f}%)")
    print_l(f"  Code generation:  {projected_gen:8.3f}s ({projected_gen/total_projected*100:5.1f}%)")
    print_l(f"  Solver execution: {projected_solver:8.3f}s ({projected_solver/total_projected*100:5.1f}%)")
    print_l(f"  Validation:       {projected_validation:8.3f}s ({projected_validation/total_projected*100:5.1f}%)")
    print_l(f"  TOTAL:           {total_projected:8.3f}s")
    
    print_l(f"\nOptimization priorities:")
    components = [
        ('Solver execution', projected_solver, projected_solver/total_projected*100),
        ('Code generation', projected_gen, projected_gen/total_projected*100),
        ('Validation', projected_validation, projected_validation/total_projected*100),
        ('Data loading', projected_data, projected_data/total_projected*100),
    ]
    components.sort(key=lambda x: x[1], reverse=True)
    
    for i, (name, time, pct) in enumerate(components, 1):
        priority = "🔴 HIGH" if pct > 30 else "🟡 MEDIUM" if pct > 10 else "🟢 LOW"
        print_l(f"  {i}. {name:20s} {time:8.3f}s ({pct:5.1f}%) {priority}")


def analyze_gpu_opportunity(solver_time, sample_count, scale_factor):
    """Analyze GPU acceleration opportunity"""
    print_l("\n" + "="*100)
    print_l("GPU ACCELERATION OPPORTUNITY")
    print_l("="*100)
    
    avg_per_sample = (solver_time / sample_count * 1000) if sample_count > 0 else 0
    projected_solver_time = solver_time * scale_factor
    projected_samples = sample_count * scale_factor
    
    print_l(f"\nCurrent (CPU baseline):")
    print_l(f"  Samples: {sample_count}")
    print_l(f"  Time: {solver_time:.3f}s")
    print_l(f"  Rate: {avg_per_sample:.3f}ms per sample")
    
    print_l(f"\nProjected at production scale:")
    print_l(f"  Samples: {projected_samples:.0f}")
    print_l(f"  Time: {projected_solver_time:.3f}s")
    print_l(f"  Rate: {avg_per_sample:.3f}ms per sample")
    
    print_l(f"\nGPU Optimization Scenarios:")
    
    # Scenario 1: GPU DSL (2-6x)
    dsl_time_best = projected_solver_time / 6
    dsl_time_worst = projected_solver_time / 2
    dsl_saved_best = projected_solver_time - dsl_time_best
    dsl_saved_worst = projected_solver_time - dsl_time_worst
    
    print_l(f"\n  1. GPU DSL Operations (2-6x speedup):")
    print_l(f"     Time: {dsl_time_worst:.3f}s - {dsl_time_best:.3f}s")
    print_l(f"     Saved: {dsl_saved_worst:.3f}s - {dsl_saved_best:.3f}s")
    print_l(f"     Effort: HIGH (implement from scratch)")
    print_l(f"     Status: NOT IMPLEMENTED")
    
    # Scenario 2: Batch Operations (10-35x)
    batch_time_best = projected_solver_time / 35
    batch_time_worst = projected_solver_time / 10
    batch_saved_best = projected_solver_time - batch_time_best
    batch_saved_worst = projected_solver_time - batch_time_worst
    
    print_l(f"\n  2. Batch Operations (10-35x speedup):")
    print_l(f"     Time: {batch_time_worst:.3f}s - {batch_time_best:.3f}s")
    print_l(f"     Saved: {batch_saved_worst:.3f}s - {batch_saved_best:.3f}s")
    print_l(f"     Effort: MEDIUM (integrate existing code)")
    print_l(f"     Status: CODE EXISTS, NOT INTEGRATED")
    
    # Scenario 3: Combined (30-50x)
    combined_time_best = projected_solver_time / 50
    combined_time_worst = projected_solver_time / 30
    combined_saved_best = projected_solver_time - combined_time_best
    combined_saved_worst = projected_solver_time - combined_time_worst
    
    print_l(f"\n  3. Combined Optimization (30-50x speedup):")
    print_l(f"     Time: {combined_time_worst:.3f}s - {combined_time_best:.3f}s")
    print_l(f"     Saved: {combined_saved_worst:.3f}s - {combined_saved_best:.3f}s")
    print_l(f"     Effort: HIGH (both optimizations)")
    print_l(f"     Status: BEST PERFORMANCE")
    
    print_l(f"\nRecommendation:")
    if projected_solver_time > 10:
        print_l(f"  🔴 HIGH PRIORITY: Solver execution is {projected_solver_time:.1f}s")
        print_l(f"     Start with batch operations (existing code, 10-35x speedup)")
        print_l(f"     Then add GPU DSL (additional 2-6x speedup)")
        print_l(f"     Combined: {projected_solver_time:.1f}s → {combined_time_worst:.1f}-{combined_time_best:.1f}s")
    elif projected_solver_time > 5:
        print_l(f"  🟡 MEDIUM PRIORITY: Solver execution is {projected_solver_time:.1f}s")
        print_l(f"     Batch operations integration recommended")
    else:
        print_l(f"  🟢 LOW PRIORITY: Solver execution is {projected_solver_time:.1f}s")
        print_l(f"     GPU optimization may not be necessary")


def main():
    parser = argparse.ArgumentParser(description='Profile ARC pipeline performance')
    parser.add_argument('--tasks', type=int, default=10, help='Number of tasks to profile')
    parser.add_argument('--scale', type=float, default=None, help='Scale factor for projection (default: auto-calculate to 400 tasks)')
    args = parser.parse_args()
    
    print_l("="*100)
    print_l("PIPELINE PERFORMANCE PROFILER")
    print_l("="*100)
    print_l(f"Profiling {args.tasks} tasks...")
    print_l("")
    
    results = {}
    
    # Phase 1: Data Loading
    data_time, train_data = profile_data_loading()
    results['data_loading'] = data_time
    
    # Get task IDs
    task_ids = list(train_data['demo'].keys())[:args.tasks]
    results['task_count'] = len(task_ids)
    
    # Phase 2: Code Generation
    gen_time = profile_code_generation(len(task_ids))
    if gen_time is None:
        print_l("\n❌ Pipeline profiling failed at code generation")
        return
    results['code_generation'] = gen_time
    
    # Phase 3: Solver Execution
    solver_result = profile_solver_execution(task_ids, train_data)
    if solver_result is None:
        print_l("\n❌ Pipeline profiling failed at solver execution")
        return
    solver_time, sample_count, avg_per_sample = solver_result
    results['solver_execution'] = (solver_time, sample_count, avg_per_sample)
    results['sample_count'] = sample_count
    
    # Phase 4: Validation
    validation_result = profile_validation(task_ids, train_data)
    if validation_result is None:
        print_l("\n❌ Pipeline profiling failed at validation")
        return
    validation_time, accuracy = validation_result
    results['validation'] = (validation_time, accuracy)
    
    # Calculate scale factor
    if args.scale is None:
        scale_factor = 400 / len(task_ids)  # Scale to 400 tasks
    else:
        scale_factor = args.scale
    
    # Projection to scale
    project_to_scale(results, scale_factor)
    
    # GPU opportunity analysis
    analyze_gpu_opportunity(solver_time, sample_count, scale_factor)
    
    # Summary
    total_time = data_time + gen_time + solver_time + validation_time
    
    print_l("\n" + "="*100)
    print_l("PROFILING COMPLETE")
    print_l("="*100)
    print_l(f"\nTotal time: {total_time:.3f}s for {len(task_ids)} tasks ({sample_count} samples)")
    print_l(f"Average: {total_time/len(task_ids)*1000:.1f}ms per task")
    print_l(f"Average: {total_time/sample_count*1000:.1f}ms per sample")
    print_l(f"Accuracy: {accuracy:.1f}%")
    print_l("")


if __name__ == '__main__':
    main()
