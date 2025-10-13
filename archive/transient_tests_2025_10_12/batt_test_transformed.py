# Test batt file that uses gpu_dsl_operations.py
# This tests the actual GPU operations (batch_mapply, batch_o_g, batch_apply)
# Unlike batt_mega_test.py which uses old batch_process_samples_gpu

from dsl import *
from gpu_dsl_operations import batch_mapply, batch_apply  # All DSL functions: mapply, apply, rot90, flip, objects, o_g, etc.
# Note: mega_batch_batt.py handles GPU coordination via gpu_dsl_operations.py

def batt(task_id, S, I, C, log_path):
    """
    Test batt that uses DSL operations that will be GPU-accelerated
    via gpu_dsl_operations.py (batch_mapply, batch_o_g, batch_apply)
    """
    s = []
    o = []
    
    # Test 1: mapply operations (should use batch_mapply GPU)
    # These will be accelerated by gpu_dsl_operations.batch_mapply
    t1 = mapply(rot90, S)  # Rotate all samples - GPU accelerated!
    t2 = mapply(flip, S)   # Flip all samples - GPU accelerated!
    t3 = mapply(rot180, S) # Rotate 180 - GPU accelerated!
    
    # Test 2: Object extraction (should use batch_o_g GPU)
    # This will be accelerated by gpu_dsl_operations.batch_o_g
    t4 = mapply(lambda g: objects(g, T=True, diagonal=False, without_bg=False), S)
    
    # Test 3: apply operations (should use batch_apply)
    # This will be accelerated by gpu_dsl_operations.batch_apply
    t5 = batch_apply(first, [S])[0]
    t6 = batch_apply(second, [S])[0]
    
    # Test 4: More complex operations
    t7 = mapply(lambda g: rot90(rot90(g)), S)  # Double rotation
    t8 = mapply(identity, S)  # Identity (GPU accelerated as no-op)
    
    # Test 5: Object extraction with different rotations
    t9 = mapply(lambda g: o_g(g, 0), S)  # Rotation 0
    t10 = mapply(lambda g: o_g(g, 1), S)  # Rotation 1
    t11 = mapply(lambda g: o_g(g, 2), S)  # Rotation 2
    t12 = mapply(lambda g: o_g(g, 3), S)  # Rotation 3
    
    # Test 6: Mixed operations
    rotated = batch_mapply(rot90, [S])[0]
    flipped = mapply(flip, rotated)
    objects_from_flipped = mapply(lambda g: objects(g, T=True, diagonal=False, without_bg=False), flipped)
    
    # Return some result (doesn't matter for benchmark)
    t13 = batch_apply(first, [S])[0]
    
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
