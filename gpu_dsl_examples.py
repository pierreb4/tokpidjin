"""
Simple Usage Examples for GPU-Accelerated DSL
"""

from gpu_dsl import rot90_batch, GPU_AVAILABLE
from dsl import rot90 as rot90_cpu
import numpy as np

# ============================================================================
# Example 1: Basic Usage
# ============================================================================

print("Example 1: Basic Usage")
print("="*60)

# Create some test grids
grids = [
    ((1, 2, 3), (4, 5, 6), (7, 8, 9)),
    ((10, 20), (30, 40)),
    ((1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)),
]

print(f"Input: {len(grids)} grids")
print(f"First grid: {grids[0]}")

# Rotate all grids
rotated = rot90_batch(grids)

print(f"Output: {len(rotated)} grids")
print(f"First rotated: {rotated[0]}")
print()

# ============================================================================
# Example 2: Automatic CPU Fallback for Small Batches
# ============================================================================

print("Example 2: Automatic Fallback")
print("="*60)

small_batch = [((1, 2), (3, 4))] * 5  # Only 5 grids
large_batch = [((1, 2), (3, 4))] * 50  # 50 grids

print(f"Small batch ({len(small_batch)} grids): Uses CPU automatically")
result_small = rot90_batch(small_batch)

print(f"Large batch ({len(large_batch)} grids): Uses GPU if available")
result_large = rot90_batch(large_batch)
print()

# ============================================================================
# Example 3: Performance Comparison
# ============================================================================

print("Example 3: Performance Comparison")
print("="*60)

if GPU_AVAILABLE:
    from timeit import default_timer as timer
    
    # Generate larger test set
    test_grids = [
        tuple(tuple(np.random.randint(0, 10) for _ in range(25)) for _ in range(25))
        for _ in range(100)
    ]
    
    # CPU version
    start = timer()
    cpu_results = [rot90_cpu(g) for g in test_grids]
    cpu_time = timer() - start
    
    # GPU version
    start = timer()
    gpu_results = rot90_batch(test_grids)
    gpu_time = timer() - start
    
    print(f"100 grids (25x25 each):")
    print(f"  CPU: {cpu_time*1000:.2f}ms")
    print(f"  GPU: {gpu_time*1000:.2f}ms")
    print(f"  Speedup: {cpu_time/gpu_time:.1f}x")
    
    # Verify correctness
    matches = all(cpu == gpu for cpu, gpu in zip(cpu_results, gpu_results))
    print(f"  Results match: {'✓' if matches else '✗'}")
else:
    print("GPU not available - skipping performance test")

print()

# ============================================================================
# Example 4: Integration Pattern
# ============================================================================

print("Example 4: Integration Pattern")
print("="*60)

def process_task_batch(tasks):
    """
    Example of how to integrate GPU batch processing into your workflow
    """
    # Collect all grids that need the same operation
    grids_to_rotate = [task['input'] for task in tasks]
    
    # Process in one batch (automatically uses GPU if beneficial)
    rotated_grids = rot90_batch(grids_to_rotate)
    
    # Update tasks with results
    for task, rotated in zip(tasks, rotated_grids):
        task['rotated_input'] = rotated
    
    return tasks

# Demo
sample_tasks = [
    {'input': ((1, 2), (3, 4)), 'id': 'task1'},
    {'input': ((5, 6), (7, 8)), 'id': 'task2'},
    {'input': ((9, 10), (11, 12)), 'id': 'task3'},
]

processed = process_task_batch(sample_tasks)
print(f"Processed {len(processed)} tasks in batch")
print(f"Task 1 rotated input: {processed[0]['rotated_input']}")
print()

# ============================================================================
# Example 5: Best Practices
# ============================================================================

print("Example 5: Best Practices")
print("="*60)
print("""
✓ DO: Accumulate operations into batches of 20+ grids
✓ DO: Use GPU for repeated operations on many grids
✓ DO: Let the library handle CPU/GPU selection automatically
✓ DO: Test correctness first, then measure performance

✗ DON'T: Use GPU for single grids (CPU is faster)
✗ DON'T: Use GPU for very simple operations on small batches
✗ DON'T: Manually manage GPU memory (library handles it)
✗ DON'T: Assume GPU is always faster without measuring

Optimal Batch Sizes:
  20-50:   Good speedup (2-3x)
  50-100:  Better speedup (3-5x)
  100-200: Best speedup (5-10x)
  200+:    Diminishing returns (memory becomes factor)
""")
