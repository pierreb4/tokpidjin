"""
Hybrid CPU/GPU o_g implementation.

Smart wrapper that automatically chooses CPU or GPU based on grid size,
providing optimal performance across all grid sizes.

Usage:
    from gpu_hybrid import o_g_hybrid
    
    # Automatic selection based on grid size
    objects = o_g_hybrid(grid, R7)
    
    # Explicit control if needed
    objects = o_g_hybrid(grid, R7, force_mode='gpu')  # Force GPU
    objects = o_g_hybrid(grid, R7, force_mode='cpu')  # Force CPU
"""

from typing import Literal
from arc_types import Grid, Objects

# Default threshold: grids smaller than this use CPU
# Based on Week 1 & 2 benchmarks:
# - < 50 cells: GPU 0.43x-0.59x (CPU faster)
# - 100 cells (10×10): GPU 1.86x (GPU faster)
# Threshold at ~60-80 cells (8×8 to 9×9)
DEFAULT_THRESHOLD = 70  # cells


def o_g_hybrid(
    grid: Grid,
    type: int,  # o_g mode (0-7)
    threshold: int = DEFAULT_THRESHOLD,
    force_mode: Literal['auto', 'cpu', 'gpu'] = 'auto',
    return_format: Literal['frozenset', 'tuple'] = 'frozenset'
) -> Objects:
    """
    Smart o_g that automatically selects CPU or GPU based on grid size.
    
    Args:
        grid: Input grid
        type: o_g mode (0-7)
        threshold: Cell count threshold (default 70)
                  Grids < threshold use CPU, >= threshold use GPU
        force_mode: Override automatic selection
                   'auto': Use threshold-based selection (default)
                   'cpu': Force CPU version
                   'gpu': Force GPU version
        return_format: Only used if GPU selected
                      'frozenset': DSL-compatible (default)
                      'tuple': Faster for GPU-resident operations
    
    Returns:
        Objects (frozenset of frozensets, or tuple of tuples if GPU + tuple mode)
    
    Performance characteristics:
        Small grids (< 8×8):  CPU is faster (no GPU overhead)
        Large grids (≥ 10×10): GPU is faster (compute > overhead)
        Mixed workload: Hybrid is optimal (30-50% better than pure GPU/CPU)
    
    Examples:
        >>> # Automatic selection
        >>> small_grid = ((1, 2), (3, 4))  # 2×2 = 4 cells → CPU
        >>> objects = o_g_hybrid(small_grid, R7)
        
        >>> # Large grid
        >>> large_grid = tuple(tuple(range(15)) for _ in range(15))  # 15×15 = 225 cells → GPU
        >>> objects = o_g_hybrid(large_grid, R7)
        
        >>> # Force GPU even for small grid
        >>> objects = o_g_hybrid(small_grid, R7, force_mode='gpu')
    """
    # Calculate grid size
    if not grid or len(grid) == 0:
        # Empty grid - use CPU (trivial case)
        from dsl import o_g as cpu_o_g
        return cpu_o_g(grid, type)
    
    h, w = len(grid), len(grid[0])
    grid_size = h * w
    
    # Determine which implementation to use
    if force_mode == 'cpu':
        use_gpu = False
    elif force_mode == 'gpu':
        use_gpu = True
    else:  # 'auto'
        use_gpu = grid_size >= threshold
    
    # Execute with selected implementation
    if use_gpu:
        try:
            from gpu_dsl_core import gpu_o_g
            return gpu_o_g(grid, type, return_format=return_format)
        except (ImportError, RuntimeError) as e:
            # GPU not available - fallback to CPU
            from dsl import o_g as cpu_o_g
            return cpu_o_g(grid, type)
    else:
        from dsl import o_g as cpu_o_g
        return cpu_o_g(grid, type)


