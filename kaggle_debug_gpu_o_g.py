"""
Simple repro to test gpu_o_g on Kaggle and identify bug.

Upload this to Kaggle and run it to see the actual GPU output.
"""

try:
    import cupy as cp
    print("CuPy GPU support enabled for Kaggle")
    CUPY_AVAILABLE = True
except ImportError:
    print("CuPy not available, using CPU only")
    CUPY_AVAILABLE = False

from dsl import o_g as cpu_o_g
if CUPY_AVAILABLE:
    from gpu_dsl_core import gpu_o_g
from constants import R7

# Test grid from benchmark
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

print("\\n" + "="*70)
print("GPU o_g Correctness Debug")
print("="*70)

print("\\nMode: R7 = 7 (univalued, diagonal, without_bg)")

# CPU version
print("\\n--- CPU o_g ---")
cpu_objects = cpu_o_g(test_grid, R7)
print(f"Number of objects: {len(cpu_objects)}")

# Sort by size and show details
cpu_sorted = sorted(
    [list(obj) for obj in cpu_objects], 
    key=lambda obj: len(obj)
)
for i, obj in enumerate(cpu_sorted):
    colors = {cell[2] for cell in obj}
    print(f"  Object {i}: size={len(obj):2d}, color={colors}")

if CUPY_AVAILABLE:
    # GPU version
    print("\\n--- GPU o_g ---")
    gpu_objects = gpu_o_g(test_grid, R7, return_format='frozenset')
    print(f"Number of objects: {len(gpu_objects)}")
    
    # Sort by size and show details
    gpu_sorted = sorted(
        [list(obj) for obj in gpu_objects], 
        key=lambda obj: len(obj)
    )
    for i, obj in enumerate(gpu_sorted):
        colors = {cell[2] for cell in obj}
        print(f"  Object {i}: size={len(obj):2d}, color={colors}")
    
    # Comparison
    print("\\n--- Comparison ---")
    if cpu_objects == gpu_objects:
        print("✓ Results MATCH")
    else:
        print("✗ Results DON'T MATCH")
        
        # Check object sizes match
        cpu_sizes = sorted([len(obj) for obj in cpu_objects])
        gpu_sizes = sorted([len(obj) for obj in gpu_objects])
        print(f"\\nCPU sizes: {cpu_sizes}")
        print(f"GPU sizes: {gpu_sizes}")
        
        if cpu_sizes == gpu_sizes:
            print("✓ Object sizes MATCH")
            print("✗ But object contents DIFFER")
            
            # Compare each object pair
            print("\\nDetailed comparison:")
            for cpu_obj, gpu_obj in zip(cpu_sorted, gpu_sorted):
                cpu_colors = {cell[2] for cell in cpu_obj}
                gpu_colors = {cell[2] for cell in gpu_obj}
                cpu_positions = {(cell[0], cell[1]) for cell in cpu_obj}
                gpu_positions = {(cell[0], cell[1]) for cell in gpu_obj}
                
                match_pos = cpu_positions == gpu_positions
                match_col = cpu_colors == gpu_colors
                
                status = "✓" if (match_pos and match_col) else "✗"
                print(f"  {status} size={len(cpu_obj):2d}: CPU color={cpu_colors}, GPU color={gpu_colors}, positions_match={match_pos}")
else:
    print("\\nSkipping GPU test (CuPy not available)")

print("\\n" + "="*70)
