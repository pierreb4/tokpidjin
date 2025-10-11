"""
Realistic GPU Hybrid Strategy Benchmark

Tests the hybrid CPU/GPU strategy on REAL ARC tasks using the actual
solver infrastructure from run_test.py. This provides realistic
performance data across diverse grid sizes and operations.

Usage:
  # Analyze grid sizes
  python benchmark_hybrid_realistic.py --analyze          # Just hybrid solvers (6 tasks)
  python benchmark_hybrid_realistic.py --analyze-all      # All ARC training tasks (400 tasks)
  python benchmark_hybrid_realistic.py --analyze -k 23b5c85d  # Specific task
  
  # Benchmark performance
  python benchmark_hybrid_realistic.py                    # Test all hybrid solvers
  python benchmark_hybrid_realistic.py -k 23b5c85d -v     # Test specific task with verbose errors
"""

import argparse
import time
import importlib
from collections import defaultdict
import numpy as np

# Import core modules
from utils import get_data, get_solver_source, load_module
from dsl import *
from constants import *

# Import solver modules
import solvers_pre
import gpu_solvers_pre
import gpu_solvers_hybrid


def get_grid_size(grid):
    """Calculate total cells in a grid."""
    if isinstance(grid, (tuple, list)):
        return len(grid) * len(grid[0]) if grid else 0
    return 0


def analyze_task_grid_sizes(data, task_ids=None):
    """
    Analyze the distribution of grid sizes in ARC tasks.
    This helps understand what threshold values make sense.
    """
    if task_ids is None:
        task_ids = list(data['demo'].keys())
    
    grid_sizes = []
    
    print("=" * 70)
    print("GRID SIZE ANALYSIS")
    print("=" * 70)
    
    for task_id in task_ids:
        task = data['demo'][task_id] + data['test'][task_id]
        
        for i, sample in enumerate(task):
            input_size = get_grid_size(sample['input'])
            output_size = get_grid_size(sample['output'])
            grid_sizes.append(input_size)
            grid_sizes.append(output_size)
            
            if len(task_ids) == 1:  # Verbose output for single task
                print(f"  Sample {i}: Input={input_size} cells, Output={output_size} cells")
    
    grid_sizes = np.array(grid_sizes)
    
    print(f"\nTotal grids analyzed: {len(grid_sizes)}")
    print(f"Grid size statistics:")
    print(f"  Min:     {grid_sizes.min()} cells")
    print(f"  Max:     {grid_sizes.max()} cells")
    print(f"  Mean:    {grid_sizes.mean():.1f} cells")
    print(f"  Median:  {np.median(grid_sizes):.1f} cells")
    print(f"  25th %:  {np.percentile(grid_sizes, 25):.1f} cells")
    print(f"  75th %:  {np.percentile(grid_sizes, 75):.1f} cells")
    
    # Distribution by size ranges
    print(f"\nGrid size distribution:")
    ranges = [(0, 30), (30, 50), (50, 70), (70, 100), (100, 200), (200, 500), (500, float('inf'))]
    for low, high in ranges:
        count = ((grid_sizes >= low) & (grid_sizes < high)).sum()
        pct = 100 * count / len(grid_sizes)
        range_str = f"{low}-{high}" if high != float('inf') else f"{low}+"
        print(f"  {range_str:>10} cells: {count:4d} ({pct:5.1f}%)")
    
    return grid_sizes


