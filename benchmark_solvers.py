#!/usr/bin/env python3
"""
Benchmark solver functions to determine GPU viability.

This script measures the actual CPU execution time of solver functions
from solvers_pre.py to validate the "50x longer than DSL ops" estimate.

Expected outcomes:
- Simple solvers (2-5 ops): 0.2-1ms → Too fast for GPU
- Medium solvers (10-20 ops): 2-10ms → GPU viable
- Complex solvers (30+ ops): 10-50ms → GPU highly viable
"""

import time
import statistics
import sys
import ast
import inspect
from typing import List, Tuple, Dict
from utils import get_data, print_l
import solvers_pre
from dsl import *
from constants import *


def count_operations(solver_func) -> int:
    """Count number of DSL operations in solver function."""
    try:
        source = inspect.getsource(solver_func)
        tree = ast.parse(source)
        
        # Count assignments (x1 = ..., x2 = ..., etc.)
        op_count = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                op_count += 1
        
        return op_count
    except Exception as e:
        return -1


def benchmark_solver(
    solver_func, 
    S: tuple, 
    I: tuple, 
    C: None,
    warmup_iters: int = 10,
    benchmark_iters: int = 50
) -> Tuple[float, bool]:
    """
    Benchmark a single solver function.
    
    Returns:
        (avg_time_ms, success): Average execution time in ms and success flag
    """
    # Warmup runs (JIT compilation, cache warming)
    for _ in range(warmup_iters):
        try:
            result = solver_func(S, I, C)
        except Exception:
            return -1.0, False
    
    # Benchmark runs
    times = []
    success = True
    
    for _ in range(benchmark_iters):
        try:
            start = time.perf_counter()
            result = solver_func(S, I, C)
            elapsed = time.perf_counter() - start
            times.append(elapsed * 1000)  # Convert to ms
        except Exception as e:
            success = False
            break
    
    if not success or len(times) == 0:
        return -1.0, False
    
    # Return median time (more robust than mean)
    return statistics.median(times), True


def select_solvers_to_benchmark() -> List[str]:
    """
    Select representative solvers of varying complexity.
    
    Returns list of solver task_ids (without 'solve_' prefix).
    """
    # Get all solver names from solvers_pre
    all_solvers = [name[6:] for name in dir(solvers_pre) 
                   if name.startswith('solve_') and not name.startswith('solve__')]
    
    # Analyze complexity of each solver
    solver_complexity = []
    for task_id in all_solvers[:100]:  # Sample first 100 for speed
        solver_func = getattr(solvers_pre, f'solve_{task_id}')
        op_count = count_operations(solver_func)
        if op_count > 0:
            solver_complexity.append((task_id, op_count))
    
    # Sort by complexity
    solver_complexity.sort(key=lambda x: x[1])
    
    # Select representative sample across complexity spectrum
    selected = []
    
    # Simple solvers (2-5 operations)
    simple = [s for s in solver_complexity if 2 <= s[1] <= 5]
    selected.extend([s[0] for s in simple[:5]])
    
    # Medium solvers (6-15 operations)
    medium = [s for s in solver_complexity if 6 <= s[1] <= 15]
    selected.extend([s[0] for s in medium[:10]])
    
    # Complex solvers (16-30 operations)
    complex_solvers = [s for s in solver_complexity if 16 <= s[1] <= 30]
    selected.extend([s[0] for s in complex_solvers[:10]])
    
    # Very complex solvers (31+ operations)
    very_complex = [s for s in solver_complexity if s[1] >= 31]
    selected.extend([s[0] for s in very_complex[:5]])
    
    return selected


