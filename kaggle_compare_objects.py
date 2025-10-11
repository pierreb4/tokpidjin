#!/usr/bin/env python3
"""
Deep debug: Compare CPU and GPU objects element by element.
"""
import sys
sys.path.insert(0, '/kaggle/working')

from arc_types import *
from dsl import objects as cpu_o_g, get_arg_rank_f, subgrid, size
from constants import R7, L1
from gpu_dsl_core import gpu_o_g
import cupy as cp

print(f"✓ CuPy available")
print()

# Test grid from solve_23b5c85d
test_grid = (
    (3, 3, 3, 0, 0, 0, 0, 1, 1, 1),
    (3, 3, 3, 0, 5, 5, 0, 1, 1, 1),
    (3, 3, 3, 0, 5, 5, 0, 1, 1, 1),
    (3, 0, 0, 0, 5, 5, 0, 1, 0, 0),
    (0, 0, 2, 2, 5, 5, 0, 0, 0, 0),
    (0, 0, 2, 2, 5, 5, 0, 4, 4, 4),
    (0, 0, 2, 2, 5, 5, 0, 4, 4, 4),
    (6, 6, 6, 0, 5, 5, 0, 4, 4, 4),
    (7, 7, 7, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
)

# Get objects from both
cpu_objects = cpu_o_g(test_grid, R7)
gpu_objects = gpu_o_g(test_grid, R7, return_format='frozenset')

print(f"CPU objects: {len(cpu_objects)} total")
print(f"GPU objects: {len(gpu_objects)} total")
print(f"Are they equal? {cpu_objects == gpu_objects}")
print()

# Find the two size=10 objects and compare them
cpu_list = list(cpu_objects)
gpu_list = list(gpu_objects)

cpu_size10 = [obj for obj in cpu_list if len(obj) == 10]
gpu_size10 = [obj for obj in gpu_list if len(obj) == 10]

print(f"CPU has {len(cpu_size10)} objects of size 10")
print(f"GPU has {len(gpu_size10)} objects of size 10")
print()

# Check if the objects themselves are equal
print("Comparing size=10 objects:")
for i, cpu_obj in enumerate(cpu_size10):
    color_cpu = {c for _, _, c in cpu_obj}
    print(f"\nCPU object {i}: color={color_cpu}")
    print(f"  Cells (sorted): {sorted(cpu_obj)}")
    
    # Find matching GPU object
    for j, gpu_obj in enumerate(gpu_size10):
        if cpu_obj == gpu_obj:
            color_gpu = {c for _, _, c in gpu_obj}
            print(f"  ✓ Matches GPU object {j}: color={gpu_color}")
            print(f"    GPU cells (sorted): {sorted(gpu_obj)}")
            break
    else:
        print(f"  ✗ NO MATCH in GPU objects!")
        # Show closest GPU object
        for j, gpu_obj in enumerate(gpu_size10):
            color_gpu = {c for _, _, c in gpu_obj}
            diff = len(cpu_obj - gpu_obj) + len(gpu_obj - cpu_obj)
            print(f"    GPU object {j}: color={color_gpu}, diff={diff} cells")

print("\n" + "="*70)
print("KEY QUESTION: Are the actual object contents identical?")
print("="*70)
