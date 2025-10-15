"""
Batch-native batt function - Auto-generated
Source: batt_gpu_operations_test.py
Generator: batch_batt_generator.py

This version processes entire batches natively using GPU operations:
- batch_mapply: Batch map-apply operations
- batch_o_g: Batch object extraction
- batch_apply: Batch apply operations
- batch_fill: Batch fill operations
"""

from dsl import *
from gpu_dsl_operations import get_gpu_ops

# Initialize GPU operations
_gpu_ops = get_gpu_ops(enable_gpu=True)

# Batch operation shortcuts
batch_mapply = _gpu_ops.batch_mapply
batch_apply = _gpu_ops.batch_apply
batch_o_g = _gpu_ops.batch_o_g
batch_fill = _gpu_ops.batch_fill
batch_colorfilter = _gpu_ops.batch_colorfilter

# Test batt file that uses gpu_dsl_operations.py
# This tests the actual GPU operations (batch_mapply, batch_o_g, batch_apply)
# Unlike batt_mega_test.py which uses old batch_process_samples_gpu

# Note: mega_batch_batt.py handles GPU coordination via gpu_dsl_operations.py

def batt_batch(task_ids, Ss, Is, Cs, log_paths):
    """
    Test batt that uses DSL operations that will be GPU-accelerated
    via gpu_dsl_operations.py (batch_mapply, batch_o_g, batch_apply)
    """
    s = []
    o = []
    
    # Test 1: mapply operations (should use batch_mapply GPU)
    # These will be accelerated by gpu_dsl_operations.batch_mapply
    t1s = batch_mapply(rot90, Ss)
    t2s = batch_mapply(flip, Ss)
    t3s = batch_mapply(rot180, Ss)
    
    # Test 2: Object extraction (should use batch_o_g GPU)
    # This will be accelerated by gpu_dsl_operations.batch_o_g
    t4s = batch_mapply(lambda g: objects(g, T=True, diagonal=False, without_bg=False), Ss)
    
    # Test 3: apply operations (should use batch_apply)
    # This will be accelerated by gpu_dsl_operations.batch_apply
    t5s = batch_apply(first, Ss)
    t6s = batch_apply(second, Ss)
    
    # Test 4: More complex operations
    t7s = batch_mapply(lambda g: rot90(rot90(g)), Ss)
    t8s = batch_mapply(identity, Ss)  # Identity (GPU accelerated as no-op)
    
    # Test 5: Object extraction with different rotations
    t9s = batch_mapply(lambda g: o_g(g, 0), Ss)
    t10s = batch_mapply(lambda g: o_g(g, 1), Ss)
    t11s = batch_mapply(lambda g: o_g(g, 2), Ss)
    t12s = batch_mapply(lambda g: o_g(g, 3), Ss)
    
    # Test 6: Mixed operations
    rotated = mapply(rot90, S)
    flipped = mapply(flip, rotated)
    objects_from_flipped = mapply(lambda g: objects(g, T=True, diagonal=False, without_bg=False), flipped)
    
    # Return some result (doesn't matter for benchmark)
    t13s = batch_apply(first, Ss)
    
    # Add differ outputs
    s.append((1, 'None', 'test_mapply_rot90', t1))
    s.append((2, 'None', 'test_mapply_flip', t2))
    s.append((3, 'None', 'test_mapply_rot180', t3))
    s.append((4, 'None', 'test_objects', t4))
    s.append((5, 'None', 'test_apply_first', t5))
    s.append((6, 'None', 'test_apply_second', t6))
    s.append((7, 'None', 'test_double_rot90', t7))
    s.append((8, 'None', 'test_identity', t8))
    s.append((9, 'None', 'test_o_g_r0', t9))
    s.append((10, 'None', 'test_o_g_r1', t10))
    s.append((11, 'None', 'test_o_g_r2', t11))
    s.append((12, 'None', 'test_o_g_r3', t12))
    s.append((13, 'None', 'test_result', t13))
    
    # Add output for reconstruction (use first sample)
    o.append((13, 'test_result', t13))
    
    return s, o
