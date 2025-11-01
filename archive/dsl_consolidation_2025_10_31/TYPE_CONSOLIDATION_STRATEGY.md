# Type Consolidation Strategy: Eliminating FrozenSet in Favor of Tuple

## Executive Summary

Currently `dsl.py` maintains **parallel type hierarchies** for nearly every operation:
- Tuple variants: `get_nth_t`, `apply_t`, `sfilter_t`, `merge_t`, etc.
- FrozenSet variants: `get_nth_f`, `apply_f`, `sfilter_f`, `merge_f`, etc.
- Generic variants: `get_nth`, `apply`, `sfilter`, `merge`, etc.

This proposal consolidates to **single-type functions that use tuples internally**, reducing code duplication and cognitive overhead by ~50%.

---

## Current Type Ecosystem

### Active Types in dsl.py (36 types total)

**Base Container Types:**
- `Tuple` - Ordered, mutable during construction, immutable when passed
- `FrozenSet` - Unordered, immutable, used for uniqueness
- `Container` - Generic base (Union of Tuple and FrozenSet)

**Specific Frozenset-based Types (9 types):**
- `IntegerSet` = FrozenSet[Integer]
- `Indices` = FrozenSet[IJ]
- `IndicesSet` = FrozenSet[Indices]
- `Object` = FrozenSet[Cell]
- `Objects` = FrozenSet[Object]
- `Patch` = Union[Object, Indices]

**Specific Tuple-based Types (7 types):**
- `Grid` = Tuple[Tuple[Integer]]
- `Samples` = Tuple[Grid, Grid]
- `TupleTuple` = Tuple[Tuple]
- `Colors` = Tuple[C_, ...]
- `TTT_iii` = Tuple[Tuple[Tuple[int, int, int], ...], ...]
- `Cell` = Tuple[I_, J_, C_]
- `Indices` (conceptually, but currently FrozenSet)

**Numeric/Scalar Types (14 types):**
- Boolean, Integer, Numerical
- F_, FL, L_, R_, R4, R8, A4, A8, C_, I_, J_, IJ

---

## Problem: Type Explosion and Duplication

### Current Duplication Pattern
Each collection operation has **3 implementations**:

```python
# Generic (delegates to type-specific)
def apply(function, container) -> Container:
    return type(container)(...)

# Tuple-specific
def apply_t(function, container: Tuple) -> Tuple:
    return tuple(function(e) for e in container)

# FrozenSet-specific
def apply_f(function, container: FrozenSet) -> FrozenSet:
    return frozenset(function(e) for e in container)
```

**Functions with this pattern (30+ functions):**
- Collection ops: `apply`, `apply_t`, `apply_f`
- Filtering: `sfilter`, `sfilter_t`, `sfilter_f`
- Merging: `merge`, `merge_t`, `merge_f`
- Selection: `get_nth`, `get_nth_t`, `get_nth_f`
- Set ops: `combine`, `combine_t`, `combine_f`
- Others: `valmax`, `argmax`, `mostcommon`, `leastcommon`, etc. (×3 each)

### Costs of Current Approach
1. **Maintenance burden**: 3× implementations = 3× bugs, 3× documentation
2. **Cognitive overhead**: Developers must choose `_t` or `_f` variant every time
3. **API surface**: 324 functions → could be 150-200 with consolidation
4. **solvers_pre.py friction**: Must remember which variant to use
5. **Type checking**: HINT_OVERLAPS must define compatibility across 3 variants

### Why Tuple is the Better Choice
| Aspect | Tuple | FrozenSet |
|--------|-------|-----------|
| **Immutability** | ✅ Yes | ✅ Yes |
| **Python Performance** | ✅ Faster (no hashing) | Slower (hashing overhead) |
| **Memory** | ✅ Smaller footprint | Larger (hash table) |
| **Hashability** | ✅ Yes (nested tuples) | ✅ Yes but limited |
| **Ordering** | ✅ Preserved | ✗ Lost (unordered) |
| **Construction Cost** | ✅ O(n) | Slower (O(n log n) with hashing) |
| **Iteration Order** | ✅ Deterministic | ✗ Non-deterministic |

---

## Proposed Architecture

### Phase 1: Type Simplification in arc_types.py

**Remove these types:**
- `IntegerSet` → Use `Tuple[Integer, ...]`
- `Indices` → Use `Tuple[IJ, ...]`
- `IndicesSet` → Use `Tuple[Indices, ...]`
- `Object` → Use `Tuple[Cell, ...]`
- `Objects` → Use `Tuple[Object, ...]`
- `Patch` → Keep as `Tuple[Cell, ...] | Tuple[IJ, ...]`

