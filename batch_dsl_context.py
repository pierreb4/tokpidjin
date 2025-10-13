"""
Batch DSL Context - Integration layer for GPU-accelerated batch operations

This module provides a context manager that intercepts DSL operations during
batch processing and routes them to GPU-accelerated batch versions.

Strategy:
1. When processing a batch, install DSL function wrappers
2. Wrappers detect when operations are called on batch data
3. Route to gpu_dsl_operations for GPU acceleration
4. Restore original functions after batch completes

Author: Pierre
Date: October 13, 2025
Week: 5 Day 3
"""

import logging
from typing import Any, Callable, List, Optional
from contextlib import contextmanager
import threading

logger = logging.getLogger(__name__)

# Thread-local storage for batch context
_batch_context = threading.local()


class BatchContext:
    """
    Context for batch DSL execution.
    
    Tracks which data is part of a batch and routes operations
    to GPU-accelerated versions when possible.
    """
    
    def __init__(self, gpu_ops=None, enable_gpu=True):
        """
        Initialize batch context.
        
        Args:
            gpu_ops: GPUDSLOperations instance for GPU acceleration
            enable_gpu: Whether to use GPU operations
        """
        self.gpu_ops = gpu_ops
        self.enable_gpu = enable_gpu and gpu_ops is not None
        self.batch_data_ids = set()  # Track which data is part of current batch
        self.operation_count = 0
        self.gpu_operation_count = 0
        
        # Store original DSL functions
        self.original_functions = {}
        
    def register_batch_data(self, data: Any) -> None:
        """Register data as part of current batch for GPU tracking"""
        self.batch_data_ids.add(id(data))
        
    def is_batch_data(self, data: Any) -> bool:
        """Check if data is part of current batch"""
        return id(data) in self.batch_data_ids
    
    def should_use_gpu(self, collection: Any) -> bool:
        """
        Decide if an operation should use GPU.
        
        Args:
            collection: Data being operated on
            
        Returns:
            True if GPU should be used
        """
        if not self.enable_gpu:
            return False
        
        # For now, always try GPU if enabled
        # Later can add size thresholds, etc.
        return True
    
    def wrap_mapply(self, original_mapply: Callable) -> Callable:
        """
        Create GPU-aware wrapper for mapply.
        
        When mapply is called on batch data, route to batch_mapply GPU operation.
        """
        def gpu_aware_mapply(func, collection):
            self.operation_count += 1
            
            # Check if we should use GPU
            if self.should_use_gpu(collection):
                try:
                    # Call GPU batch operation with single collection
                    result = self.gpu_ops.batch_mapply([collection], func)
                    self.gpu_operation_count += 1
                    logger.debug(f"GPU mapply: {func.__name__} on {len(collection)} items")
                    return result[0]  # Return first (only) result
                except Exception as e:
                    logger.warning(f"GPU mapply failed, falling back to CPU: {e}")
                    # Fall through to CPU version
            
            # CPU fallback
            return original_mapply(func, collection)
        
        return gpu_aware_mapply
    
    def wrap_apply(self, original_apply: Callable) -> Callable:
        """
        Create GPU-aware wrapper for apply.
        """
        def gpu_aware_apply(func, collection):
            self.operation_count += 1
            
            if self.should_use_gpu(collection):
                try:
                    result = self.gpu_ops.batch_apply([collection], func)
                    self.gpu_operation_count += 1
                    logger.debug(f"GPU apply: {func.__name__}")
                    return result[0]
                except Exception as e:
                    logger.warning(f"GPU apply failed, falling back to CPU: {e}")
            
            return original_apply(func, collection)
        
        return gpu_aware_apply
    
    def install_wrappers(self) -> None:
        """
        Install GPU-aware wrappers for DSL functions.
        
        This monkey-patches dsl module to intercept operations.
        """
        if not self.enable_gpu:
            return
        
        try:
            import dsl
            
            # Wrap mapply
            if hasattr(dsl, 'mapply'):
                self.original_functions['mapply'] = dsl.mapply
                dsl.mapply = self.wrap_mapply(dsl.mapply)
                logger.debug("Installed GPU-aware mapply wrapper")
            
            # Wrap apply
            if hasattr(dsl, 'apply'):
                self.original_functions['apply'] = dsl.apply
                dsl.apply = self.wrap_apply(dsl.apply)
                logger.debug("Installed GPU-aware apply wrapper")
                
            logger.info(f"Installed {len(self.original_functions)} GPU-aware DSL wrappers")
            
        except Exception as e:
            logger.error(f"Failed to install DSL wrappers: {e}")
            self.enable_gpu = False
    
    def restore_functions(self) -> None:
        """
        Restore original DSL functions.
        
        Removes monkey-patches after batch completes.
        """
        if not self.original_functions:
            return
        
        try:
            import dsl
            
            for func_name, original_func in self.original_functions.items():
                setattr(dsl, func_name, original_func)
                
            logger.debug(f"Restored {len(self.original_functions)} original DSL functions")
            
            if self.operation_count > 0:
                gpu_percent = (self.gpu_operation_count / self.operation_count) * 100
                logger.info(f"Batch complete: {self.gpu_operation_count}/{self.operation_count} "
                          f"operations used GPU ({gpu_percent:.1f}%)")
            
            self.original_functions.clear()
            
        except Exception as e:
            logger.error(f"Failed to restore DSL functions: {e}")


@contextmanager
def batch_dsl_context(gpu_ops=None, enable_gpu=True):
    """
    Context manager for batch DSL execution with GPU acceleration.
    
    Usage:
        with batch_dsl_context(gpu_ops=my_gpu_ops, enable_gpu=True):
            # DSL operations will be GPU-accelerated
            result = batt(task_id, S, I, C, log_path)
    
    Args:
        gpu_ops: GPUDSLOperations instance
        enable_gpu: Whether to enable GPU acceleration
        
    Yields:
        BatchContext instance
    """
    # Create and activate context
    context = BatchContext(gpu_ops=gpu_ops, enable_gpu=enable_gpu)
    _batch_context.current = context
    
    try:
        # Install wrappers before entering context
        context.install_wrappers()
        yield context
        
    finally:
        # Always restore original functions
        context.restore_functions()
        _batch_context.current = None


def get_current_batch_context() -> Optional[BatchContext]:
    """Get the current batch context, if any"""
    return getattr(_batch_context, 'current', None)
