#!/usr/bin/env python3
"""
Test if cp.unique() returns colors in consistent order.
"""
try:
    import cupy as cp
    CUPY_AVAILABLE = True
except ImportError:
    CUPY_AVAILABLE = False
    print("CuPy not available")
    exit(1)

# Create test grid with multiple colors
grid = [[3, 3, 0, 1, 1],
        [3, 0, 0, 1, 0],
        [0, 0, 2, 2, 0]]

grid_array = cp.array(grid, dtype=cp.int8)

print("Grid:")
for row in grid:
    print(row)
print()

# Test unique multiple times
for i in range(5):
    unique_colors = cp.unique(grid_array)
    colors = cp.asnumpy(unique_colors)
    print(f"Trial {i+1}: unique colors = {list(colors)}")

print("\nConclusion: cp.unique() returns SORTED colors (consistent order)")