def benchmark_solver_realistic(task_id, data, n_trials=50, verbose=False):
    """
    Benchmark a single solver on real ARC task data.
    
    Args:
        task_id: The ARC task ID (e.g., '23b5c85d')
        data: The ARC dataset
        n_trials: Number of benchmark trials per sample
        verbose: Show detailed error messages
    
    Returns:
        dict: Results including times, correctness, and grid info
        None: If solver versions not available or task not found
    """
    # Check if we have all three solver versions
    cpu_solver_name = f'solve_{task_id}'
    gpu_solver_name = f'gpu_solve_{task_id}'
    hybrid_solver_name = f'gpu_solve_{task_id}_hybrid'
    
    has_cpu = hasattr(solvers_pre, cpu_solver_name)
    has_gpu = hasattr(gpu_solvers_pre, gpu_solver_name)
    has_hybrid = hasattr(gpu_solvers_hybrid, hybrid_solver_name)
    
    if verbose:
        print(f"  Checking {task_id}: CPU={has_cpu}, GPU={has_gpu}, Hybrid={has_hybrid}")
    
    if not (has_cpu and has_gpu and has_hybrid):
        missing = []
        if not has_cpu:
            missing.append("CPU")
        if not has_gpu:
            missing.append("GPU")
        if not has_hybrid:
            missing.append("Hybrid")
        if verbose:
            print(f"  Missing solver versions: {', '.join(missing)}")
        return None
    
    # Get the solvers
    cpu_solver = getattr(solvers_pre, cpu_solver_name)
    gpu_solver = getattr(gpu_solvers_pre, gpu_solver_name)
    hybrid_solver = getattr(gpu_solvers_hybrid, hybrid_solver_name)
    
    # Get task data
    if task_id not in data['demo']:
        if verbose:
            print(f"  Task {task_id} not found in dataset")
        return None
    
    task = data['demo'][task_id] + data['test'][task_id]
    S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in task)
    
    results = {
        'task_id': task_id,
        'samples': [],
        'cpu_correct': 0,
        'gpu_correct': 0,
        'hybrid_correct': 0,
        'errors': [],  # Track errors encountered
    }
    
    # Test each sample in the task
    for sample_idx, sample in enumerate(task):
        I = sample['input']
        expected = sample['output']
        grid_size = get_grid_size(I)
        
        sample_result = {
            'index': sample_idx,
            'grid_size': grid_size,
            'cpu_time': 0,
            'gpu_time': 0,
            'hybrid_time': 0,
            'cpu_correct': False,
            'gpu_correct': False,
            'hybrid_correct': False,
        }
        
        # Test CPU version
        try:
            cpu_output = cpu_solver(S, I, None)
            sample_result['cpu_correct'] = (cpu_output == expected)
            
            # Benchmark
            start = time.perf_counter()
            for _ in range(n_trials):
                cpu_solver(S, I, None)
            sample_result['cpu_time'] = (time.perf_counter() - start) / n_trials * 1000
        except Exception as e:
            error_msg = f"CPU error on sample {sample_idx}: {type(e).__name__}: {str(e)}"
            if verbose:
                print(f"  {error_msg}")
            results['errors'].append(error_msg)
        
        # Test GPU version
        try:
            gpu_output = gpu_solver(S, I, None)
            sample_result['gpu_correct'] = (gpu_output == expected)
            
            # Benchmark
            start = time.perf_counter()
            for _ in range(n_trials):
                gpu_solver(S, I, None)
            sample_result['gpu_time'] = (time.perf_counter() - start) / n_trials * 1000
        except Exception as e:
            error_msg = f"GPU error on sample {sample_idx}: {type(e).__name__}: {str(e)}"
            if verbose:
                print(f"  {error_msg}")
            results['errors'].append(error_msg)
        
        # Test Hybrid version
        try:
            hybrid_output = hybrid_solver(S, I, None)
            sample_result['hybrid_correct'] = (hybrid_output == expected)
            
            # Benchmark
            start = time.perf_counter()
            for _ in range(n_trials):
                hybrid_solver(S, I, None)
            sample_result['hybrid_time'] = (time.perf_counter() - start) / n_trials * 1000
        except Exception as e:
            error_msg = f"Hybrid error on sample {sample_idx}: {type(e).__name__}: {str(e)}"
            if verbose:
                print(f"  {error_msg}")
            results['errors'].append(error_msg)
        
        results['samples'].append(sample_result)
        results['cpu_correct'] += sample_result['cpu_correct']
        results['gpu_correct'] += sample_result['gpu_correct']
        results['hybrid_correct'] += sample_result['hybrid_correct']
    
    return results


