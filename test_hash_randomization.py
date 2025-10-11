#!/usr/bin/env python3
"""
Test if hash randomization explains the frozenset iteration order issue.
"""

# Create two identical frozensets using different construction methods
obj1 = frozenset([(0, 0, 3), (0, 1, 3), (0, 2, 3)])
obj2 = frozenset([(0, 0, 1), (0, 1, 1), (0, 2, 1)])

# Method 1: Build from list in order [obj1, obj2]
list1 = [obj1, obj2]
fs1 = frozenset(list1)

# Method 2: Build from list in reverse order [obj2, obj1]
list2 = [obj2, obj1]
fs2 = frozenset(list2)

print("="*70)
print("HASH VALUES")
print("="*70)
print(f"hash(obj1): {hash(obj1)}")
print(f"hash(obj2): {hash(obj2)}")
print(f"hash(fs1): {hash(fs1)}")
print(f"hash(fs2): {hash(fs2)}")
print()

print("="*70)
print("EQUALITY TEST")
print("="*70)
print(f"fs1 == fs2: {fs1 == fs2}")
print(f"fs1 is fs2: {fs1 is fs2}")
print()

print("="*70)
print("ITERATION ORDER TEST")
print("="*70)
print("fs1 iteration:")
for i, obj in enumerate(fs1):
    color = list(obj)[0][2]
    print(f"  [{i}] hash={hash(obj):20d}, color={color}")

print("\nfs2 iteration:")
for i, obj in enumerate(fs2):
    color = list(obj)[0][2]
    print(f"  [{i}] hash={hash(obj):20d}, color={color}")

print()
if list(fs1) == list(fs2):
    print("✓ Iteration orders MATCH")
else:
    print("✗ Iteration orders DIFFER")

print()
print("="*70)
print("CONCLUSION")
print("="*70)
print("Run this script MULTIPLE TIMES with PYTHONHASHSEED=random")
print("If iteration order stays the same: Hash values are stable within a process")
print("If iteration order changes: Hash randomization affects order")
print()
print("The KEY insight: CPU and GPU might build frozensets that are EQUAL")
print("but have different iteration orders due to how elements are added!")
print("="*70)
