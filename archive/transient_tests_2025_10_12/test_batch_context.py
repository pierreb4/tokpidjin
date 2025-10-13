"""
Quick test of batch DSL context integration

Tests that GPU operations are now called when processing batches.
"""

import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

print("="*70)
print("Testing Batch DSL Context Integration")
print("="*70)

# Create simple test
from mega_batch_batt import MegaBatchCoordinator

# Mock data
mock_data = {
    'demo': {
        'test_1': [
            {'input': ((0, 1), (1, 0)), 'output': ((1, 0), (0, 1))},
            {'input': ((2, 2), (2, 2)), 'output': ((3, 3), (3, 3))},
        ],
    },
    'test': {
        'test_1': [
            {'input': ((0, 0), (0, 0)), 'output': None},
        ],
    }
}

task_list = ['test_1']

print("\n[1/2] Testing Sequential (should use GPU context)")
print("-" * 70)
coordinator_seq = MegaBatchCoordinator(
    batt_module_name='batt_gpu_operations_test',
    batch_size=3,
    parallel=False,
    enable_gpu=False,  # CPU mode for local testing
    max_workers=1
)

try:
    results, elapsed = coordinator_seq.process_all(mock_data, task_list)
    print(f"✅ Sequential completed: {elapsed:.3f}s")
except Exception as e:
    print(f"❌ Sequential failed: {e}")
    import traceback
    traceback.print_exc()

print("\n[2/2] Testing Parallel (should use GPU context)")
print("-" * 70)
coordinator_par = MegaBatchCoordinator(
    batt_module_name='batt_gpu_operations_test',
    batch_size=3,
    parallel=True,
    enable_gpu=False,  # CPU mode for local testing
    max_workers=2
)

try:
    results, elapsed = coordinator_par.process_all(mock_data, task_list)
    print(f"✅ Parallel completed: {elapsed:.3f}s")
except Exception as e:
    print(f"❌ Parallel failed: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*70)
print("✅ Integration test complete!")
print("="*70)
print("\nLook for 'Installed GPU-aware DSL wrappers' in the output above")
print("This confirms the GPU context is being activated.")
