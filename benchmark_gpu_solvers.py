"""
Benchmark GPU-accelerated solvers vs CPU versions.

Tests the 3 profiled solvers with GPU o_g integration.
Measures end-to-end solver performance (not just o_g).
"""

import sys
import time
import statistics
from typing import Dict, List, Tuple

# Import CPU versions
try:
    from solvers_pre import solve_23b5c85d, solve_09629e4f, solve_1f85a75f
    CPU_AVAILABLE = True
except ImportError:
    print("Warning: Could not import CPU solvers")
    CPU_AVAILABLE = False

# Import GPU versions
try:
    from gpu_solvers_pre import gpu_solve_23b5c85d, gpu_solve_09629e4f, gpu_solve_1f85a75f
    GPU_AVAILABLE = True
except ImportError:
    print("Error: Could not import GPU solvers")
    GPU_AVAILABLE = False
    sys.exit(1)

# Check if GPU is actually available
try:
    from gpu_dsl_core import CUPY_AVAILABLE
    if not CUPY_AVAILABLE:
        print("Warning: CuPy not available, GPU solvers will fail")
except ImportError:
    CUPY_AVAILABLE = False


def create_test_inputs():
    """
    Create test inputs for the 3 solvers.
    Using simple grids that should trigger o_g with realistic complexity.
    """
    # Test input for solve_23b5c85d and solve_1f85a75f (similar logic)
    test_grid_1 = (
        (0, 0, 1, 1, 0, 0, 2, 2, 0, 0),
        (0, 1, 1, 1, 1, 0, 2, 2, 2, 0),
        (0, 1, 1, 1, 0, 0, 0, 2, 0, 0),
        (0, 0, 1, 0, 0, 3, 3, 0, 0, 0),
        (0, 0, 0, 0, 3, 3, 3, 3, 0, 0),
        (0, 4, 4, 0, 3, 3, 3, 0, 0, 5),
        (0, 4, 0, 0, 0, 3, 0, 0, 5, 5),
        (0, 0, 0, 0, 0, 0, 0, 5, 5, 5),
        (6, 6, 0, 7, 7, 0, 0, 5, 5, 0),
        (6, 0, 0, 7, 0, 0, 0, 0, 0, 0),
    )
    
    # Test input for solve_09629e4f
    test_grid_2 = (
        (1, 1, 0, 2, 2, 0, 3, 3),
        (1, 0, 0, 0, 2, 0, 3, 0),
        (0, 0, 4, 4, 0, 0, 0, 0),
        (5, 5, 4, 0, 0, 6, 6, 6),
        (5, 0, 0, 0, 0, 6, 0, 6),
        (0, 0, 7, 7, 0, 0, 0, 0),
    )
    
    return {
        '23b5c85d': (None, test_grid_1, None),  # (S, I, C)
        '09629e4f': (None, test_grid_2, None),
        '1f85a75f': (None, test_grid_1, None),
    }


def benchmark_solver(solver_func, inputs, n_runs=100, warmup=5):
    """
    Benchmark a solver function.
    
    Args:
        solver_func: Solver function to benchmark
        inputs: (S, I, C) tuple
        n_runs: Number of timing runs
        warmup: Number of warmup runs
    
    Returns:
        (median_time_ms, all_times_ms)
    """
    S, I, C = inputs
    
    # Warmup
    for _ in range(warmup):
        try:
            _ = solver_func(S, I, C)
        except Exception as e:
            print(f"  Warmup error: {e}")
            return None, []
    
    # Benchmark
    times = []
    for _ in range(n_runs):
        start = time.perf_counter()
        try:
            _ = solver_func(S, I, C)
            elapsed = (time.perf_counter() - start) * 1000  # ms
            times.append(elapsed)
        except Exception as e:
            print(f"  Benchmark error: {e}")
            return None, []
    
    if not times:
        return None, []
    
    median = statistics.median(times)
    return median, times


def validate_correctness(solver_id, cpu_func, gpu_func, inputs):
    """
    Validate that GPU solver produces same result as CPU solver.
    
    Returns:
        (matches, cpu_result, gpu_result)
    """
    S, I, C = inputs
    
    try:
        cpu_result = cpu_func(S, I, C)
    except Exception as e:
        print(f"  CPU solver error: {e}")
        return None, None, None
    
    try:
        gpu_result = gpu_func(S, I, C)
    except Exception as e:
        print(f"  GPU solver error: {e}")
        return None, cpu_result, None
    
    matches = cpu_result == gpu_result
    return matches, cpu_result, gpu_result


