# Hash Randomization and Frozenset Iteration Order

## The Discovery

You asked an **excellent question**: "What about hash randomization?"

This is indeed related, but the core issue is more subtle.

## Python Frozenset Behavior

### What Python Guarantees
✅ Equal frozensets have the same hash value
✅ Equal frozensets compare equal with `==`
✅ Frozensets are immutable

### What Python Does NOT Guarantee
❌ Iteration order is NOT part of the frozenset contract
❌ Equal frozensets built differently may iterate differently (in theory)

### CPython Implementation (current)
In practice, CPython's frozenset **does** maintain consistent iteration order based on internal hash table structure. But this is an **implementation detail**.

## Our Problem

### Why CPU and GPU Differ

**CPU `o_g()`** (dsl.py):
```python
for loc in unvisited:  # Row-by-row scan
    # Build objects in grid scan order
    objs.add(frozenset(obj))
return frozenset(objs)
```

**GPU `gpu_o_g()`** (gpu_dsl_core.py):
```python
for color in unique_colors:  # Process by color
    # Extract objects for each color
    objects_list.append(obj)
return frozenset(frozenset(obj) for obj in objects_list)
```

**Result**: Even though they create the **same objects** (equal frozensets), the objects might be **added to the outer frozenset in different orders**.

### Why This Matters

`get_arg_rank_f` does:
```python
ranked = sorted(container, key=size, reverse=True)
return ranked[rank]
```

When sizes are **tied**, `sorted()` uses **stable sort** which preserves the **original iteration order** of the frozenset!

- CPU frozenset iterates: [obj_color3, obj_color1] → sorted preserves this for ties
- GPU frozenset iterates: [obj_color1, obj_color3] → sorted preserves this for ties

**Result**: `L1` (last element) selects different objects!

## The Solution

We have **two options**:

### Option A: Make GPU Match CPU Order (HARD)
Try to replicate CPU's exact scan order in GPU code.
- ❌ Complex to implement
- ❌ Fragile (depends on CPU implementation details)
- ❌ May not even be possible with different algorithms

### Option B: Add Secondary Sort Key (EASY) ✅
Modify `get_arg_rank_f` to break ties deterministically:

```python
def get_arg_rank_f(container: 'FrozenSet', compfunc: 'Callable', rank: 'FL') -> 'Any':
    # Sort by compfunc, then by min cell coordinates for ties
    ranked = sorted(container, 
                   key=lambda obj: (compfunc(obj), tuple(sorted(obj))),
                   reverse=True)
    return ranked[rank] if -len(ranked) <= rank < len(ranked) else frozenset()
```

**But wait!** Modifying `dsl.py` would affect **all solvers**, not just GPU ones!

### Option C: Ensure GPU Builds Identical Frozenset (BEST) ✅

The key insight: If we build the frozenset **exactly the same way** as CPU, it will have the **same iteration order**!

**CPU builds**: `set()` → add objects → `frozenset(set)`
**GPU should build**: `set()` → add objects in same order → `frozenset(set)`

Instead of:
```python
return frozenset(frozenset(obj) for obj in objects_list)
```

Do:
```python
objs = set()
for obj in objects_list:
    objs.add(frozenset(obj))
return frozenset(objs)
```

This uses Python's **set**, which will hash and order objects the **same way** CPU does!

## Next Steps

1. Run `kaggle_definitive_test.py` to confirm objects are equal but iterate differently
2. Modify `gpu_o_g` to use `set()` intermediate (matching CPU construction)
3. Test to verify iteration orders now match
4. Week 2 should finally pass! 🎯

---
**Status**: Root cause identified - construction order affects frozenset iteration
**Solution**: Build frozenset using set() intermediate (like CPU does)
**Confidence**: Very high - this matches the symptoms exactly
