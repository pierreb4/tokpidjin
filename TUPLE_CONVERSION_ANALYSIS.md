# Tuple Conversion Analysis for GPU Strategy

## Summary

Analysis of solvers using `objects()` and `o_g()` to identify which DSL functions need tuple variants for GPU optimization.

## Solvers Using o_g/objects

Found 20+ solvers in `solvers_pre.py` that use `o_g()`:
- solve_80af3007, solve_3618c87e, solve_045e512c, solve_88a10436
- solve_543a7ed5, solve_8403a5d5, solve_952a094c, solve_ba97ae07
- solve_2013d3e2, solve_60b61512, solve_941d9a10, solve_445eab21
- solve_be94b721, solve_9aec4887, solve_6d58a25d, solve_264363fd
- solve_7468f01a, solve_5521c0d9, solve_97a05b5b, solve_5ad4f10b
- solve_23b5c85d, and more...

## Example Solver Chains

### Simple Example: solve_3618c87e (5 lines)
```python
x1 = o_g(I, R5)              # Objects (frozenset of frozensets)
x2 = sizefilter(x1, ONE)     # Objects → Objects
x3 = merge_f(x2)             # Objects → Object (single frozenset)
O = move(I, x3, TWO_BY_ZERO)
```

### Medium Example: solve_88a10436 (11 lines)
```python
x1 = o_g(I, R1)              # Objects
x2 = colorfilter(x1, FIVE)   # Objects → Objects
x3 = difference(x1, x2)      # Objects → Objects
x4 = get_nth_f(x3, F0)       # Objects → Object
x5 = normalize(x4)
x6 = get_nth_f(x2, F0)       # Objects → Object
x7 = center(x6)
x8 = shift(x5, x7)
x9 = shift(x8, NEG_UNITY)
O = paint(I, x9)
```

### Complex Example: solve_543a7ed5 (7 lines)
```python
x1 = o_g(I, R5)              # Objects
x2 = colorfilter(x1, SIX)    # Objects → Objects
x3 = mapply(outbox, x2)      # Objects → Indices (merged)
x4 = fill(I, THREE, x3)
x5 = mapply(delta, x2)       # Objects → Indices (merged)
O = fill(x4, FOUR, x5)
```

### Complex Example: solve_045e512c (13+ lines)
```python
x1 = o_g(I, R7)                    # Objects
x2 = get_arg_rank_f(x1, size, F0)  # Objects → Object (largest)
x3 = lbind(shift, x2)
x4 = lbind(mapply, x3)
...
x13 = remove_f(x2, x1)             # Objects → Objects
```

## Functions Operating on Objects (Frozenset)

### Core Functions Needing Tuple Variants

| Function | Current Signature | Returns | Priority | Notes |
|----------|------------------|---------|----------|-------|
| **colorfilter** | `(Objects, C_) → Objects` | frozenset | HIGH | Filter by color - simple |
| **sizefilter** | `(Container, Integer) → Container` | frozenset | HIGH | Filter by size - simple |
| **get_nth_f** | `(FrozenSet, FL) → Any` | item | HIGH | Get nth element |
| **get_arg_rank_f** | `(FrozenSet, Callable, FL) → Any` | item | HIGH | Get element by rank |
| **difference** | `(FrozenSet, FrozenSet) → FrozenSet` | frozenset | MEDIUM | Set difference |
| **remove_f** | `(Any, FrozenSet) → FrozenSet` | frozenset | MEDIUM | Remove element |
| **merge_f** | `(ContainerContainer) → Container` | frozenset | MEDIUM | Flatten nested |
| **mapply** | `(Callable, ContainerContainer) → FrozenSet` | frozenset | LOW | Calls merge |

### Already Have Tuple Variants

✅ **merge_t** - Already exists  
✅ **mapply_t** - Already exists  
✅ **objects_g** - Just created!  
✅ **o_g_tuple** - Just created!

## Recommended Implementation Order

### Phase 1: High Priority (Simple Filters)
These are straightforward conversions:

1. **colorfilter_t** - Filter tuple by color
   ```python
   def colorfilter_t(objs: Tuple, color: int) -> Tuple:
       return tuple(obj for obj in objs if obj[0][2] == color)
   ```

2. **sizefilter_t** - Filter tuple by size
   ```python
   def sizefilter_t(container: Tuple, n: int) -> Tuple:
       return tuple(item for item in container if len(item) == n)
   ```

3. **get_nth_t** - Get nth element from tuple
   ```python
   def get_nth_t(container: Tuple, rank: int) -> Any:
       return container[rank] if -len(container) <= rank < len(container) else ()
   ```

4. **get_arg_rank_t** - Get element by rank (already exists for Tuple!)
   - Check if this works for tuple of tuples

### Phase 2: Medium Priority (Set Operations)

