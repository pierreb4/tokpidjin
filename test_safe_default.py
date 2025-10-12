#!/usr/bin/env python3
"""Test the _get_safe_default helper function from safe_dsl.py"""

from pile import *
from safe_dsl import _get_safe_default


# Test cases
if __name__ == "__main__":
    print("Testing _get_safe_default from safe_dsl.py:")
    
    # Test FrozenSet return types
    result = _get_safe_default(objects)
    print(f"objects -> {result!r} (expected: frozenset())")
    assert result == frozenset(), f"Expected frozenset(), got {result!r}"
    
    # Test Tuple return types
    result = _get_safe_default(identity)
    print(f"identity -> {result!r} (expected: ())")
    assert result == (), f"Expected (), got {result!r}"
    
    # Test Integer return types
    result = _get_safe_default(size)
    print(f"size -> {result!r} (expected: 0)")
    assert result == 0, f"Expected 0, got {result!r}"
    
    # Test Callable return types
    result = _get_safe_default(rbind)
    print(f"rbind -> {result!r} (expected: callable)")
    assert callable(result), f"Expected callable, got {result!r}"
    
    # Test that it works in exception handlers
    print("\nTesting in exception handlers:")
    
    # This should fail but return appropriate default
    try:
        result = objects("invalid", "args")  # Wrong signature
    except (TypeError, AttributeError, ValueError):
        result = _get_safe_default(objects)
    print(f"objects with bad args -> {result!r} (expected: frozenset())")
    assert result == frozenset()
    
    # This should fail but return appropriate default
    try:
        result = size("not", "enough", "args")  # Wrong signature
    except (TypeError, AttributeError, ValueError):
        result = _get_safe_default(size)
    print(f"size with bad args -> {result!r} (expected: 0)")
    assert result == 0
    
    print("\n✅ All tests passed!")
    print("✅ Using _get_safe_default from safe_dsl.py (no duplication)")

