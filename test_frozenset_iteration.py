#!/usr/bin/env python3
"""
Test to understand frozenset iteration order.
Key insight: Frozenset iteration order is based on hash values, NOT insertion order!
"""

# Create two objects with same size
obj1 = frozenset([(0,0,3), (0,1,3)])  # color 3
obj2 = frozenset([(0,0,1), (0,1,1)])  # color 1

print("Testing frozenset iteration order:")
print(f"obj1 (color 3): {obj1}")
print(f"obj2 (color 1): {obj2}")
print()

# Create frozenset of objects in different orders
fs1 = frozenset([obj1, obj2])  # obj1 first
fs2 = frozenset([obj2, obj1])  # obj2 first

print("Frozenset of objects (insertion order: obj1, obj2):")
for i, obj in enumerate(fs1):
    print(f"  [{i}] {obj}")
print()

print("Frozenset of objects (insertion order: obj2, obj1):")
for i, obj in enumerate(fs2):
    print(f"  [{i}] {obj}")
print()

print("Are they equal? ", fs1 == fs2)
print()

# Now let's see what happens when we sort by size
size = lambda obj: len(obj)

sorted1 = sorted(fs1, key=size, reverse=True)
sorted2 = sorted(fs2, key=size, reverse=True)

print("Sorted fs1 (by size):")
for i, obj in enumerate(sorted1):
    print(f"  [{i}] {obj}")
print()

print("Sorted fs2 (by size):")
for i, obj in enumerate(sorted2):
    print(f"  [{i}] {obj}")
print()

print("Do sorted lists match?", sorted1 == sorted2)
print()

# KEY INSIGHT: When size is tied, sorted() uses STABLE SORT
# which preserves the ITERATION ORDER from the frozenset!
# And frozenset iteration order is based on HASH VALUES, not insertion order!

print("=" * 70)
print("CRITICAL INSIGHT:")
print("When sorted() has a tie (same size), it preserves FROZENSET ITERATION ORDER")
print("Frozenset iteration order is based on HASH VALUES of the objects")
print("So even if we create the frozenset with same objects, the iteration")
print("order can vary based on hash values!")
print("=" * 70)