def main():
    print_l("=" * 80)
    print_l("SOLVER FUNCTION BENCHMARK")
    print_l("Measuring CPU execution time to determine GPU viability")
    print_l("=" * 80)
    print()
    
    # Load ARC data
    print_l("Loading ARC data...")
    train_data = get_data(train=True)
    eval_data = get_data(train=False)
    total_data = {k: {**train_data[k], **eval_data[k]} for k in ['demo', 'test']}
    print_l(f"Loaded {len(total_data['demo'])} tasks")
    print()
    
    # Select solvers to benchmark
    print_l("Selecting representative solvers...")
    selected_solvers = select_solvers_to_benchmark()
    print_l(f"Selected {len(selected_solvers)} solvers across complexity spectrum")
    print()
    
    # Benchmark each solver
    print_l("=" * 80)
    print_l(f"{'Task ID':<12} {'Ops':<6} {'Time (ms)':<12} {'Category':<15} {'GPU Viable'}")
    print_l("=" * 80)
    
    results = []
    
    for task_id in selected_solvers:
        # Get solver function
        solver_func = getattr(solvers_pre, f'solve_{task_id}')
        op_count = count_operations(solver_func)
        
        # Get task data
        if task_id not in total_data['demo']:
            continue
        
        task = total_data['demo'][task_id]
        if len(task) == 0:
            continue
        
        # Use first sample for benchmarking
        sample = task[0]
        S = tuple((tuple(s['input']), tuple(s['output'])) for s in task)
        I = sample['input']
        
        # Benchmark
        avg_time_ms, success = benchmark_solver(solver_func, S, I, None)
        
        if not success:
            continue
        
        # Categorize
        if avg_time_ms < 1.0:
            category = "Too Fast"
            gpu_viable = "❌ No"
        elif avg_time_ms < 5.0:
            category = "Borderline"
            gpu_viable = "⚠️  Maybe"
        elif avg_time_ms < 15.0:
            category = "Good Candidate"
            gpu_viable = "✅ Yes"
        else:
            category = "Excellent"
            gpu_viable = "✅✅ Yes"
        
        results.append({
            'task_id': task_id,
            'op_count': op_count,
            'time_ms': avg_time_ms,
            'category': category,
            'gpu_viable': gpu_viable
        })
        
        print_l(f"{task_id:<12} {op_count:<6} {avg_time_ms:>8.3f} ms  {category:<15} {gpu_viable}")
    
    print_l("=" * 80)
    print()
    
    # Summary statistics
    if len(results) > 0:
        times = [r['time_ms'] for r in results]
        op_counts = [r['op_count'] for r in results]
        
        print_l("SUMMARY STATISTICS")
        print_l("=" * 80)
        print_l(f"Total solvers benchmarked: {len(results)}")
        print_l("")
        print_l(f"Execution Time (ms):")
        print_l(f"  Min:    {min(times):.3f} ms")
        print_l(f"  Median: {statistics.median(times):.3f} ms")
        print_l(f"  Mean:   {statistics.mean(times):.3f} ms")
        print_l(f"  Max:    {max(times):.3f} ms")
        print_l("")
        print_l(f"Operation Count:")
        print_l(f"  Min:    {min(op_counts)}")
        print_l(f"  Median: {int(statistics.median(op_counts))}")
        print_l(f"  Mean:   {statistics.mean(op_counts):.1f}")
        print_l(f"  Max:    {max(op_counts)}")
        print_l("")
        
        # GPU viability breakdown
        too_fast = len([r for r in results if r['category'] == 'Too Fast'])
        borderline = len([r for r in results if r['category'] == 'Borderline'])
        good = len([r for r in results if r['category'] == 'Good Candidate'])
        excellent = len([r for r in results if r['category'] == 'Excellent'])
        
        print_l(f"GPU Viability Breakdown:")
        print_l(f"  Too Fast (<1ms):        {too_fast:>3} ({too_fast/len(results)*100:>5.1f}%)")
        print_l(f"  Borderline (1-5ms):     {borderline:>3} ({borderline/len(results)*100:>5.1f}%)")
        print_l(f"  Good Candidate (5-15ms): {good:>3} ({good/len(results)*100:>5.1f}%)")
        print_l(f"  Excellent (>15ms):      {excellent:>3} ({excellent/len(results)*100:>5.1f}%)")
        print_l("")
        
        gpu_viable_count = borderline + good + excellent
        print_l(f"GPU Viable (≥1ms):      {gpu_viable_count:>3} ({gpu_viable_count/len(results)*100:>5.1f}%)")
        print_l("=" * 80)
        print_l("")
        
        # Comparison to p_g
        print_l("COMPARISON TO INDIVIDUAL DSL OPERATION (p_g)")
        print_l("=" * 80)
        p_g_time = 0.1159  # From our p_g benchmark
        median_solver_time = statistics.median(times)
        speedup_vs_p_g = median_solver_time / p_g_time
        
        print_l(f"p_g CPU time:           {p_g_time:.4f} ms")
        print_l(f"Median solver time:     {median_solver_time:.4f} ms")
        print_l(f"Solver is {speedup_vs_p_g:.1f}x longer than p_g")
        print_l("")
        
        gpu_overhead = 0.2  # ms
        print_l(f"GPU overhead:           {gpu_overhead:.4f} ms")
        print_l(f"Overhead for p_g:       {gpu_overhead/p_g_time*100:.1f}% (kills speedup)")
        print_l(f"Overhead for median solver: {gpu_overhead/median_solver_time*100:.1f}% (negligible)")
        print_l("=" * 80)
        print_l("")
        
        # Recommendations
        print_l("RECOMMENDATIONS")
        print_l("=" * 80)
        
        if median_solver_time >= 5.0:
            print_l("✅ SOLVERS ARE EXCELLENT GPU CANDIDATES")
            print_l("")
            print_l(f"Median solver time ({median_solver_time:.1f}ms) is {speedup_vs_p_g:.0f}x longer than p_g.")
            print_l(f"GPU overhead ({gpu_overhead}ms) is only {gpu_overhead/median_solver_time*100:.1f}% of execution time.")
            print_l("")
            print_l("Expected GPU speedup: 2-4x")
            print_l("")
            print_l("Next steps:")
            print_l("1. Implement GPU version of one medium-complexity solver")
            print_l("2. Benchmark GPU vs CPU (expect 2-4x speedup)")
            print_l("3. If successful, scale to 50-100 solvers")
            print_l("4. Consider batching for 4-8x speedup")
        elif median_solver_time >= 1.0:
            print_l("⚠️  SOLVERS ARE BORDERLINE GPU CANDIDATES")
            print_l("")
            print_l(f"Median solver time ({median_solver_time:.1f}ms) is only {speedup_vs_p_g:.0f}x longer than p_g.")
            print_l(f"GPU overhead ({gpu_overhead}ms) is {gpu_overhead/median_solver_time*100:.1f}% of execution time.")
            print_l("")
            print_l("Expected GPU speedup: 1.2-2x (marginal)")
            print_l("")
            print_l("Recommendations:")
            print_l("- Focus on complex solvers (>5ms)")
            print_l("- Consider Numba JIT instead of GPU")
            print_l("- Test one solver before committing")
        else:
            print_l("❌ SOLVERS ARE TOO FAST FOR GPU")
            print_l("")
            print_l(f"Median solver time ({median_solver_time:.1f}ms) is only {speedup_vs_p_g:.0f}x longer than p_g.")
            print_l(f"GPU overhead ({gpu_overhead}ms) is {gpu_overhead/median_solver_time*100:.1f}% of execution time.")
            print_l("")
            print_l("GPU acceleration not recommended.")
            print_l("")
            print_l("Consider:")
            print_l("- Numba JIT compilation for CPU")
            print_l("- PyPy for faster Python execution")
            print_l("- Profile-guided optimization")
        
        print_l("=" * 80)


if __name__ == '__main__':
    main()
