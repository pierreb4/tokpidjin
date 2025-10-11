#!/usr/bin/env python3
"""
Test: Can two equal frozensets have different iteration orders?
HYPOTHESIS: No! Frozensets are IMMUTABLE and hash-based.
If fs1 == fs2, they must iterate in the same order!
"""

obj1 = frozenset([(0,0,3), (0,1,3)])
obj2 = frozenset([(0,0,1), (0,1,1)])

# Create two equal frozensets in different ways
fs1 = frozenset([obj1, obj2])
fs2 = frozenset([obj2, obj1])  # Different insertion order

print(f"fs1 == fs2: {fs1 == fs2}")
print(f"fs1 is fs2: {fs1 is fs2}")
print()

print("fs1 iteration:")
for i, obj in enumerate(fs1):
    color = list(obj)[0][2]
    print(f"  [{i}] color={color}")
print()

print("fs2 iteration:")
for i, obj in enumerate(fs2):
    color = list(obj)[0][2]
    print(f"  [{i}] color={color}")
print()

# Sort both
size = lambda obj: len(obj)
sorted1 = sorted(fs1, key=size, reverse=True)
sorted2 = sorted(fs2, key=size, reverse=True)

print("sorted(fs1, key=size):")
for i, obj in enumerate(sorted1):
    color = list(obj)[0][2]
    print(f"  [{i}] color={color}")
print()

print("sorted(fs2, key=size):")
for i, obj in enumerate(sorted2):
    color = list(obj)[0][2]
    print(f"  [{i}] color={color}")
print()

print(f"sorted1 == sorted2: {sorted1 == sorted2}")

print("\n" + "="*70)
print("CONCLUSION: Equal frozensets MUST iterate in same order!")
print("If they iterate differently, they're NOT equal!")
print("="*70)
