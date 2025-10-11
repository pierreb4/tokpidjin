"""
Debug script to identify the gpu_o_g correctness issue.

Issue: 2/3 solvers return wrong colors
- solve_23b5c85d: CPU=(7,7), GPU=(4,4) - wrong color!
- solve_1f85a75f: CPU=color 3, GPU=color 1 - wrong color!
- Shapes are correct, only colors differ

Theory: Object ordering or color extraction bug in gpu_o_g
"""

from dsl import o_g as cpu_o_g
from gpu_dsl_core import gpu_o_g
from constants import R7

# Test grid from benchmark (10x10)
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

print("=" * 70)
print("DEBUG: gpu_o_g correctness issue")
print("=" * 70)

# Extract objects with R7 (univalued=T, diagonal=T, without_bg=T)
print(f"\nMode: R7 = {R7} (univalued, diagonal, without_bg)")
print("Expected: Extract same-color connected components, excluding background (0)")

print("\n--- CPU o_g ---")
cpu_objects = cpu_o_g(test_grid, R7)
print(f"Number of objects: {len(cpu_objects)}")

# Sort and display each object
cpu_objects_list = sorted(list(cpu_objects), key=lambda obj: (len(obj), sorted(list(obj))))
for i, obj in enumerate(cpu_objects_list):
    obj_list = sorted(list(obj))
    colors = set(cell[2] for cell in obj_list)
    positions = [(cell[0], cell[1]) for cell in obj_list]
    print(f"  Object {i}: size={len(obj)}, colors={colors}, positions={positions[:5]}{'...' if len(positions) > 5 else ''}")

print("\n--- GPU o_g ---")
gpu_objects = gpu_o_g(test_grid, R7, return_format='frozenset')
print(f"Number of objects: {len(gpu_objects)}")

# Sort and display each object
gpu_objects_list = sorted(list(gpu_objects), key=lambda obj: (len(obj), sorted(list(obj))))
for i, obj in enumerate(gpu_objects_list):
    obj_list = sorted(list(obj))
    colors = set(cell[2] for cell in obj_list)
    positions = [(cell[0], cell[1]) for cell in obj_list]
    print(f"  Object {i}: size={len(obj)}, colors={colors}, positions={positions[:5]}{'...' if len(positions) > 5 else ''}")

print("\n--- Comparison ---")
if cpu_objects == gpu_objects:
    print("✓ Results MATCH")
else:
    print("✗ Results DON'T MATCH")
    
    # Find differences
    cpu_only = cpu_objects - gpu_objects
    gpu_only = gpu_objects - cpu_objects
    
    if cpu_only:
        print(f"\nObjects in CPU but not GPU: {len(cpu_only)}")
        for obj in list(cpu_only)[:3]:
            obj_list = sorted(list(obj))[:5]
            colors = set(cell[2] for cell in obj_list)
            print(f"  {obj_list}... (colors={colors})")
    
    if gpu_only:
        print(f"\nObjects in GPU but not CPU: {len(gpu_only)}")
        for obj in list(gpu_only)[:3]:
            obj_list = sorted(list(obj))[:5]
            colors = set(cell[2] for cell in obj_list)
            print(f"  {obj_list}... (colors={colors})")
    
    # Check if shapes match but colors differ
    print("\n--- Detailed Cell-by-Cell Check ---")
    print("Checking if same positions but different colors...")
    
    # Convert to position sets (ignoring colors)
    cpu_positions = {frozenset((cell[0], cell[1]) for cell in obj) for obj in cpu_objects}
    gpu_positions = {frozenset((cell[0], cell[1]) for cell in obj) for obj in gpu_objects}
    
    if cpu_positions == gpu_positions:
        print("✓ Object shapes/positions MATCH")
        print("✗ But colors DIFFER - this is the bug!")
        print("\nShowing first mismatched object:")
        for cpu_obj, gpu_obj in zip(cpu_objects_list, gpu_objects_list):
            cpu_list = sorted(list(cpu_obj))
            gpu_list = sorted(list(gpu_obj))
            if cpu_list != gpu_list:
                print(f"  CPU: {cpu_list[:3]}...")
                print(f"  GPU: {gpu_list[:3]}...")
                cpu_colors = set(cell[2] for cell in cpu_list)
                gpu_colors = set(cell[2] for cell in gpu_list)
                print(f"  CPU colors: {cpu_colors}")
                print(f"  GPU colors: {gpu_colors}")
                break
    else:
        print("✗ Even object shapes DIFFER")

print("\n" + "=" * 70)
