"""
Kaggle GPU Testing Script for gpu_o_g

This script should be run on Kaggle with GPU enabled.
It will test the GPU o_g implementation and measure performance.

Setup:
1. Create new Kaggle notebook
2. Enable GPU (Settings -> Accelerator -> GPU L4)
3. Upload: gpu_dsl_core.py, test_gpu_dsl_core.py, dsl.py, arc_types.py, utils.py
4. Run this script

Expected Results:
- Correctness: 100% (all 128 tests pass)
- Performance: 2.3-7.8x speedup vs CPU
"""

import sys
import subprocess

# Install dependencies if needed
print("="*70)
print("KAGGLE GPU SETUP")
print("="*70)

# Check if CuPy is available
try:
    import cupy as cp
    print("✓ CuPy available")
    print(f"  CuPy version: {cp.__version__}")
    
    # Check GPU
    try:
        gpu_name = cp.cuda.runtime.getDeviceProperties(0)['name'].decode()
        print(f"  GPU: {gpu_name}")
    except:
        print("  GPU: Detection failed")
except ImportError:
    print("✗ CuPy not available")
    print("  Installing CuPy...")
    subprocess.run([sys.executable, "-m", "pip", "install", "cupy-cuda12x"], check=True)
    print("✓ CuPy installed")

# Check NumPy
try:
    import numpy as np
    print(f"✓ NumPy available (version {np.__version__})")
except ImportError:
    print("✗ NumPy not available - installing...")
    subprocess.run([sys.executable, "-m", "pip", "install", "numpy"], check=True)

print()

# Run tests
print("="*70)
print("RUNNING TESTS")
print("="*70)
print()

# Import test module
from test_gpu_dsl_core import TestGPUO_G

# Run tests
tester = TestGPUO_G()
tester.run_all(verbose=False)

# Additional profiler integration test
print("\n" + "="*70)
print("PROFILED SOLVER INTEGRATION TEST")
print("="*70)

try:
    from gpu_dsl_core import gpu_o_g
    from dsl import o_g as cpu_o_g
    import time
    
    # Test grid from profiled solvers (representative)
    test_grid = (
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
    
    print(f"\nTest grid: 10x10")
    print(f"Testing mode 3 (non-bg, 8-connectivity) - common in profiled solvers")
    
    # Warmup
    for _ in range(5):
        _ = gpu_o_g(test_grid, 3, return_format='frozenset')
    
    # Benchmark
    n_runs = 100
    
    cpu_times = []
    for _ in range(n_runs):
        start = time.perf_counter()
        cpu_result = cpu_o_g(test_grid, 3)
        cpu_times.append((time.perf_counter() - start) * 1000)
    
    gpu_times_fs = []
    for _ in range(n_runs):
        start = time.perf_counter()
        gpu_result_fs = gpu_o_g(test_grid, 3, return_format='frozenset')
        gpu_times_fs.append((time.perf_counter() - start) * 1000)
    
    gpu_times_t = []
    for _ in range(n_runs):
        start = time.perf_counter()
        gpu_result_t = gpu_o_g(test_grid, 3, return_format='tuple')
        gpu_times_t.append((time.perf_counter() - start) * 1000)
    
    # Calculate stats
    import statistics
    
    cpu_median = statistics.median(cpu_times)
    gpu_fs_median = statistics.median(gpu_times_fs)
    gpu_t_median = statistics.median(gpu_times_t)
    
    speedup_fs = cpu_median / gpu_fs_median
    speedup_t = cpu_median / gpu_t_median
    
    print(f"\nResults ({n_runs} runs, median):")
    print(f"  CPU:              {cpu_median:.3f} ms")
    print(f"  GPU (frozenset):  {gpu_fs_median:.3f} ms ({speedup_fs:.2f}x speedup)")
    print(f"  GPU (tuple):      {gpu_t_median:.3f} ms ({speedup_t:.2f}x speedup)")
    
    print(f"\nExpected performance:")
    print(f"  CPU: 4-7ms")
    print(f"  GPU (frozenset): 1.45-2.15ms (2.3-4.8x speedup)")
    print(f"  GPU (tuple): 0.95-1.65ms (2.5-7.8x speedup)")
    
    if speedup_fs >= 2.3:
        print(f"\n✓ Frozenset speedup MEETS expectations ({speedup_fs:.2f}x >= 2.3x)")
    else:
        print(f"\n⚠ Frozenset speedup below expectations ({speedup_fs:.2f}x < 2.3x)")
    
    if speedup_t >= 2.5:
        print(f"✓ Tuple speedup MEETS expectations ({speedup_t:.2f}x >= 2.5x)")
    else:
        print(f"⚠ Tuple speedup below expectations ({speedup_t:.2f}x < 2.5x)")
    
    # Correctness check
    if cpu_result == gpu_result_fs:
        print(f"\n✓ Results match (correctness verified)")
    else:
        print(f"\n✗ Results don't match - correctness issue!")

except Exception as e:
    print(f"Error in integration test: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*70)
print("FINAL SUMMARY")
print("="*70)

if tester.failed == 0:
    print("✓ ALL CORRECTNESS TESTS PASSED")
    print("✓ Ready for Week 2: Solver Integration")
else:
    print(f"✗ {tester.failed} tests failed")
    print("⚠ Fix issues before proceeding to Week 2")

print("="*70)