**Keep these base types:**
- `Container` → Becomes alias for `Tuple` (removing FrozenSet support)
- `Tuple` → Primary collection type
- `FrozenSet` → Optional, only where it's truly semantically required (currently nowhere)

**New type ecosystem (18 types instead of 36):**
```python
# Base
Tuple[T]  # Primary collection type

# Scalar types (14)
Boolean, Integer, Numerical, F_, FL, L_, R_, R4, R8, A4, A8, C_, I_, J_, IJ

# Specific tuple types (4)
Grid = Tuple[Tuple[Integer]]
Samples = Tuple[Tuple[Grid, Grid]]  # Could be Tuple[Sample, ...] if we define Sample
Colors = Tuple[C_, ...]
Cell = Tuple[I_, J_, C_]

# Composite types
TupleTuple = Tuple[Tuple, ...]
TTT_iii = Tuple[Tuple[Tuple[int, int, int], ...], ...]
```

### Phase 2: Function Consolidation

**Consolidate 3 variants → 1 function** for each collection operation:

```python
# OLD (3 implementations)
def apply(function, container) -> Container:          # Generic
def apply_t(function, container: Tuple) -> Tuple:     # Tuple-specific
def apply_f(function, container: FrozenSet) -> FrozenSet:  # FrozenSet-specific

# NEW (1 implementation)
def apply(function, container: Tuple) -> Tuple:
    return tuple(function(e) for e in container)
```

**Functions affected (~30):**
- Collection ops: `apply`, `rapply`, `mapply`, `papply`, `mpapply`, `prapply`
- Filtering: `sfilter`, `mfilter`, `extract`
- Merging: `merge`, `combine`
- Selection: `get_nth`, `get_nth_by_key`, `get_arg_rank`, `get_val_rank`, `get_common_rank`
- Stats: `size`, `valmax`, `valmin`, `argmax`, `argmin`, `mostcommon`, `leastcommon`
- Removal: `remove`, `other`
- Set ops: `combine`, `intersection`, `difference`
- Iteration: `first`, `last`, `order`

**Result:**
- **~180 functions eliminated** (reduce dsl.py by ~2000 lines)
- **1 function per operation** (easier to understand and maintain)
- **Simplified HINT_OVERLAPS** (no `_t`/`_f` variants to track)

### Phase 3: Update HINT_OVERLAPS

**Simplify type compatibility:**

```python
# CURRENT (27 types)
HINT_OVERLAPS = {
    'Tuple': {...},
    'FrozenSet': {...},
    'IntegerSet': {...},
    'Indices': {...},
    'Object': {...},
    'Objects': {...},
    ...
}

# NEW (18 types)
HINT_OVERLAPS = {
    'Tuple': {'Tuple', 'Container', 'Grid', 'Samples', 'Colors', 'TupleTuple', 'TTT_iii'},
    'Grid': {'Tuple', 'Container', 'Grid', 'Samples'},
    'Samples': {'Tuple', 'Container', 'Grid', 'Samples'},
    'Colors': {'Tuple', 'Container'},
    'Cell': {'Tuple', 'Container'},
    # ... numeric types unchanged
}
```

---

## Implementation Roadmap

### Step 1: Update arc_types.py (30 minutes)
- Remove `IntegerSet`, `Indices`, `IndicesSet`, `Object`, `Objects` type definitions
- Update `Patch` definition
- Add type aliases for clarity

### Step 2: Update dsl.py (2-3 hours)
- Consolidate collection functions (30+ functions → 10-15)
- Replace all `_t` and `_f` specific implementations with single tuple-based versions
- Update docstrings
- Keep `initset()` but have it return `()` instead of `frozenset({value})`

### Step 3: Update constants.py (15 minutes)
- Simplify HINT_OVERLAPS dictionary
- Remove frozenset-specific type overlaps

### Step 4: Update solvers_pre.py (1 hour)
- Replace `apply_f` → `apply`
- Replace `get_nth_f` → `get_nth`
- Replace `merge_f` → `merge`
- Replace `sfilter_f` → `sfilter`
- Replace `mfilter_f` → `mfilter`
- ~40-50 function calls need updating

### Step 5: Update card.py (15 minutes)
- Update function signatures in type checking
- Update HINT_OVERLAPS references

### Step 6: Test & Validation (1-2 hours)
- Run existing test suite
- Verify solvers still produce correct output
- Check performance (should improve)

---

## Migration Path for Specific Operations

