#!/usr/bin/env python3
"""Test the pattern used in generated batch files"""

from pile import *
from safe_dsl import _get_safe_default


def test_generated_pattern():
    """Simulate the pattern used in generated batch files"""
    
    print("Testing generated code pattern:")
    print("=" * 60)
    
    # Test 1: Wrong signature (like rbind example)
    print("\n1. Wrong signature test (rbind with wrong args):")
    try:
        t8 = rbind(initset, R5)  # initset takes 1 arg, creates wrong signature
    except (TypeError, AttributeError, ValueError):
        t8 = _get_safe_default(rbind)
    print(f"   t8 = {t8!r} (expected: callable)")
    assert callable(t8), "Expected callable"
    
    try:
        t9 = t8(identity(((1, 2), (3, 4))))  # Try to call the malformed function
    except (TypeError, AttributeError, ValueError):
        # Can't get type hints for the lambda, so use identity as proxy
        t9 = _get_safe_default(identity)
    print(f"   t9 = {t9!r} (expected: ())")
    assert t9 == (), "Expected ()"
    
    # Test 2: FrozenSet function fails
    print("\n2. FrozenSet function test:")
    try:
        t1 = objects("bad", "args")
    except (TypeError, AttributeError, ValueError):
        t1 = _get_safe_default(objects)
    print(f"   t1 = {t1!r} (expected: frozenset())")
    assert t1 == frozenset(), "Expected frozenset()"
    
    # Test 3: Integer function fails
    print("\n3. Integer function test:")
    try:
        t2 = size("bad", "args")
    except (TypeError, AttributeError, ValueError):
        t2 = _get_safe_default(size)
    print(f"   t2 = {t2!r} (expected: 0)")
    assert t2 == 0, "Expected 0"
    
    # Test 4: Tuple function fails
    print("\n4. Tuple function test (Any return type):")
    try:
        t3 = identity("bad", "args")
    except (TypeError, AttributeError, ValueError):
        t3 = _get_safe_default(identity)
    print(f"   t3 = {t3!r} (expected: ())")
    assert t3 == (), "Expected ()"
    
    # Test 5: Non-callable variable
    print("\n5. Non-callable variable test:")
    t6 = 0.2  # Float value
    try:
        t7 = t6(None, None)  # Try to call it
    except (TypeError, AttributeError, ValueError):
        # t6 is not a function, use identity as fallback
        t7 = _get_safe_default(identity)
    print(f"   t7 = {t7!r} (expected: ())")
    assert t7 == (), "Expected ()"
    
    print("\n" + "=" * 60)
    print("✅ All generated pattern tests passed!")
    print("✅ Using _get_safe_default from safe_dsl.py")


if __name__ == "__main__":
    test_generated_pattern()
