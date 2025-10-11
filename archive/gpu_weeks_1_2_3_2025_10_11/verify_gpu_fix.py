"""
Verification script to check if gpu_dsl_core.py has the sorting fix.
Run this on Kaggle to confirm you have the correct version.
"""

import inspect

try:
    from gpu_dsl_core import gpu_o_g
    
    # Get the source code of gpu_o_g
    source = inspect.getsource(gpu_o_g)
    
    # Check if the fix is present
    has_sort = "objects_list.sort" in source
    has_min_row = "min(cell[0]" in source
    has_min_col = "min(cell[1]" in source
    
    print("=" * 70)
    print("GPU_DSL_CORE.PY VERSION CHECK")
    print("=" * 70)
    
    if has_sort and has_min_row and has_min_col:
        print("\n✅ CORRECT VERSION - Sorting fix is present!")
        print("\nThe fix includes:")
        print("  - objects_list.sort() ✓")
        print("  - Sort by min(cell[0]) for row ✓")
        print("  - Sort by min(cell[1]) for col ✓")
        print("\nThis is the FIXED version that should pass correctness tests.")
    else:
        print("\n❌ OLD VERSION - Sorting fix is MISSING!")
        print("\nMissing components:")
        if not has_sort:
            print("  - objects_list.sort() ✗")
        if not has_min_row:
            print("  - Sort by min(cell[0]) ✗")
        if not has_min_col:
            print("  - Sort by min(cell[1]) ✗")
        print("\n⚠️  YOU NEED TO RE-UPLOAD THE FIXED gpu_dsl_core.py FILE!")
        print("    The current file on Kaggle is the OLD version.")
        print("    Download the latest from GitHub or your local machine.")
    
    print("\n" + "=" * 70)
    
except Exception as e:
    print(f"Error checking version: {e}")
    print("Make sure gpu_dsl_core.py is uploaded to Kaggle.")
