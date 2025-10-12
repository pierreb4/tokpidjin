#!/usr/bin/env python3
"""
Test GPU batch processing for Kaggle environment
Tests for T4x2, P100, and L4x4 GPUs
"""

import time
import numpy as np
from timeit import default_timer as timer

# Test imports
try:
    from dsl import GPU_AVAILABLE, batch_grid_operations, gpu_grid_transform
    from run_batt import GPUBatchProcessor, configure_gpu_memory, get_optimal_batch_size
    print("✓ All imports successful")
except ImportError as e:
    print(f"✗ Import error: {e}")
    exit(1)

def generate_test_grids(num_grids=100, size=(20, 20)):
    """Generate random test grids"""
    return [np.random.randint(0, 10, size=size) for _ in range(num_grids)]

def simple_operation(grid):
    """Simple grid operation for testing"""
    if hasattr(grid, 'sum'):  # numpy/cupy array
        return grid + 1
    return grid

def test_gpu_detection():
    """Test 1: GPU Detection"""
    print("\n=== Test 1: GPU Detection ===")
    print(f"GPU Available: {GPU_AVAILABLE}")
    
    if GPU_AVAILABLE:
        import cupy as cp
        try:
            gpu_count = cp.cuda.runtime.getDeviceCount()
            print(f"GPU Count: {gpu_count}")
            for i in range(gpu_count):
                device = cp.cuda.Device(i)
                mem_info = device.mem_info
                print(f"  GPU {i}:")
                print(f"    Compute Capability: {device.compute_capability}")
                print(f"    Total Memory: {mem_info[1]/(1024**3):.2f}GB")
                print(f"    Free Memory: {mem_info[0]/(1024**3):.2f}GB")
            return True
        except Exception as e:
            print(f"  Error: {e}")
            return False
    else:
        print("  No GPU available, tests will run on CPU")
        return False

def test_memory_configuration():
    """Test 2: Memory Configuration"""
    print("\n=== Test 2: Memory Configuration ===")
    
    success = configure_gpu_memory()
    print(f"Configuration successful: {success}")
    
    if GPU_AVAILABLE:
        import cupy as cp
        try:
            mem_info = cp.cuda.Device().mem_info
            print(f"After configuration:")
            print(f"  Free: {mem_info[0]/(1024**3):.2f}GB")
            print(f"  Total: {mem_info[1]/(1024**3):.2f}GB")
        except Exception as e:
            print(f"  Error: {e}")
    
    return success

def test_batch_size_calculation():
    """Test 3: Optimal Batch Size"""
    print("\n=== Test 3: Optimal Batch Size Calculation ===")
    
    test_cases = [
        (None, None, "Default"),
        (100, 50, "Small grids (10x10)"),
        (400, 50, "Medium grids (20x20)"),
        (900, 50, "Large grids (30x30)"),
    ]
    
    for grid_size, num_samples, description in test_cases:
        batch_size = get_optimal_batch_size(grid_size, num_samples)
        print(f"  {description}: batch_size={batch_size}")
    
    return True

def test_batch_operations():
    """Test 4: Batch Grid Operations"""
    print("\n=== Test 4: Batch Grid Operations ===")
    
    sizes = [10, 50, 100]
    for num_grids in sizes:
        grids = generate_test_grids(num_grids, size=(15, 15))
        
        # CPU timing
        start = timer()
        cpu_results = [simple_operation(g) for g in grids]
        cpu_time = timer() - start
        
        # Batch timing (GPU if available, otherwise CPU)
        start = timer()
        batch_results = batch_grid_operations(grids, simple_operation)
        batch_time = timer() - start
        
        speedup = cpu_time / batch_time if batch_time > 0 else 1.0
        print(f"  {num_grids} grids (15x15):")
        print(f"    Sequential: {cpu_time*1000:.2f}ms")
        print(f"    Batch: {batch_time*1000:.2f}ms")
        print(f"    Speedup: {speedup:.2f}x")
    
    return True

def test_gpu_batch_processor():
    """Test 5: GPUBatchProcessor"""
    print("\n=== Test 5: GPUBatchProcessor ===")
    
    processor = GPUBatchProcessor(batch_size=32, use_gpu=True)
    
    # Create dummy tasks
    tasks = [{'id': i, 'data': np.random.rand(10, 10)} for i in range(64)]
    
    start = timer()
    results = processor.process_tasks_batch(tasks)
    elapsed = timer() - start
    
    print(f"  Processed {len(tasks)} tasks in {elapsed*1000:.2f}ms")
    print(f"  Results: {len(results)}")
    print(f"  GPU used: {processor.use_gpu}")
    
    return len(results) == len(tasks)

def test_memory_cleanup():
    """Test 6: Memory Cleanup"""
    print("\n=== Test 6: Memory Cleanup ===")
    
    if GPU_AVAILABLE:
        import cupy as cp
        
        # Create some GPU arrays
        arrays = [cp.random.rand(1000, 1000) for _ in range(10)]
        
        mem_before = cp.cuda.Device().mem_info[0]
        print(f"  Memory before cleanup: {mem_before/(1024**3):.2f}GB free")
        
        # Delete arrays and cleanup
        del arrays
        from run_batt import gpu_memory_cleanup
        gpu_memory_cleanup()
        
        mem_after = cp.cuda.Device().mem_info[0]
        print(f"  Memory after cleanup: {mem_after/(1024**3):.2f}GB free")
        print(f"  Freed: {(mem_after-mem_before)/(1024**3):.2f}GB")
        
        return mem_after >= mem_before
    else:
        print("  Skipping (no GPU)")
        return True

def main():
    """Run all tests"""
    print("=" * 60)
    print("GPU Batch Processing Tests for Kaggle")
    print("=" * 60)
    
    tests = [
        ("GPU Detection", test_gpu_detection),
        ("Memory Configuration", test_memory_configuration),
        ("Batch Size Calculation", test_batch_size_calculation),
        ("Batch Operations", test_batch_operations),
        ("GPUBatchProcessor", test_gpu_batch_processor),
        ("Memory Cleanup", test_memory_cleanup),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n✗ Test failed with exception: {e}")
            import traceback
            traceback.print_exc()
            results.append((name, False))
    
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    passed = sum(1 for _, r in results if r)
    total = len(results)
    
    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {name}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
