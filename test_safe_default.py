#!/usr/bin/env python3
"""Test the _safe_default helper function generation"""

from pile import *
from typing import get_type_hints


def _safe_default(func):
    """Get type-appropriate default for failed operations"""
    try:
        hints = get_type_hints(func)
        return_type = str(hints.get('return', ''))
        
        # FrozenSet-based types
        if any(t in return_type for t in ['FrozenSet', 'Object', 'Objects', 'Indices', 'IndicesSet', 'IntegerSet', 'Patch']):
            return frozenset()
        # Tuple-based types
        elif any(t in return_type for t in ['Tuple', 'Grid', 'IJ', 'Samples', 'TupleTuple', 'Container', 'Cell']):
            return ()
        # Numeric types
        elif any(t in return_type for t in ['Integer', 'Numerical', 'int']):
            return 0
        # Boolean types
        elif any(t in return_type for t in ['Boolean', 'bool']):
            return False
        # Callable types
        elif 'Callable' in return_type:
            return lambda *a, **k: ()
        else:
            return ()
    except:
        return ()


# Test cases
if __name__ == "__main__":
    print("Testing _safe_default with DSL functions:")
    
    # Test FrozenSet return types
    result = _safe_default(objects)
    print(f"objects -> {result!r} (expected: frozenset())")
    assert result == frozenset(), f"Expected frozenset(), got {result!r}"
    
    # Test Tuple return types
    result = _safe_default(identity)
    print(f"identity -> {result!r} (expected: ())")
    assert result == (), f"Expected (), got {result!r}"
    
    # Test Integer return types
    result = _safe_default(size)
    print(f"size -> {result!r} (expected: 0)")
    assert result == 0, f"Expected 0, got {result!r}"
    
    # Test Callable return types
    result = _safe_default(rbind)
    print(f"rbind -> {result!r} (expected: lambda)")
    assert callable(result), f"Expected callable, got {result!r}"
    
    # Test that it works in exception handlers
    print("\nTesting in exception handlers:")
    
    # This should fail but return appropriate default
    try:
        result = objects("invalid", "args")  # Wrong signature
    except (TypeError, AttributeError, ValueError):
        result = _safe_default(objects)
    print(f"objects with bad args -> {result!r} (expected: frozenset())")
    assert result == frozenset()
    
    # This should fail but return appropriate default
    try:
        result = size("not", "enough", "args")  # Wrong signature
    except (TypeError, AttributeError, ValueError):
        result = _safe_default(size)
    print(f"size with bad args -> {result!r} (expected: 0)")
    assert result == 0
    
    print("\n✅ All tests passed!")
