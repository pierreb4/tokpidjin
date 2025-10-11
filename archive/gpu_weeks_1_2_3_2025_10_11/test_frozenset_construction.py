#!/usr/bin/env python3
"""
Critical test: Can two equal frozensets have different iteration orders?
This tests if internal structure differs based on construction.
"""

# Create objects with hash values that might collide
obj_a = frozenset([(0, 0, 3), (0, 1, 3)])
obj_b = frozenset([(0, 0, 1), (0, 1, 1)])

print(f"obj_a hash: {hash(obj_a)}")
print(f"obj_b hash: {hash(obj_b)}")
print()

# Build frozenset by adding elements in different orders
# Method 1: Add obj_a first
temp_set1 = set()
temp_set1.add(obj_a)
temp_set1.add(obj_b)
fs1 = frozenset(temp_set1)

# Method 2: Add obj_b first
temp_set2 = set()
temp_set2.add(obj_b)
temp_set2.add(obj_a)
fs2 = frozenset(temp_set2)

print("="*70)
print(f"fs1 == fs2: {fs1 == fs2}")
print(f"hash(fs1) == hash(fs2): {hash(fs1) == hash(fs2)}")
print()

print("fs1 iteration (obj_a added first):")
for obj in fs1:
    color = list(obj)[0][2]
    print(f"  color={color}, hash={hash(obj)}")

print("\nfs2 iteration (obj_b added first):")
for obj in fs2:
    color = list(obj)[0][2]
    print(f"  color={color}, hash={hash(obj)}")

print()
if list(fs1) == list(fs2):
    print("✓ Same iteration order")
else:
    print("✗ DIFFERENT iteration order despite being equal!")
    print("\nThis proves: Equal frozensets CAN have different iteration orders")
    print("if they were constructed with different element insertion orders!")

# Now the critical insight for our GPU issue:
print()
print("="*70)
print("INSIGHT FOR GPU BUG:")
print("="*70)
print("CPU o_g(): Scans grid row-by-row, building objects in scan order")
print("GPU o_g(): Processes by color, then extracts objects from labels")
print()
print("Even if they build the SAME objects (equal frozensets),")
print("the ORDER objects are added to the frozenset might differ!")
print()
print("Result: cpu_objects == gpu_objects (TRUE)")
print("But: list(cpu_objects) != list(gpu_objects) (DIFFERENT ITERATION)")
print("="*70)
