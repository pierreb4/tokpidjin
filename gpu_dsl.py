"""
GPU-Accelerated DSL Functions
==============================

This module contains GPU-accelerated versions of DSL functions for improved performance.
Start with simple functions and gradually add more complex ones.

Usage:
    from gpu_dsl import rot90_batch, GPU_AVAILABLE
    
    if GPU_AVAILABLE:
        results = rot90_batch(list_of_grids)
    else:
        results = [rot90(g) for g in list_of_grids]
"""

import numpy as np

try:
    import cupy as cp
    GPU_AVAILABLE = True
    print("GPU-DSL: CuPy available, GPU acceleration enabled")
except ImportError:
    GPU_AVAILABLE = False
    cp = np  # Fallback to numpy
    print("GPU-DSL: CuPy not available, using CPU")

from dsl import rot90 as rot90_cpu


# ============================================================================
# Helper Functions
# ============================================================================

def grid_to_array(grid):
    """Convert tuple-based grid to numpy array"""
    return np.array(grid, dtype=np.int32)


def array_to_grid(arr):
    """Convert numpy array back to tuple-based grid"""
    return tuple(tuple(int(x) for x in row) for row in arr)


def grids_to_batch(grids):
    """
    Convert list of grids to batch tensor
    Returns: (batch_size, max_height, max_width) array with padding
    """
    if not grids:
        return np.array([])
    
    # Convert to arrays
    arrays = [grid_to_array(g) for g in grids]
    
    # Find max dimensions
    max_h = max(arr.shape[0] for arr in arrays)
    max_w = max(arr.shape[1] for arr in arrays)
    
    # Create padded batch
    batch = np.zeros((len(arrays), max_h, max_w), dtype=np.int32)
    original_shapes = []
    
    for i, arr in enumerate(arrays):
        h, w = arr.shape
        batch[i, :h, :w] = arr
        original_shapes.append((h, w))
    
    return batch, original_shapes


def batch_to_grids(batch, original_shapes):
    """Convert batch tensor back to list of grids with original shapes"""
    grids = []
    for i, (h, w) in enumerate(original_shapes):
        arr = batch[i, :h, :w]
        # Move to CPU if on GPU
        if GPU_AVAILABLE and isinstance(arr, cp.ndarray):
            arr = cp.asnumpy(arr)
        grids.append(array_to_grid(arr))
    return grids


# ============================================================================
# GPU-Accelerated Functions
# ============================================================================

def rot90_vectorized(batch):
    """
    Vectorized 90-degree rotation for batch of grids
    
    Args:
        batch: (batch_size, h, w) array (CuPy or NumPy)
    
    Returns:
        Rotated batch with shape (batch_size, w, h)
    """
    if GPU_AVAILABLE and isinstance(batch, cp.ndarray):
        # GPU version: rotate 90 degrees clockwise
        # axes=(1,2) means rotate the height x width dimensions
        return cp.rot90(batch, k=-1, axes=(1, 2))
    else:
        # CPU version
        return np.rot90(batch, k=-1, axes=(1, 2))


def rot90_batch(grids, min_batch_size=10):
    """
    Process multiple grids with GPU acceleration
    
    Args:
        grids: List of grids (tuple of tuples)
        min_batch_size: Minimum number of grids to use GPU (default: 10)
    
    Returns:
        List of rotated grids
    
    Example:
        >>> grids = [((1, 2), (3, 4)), ((5, 6), (7, 8))]
        >>> rotated = rot90_batch(grids)
        >>> print(rotated[0])
        ((3, 1), (4, 2))
    """
    if not grids:
        return []
    
    # For small batches or no GPU, use CPU
    if not GPU_AVAILABLE or len(grids) < min_batch_size:
        return [rot90_cpu(g) for g in grids]
    
    try:
        # Convert to batch tensor
        batch, original_shapes = grids_to_batch(grids)
        
        # Move to GPU
        batch_gpu = cp.asarray(batch)
        
        # Apply rotation
        rotated_gpu = rot90_vectorized(batch_gpu)
        
        # Move back to CPU
        rotated_cpu = cp.asnumpy(rotated_gpu)
        
        # Adjust shapes after rotation (h and w are swapped)
        rotated_shapes = [(w, h) for h, w in original_shapes]
        
        # Convert back to grids
        result = batch_to_grids(rotated_cpu, rotated_shapes)
        
        return result
        
    except Exception as e:
        # Fallback to CPU on any error
        print(f"GPU processing failed: {e}, falling back to CPU")
        return [rot90_cpu(g) for g in grids]