### Example 1: Filter Operation
```python
# BEFORE
def sfilter(container, condition):
    return type(container)(e for e in container if condition(e))

def sfilter_t(container, condition):
    return tuple(e for e in container if condition(e))

def sfilter_f(container, condition):
    return frozenset(e for e in container if condition(e))

# AFTER
def sfilter(container: Tuple, condition: Callable) -> Tuple:
    return tuple(e for e in container if condition(e))
```

### Example 2: Merge Operation
```python
# BEFORE
def merge(containers):
    """merging"""
    return merge_t(containers) if isinstance(containers, tuple) else merge_f(containers)

def merge_t(containers):
    """merging for tuples"""
    return sum(containers, ())

def merge_f(containers):
    """merging for frozensets"""
    return frozenset().union(*containers)

# AFTER
def merge(containers: Tuple) -> Tuple:
    """merging"""
    return sum(containers, ())
```

### Example 3: Get Nth Operation
```python
# BEFORE
def get_nth(container, rank):
    if isinstance(container, frozenset):
        return get_nth_f(container, rank)
    return get_nth_t(container, rank)

def get_nth_t(container: Tuple, rank: FL) -> Any:
    index = rank if rank >= 0 else len(container) + rank
    return container[index] if 0 <= index < len(container) else ()

def get_nth_f(container: FrozenSet, rank: FL) -> Any:
    sorted_container = tuple(sorted(container))
    index = rank if rank >= 0 else len(sorted_container) + rank
    return sorted_container[index] if 0 <= index < len(sorted_container) else frozenset()

# AFTER
def get_nth(container: Tuple, rank: FL) -> Any:
    index = rank if rank >= 0 else len(container) + rank
    return container[index] if 0 <= index < len(container) else ()
```

---

## Benefits Summary

### Code Reduction
- **Current**: ~3500+ functions (including variants)
- **After**: ~2500-2700 functions (remove ~800 `_t`/`_f` variants)
- **Lines saved**: ~2000 lines in dsl.py

### Cognitive Load Reduction
- **Before**: Developers must choose `apply_t`, `apply_f`, or generic `apply`
- **After**: One `apply` function works for all collections

### Type System Simplification
- **Before**: 36 types in arc_types.py, 27 in HINT_OVERLAPS
- **After**: 18 types in arc_types.py, 15 in HINT_OVERLAPS

### Performance Improvements
- **Tuple faster than FrozenSet**: No hashing overhead
- **Simpler operations**: Direct index access vs. iteration
- **Memory efficiency**: Tuples use less memory per element

### Maintainability
- **Single source of truth**: One implementation per operation
- **Easier testing**: One path to test instead of three
- **Clearer solvers**: solvers_pre.py becomes more readable

---

## Potential Concerns & Mitigations

| Concern | Mitigation |
|---------|-----------|
| **Tuple order matters** | That's a feature, not a bug - order is preserved |
| **Set uniqueness lost** | Tuples can have duplicates, but most ops don't require uniqueness |
| **Hash-based lookup** | Use `elem in container` (still O(n) but acceptable) |
| **Backward compatibility** | Small adjustments to solvers_pre.py needed |
| **Existing code breaking** | Comprehensive migration plan with gradual updates |

---

## Special Cases

### `initset(value)` Function
**Current**: Returns `frozenset({value})`
**Proposed**: Return `(value,)` (single-element tuple)
- All downstream operations already handle tuples
- Maintains semantic meaning of "initialization"

### `product(a, b)` Function
**Current**: Returns FrozenSet[Tuple]
**Proposed**: Return Tuple[Tuple] (tuple of tuples)
- Cartesian product is naturally a collection of pairs
- Tuples maintain structure better

### Operations Requiring Uniqueness
**Examples**: `intersection`, `difference`, `combine`
**Approach**: These can still work with tuples
- `intersection(a, b)`: Return tuple of elements in both
- `difference(a, b)`: Return tuple of elements in a but not b
- `combine(a, b)`: Return `a + b` (concatenation)

---

## Next Steps

1. **Approval**: Get consensus on this approach
2. **Create branch**: `feature/type-consolidation`
3. **Implement Phase 1-2**: Update arc_types.py and dsl.py
4. **Test thoroughly**: Ensure all solvers produce identical output
5. **Update solvers_pre.py**: Migrate function calls
6. **Validate**: Performance benchmarking and correctness verification
7. **Merge**: Integrate into main branch

---

## Questions for Discussion

1. **Scope**: Should we phase this in gradually or do it all at once?
2. **Tuple defaults**: For empty containers, should default be `()` or keep special cases?
3. **Performance**: Any operations where FrozenSet is genuinely required?
4. **Migration timeline**: When should this be implemented?
5. **Backward compatibility**: Any external dependencies relying on FrozenSet return types?