def print_solver_results(results):
    """Print detailed results for a single solver."""
    print(f"\nTesting solver: {results['task_id']}")
    print(f"  Correctness: CPU={results['cpu_correct']}/{len(results['samples'])}, "
          f"GPU={results['gpu_correct']}/{len(results['samples'])}, "
          f"Hybrid={results['hybrid_correct']}/{len(results['samples'])}")
    
    # Show errors if any
    if results['errors']:
        print(f"  Errors encountered: {len(results['errors'])}")
        for error in results['errors'][:3]:  # Show first 3 errors
            print(f"    - {error}")
        if len(results['errors']) > 3:
            print(f"    ... and {len(results['errors']) - 3} more")
    
    for sample in results['samples']:
        idx = sample['index']
        size = sample['grid_size']
        cpu_t = sample['cpu_time']
        gpu_t = sample['gpu_time']
        hyb_t = sample['hybrid_time']
        
        # Determine which performed best
        times = [('CPU', cpu_t), ('GPU', gpu_t), ('Hybrid', hyb_t)]
        times = [(name, t) for name, t in times if t > 0]
        if times:
            best = min(times, key=lambda x: x[1])[0]
        else:
            best = 'N/A'
        
        # Check correctness
        correct_str = ""
        if not sample['cpu_correct']:
            correct_str += " [CPU WRONG]"
        if not sample['gpu_correct']:
            correct_str += " [GPU WRONG]"
        if not sample['hybrid_correct']:
            correct_str += " [HYBRID WRONG]"
        
        print(f"  Sample {idx} ({size:3d} cells): "
              f"CPU={cpu_t:6.2f}ms, GPU={gpu_t:6.2f}ms, Hybrid={hyb_t:6.2f}ms "
              f"→ Best: {best}{correct_str}")


def print_summary(all_results):
    """Print summary statistics across all tested solvers."""
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    # Aggregate results
    total_samples = sum(len(r['samples']) for r in all_results)
    total_cpu_correct = sum(r['cpu_correct'] for r in all_results)
    total_gpu_correct = sum(r['gpu_correct'] for r in all_results)
    total_hybrid_correct = sum(r['hybrid_correct'] for r in all_results)
    
    print(f"\nTotal samples tested: {total_samples}")
    print(f"Correctness:")
    print(f"  CPU:    {total_cpu_correct}/{total_samples} "
          f"({100*total_cpu_correct/total_samples:.1f}%)")
    print(f"  GPU:    {total_gpu_correct}/{total_samples} "
          f"({100*total_gpu_correct/total_samples:.1f}%)")
    print(f"  Hybrid: {total_hybrid_correct}/{total_samples} "
          f"({100*total_hybrid_correct/total_samples:.1f}%)")
    
    # Performance analysis by grid size ranges
    print(f"\nPerformance by grid size:")
    size_buckets = defaultdict(lambda: {'cpu': [], 'gpu': [], 'hybrid': []})
    
    for results in all_results:
        for sample in results['samples']:
            size = sample['grid_size']
            # Categorize by size
            if size < 50:
                bucket = '<50'
            elif size < 70:
                bucket = '50-70'
            elif size < 100:
                bucket = '70-100'
            elif size < 200:
                bucket = '100-200'
            else:
                bucket = '200+'
            
            size_buckets[bucket]['cpu'].append(sample['cpu_time'])
            size_buckets[bucket]['gpu'].append(sample['gpu_time'])
            size_buckets[bucket]['hybrid'].append(sample['hybrid_time'])
    
    print(f"\n{'Size Range':<12} {'Count':>6} {'CPU (ms)':>10} {'GPU (ms)':>10} "
          f"{'Hybrid (ms)':>10} {'Best':>8}")
    print("-" * 70)
    
    for bucket in ['<50', '50-70', '70-100', '100-200', '200+']:
        if bucket not in size_buckets:
            continue
        
        data = size_buckets[bucket]
        count = len(data['cpu'])
        cpu_avg = np.mean(data['cpu'])
        gpu_avg = np.mean(data['gpu'])
        hyb_avg = np.mean(data['hybrid'])
        
        best = min([('CPU', cpu_avg), ('GPU', gpu_avg), ('Hybrid', hyb_avg)],
                   key=lambda x: x[1])[0]
        
        print(f"{bucket:<12} {count:>6} {cpu_avg:>9.2f} {gpu_avg:>10.2f} "
              f"{hyb_avg:>10.2f} {best:>8}")
    
    # Overall averages
    all_cpu = [s['cpu_time'] for r in all_results for s in r['samples']]
    all_gpu = [s['gpu_time'] for r in all_results for s in r['samples']]
    all_hybrid = [s['hybrid_time'] for r in all_results for s in r['samples']]
    
    print("-" * 70)
    print(f"{'AVERAGE':<12} {len(all_cpu):>6} {np.mean(all_cpu):>9.2f} "
          f"{np.mean(all_gpu):>10.2f} {np.mean(all_hybrid):>10.2f}")
    
    print(f"\nSpeedups:")
    print(f"  GPU vs CPU:    {np.mean(all_cpu)/np.mean(all_gpu):.2f}x")
    print(f"  Hybrid vs CPU: {np.mean(all_cpu)/np.mean(all_hybrid):.2f}x")
    print(f"  Hybrid vs GPU: {np.mean(all_gpu)/np.mean(all_hybrid):.2f}x")


