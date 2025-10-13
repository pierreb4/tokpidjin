"""
Batch Validation for Vectorized Batt Processing

Provides pre-validation for vectorized batt operations that skip try/except blocks.
Since GPU kernels can't handle Python exceptions, we validate inputs before operations.

Pattern:
    valid, result = validate_and_call(func, *args)
    if not valid:
        result = safe_default

This replaces the try/except pattern in standard mode while maintaining type safety.

Author: Pierre
Date: October 13, 2025
"""

from typing import Any, Callable, Tuple, get_type_hints
from safe_dsl import _get_safe_default
import logging

logger = logging.getLogger(__name__)


def validate_type(value: Any, expected_type_str: str) -> bool:
    """
    Validate if value matches expected ARC type.
    
    Args:
        value: The value to validate
        expected_type_str: String representation of expected type
        
    Returns:
        True if type matches, False otherwise
    """
    # None always fails validation
    if value is None:
        return False
    
    # FrozenSet-based types
    if any(t in expected_type_str for t in [
        'FrozenSet', 'Object', 'Objects', 
        'Indices', 'IndicesSet', 'IntegerSet', 'Patch'
    ]):
        return isinstance(value, frozenset)
    
    # Tuple-based types (Grid, Cell, Container, etc.)
    elif any(t in expected_type_str for t in [
        'Tuple', 'Grid', 'IJ', 'Samples', 
        'TupleTuple', 'Container', 'Cell'
    ]):
        return isinstance(value, tuple)
    
    # Numeric types
    elif any(t in expected_type_str for t in ['Integer', 'Numerical', 'int']):
        return isinstance(value, (int, float))
    
    # Boolean types
    elif any(t in expected_type_str for t in ['Boolean', 'bool']):
        return isinstance(value, bool)
    
    # Callable types
    elif 'Callable' in expected_type_str:
        return callable(value)
    
    # Any type - always valid
    elif 'Any' in expected_type_str:
        return True
    
    # Unknown type - be permissive
    else:
        return True


def validate_args(func: Callable, *args) -> Tuple[bool, str]:
    """
    Validate function arguments match expected types.
    
    Args:
        func: Function to validate arguments for
        *args: Arguments to validate
        
    Returns:
        (valid, error_message) tuple
        - valid: True if all args match expected types
        - error_message: Error description if invalid
    """
    try:
        hints = get_type_hints(func)
        
        # Get parameter names (skip 'return')
        param_names = [k for k in hints.keys() if k != 'return']
        
        # If no type hints, assume valid
        if not param_names:
            return True, ""
        
        # Check each argument
        for i, (arg, param_name) in enumerate(zip(args, param_names)):
            expected_type = hints.get(param_name)
            if expected_type is None:
                continue
            
            type_str = str(expected_type)
            if not validate_type(arg, type_str):
                return False, f"Arg {i} ({param_name}): expected {type_str}, got {type(arg).__name__}"
        
        return True, ""
        
    except Exception as e:
        # If validation itself fails, be permissive
        logger.debug(f"Validation error for {func.__name__}: {e}")
        return True, ""


def validate_and_call(func: Callable, *args, **kwargs) -> Tuple[bool, Any]:
    """
    Validate arguments and call function, returning safe default on failure.
    
    This is the main entry point for vectorized batch processing.
    
    Args:
        func: Function to call
        *args: Positional arguments
        **kwargs: Keyword arguments
        
    Returns:
        (success, result) tuple
        - success: True if validation passed and function succeeded
        - result: Function result or safe default
        
    Example:
        success, result = validate_and_call(compose, t1, t2)
        if not success:
            # Handle error at batch level
            batch_errors.append((idx, "compose failed"))
    """
    # Validate arguments
    valid, error_msg = validate_args(func, *args)
    if not valid:
        logger.debug(f"{func.__name__} validation failed: {error_msg}")
        return False, _get_safe_default(func)
    
    # Try to call function
    try:
        result = func(*args, **kwargs)
        return True, result
    except Exception as e:
        # Function call failed
        logger.debug(f"{func.__name__} execution failed: {e}")
        return False, _get_safe_default(func)


def batch_validate_and_call(func: Callable, batch_args: list) -> Tuple[list, list]:
    """
    Validate and call function on batch of argument tuples.
    
    GPU-optimized pattern: process entire batch at once, track errors separately.
    
    Args:
        func: Function to call
        batch_args: List of argument tuples [(args1,), (args2,), ...]
        
    Returns:
        (results, errors) tuple
        - results: List of results (or safe defaults)
        - errors: List of (idx, error_msg) for failed calls
        
    Example:
        results, errors = batch_validate_and_call(compose, [
            (t1_0, t2_0),
            (t1_1, t2_1),
            (t1_2, t2_2),
        ])
        # results = [result_0, result_1, result_2]
        # errors = [(1, "compose failed: type mismatch")]
    """
    results = []
    errors = []
    
    for idx, args in enumerate(batch_args):
        success, result = validate_and_call(func, *args)
        results.append(result)
        
        if not success:
            errors.append((idx, f"{func.__name__} failed"))
    
    return results, errors


def safe_batch_operation(func: Callable, *batch_inputs) -> Tuple[list, list]:
    """
    Apply function element-wise to batch inputs with validation.
    
    Pattern for vectorized batt:
        t2_batch, errors = safe_batch_operation(compose, t0_batch, t1_batch)
    
    Args:
        func: Function to apply
        *batch_inputs: Variable number of batched inputs (all same length)
        
    Returns:
        (results, errors) tuple
        
    Example:
        # Process batch of 1000 samples
        t1_batch = [grid1, grid2, ..., grid1000]
        t2_batch = [grid1, grid2, ..., grid1000]
        t3_batch, errors = safe_batch_operation(compose, t1_batch, t2_batch)
    """
    if not batch_inputs:
        return [], []
    
    # Check all batches have same length
    batch_size = len(batch_inputs[0])
    if not all(len(batch) == batch_size for batch in batch_inputs):
        logger.error("Batch size mismatch")
        return [_get_safe_default(func)] * batch_size, [(i, "size mismatch") for i in range(batch_size)]
    
    # Zip inputs into argument tuples
    batch_args = list(zip(*batch_inputs))
    
    # Process batch
    return batch_validate_and_call(func, batch_args)


# Example usage
if __name__ == '__main__':
    # Mock DSL functions for testing
    def compose(f: Callable, g: Callable) -> Callable:
        """Compose two functions"""
        return lambda x: f(g(x))
    
    def identity(x: Any) -> Any:
        """Identity function"""
        return x
    
    def bad_function(x: int) -> int:
        """Function that always fails"""
        raise ValueError("Always fails")
    
    # Test individual validation
    print("Testing validate_and_call:")
    success, result = validate_and_call(compose, identity, identity)
    print(f"compose(identity, identity): success={success}, result={result}")
    
    success, result = validate_and_call(bad_function, 42)
    print(f"bad_function(42): success={success}, result={result}")
    
    # Test batch validation
    print("\nTesting batch_validate_and_call:")
    results, errors = batch_validate_and_call(bad_function, [
        (1,), (2,), (3,), (4,), (5,)
    ])
    print(f"Batch results: {results}")
    print(f"Batch errors: {errors}")
    
    # Test safe batch operation
    print("\nTesting safe_batch_operation:")
    batch1 = [1, 2, 3, 4, 5]
    batch2 = [10, 20, 30, 40, 50]
    results, errors = safe_batch_operation(lambda x, y: x + y, batch1, batch2)
    print(f"Add batch results: {results}")
    print(f"Add batch errors: {errors}")
    
    print("\n✅ Validation system working!")
