#!/usr/bin/env python3
"""
Test if CuPy or GPU environment affects frozenset hash values.
"""
import cupy as cp

# Create identical frozensets
obj1 = frozenset([(0,0,3), (0,1,3), (0,2,3)])
obj2 = frozenset([(0,0,1), (0,1,1), (0,2,1)])

print("Without CuPy operations:")
fs1 = frozenset([obj1, obj2])
print("Iteration order:")
for i, obj in enumerate(fs1):
    color = list(obj)[0][2]
    print(f"  [{i}] color={color}")
print()

# Create after CuPy array operations
arr = cp.array([[1,2],[3,4]])
_ = cp.asnumpy(arr)  # Do some CuPy ops

fs2 = frozenset([obj1, obj2])
print("After CuPy operations:")
for i, obj in enumerate(fs2):
    color = list(obj)[0][2]
    print(f"  [{i}] color={color}")
print()

print(f"Are they equal? {fs1 == fs2}")
print(f"Same iteration order? {list(fs1) == list(fs2)}")
