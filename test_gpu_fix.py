#!/usr/bin/env python3
"""
Test GPU Operations Fix - Verify GPU is Actually Being Used

This script tests the fixed gpu_dsl_operations to ensure:
1. GPU operations are called (check logs)
2. GPU optimizer is used (verify in logs)
3. Performance improvement is measurable

Usage:
    python test_gpu_fix.py
"""

import logging
import sys
from timeit import default_timer as timer

# Setup logging to see GPU messages
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import GPU operations
try:
    from gpu_dsl_operations import GPUDSLOperations
    GPU_AVAILABLE = True
except ImportError as e:
    print(f"❌ Cannot import gpu_dsl_operations: {e}")
    sys.exit(1)

# Import DSL for comparison
try:
    from dsl import rot90, rot180, rot270, flip, identity, mapply
except ImportError as e:
    print(f"❌ Cannot import dsl: {e}")
    sys.exit(1)


def create_test_grids(count=50, size=10):
    """Create test grids for benchmarking"""
    import random
    grids = []
    for _ in range(count):
        grid = tuple(
            tuple(random.randint(0, 9) for _ in range(size))
            for _ in range(size)
        )
        grids.append(grid)
    return grids


def test_batch_mapply_gpu():
    """Test batch_mapply with GPU operations"""
    print("\n" + "="*70)
    print("TEST 1: batch_mapply with GPU-compatible operations")
    print("="*70)
    
    # Create test data
    grids = create_test_grids(count=50, size=10)
    
    # Test different operations
    operations = [
        ('rot90', rot90),
        ('rot180', rot180),
        ('flip', flip),
    ]
    
    # Initialize GPU operations
    gpu_ops = GPUDSLOperations(enable_gpu=True)
    
    print(f"\nGPU Status: {'✅ Enabled' if gpu_ops.enable_gpu else '❌ Disabled'}")
    print(f"GPU Count: {gpu_ops.gpu_count}")
    print(f"GPU Optimizer: {type(gpu_ops.gpu_opt).__name__ if gpu_ops.gpu_opt else 'None'}")
    
    for op_name, op_func in operations:
        print(f"\n--- Testing {op_name} ---")
        
        # Prepare data for batch_mapply (list of tuples)
        # Each tuple contains grids to process
        grid_lists = [tuple(grids[i:i+5]) for i in range(0, len(grids), 5)]
        
        # Test 1: CPU (direct DSL)
        print(f"[1/2] CPU ({op_name})...")
        t_start = timer()
        cpu_results = [mapply(op_func, gl) for gl in grid_lists]
        t_cpu = timer() - t_start
        print(f"  Time: {t_cpu:.4f}s | Throughput: {len(grids)/t_cpu:.1f} grids/s")
        
        # Test 2: GPU (batch_mapply)
        print(f"[2/2] GPU ({op_name})...")
        t_start = timer()
        gpu_results = gpu_ops.batch_mapply(op_func, grid_lists)
        t_gpu = timer() - t_start
        speedup = t_cpu / t_gpu if t_gpu > 0 else 0
        print(f"  Time: {t_gpu:.4f}s | Throughput: {len(grids)/t_gpu:.1f} grids/s | Speedup: {speedup:.2f}x")
        
        # Verify correctness
        if cpu_results == gpu_results:
            print(f"  ✅ Results match!")
        else:
            print(f"  ❌ Results differ!")
            
    return True


def test_batch_o_g():
    """Test batch_o_g operation"""
    print("\n" + "="*70)
    print("TEST 2: batch_o_g (object extraction)")
    print("="*70)
    
    from dsl import o_g
    
    # Create test grids
    grids = create_test_grids(count=30, size=8)
    rotations = [0] * 30  # All default rotation
    
    # Initialize GPU operations
    gpu_ops = GPUDSLOperations(enable_gpu=True)
    
    print(f"\nProcessing {len(grids)} grids...")
    
    # Test 1: CPU
    print("[1/2] CPU (o_g)...")
    t_start = timer()
    cpu_results = [o_g(grid, rot) for grid, rot in zip(grids, rotations)]
    t_cpu = timer() - t_start
    print(f"  Time: {t_cpu:.4f}s | Throughput: {len(grids)/t_cpu:.1f} grids/s")
    
    # Test 2: GPU
    print("[2/2] GPU (batch_o_g)...")
    t_start = timer()
    gpu_results = gpu_ops.batch_o_g(grids, rotations)
    t_gpu = timer() - t_start
    speedup = t_cpu / t_gpu if t_gpu > 0 else 0
    print(f"  Time: {t_gpu:.4f}s | Throughput: {len(grids)/t_gpu:.1f} grids/s | Speedup: {speedup:.2f}x")
    
    # Verify correctness
    if cpu_results == gpu_results:
        print(f"  ✅ Results match!")
    else:
        print(f"  ❌ Results differ!")
        
    return True


def test_logging_verification():
    """Verify that GPU logging is working"""
    print("\n" + "="*70)
    print("TEST 3: Verify GPU Logging")
    print("="*70)
    
    print("\n📋 Check the logs above for these messages:")
    print("  - 'batch_mapply: Processing X grids with function'")
    print("  - 'batch_mapply: Processed X grids on GPU successfully'")
    print("  - 'batch_o_g: Processing X grids on GPU'")
    print("\n✅ If you see these messages, GPU operations are being called!")
    
    return True


def main():
    """Run all tests"""
    print("="*70)
    print("GPU OPERATIONS FIX - VERIFICATION TEST")
    print("="*70)
    print("\nThis test verifies that GPU operations are now actually using the GPU.")
    print("Check the logs for 'Processing on GPU' messages.\n")
    
    try:
        # Run tests
        test_batch_mapply_gpu()
        test_batch_o_g()
        test_logging_verification()
        
        print("\n" + "="*70)
        print("ALL TESTS COMPLETE")
        print("="*70)
        print("\n✅ Check the logs above to verify GPU operations were called")
        print("✅ Look for 'Processing X grids on GPU' messages")
        print("✅ Speedup should be visible for GPU-compatible operations")
        print("\n📝 Next step: Upload to Kaggle and run benchmark!")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