# ============================================================================
# Testing and Benchmarking
# ============================================================================

def test_rot90_correctness():
    """Test that GPU and CPU versions produce identical results"""
    print("\n" + "="*60)
    print("Testing rot90 correctness...")
    print("="*60)
    
    test_grids = [
        ((1, 2, 3), (4, 5, 6), (7, 8, 9)),
        ((1, 2), (3, 4)),
        ((5,),),
        ((1, 2, 3, 4, 5), (6, 7, 8, 9, 10)),
    ]
    
    for i, grid in enumerate(test_grids):
        print(f"\nTest {i+1}: Grid shape {len(grid)}x{len(grid[0])}")
        print(f"Input:  {grid}")
        
        # CPU version
        cpu_result = rot90_cpu(grid)
        print(f"CPU:    {cpu_result}")
        
        # GPU batch version
        gpu_result = rot90_batch([grid], min_batch_size=1)[0]
        print(f"GPU:    {gpu_result}")
        
        # Compare
        if cpu_result == gpu_result:
            print("✓ PASS")
        else:
            print("✗ FAIL - Results don't match!")
            return False
    
    print("\n" + "="*60)
    print("All tests passed! ✓")
    print("="*60)
    return True


def benchmark_rot90(sizes=[10, 50, 100, 200], grid_size=(25, 25)):
    """Benchmark CPU vs GPU performance"""
    import time
    
    print("\n" + "="*60)
    print("Benchmarking rot90 performance...")
    print("="*60)
    print(f"Grid size: {grid_size[0]}x{grid_size[1]}")
    print(f"Batch sizes: {sizes}")
    print()
    
    results = []
    
    for batch_size in sizes:
        # Generate test data
        grids = [tuple(tuple(np.random.randint(0, 10) for _ in range(grid_size[1])) 
                       for _ in range(grid_size[0])) 
                for _ in range(batch_size)]
        
        # CPU benchmark
        start = time.time()
        cpu_results = [rot90_cpu(g) for g in grids]
        cpu_time = time.time() - start
        
        # GPU benchmark
        if GPU_AVAILABLE and batch_size >= 10:
            start = time.time()
            gpu_results = rot90_batch(grids, min_batch_size=10)
            gpu_time = time.time() - start
            
            speedup = cpu_time / gpu_time if gpu_time > 0 else 0
            results.append((batch_size, cpu_time, gpu_time, speedup))
            
            print(f"Batch size {batch_size:3d}: "
                  f"CPU {cpu_time*1000:6.2f}ms | "
                  f"GPU {gpu_time*1000:6.2f}ms | "
                  f"Speedup: {speedup:4.1f}x")
        else:
            results.append((batch_size, cpu_time, None, None))
            print(f"Batch size {batch_size:3d}: CPU {cpu_time*1000:6.2f}ms | "
                  f"GPU: {'N/A (batch too small)' if batch_size < 10 else 'N/A (no GPU)'}")
    
    print("\n" + "="*60)
    if GPU_AVAILABLE:
        best_speedup = max((r[3] for r in results if r[3] is not None), default=0)
        print(f"Best speedup: {best_speedup:.1f}x")
    print("="*60)
    
    return results


# ============================================================================
# Main - Run tests when executed directly
# ============================================================================

if __name__ == "__main__":
    print("\nGPU-DSL Module Test Suite")
    print("="*60)
    print(f"GPU Available: {GPU_AVAILABLE}")
    
    if GPU_AVAILABLE:
        print(f"CuPy version: {cp.__version__}")
        try:
            device = cp.cuda.Device()
            print(f"GPU Device: {device.compute_capability}")
            mem = device.mem_info
            print(f"GPU Memory: {mem[1]/1024**3:.1f}GB total, "
                  f"{(mem[1]-mem[0])/1024**3:.1f}GB used")
        except:
            print("Could not get GPU device info")
    
    # Run tests
    if test_rot90_correctness():
        benchmark_rot90()