def benchmark_threshold(
    grid_sizes: list = None,
    num_trials: int = 100
) -> dict:
    """
    Benchmark CPU vs GPU across different grid sizes to find optimal threshold.
    
    Args:
        grid_sizes: List of (height, width) tuples to test
                   Default: [(5,5), (8,8), (10,10), (12,12), (15,15), (20,20)]
        num_trials: Number of trials per size (default 100)
    
    Returns:
        Dictionary with results:
        {
            'grid_size': [(5, 5), ...],
            'cpu_times': [0.5, ...],      # milliseconds
            'gpu_times': [1.2, ...],
            'speedups': [0.42, ...],      # GPU speedup (>1 = GPU faster)
            'optimal_threshold': 70       # Recommended threshold
        }
    
    Usage:
        >>> from gpu_hybrid import benchmark_threshold
        >>> results = benchmark_threshold()
        >>> print(f"Optimal threshold: {results['optimal_threshold']} cells")
        >>> 
        >>> # Use custom threshold
        >>> objects = o_g_hybrid(grid, R7, threshold=results['optimal_threshold'])
    """
    import numpy as np
    import time
    from dsl import o_g as cpu_o_g
    from gpu_dsl_core import gpu_o_g
    from constants import R7
    
    if grid_sizes is None:
        grid_sizes = [(5, 5), (8, 8), (10, 10), (12, 12), (15, 15), (20, 20)]
    
    results = {
        'grid_sizes': [],
        'cell_counts': [],
        'cpu_times': [],
        'gpu_times': [],
        'speedups': [],
        'optimal_threshold': DEFAULT_THRESHOLD
    }
    
    print("Benchmarking CPU vs GPU across grid sizes...")
    print(f"Trials per size: {num_trials}")
    print()
    
    for h, w in grid_sizes:
        cell_count = h * w
        
        # Create test grid (random colors 0-9)
        grid = tuple(tuple(np.random.randint(0, 10) for _ in range(w)) for _ in range(h))
        
        # Benchmark CPU
        cpu_times_ms = []
        for _ in range(num_trials):
            start = time.perf_counter()
            _ = cpu_o_g(grid, R7)
            cpu_times_ms.append((time.perf_counter() - start) * 1000)
        cpu_median = np.median(cpu_times_ms)
        
        # Benchmark GPU
        gpu_times_ms = []
        for _ in range(num_trials):
            start = time.perf_counter()
            _ = gpu_o_g(grid, R7)
            gpu_times_ms.append((time.perf_counter() - start) * 1000)
        gpu_median = np.median(gpu_times_ms)
        
        speedup = cpu_median / gpu_median
        
        results['grid_sizes'].append((h, w))
        results['cell_counts'].append(cell_count)
        results['cpu_times'].append(cpu_median)
        results['gpu_times'].append(gpu_median)
        results['speedups'].append(speedup)
        
        faster = "GPU" if speedup > 1.0 else "CPU"
        print(f"{h:2d}×{w:2d} ({cell_count:3d} cells): CPU {cpu_median:5.2f}ms, GPU {gpu_median:5.2f}ms, "
              f"Speedup {speedup:.2f}x → {faster}")
    
    # Find optimal threshold (where GPU becomes faster)
    speedups = np.array(results['speedups'])
    cell_counts = np.array(results['cell_counts'])
    
    # Find crossover point (where speedup > 1.0)
    gpu_faster_idx = np.where(speedups >= 1.0)[0]
    if len(gpu_faster_idx) > 0:
        # Use the first size where GPU is faster
        threshold_idx = gpu_faster_idx[0]
        optimal_threshold = cell_counts[threshold_idx]
        results['optimal_threshold'] = int(optimal_threshold)
    else:
        # GPU never faster - keep default
        print("\n⚠️  GPU not faster on any tested size - keeping default threshold")
        results['optimal_threshold'] = DEFAULT_THRESHOLD
    
    print()
    print(f"Optimal threshold: {results['optimal_threshold']} cells")
    print(f"  → Use GPU for grids ≥ {results['optimal_threshold']} cells")
    print(f"  → Use CPU for grids < {results['optimal_threshold']} cells")
    
    return results


# Convenience function for easy import
def get_optimal_o_g():
    """
    Returns the optimal o_g function for the current environment.
    
    Returns:
        o_g_hybrid function configured with default settings
    
    Usage:
        >>> from gpu_hybrid import get_optimal_o_g
        >>> o_g = get_optimal_o_g()
        >>> objects = o_g(grid, R7)  # Automatically uses CPU or GPU
    """
    return o_g_hybrid


if __name__ == '__main__':
    # Run benchmark when executed directly
    print("="*70)
    print("GPU HYBRID STRATEGY - THRESHOLD BENCHMARK")
    print("="*70)
    print()
    
    results = benchmark_threshold()
    
    print()
    print("="*70)
    print("RESULTS SUMMARY")
    print("="*70)
    
    for i, (size, cells, cpu_time, gpu_time, speedup) in enumerate(zip(
        results['grid_sizes'],
        results['cell_counts'],
        results['cpu_times'],
        results['gpu_times'],
        results['speedups']
    )):
        h, w = size
        faster = "GPU ✓" if speedup >= 1.0 else "CPU ✓"
        print(f"{h:2d}×{w:2d} ({cells:3d} cells): {speedup:5.2f}x speedup → {faster}")
    
    print()
    print(f"RECOMMENDED THRESHOLD: {results['optimal_threshold']} cells")
    print()
    print("To use in your code:")
    print("  from gpu_hybrid import o_g_hybrid")
    print("  objects = o_g_hybrid(grid, R7)  # Automatic CPU/GPU selection")
