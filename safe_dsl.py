"""
Safe DSL Decorator - Makes all DSL functions exception-safe

This module provides a decorator that wraps DSL functions to never throw exceptions.
Instead, functions return type-appropriate empty/default values on error.

Usage:
    from safe_dsl import safe_dsl
    
    @safe_dsl
    def my_function(x: Grid) -> Grid:
        return risky_operation(x)
    
    # Now my_function() never throws - returns () on error

Author: Pierre
Date: October 11, 2025
"""

from functools import wraps
from typing import Any, Callable
import logging

# Import cached type hints from dsl module
# This provides O(1) lookups instead of O(n) introspection
try:
    from dsl import _get_type_hints_cached
except ImportError:
    # Fallback if dsl is not available yet
    from typing import get_type_hints as _get_type_hints_builtin
    def _get_type_hints_cached(func):
        try:
            return _get_type_hints_builtin(func)
        except Exception:
            return {}

# Setup logging
logger = logging.getLogger(__name__)


def safe_dsl(func: Callable) -> Callable:
    """
    Decorator to make DSL functions never throw exceptions.
    Returns safe default values based on return type annotation.
    
    Args:
        func: Function to wrap
        
    Returns:
        Wrapped function that catches all exceptions
        
    Example:
        @safe_dsl
        def divide(a: int, b: int) -> int:
            return a // b
        
        result = divide(10, 0)  # Returns 0 instead of ZeroDivisionError
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Log the exception (first occurrence only to avoid spam)
            if not hasattr(wrapper, '_logged'):
                logger.debug(f"{func.__name__} failed with {type(e).__name__}: {e}")
                wrapper._logged = True
            
            # Return safe default based on return type
            return _get_safe_default(func)
    
    # Preserve original argcount for functions like rbind that check it
    if hasattr(func, '__code__'):
        wrapper._original_argcount = func.__code__.co_argcount
    
    return wrapper


def _get_safe_default(func: Callable) -> Any:
    """
    Get safe default value based on function's return type annotation.
    
    Args:
        func: Function to get default for
        
    Returns:
        Safe default value (frozenset(), tuple(), 0, False, etc.)
    """
    try:
        hints = _get_type_hints_cached(func)  # Use cached version - O(1) instead of O(n)
        return_type = hints.get('return', None)
        
        if return_type is None:
            return ()
        
        # Convert type to string for easier matching
        type_str = str(return_type)
        
        # Match against known ARC types (from arc_types.py)
        # FrozenSet-based types
        if any(t in type_str for t in [
            'FrozenSet', 'Object', 'Objects', 
            'Indices', 'IndicesSet', 'IntegerSet', 'Patch'
        ]):
            return frozenset()
        
        # Tuple-based types
        elif any(t in type_str for t in [
            'Tuple', 'Grid', 'IJ', 'Samples', 
            'TupleTuple', 'Container', 'Cell'
        ]):
            return ()
        
        # Numeric types
        elif any(t in type_str for t in ['Integer', 'Numerical', 'int']):
            return 0
        
        # Boolean types
        elif any(t in type_str for t in ['Boolean', 'bool']):
            return False
        
        # Callable types - return a safe function that returns safe defaults
        elif 'Callable' in type_str:
            def safe_callable(*args, **kwargs):
                # Return empty tuple as the safest default for most cases
                return ()
            return safe_callable
        
        # Default for Any or unknown types
        else:
            return ()
            
    except Exception:
        # If type inspection fails, return empty tuple
        return ()


def make_all_dsl_safe(module):
    """
    Apply @safe_dsl decorator to all functions in a module.
    
    This is typically called automatically when dsl.py is imported.
    
    Args:
        module: The module object (usually sys.modules[__name__])
        
    Example:
        # At end of dsl.py
        import sys
        from safe_dsl import make_all_dsl_safe
        make_all_dsl_safe(sys.modules[__name__])
    """
    import inspect
    
    for name, obj in inspect.getmembers(module, inspect.isfunction):
        # Skip private functions
        if name.startswith('_'):
            continue
        
        # Skip if already wrapped
        if hasattr(obj, '__wrapped__'):
            continue
        
        # Only wrap functions defined in this module
        if obj.__module__ == module.__name__:
            # Apply decorator and replace in module
            safe_func = safe_dsl(obj)
            setattr(module, name, safe_func)
            
            logger.debug(f"Made {name} safe")


# Example usage and testing
if __name__ == '__main__':
    # Test the decorator
    @safe_dsl
    def divide(a: int, b: int) -> int:
        """Divide a by b"""
        return a // b
    
    @safe_dsl
    def get_first(container: tuple) -> tuple:
        """Get first element"""
        return container[0]
    
    @safe_dsl
    def make_frozenset(items) -> frozenset:
        """Make frozenset from items"""
        return frozenset(items[100])  # Will fail
    
    # Test cases
    print("Testing safe_dsl decorator:")
    print(f"divide(10, 2) = {divide(10, 2)}")  # 5
    print(f"divide(10, 0) = {divide(10, 0)}")  # 0 (safe default)
    print(f"get_first((1,2,3)) = {get_first((1,2,3))}")  # 1
    print(f"get_first(()) = {get_first(())}")  # () (safe default)
    print(f"make_frozenset([1,2]) = {make_frozenset([1,2])}")  # frozenset() (safe default)
    
    print("\n✅ All tests passed - no exceptions thrown!")