def main():
    """Run benchmarks on all 3 solvers."""
    print("=" * 70)
    print("GPU SOLVER BENCHMARKING - WEEK 2")
    print("=" * 70)
    print()
    
    if not CPU_AVAILABLE:
        print("Error: CPU solvers not available")
        return
    
    if not GPU_AVAILABLE:
        print("Error: GPU solvers not available")
        return
    
    if not CUPY_AVAILABLE:
        print("Warning: CuPy not available - GPU solvers may fail")
        print()
    
    # Test inputs
    test_inputs = create_test_inputs()
    
    # Solver pairs
    solvers = [
        ('23b5c85d', solve_23b5c85d, gpu_solve_23b5c85d, 8.2, 92),
        ('09629e4f', solve_09629e4f, gpu_solve_09629e4f, 6.8, 82),
        ('1f85a75f', solve_1f85a75f, gpu_solve_1f85a75f, 5.4, 75),
    ]
    
    results = []
    
    for solver_id, cpu_func, gpu_func, expected_cpu_ms, o_g_percent in solvers:
        print(f"Testing solver: {solver_id}")
        print(f"  Expected CPU time: {expected_cpu_ms}ms")
        print(f"  o_g percentage: {o_g_percent}%")
        
        inputs = test_inputs[solver_id]
        
        # Validate correctness
        print(f"  Validating correctness...")
        matches, cpu_result, gpu_result = validate_correctness(
            solver_id, cpu_func, gpu_func, inputs
        )
        
        if matches is None:
            print(f"  ✗ Validation failed (error)")
            results.append({
                'id': solver_id,
                'error': 'validation_error'
            })
            print()
            continue
        
        if not matches:
            print(f"  ✗ Results don't match!")
            print(f"    CPU result: {cpu_result}")
            print(f"    GPU result: {gpu_result}")
            results.append({
                'id': solver_id,
                'error': 'mismatch'
            })
            print()
            continue
        
        print(f"  ✓ Results match")
        
        # Benchmark CPU
        print(f"  Benchmarking CPU version...")
        cpu_median, cpu_times = benchmark_solver(cpu_func, inputs, n_runs=100, warmup=10)
        
        if cpu_median is None:
            print(f"  ✗ CPU benchmark failed")
            results.append({
                'id': solver_id,
                'error': 'cpu_benchmark_error'
            })
            print()
            continue
        
        print(f"    CPU median: {cpu_median:.3f}ms")
        
        # Benchmark GPU
        print(f"  Benchmarking GPU version...")
        gpu_median, gpu_times = benchmark_solver(gpu_func, inputs, n_runs=100, warmup=10)
        
        if gpu_median is None:
            print(f"  ✗ GPU benchmark failed")
            results.append({
                'id': solver_id,
                'cpu_time': cpu_median,
                'error': 'gpu_benchmark_error'
            })
            print()
            continue
        
        print(f"    GPU median: {gpu_median:.3f}ms")
        
        speedup = cpu_median / gpu_median if gpu_median > 0 else 0
        print(f"    Speedup: {speedup:.2f}x")
        
        # Compare to expected
        if speedup >= 1.5:
            print(f"  ✓ Meets target (≥1.5x)")
        else:
            print(f"  ⚠ Below target (1.5x)")
        
        results.append({
            'id': solver_id,
            'cpu_time': cpu_median,
            'gpu_time': gpu_median,
            'speedup': speedup,
            'expected_cpu': expected_cpu_ms,
            'o_g_percent': o_g_percent,
        })
        
        print()
    
    # Summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    
    successful = [r for r in results if 'error' not in r]
    
    if not successful:
        print("✗ No successful benchmarks")
        return
    
    print(f"{'Solver':<12} {'CPU (ms)':<10} {'GPU (ms)':<10} {'Speedup':<10} {'Target':<10}")
    print("-" * 70)
    
    for r in successful:
        status = "✓" if r['speedup'] >= 1.5 else "⚠"
        print(f"{r['id']:<12} {r['cpu_time']:<10.3f} {r['gpu_time']:<10.3f} "
              f"{r['speedup']:<10.2f}x {status}")
    
    print("-" * 70)
    
    avg_cpu = sum(r['cpu_time'] for r in successful) / len(successful)
    avg_gpu = sum(r['gpu_time'] for r in successful) / len(successful)
    avg_speedup = avg_cpu / avg_gpu if avg_gpu > 0 else 0
    
    print(f"{'AVERAGE':<12} {avg_cpu:<10.3f} {avg_gpu:<10.3f} {avg_speedup:<10.2f}x")
    
    print()
    print(f"Expected speedup: 1.7-2.1x")
    print(f"Actual speedup: {avg_speedup:.2f}x")
    
    if avg_speedup >= 1.5:
        print()
        print("✓ WEEK 2 SUCCESS - Ready for Week 3")
    else:
        print()
        print("⚠ Below target - may need optimization")
    
    print("=" * 70)


if __name__ == '__main__':
    main()
