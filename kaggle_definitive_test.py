#!/usr/bin/env python3
"""
DEFINITIVE TEST: Verify if CPU and GPU objects are TRULY equal.
This will tell us EXACTLY what's different.
"""
import sys
sys.path.insert(0, '/kaggle/working')

from arc_types import *
from dsl import o_g as cpu_o_g
from constants import R7
from gpu_dsl_core import gpu_o_g

# Test grid
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

print("Getting CPU objects...")
cpu_objects = cpu_o_g(test_grid, R7)
print(f"CPU: {len(cpu_objects)} objects")

print("\nGetting GPU objects...")
gpu_objects = gpu_o_g(test_grid, R7, return_format='frozenset')
print(f"GPU: {len(gpu_objects)} objects")

print("\n" + "="*70)
print("EQUALITY TEST")
print("="*70)
print(f"cpu_objects == gpu_objects: {cpu_objects == gpu_objects}")
print(f"cpu_objects is gpu_objects: {cpu_objects is gpu_objects}")
print(f"id(cpu_objects): {id(cpu_objects)}")
print(f"id(gpu_objects): {id(gpu_objects)}")

print("\n" + "="*70)
print("HASH TEST")
print("="*70)
print(f"hash(cpu_objects): {hash(cpu_objects)}")
print(f"hash(gpu_objects): {hash(gpu_objects)}")
print(f"Hashes equal: {hash(cpu_objects) == hash(gpu_objects)}")

print("\n" + "="*70)
print("ITERATION TEST")
print("="*70)
cpu_list = list(cpu_objects)
gpu_list = list(gpu_objects)
print(f"Length of cpu_list: {len(cpu_list)}")
print(f"Length of gpu_list: {len(gpu_list)}")
print(f"cpu_list == gpu_list: {cpu_list == gpu_list}")

if cpu_list != gpu_list:
    print("\n✗ ITERATION ORDERS DIFFER!")
    print("\nComparing element by element:")
    for i in range(min(len(cpu_list), len(gpu_list))):
        cpu_obj = cpu_list[i]
        gpu_obj = gpu_list[i]
        cpu_color = {c for _, _, c in cpu_obj}
        gpu_color = {c for _, _, c in gpu_obj}
        match = "✓" if cpu_obj == gpu_obj else "✗"
        print(f"  [{i}] {match} CPU color={cpu_color}, GPU color={gpu_color}, equal={cpu_obj == gpu_obj}")
else:
    print("\n✓ ITERATION ORDERS MATCH!")

print("\n" + "="*70)
print("SET DIFFERENCE TEST")
print("="*70)
cpu_only = cpu_objects - gpu_objects
gpu_only = gpu_objects - cpu_objects
print(f"Objects in CPU but not GPU: {len(cpu_only)}")
print(f"Objects in GPU but not CPU: {len(gpu_only)}")

if cpu_only:
    print("\nCPU-only objects:")
    for obj in cpu_only:
        color = {c for _, _, c in obj}
        print(f"  Size={len(obj)}, color={color}")
        print(f"    Cells: {sorted(obj)[:3]}...")  # Show first 3 cells

if gpu_only:
    print("\nGPU-only objects:")
    for obj in gpu_only:
        color = {c for _, _, c in obj}
        print(f"  Size={len(obj)}, color={color}")
        print(f"    Cells: {sorted(obj)[:3]}...")  # Show first 3 cells

print("\n" + "="*70)
print("CONCLUSION")
print("="*70)
if cpu_objects == gpu_objects and cpu_list == gpu_list:
    print("✅ PERFECT MATCH - Objects equal AND iterate in same order!")
elif cpu_objects == gpu_objects:
    print("⚠️  WEIRD - Objects equal but iterate differently!")
    print("    This should be IMPOSSIBLE for frozensets!")
else:
    print("❌ OBJECTS DIFFER - Not equal as sets!")
print("="*70)
