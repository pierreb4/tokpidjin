#!/usr/bin/env python3
"""
Test the ACTUAL scenario from solve_23b5c85d.
Reproduce CPU vs GPU order difference with size=10 objects.
"""

# Create objects matching the actual test case
# Both size=10, but different colors
obj_color3 = frozenset([
    (0, 0, 3), (0, 1, 3), (0, 2, 3), (1, 0, 3), (1, 1, 3),
    (1, 2, 3), (2, 0, 3), (2, 1, 3), (2, 2, 3), (3, 0, 3)
])

obj_color1 = frozenset([
    (0, 7, 1), (0, 8, 1), (0, 9, 1), (1, 7, 1), (1, 8, 1),
    (1, 9, 1), (2, 7, 1), (2, 8, 1), (2, 9, 1), (3, 7, 1)
])

print(f"obj_color3 size: {len(obj_color3)}")
print(f"obj_color1 size: {len(obj_color1)}")
print()

# Create frozenset of ALL objects (like CPU does)
all_objects = frozenset([obj_color3, obj_color1])

print("Iteration order of frozenset:")
for i, obj in enumerate(all_objects):
    color = list(obj)[0][2]  # Get color from first cell
    print(f"  [{i}] size={len(obj)}, color={color}")
print()

# Sort by size (what get_arg_rank_f does)
size = lambda obj: len(obj)
sorted_objs = sorted(all_objects, key=size, reverse=True)

print("After sorted(frozenset, key=size, reverse=True):")
for i, obj in enumerate(sorted_objs):
    color = list(obj)[0][2]  # Get color from first cell
    print(f"  [{i}] size={len(obj)}, color={color}")
print()

# Now test with LISTS instead (like our GPU creates)
# Try both orders
list1 = [obj_color3, obj_color1]
list2 = [obj_color1, obj_color3]

print("List order 1 (color3, color1):")
sorted1 = sorted(list1, key=size, reverse=True)
for i, obj in enumerate(sorted1):
    color = list(obj)[0][2]
    print(f"  [{i}] size={len(obj)}, color={color}")
print()

print("List order 2 (color1, color3):")
sorted2 = sorted(list2, key=size, reverse=True)
for i, obj in enumerate(sorted2):
    color = list(obj)[0][2]
    print(f"  [{i}] size={len(obj)}, color={color}")
print()

print("=" * 70)
print("KEY INSIGHT:")
print("When we convert list to frozenset, the iteration order changes!")
print("CPU: objects() function builds frozenset directly")
print("GPU: We build list, then convert to frozenset")
print("The frozenset iteration order is based on hash values of the objects!")
print("=" * 70)
