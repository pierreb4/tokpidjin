"""
Batt GPU Support - Preamble for generated batt files.

This module provides GPU initialization and batch processing support
that gets imported by generated batt files instead of being inlined.

Exports:
    - GPU optimization objects (gpu_opt, multi_gpu_opt, USE_GPU, etc.)
    - batch_process_samples_gpu() - GPU-accelerated sample processing
    - Batch validation functions from batt_validation module
"""

# Export validation functions for vectorized mode
from batt_validation import (
    validate_and_call,
    batch_validate_and_call,
    safe_batch_operation
)

try:
    from gpu_optimizations import auto_select_optimizer, MultiGPUOptimizer
    import cupy as cp
    
    gpu_opt = auto_select_optimizer()
    USE_GPU = gpu_opt is not None
    
    # Check for multi-GPU support
    gpu_count = cp.cuda.runtime.getDeviceCount() if USE_GPU else 0
    if gpu_count >= 2:
        multi_gpu_opt = MultiGPUOptimizer()
        USE_MULTI_GPU = True
        print(f"Batt GPU: Enabled ({gpu_count} GPUs, {gpu_opt.__class__.__name__})")
    else:
        multi_gpu_opt = None
        USE_MULTI_GPU = False
        if USE_GPU:
            print(f"Batt GPU: Enabled (1 GPU, {gpu_opt.__class__.__name__})")
except Exception as e:
    gpu_opt = None
    multi_gpu_opt = None
    USE_GPU = False
    USE_MULTI_GPU = False
    gpu_count = 0


def batch_process_samples_gpu(S):
    """
    GPU-accelerated batch processing of samples.
    
    Pattern: apply(first/second, S) + mapply(p_g, ...)
    
    NOTE: GPU has significant overhead (initialization, transfers).
    For small batches (< 100 samples), CPU is actually FASTER!
    - Local CPU: ~10ms per batt() call
    - Kaggle GPU: ~127ms per batt() call (10x slower!)
    
    GPU only beneficial for mega-batches (100+ samples).
    For normal batt execution (2-5 samples), use CPU fallback.
    
    Args:
        S: Tuple of (input, output) sample pairs
        
    Returns:
        Tuple of (inputs, outputs, processed_inputs, processed_outputs)
    """
    from pile import apply, first, second, mapply, p_g
    
    # GPU overhead dominates for small batches - use CPU fallback
    # Threshold: 100 samples (GPU beneficial for mega-batch operations only)
    if not USE_GPU or len(S) < 100:
        # CPU fallback for small batches or no GPU
        t1 = apply(first, S)
        t2 = apply(second, S)
        t3 = mapply(p_g, t1)
        t4 = mapply(p_g, t2)
        return t1, t2, t3, t4
    
    try:
        # Extract all grids
        inputs = [sample[0] for sample in S]
        outputs = [sample[1] for sample in S]
        
        # Multi-GPU for large batches (L4x4)
        if USE_MULTI_GPU and len(S) >= 120:
            # Process on multiple GPUs in parallel
            processed_inputs = multi_gpu_opt.batch_grid_op_multi_gpu(
                inputs, lambda x: x, num_gpus=gpu_count
            )
            processed_outputs = multi_gpu_opt.batch_grid_op_multi_gpu(
                outputs, lambda x: x, num_gpus=gpu_count
            )
        else:
            # Single GPU batch processing
            processed_inputs = gpu_opt.batch_grid_op_optimized(
                inputs, lambda x: x, vectorized=False
            )
            processed_outputs = gpu_opt.batch_grid_op_optimized(
                outputs, lambda x: x, vectorized=False
            )
        
        return tuple(inputs), tuple(outputs), tuple(processed_inputs), tuple(processed_outputs)
    
    except Exception as e:
        # Fallback to CPU on any GPU error
        t1 = apply(first, S)
        t2 = apply(second, S)
        t3 = mapply(p_g, t1)
        t4 = mapply(p_g, t2)
        return t1, t2, t3, t4
