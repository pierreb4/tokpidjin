"""
Comprehensive test to verify the sorting fix works correctly.
Tests the exact scenario from the failing solvers.
"""

try:
    import cupy as cp
    print("✓ CuPy available")
    CUPY_AVAILABLE = True
except ImportError:
    print("✗ CuPy not available")
    CUPY_AVAILABLE = False

if CUPY_AVAILABLE:
    from dsl import o_g as cpu_o_g, get_arg_rank_f, size, subgrid
    from gpu_dsl_core import gpu_o_g
    from constants import R7, L1
    
    # Test grid from the failing solver
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
    
    print("\n" + "="*70)
    print("VERIFICATION TEST: solve_23b5c85d")
    print("="*70)
    
    print("\nSolver: x1=o_g(I,R7), x2=get_arg_rank_f(x1,size,L1), O=subgrid(x2,I)")
    
    # CPU version
    print("\n--- CPU Version ---")
    cpu_objects = cpu_o_g(test_grid, R7)
    cpu_selected = get_arg_rank_f(cpu_objects, size, L1)
    cpu_result = subgrid(cpu_selected, test_grid)
    cpu_color = {cell[2] for cell in cpu_selected}
    print(f"Selected object color: {cpu_color}")
    print(f"Result: {cpu_result}")
    
    # GPU version
    print("\n--- GPU Version ---")
    gpu_objects = gpu_o_g(test_grid, R7, return_format='frozenset')
    gpu_selected = get_arg_rank_f(gpu_objects, size, L1)
    gpu_result = subgrid(gpu_selected, test_grid)
    gpu_color = {cell[2] for cell in gpu_selected}
    print(f"Selected object color: {gpu_color}")
    print(f"Result: {gpu_result}")
    
    # Comparison
    print("\n" + "="*70)
    if cpu_result == gpu_result:
        print("✅ SUCCESS! Results match!")
        print(f"Both selected color: {cpu_color}")
        print(f"Both returned: {cpu_result}")
    else:
        print("❌ FAILURE! Results don't match!")
        print(f"CPU selected color {cpu_color}, GPU selected color {gpu_color}")
        print(f"CPU result: {cpu_result}")
        print(f"GPU result: {gpu_result}")
    
    # Additional verification: Check object equality
    print("\n--- Object Set Comparison ---")
    if cpu_objects == gpu_objects:
        print("✓ Objects are equal as frozensets")
    else:
        print("✗ Objects differ!")
        print(f"CPU: {len(cpu_objects)} objects")
        print(f"GPU: {len(gpu_objects)} objects")
    
    # Detailed comparison of sorted objects
    print("\n--- Sorted Order Comparison ---")
    cpu_sorted = sorted(cpu_objects, key=size, reverse=True)
    gpu_sorted = sorted(gpu_objects, key=size, reverse=True)
    
    print("CPU order (by size):")
    for i, obj in enumerate(cpu_sorted):
        color = {c for _, _, c in obj}
        marker = " ← L1" if i == len(cpu_sorted)-1 else ""
        print(f"  [{i}] size={len(obj):2d}, color={color}{marker}")
    
    print("\nGPU order (by size):")
    for i, obj in enumerate(gpu_sorted):
        color = {c for _, _, c in obj}
        marker = " ← L1" if i == len(gpu_sorted)-1 else ""
        print(f"  [{i}] size={len(obj):2d}, color={color}{marker}")
    
    # Check if order matches
    if all(len(c) == len(g) and {cell[2] for cell in c} == {cell[2] for cell in g} 
           for c, g in zip(cpu_sorted, gpu_sorted)):
        print("\n✓ Sorted orders match! Fix is working!")
    else:
        print("\n✗ Sorted orders differ! Fix not working yet!")
    
    print("="*70)
else:
    print("\nCannot run test without CuPy")