5. **difference_t** - Tuple difference
   ```python
   def difference_t(a: Tuple, b: Tuple) -> Tuple:
       b_set = set(b)  # Use set for O(1) lookup
       return tuple(e for e in a if e not in b_set)
   ```

6. **remove_t** - Remove element from tuple
   ```python
   def remove_t(value: Any, container: Tuple) -> Tuple:
       return tuple(e for e in container if e != value)
   ```

### Phase 3: Low Priority (Already Have Variants)

7. **mapply_t** - Already exists!
8. **merge_t** - Already exists!

## Conversion Pattern for Solvers

### Example: solve_3618c87e
**Original (frozenset):**
```python
def solve_3618c87e(S, I, C):
    x1 = o_g(I, R5)           # frozenset
    x2 = sizefilter(x1, ONE)  # frozenset
    x3 = merge_f(x2)          # frozenset
    O = move(I, x3, TWO_BY_ZERO)
    return O
```

**Converted (tuple):**
```python
def solve_3618c87e_tuple(S, I, C):
    x1 = o_g_tuple(I, R5)        # tuple
    x2 = sizefilter_t(x1, ONE)   # tuple
    x3 = merge_t(x2)             # tuple
    O = move(I, x3, TWO_BY_ZERO)
    return O
```

### Example: solve_88a10436
**Original (frozenset):**
```python
def solve_88a10436(S, I, C):
    x1 = o_g(I, R1)
    x2 = colorfilter(x1, FIVE)
    x3 = difference(x1, x2)
    x4 = get_nth_f(x3, F0)
    ...
```

**Converted (tuple):**
```python
def solve_88a10436_tuple(S, I, C):
    x1 = o_g_tuple(I, R1)
    x2 = colorfilter_t(x1, FIVE)
    x3 = difference_t(x1, x2)
    x4 = get_nth_t(x3, F0)
    ...
```

## Implementation Strategy

### Step 1: Create Core Tuple Functions (High Priority)
Implement in `dsl.py`:
- colorfilter_t
- sizefilter_t  
- get_nth_t (or verify get_nth_by_key_t works)
- difference_t
- remove_t

### Step 2: Test on Simple Solvers
Start with the simplest solvers:
1. solve_3618c87e (5 lines, uses: o_g, sizefilter, merge_f)
2. solve_88a10436 (11 lines, uses: o_g, colorfilter, difference, get_nth_f)

### Step 3: Validate Correctness
- Run both frozenset and tuple versions
- Compare outputs (convert tuple→frozenset for comparison)
- Ensure 100% correctness

### Step 4: Benchmark Performance
- Profile CPU vs GPU versions
- Measure speedup on realistic grid sizes (>70 cells)
- Target: 2-3x speedup for simple solvers, 3-6x for complex

### Step 5: Scale to 20-50 Solvers
- Convert more solvers using the pattern
- Focus on solvers with mean grid size >100 cells
- Validate correctness on all

## Expected Outcomes

### Simple Solvers (5-10 lines)
- **Conversion effort:** LOW (replace 3-5 function calls)
- **Expected speedup:** 2-3x on grids >70 cells
- **Risk:** LOW (simple operations)

### Medium Solvers (10-20 lines)
- **Conversion effort:** MEDIUM (replace 5-10 function calls)
- **Expected speedup:** 3-5x on grids >100 cells
- **Risk:** MEDIUM (more complex chains)

### Complex Solvers (20+ lines)
- **Conversion effort:** HIGH (replace 10+ function calls)
- **Expected speedup:** 4-6x on grids >150 cells
- **Risk:** MEDIUM-HIGH (complex logic)

## Next Steps

1. ✅ **DONE:** Create objects_g and o_g_tuple
2. **TODO:** Implement Phase 1 functions (colorfilter_t, sizefilter_t, get_nth_t, difference_t, remove_t)
3. **TODO:** Test on solve_3618c87e and solve_88a10436
4. **TODO:** Validate 100% correctness
5. **TODO:** Benchmark on Kaggle
6. **TODO:** Scale to 20-50 solvers

## Estimated Timeline

- **Week 4 Day 1-2:** Implement Phase 1 functions (5 functions)
- **Week 4 Day 3:** Test on 2-3 simple solvers
- **Week 4 Day 4:** Validate correctness and benchmark
- **Week 4 Day 5-7:** Scale to 20-50 solvers

Total estimated time: **5-7 days** for 20-50 solver conversions

## Risk Assessment

### Low Risk
- ✅ Strategy validated on 8,616 grids
- ✅ 70-cell threshold proven optimal
- ✅ 65% of grids are GPU-friendly
- ✅ Simple operations (filters, indexing)

### Medium Risk
- ⚠️ Need to maintain 100% correctness
- ⚠️ Tuple ordering must match frozenset iteration
- ⚠️ Some functions may have edge cases

### Mitigation
- Test extensively on demo samples first
- Compare tuple vs frozenset outputs
- Add validation layer to catch mismatches
- Start with simplest solvers first
