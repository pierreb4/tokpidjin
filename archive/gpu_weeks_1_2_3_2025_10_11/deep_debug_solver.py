"""
Deep debug of the object ordering issue.
This will show EXACTLY how get_arg_rank_f selects objects.
"""

from dsl import o_g as cpu_o_g, get_arg_rank_f, size, subgrid
from gpu_dsl_core import gpu_o_g
from constants import R7, L1

# Test grid
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

print("="*70)
print("DETAILED DEBUG: solve_23b5c85d")
print("="*70)

print("\nSolver logic:")
print("  x1 = o_g(I, R7)              # Extract objects")
print("  x2 = get_arg_rank_f(x1, size, L1)  # Get largest (L1=-1)")
print("  O = subgrid(x2, I)           # Extract subgrid")

# CPU version
print("\n--- CPU Version ---")
cpu_objects = cpu_o_g(test_grid, R7)
print(f"Objects count: {len(cpu_objects)}")

# Show each object
cpu_list = list(cpu_objects)
for i, obj in enumerate(cpu_list):
    obj_list = list(obj)
    colors = {cell[2] for cell in obj_list}
    min_pos = (min(cell[0] for cell in obj_list), min(cell[1] for cell in obj_list))
    print(f"  Object {i}: size={len(obj):2d}, color={colors}, min_pos={min_pos}")

# get_arg_rank_f with size, L1
print(f"\nCalling get_arg_rank_f(objects, size, L1={L1}):")
print("  This sorts by size (descending) and takes index -1 (last)")

ranked = sorted(cpu_objects, key=size, reverse=True)
print(f"\nAfter sorting by size (descending):")
for i, obj in enumerate(ranked):
    obj_list = list(obj)
    colors = {cell[2] for cell in obj_list}
    min_pos = (min(cell[0] for cell in obj_list), min(cell[1] for cell in obj_list))
    marker = " ← SELECTED (index -1)" if i == len(ranked) - 1 else ""
    print(f"  [{i:2d}] size={len(obj):2d}, color={colors}, min_pos={min_pos}{marker}")

selected_cpu = get_arg_rank_f(cpu_objects, size, L1)
print(f"\nSelected object: size={len(selected_cpu)}, color={set(cell[2] for cell in selected_cpu)}")

cpu_result = subgrid(selected_cpu, test_grid)
print(f"Final CPU result: {cpu_result}")

# GPU version
print("\n--- GPU Version ---")
gpu_objects = gpu_o_g(test_grid, R7, return_format='frozenset')
print(f"Objects count: {len(gpu_objects)}")

# Show each object
gpu_list = list(gpu_objects)
for i, obj in enumerate(gpu_list):
    obj_list = list(obj)
    colors = {cell[2] for cell in obj_list}
    min_pos = (min(cell[0] for cell in obj_list), min(cell[1] for cell in obj_list))
    print(f"  Object {i}: size={len(obj):2d}, color={colors}, min_pos={min_pos}")

print(f"\nCalling get_arg_rank_f(objects, size, L1={L1}):")

ranked_gpu = sorted(gpu_objects, key=size, reverse=True)
print(f"\nAfter sorting by size (descending):")
for i, obj in enumerate(ranked_gpu):
    obj_list = list(obj)
    colors = {cell[2] for cell in obj_list}
    min_pos = (min(cell[0] for cell in obj_list), min(cell[1] for cell in obj_list))
    marker = " ← SELECTED (index -1)" if i == len(ranked_gpu) - 1 else ""
    print(f"  [{i:2d}] size={len(obj):2d}, color={colors}, min_pos={min_pos}{marker}")

selected_gpu = get_arg_rank_f(gpu_objects, size, L1)
print(f"\nSelected object: size={len(selected_gpu)}, color={set(cell[2] for cell in selected_gpu)}")

gpu_result = subgrid(selected_gpu, test_grid)
print(f"Final GPU result: {gpu_result}")

# Comparison
print("\n" + "="*70)
print("COMPARISON")
print("="*70)
print(f"CPU result: {cpu_result}")
print(f"GPU result: {gpu_result}")
print(f"Match: {cpu_result == gpu_result}")

if cpu_result != gpu_result:
    print("\n⚠ MISMATCH DETECTED!")
    print(f"CPU selected color: {set(cell[2] for cell in selected_cpu)}")
    print(f"GPU selected color: {set(cell[2] for cell in selected_gpu)}")
