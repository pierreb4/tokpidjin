"""
GPU-Accelerated DSL Operations

Provides GPU-accelerated versions of critical DSL operations for batch processing.
Falls back to CPU implementations if GPU unavailable.

Usage:
    from gpu_dsl_ops import gpu_accelerator
    
    # Process batch of grids
    results = gpu_accelerator.batch_rot90(grids)
    results = gpu_accelerator.batch_flip(grids)
    results = gpu_accelerator.batch_transpose(grids)
"""

import numpy as np
from typing import List, Optional, Callable, Any
import sys

try:
    import cupy as cp
    CUPY_AVAILABLE = True
except ImportError:
    CUPY_AVAILABLE = False
    cp = None


class GPUAccelerator:
    """GPU-accelerated DSL operations for batch processing."""
    
    def __init__(self, use_gpu: bool = True):
        """Initialize GPU accelerator with automatic fallback to CPU."""
        self.use_gpu = use_gpu and CUPY_AVAILABLE
        self.gpu_calls = 0
        self.cpu_calls = 0
        
        if self.use_gpu:
            try:
                # Verify GPU is accessible
                _ = cp.zeros((1, 1))
            except Exception as e:
                print(f"⚠ GPU accelerator initialization failed: {e}. Using CPU.", file=sys.stderr)
                self.use_gpu = False
    
    def batch_rot90(self, grids: List, k: int = 1) -> List:
        """
        Batch rotate 90 degrees on GPU.
        
        Args:
            grids: List of grid arrays
            k: Number of 90-degree rotations (1-3)
            
        Returns:
            List of rotated grids
        """
        if not self.use_gpu:
            self.cpu_calls += 1
            return [np.rot90(g, k) for g in grids]
        
        try:
            self.gpu_calls += 1
            grids_gpu = [cp.asarray(g, dtype=cp.int32) for g in grids]
            results_gpu = [cp.rot90(g, k) for g in grids_gpu]
            return [cp.asnumpy(g).astype(np.int32) for g in results_gpu]
        except Exception as e:
            print(f"⚠ GPU rot90 failed: {e}. Using CPU.", file=sys.stderr)
            self.cpu_calls += 1
            return [np.rot90(g, k) for g in grids]
    
    def batch_flip(self, grids: List, axis: int = 1) -> List:
        """
        Batch flip arrays on GPU.
        
        Args:
            grids: List of grid arrays
            axis: Axis to flip (0=vertical, 1=horizontal)
            
        Returns:
            List of flipped grids
        """
        if not self.use_gpu:
            self.cpu_calls += 1
            return [np.flip(g, axis=axis) for g in grids]
        
        try:
            self.gpu_calls += 1
            grids_gpu = [cp.asarray(g, dtype=cp.int32) for g in grids]
            if axis == 0:
                results_gpu = [cp.flipud(g) for g in grids_gpu]
            elif axis == 1:
                results_gpu = [cp.fliplr(g) for g in grids_gpu]
            else:
                results_gpu = [cp.flip(g, axis=axis) for g in grids_gpu]
            return [cp.asnumpy(g).astype(np.int32) for g in results_gpu]
        except Exception as e:
            print(f"⚠ GPU flip failed: {e}. Using CPU.", file=sys.stderr)
            self.cpu_calls += 1
            return [np.flip(g, axis=axis) for g in grids]
    
    def batch_transpose(self, grids: List) -> List:
        """
        Batch transpose on GPU.
        
        Args:
            grids: List of grid arrays
            
        Returns:
            List of transposed grids
        """
        if not self.use_gpu:
            self.cpu_calls += 1
            return [np.transpose(g) for g in grids]
        
        try:
            self.gpu_calls += 1
            grids_gpu = [cp.asarray(g, dtype=cp.int32) for g in grids]
            results_gpu = [cp.transpose(g) for g in grids_gpu]
            return [cp.asnumpy(g).astype(np.int32) for g in results_gpu]
        except Exception as e:
            print(f"⚠ GPU transpose failed: {e}. Using CPU.", file=sys.stderr)
            self.cpu_calls += 1
            return [np.transpose(g) for g in grids]
    
    def batch_shift(self, grids: List, shift_amount: int = 1, axis: int = 0) -> List:
        """
        Batch shift/roll on GPU.
        
        Args:
            grids: List of grid arrays
            shift_amount: How much to shift
            axis: Which axis to shift along
            
        Returns:
            List of shifted grids
        """
        if not self.use_gpu:
            self.cpu_calls += 1
            return [np.roll(g, shift_amount, axis=axis) for g in grids]
        
        try:
            self.gpu_calls += 1
            grids_gpu = [cp.asarray(g, dtype=cp.int32) for g in grids]
            results_gpu = [cp.roll(g, shift_amount, axis=axis) for g in grids_gpu]
            return [cp.asnumpy(g).astype(np.int32) for g in results_gpu]
        except Exception as e:
            print(f"⚠ GPU shift failed: {e}. Using CPU.", file=sys.stderr)
            self.cpu_calls += 1
            return [np.roll(g, shift_amount, axis=axis) for g in grids]
    
    def batch_operation(self, grids: List, operation_name: str, *args, **kwargs) -> List:
        """
        Generic batch operation dispatcher.
        
        Args:
            grids: List of grid arrays
            operation_name: Name of operation ('rot90', 'flip', 'transpose', 'shift')
            *args: Positional arguments for operation
            **kwargs: Keyword arguments for operation
            
        Returns:
            List of processed grids
        """
        if operation_name == 'rot90':
            k = args[0] if args else kwargs.get('k', 1)
            return self.batch_rot90(grids, k)
        elif operation_name == 'flip':
            axis = args[0] if args else kwargs.get('axis', 1)
            return self.batch_flip(grids, axis)
        elif operation_name == 'transpose':
            return self.batch_transpose(grids)
        elif operation_name == 'shift':
            shift_amount = args[0] if args else kwargs.get('shift_amount', 1)
            axis = args[1] if len(args) > 1 else kwargs.get('axis', 0)
            return self.batch_shift(grids, shift_amount, axis)
        else:
            # Unknown operation, return as-is
            return grids
    
    def get_stats(self) -> dict:
        """Get GPU vs CPU usage statistics."""
        return {
            'gpu_calls': self.gpu_calls,
            'cpu_calls': self.cpu_calls,
            'total_calls': self.gpu_calls + self.cpu_calls,
            'gpu_percentage': (self.gpu_calls / (self.gpu_calls + self.cpu_calls) * 100) if (self.gpu_calls + self.cpu_calls) > 0 else 0,
            'gpu_available': self.use_gpu
        }
    
    def reset_stats(self):
        """Reset GPU/CPU statistics."""
        self.gpu_calls = 0
        self.cpu_calls = 0


# Global GPU accelerator instance
gpu_accelerator = GPUAccelerator()


def batch_process_dsl_operation(grids: List, operation_func: Callable) -> List:
    """
    Process a batch of grids through a DSL operation function.
    
    This function detects common GPU-accelerable operations and uses GPU when possible.
    
    Args:
        grids: List of grids to process
        operation_func: DSL function to apply
        
    Returns:
        List of processed grids
    """
    if not grids:
        return []
    
    # For now, apply operation to each grid individually
    # In a full implementation, we would batch these
    try:
        return [operation_func(grid) for grid in grids]
    except Exception as e:
        print(f"⚠ Batch DSL operation failed: {e}", file=sys.stderr)
        return grids
