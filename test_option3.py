#!/usr/bin/env python3
"""
Quick test of Option 3 (batch-native) batt file

Tests that the transformed batt file works correctly with batch operations.
"""

import sys
sys.path.insert(0, '/kaggle/input/tokpidjin')

# Test imports
print("Testing imports...")
try:
    from batt_test_transformed import batt
    print("✅ batt imported successfully")
except Exception as e:
    print(f"❌ Failed to import batt: {e}")
    sys.exit(1)

# Create test data
print("\nCreating test data...")
test_grid = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
S = (test_grid,)  # Tuple of one grid
I = test_grid
C = None

print(f"  S = {S}")
print(f"  I = {I}")

# Test batt
print("\nTesting batt function...")
try:
    s_result, o_result = batt('test_task', S, I, C, 'test.log')
    print(f"✅ batt executed successfully")
    print(f"  s_result: {len(s_result)} items")
    print(f"  o_result: {len(o_result)} items")
    
    # Show first few results
    print(f"\n  First few s_result items:")
    for item in s_result[:3]:
        print(f"    {item}")
        
except Exception as e:
    print(f"❌ batt execution failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n" + "="*70)
print("✅ ALL TESTS PASSED - Ready for benchmark!")
print("="*70)
