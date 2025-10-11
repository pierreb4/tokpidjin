"""
Kaggle deep debug to understand why sorting fix doesn't work.
"""

try:
    import cupy as cp
    print("CuPy available")
except ImportError:
    print("CuPy not available")

from dsl import o_g as cpu_o_g, get_arg_rank_f, size, subgrid
from gpu_dsl_core import gpu_o_g
from constants import R7, L1

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
print("DEEP DEBUG: Why sorting fix doesn't work")
print("="*70)

# CPU
print("\\n--- CPU o_g ---")
cpu_objs = cpu_o_g(test_grid, R7)
print(f"Count: {len(cpu_objs)}")

cpu_sorted = sorted(cpu_objs, key=size, reverse=True)
print("\\nSorted by size (descending):")
for i, obj in enumerate(cpu_sorted):
    color = {c for _, _, c in obj}
    min_rc = (min(r for r, _, _ in obj), min(c for _, c, _ in obj))
    mark = " ← L1" if i == len(cpu_sorted)-1 else ""
    print(f"  [{i}] size={len(obj):2d}, color={color}, min_rc={min_rc}{mark}")

cpu_selected = get_arg_rank_f(cpu_objs, size, L1)
cpu_result = subgrid(cpu_selected, test_grid)
print(f"\\nCPU result: {cpu_result}")

# GPU
print("\\n--- GPU o_g ---")
gpu_objs = gpu_o_g(test_grid, R7, return_format='frozenset')
print(f"Count: {len(gpu_objs)}")

gpu_sorted = sorted(gpu_objs, key=size, reverse=True)
print("\\nSorted by size (descending):")
for i, obj in enumerate(gpu_sorted):
    color = {c for _, _, c in obj}
    min_rc = (min(r for r, _, _ in obj), min(c for _, c, _ in obj))
    mark = " ← L1" if i == len(gpu_sorted)-1 else ""
    print(f"  [{i}] size={len(obj):2d}, color={color}, min_rc={min_rc}{mark}")

gpu_selected = get_arg_rank_f(gpu_objs, size, L1)
gpu_result = subgrid(gpu_selected, test_grid)
print(f"\\nGPU result: {gpu_result}")

# Compare
print("\\n" + "="*70)
if cpu_result == gpu_result:
    print("✓ MATCH!")
else:
    print("✗ MISMATCH!")
    cpu_color = {c for _, _, c in cpu_selected}
    gpu_color = {c for _, _, c in gpu_selected}
    print(f"CPU color: {cpu_color}")
    print(f"GPU color: {gpu_color}")
    
    # Check if objects are actually equal
    if cpu_objs == gpu_objs:
        print("\\nObjects are EQUAL as frozensets")
        print("But iteration order causes different selection!")
    else:
        print("\\nObjects are DIFFERENT!")
        print(f"CPU: {len(cpu_objs)} objects")
        print(f"GPU: {len(gpu_objs)} objects")

print("="*70)