def main():
    parser = argparse.ArgumentParser(description="Realistic GPU Hybrid Benchmark")
    parser.add_argument("-k", "--task_id", help="Specific task to test", type=str)
    parser.add_argument("--analyze", help="Only analyze grid sizes", action="store_true")
    parser.add_argument("--analyze-all", help="Analyze all ARC tasks (not just hybrid solvers)", 
                        action="store_true")
    parser.add_argument("-n", "--trials", help="Number of benchmark trials", 
                        type=int, default=50)
    parser.add_argument("-v", "--verbose", help="Show detailed error messages",
                        action="store_true")
    args = parser.parse_args()
    
    # Load ARC data
    print("Loading ARC data...")
    train_data = get_data(train=True)
    
    # Get available hybrid solvers
    hybrid_solvers = [name[10:-7] for name in dir(gpu_solvers_hybrid)
                      if name.startswith('gpu_solve_') and name.endswith('_hybrid')]
    
    print(f"Found {len(hybrid_solvers)} hybrid solver(s): {', '.join(hybrid_solvers)}")
    
    # Determine which tasks to analyze/test
    if args.analyze or args.analyze_all:
        # For analysis, can use all tasks or just hybrid solvers
        if args.analyze_all:
            task_ids = list(train_data['demo'].keys())
            print(f"\nAnalyzing ALL {len(task_ids)} ARC training tasks")
        elif args.task_id:
            task_ids = [args.task_id]
            print(f"\nAnalyzing specific task: {args.task_id}")
        else:
            task_ids = hybrid_solvers
            print(f"\nAnalyzing {len(task_ids)} hybrid solver tasks")
        
        analyze_task_grid_sizes(train_data, task_ids)
        return
    
    # For benchmarking, determine which tasks to test
    if args.task_id:
        task_ids = [args.task_id]
        print(f"\nTesting specific task: {args.task_id}")
    else:
        task_ids = hybrid_solvers
        print(f"\nTesting all {len(task_ids)} hybrid solvers")
    
    print("\n" + "=" * 70)
    print("REALISTIC HYBRID STRATEGY BENCHMARK")
    print("=" * 70)
    print(f"\nTrials per sample: {args.trials}")
    print(f"Verbose mode: {'ON' if args.verbose else 'OFF'}")
    
    # Benchmark each solver
    all_results = []
    skipped = []
    
    for task_id in task_ids:
        results = benchmark_solver_realistic(task_id, train_data, args.trials, 
                                            verbose=args.verbose)
        if results:
            all_results.append(results)
            print_solver_results(results)
        else:
            skipped.append(task_id)
            if args.verbose:
                print(f"\nSkipping {task_id}: Not all versions available or task not found")
    
    # Print summary
    if all_results:
        print_summary(all_results)
    else:
        print("\n❌ No solvers could be tested!")
        
    # Show skipped solvers
    if skipped:
        print(f"\n⚠️  Skipped {len(skipped)} solver(s): {', '.join(skipped)}")
        if not args.verbose:
            print("   Use -v/--verbose to see why they were skipped")
    
    # Final status
    print("\n" + "=" * 70)
    if all_results:
        print(f"✅ Successfully tested {len(all_results)}/{len(task_ids)} solvers")
    else:
        print("❌ No valid results - check that hybrid solvers exist")
    print("=" * 70)


if __name__ == "__main__":
    main()
