# Phase 2 Analysis: DSL Bottleneck Deep Dive

## Top Bottlenecks Analysis

### 1. mapply_t (2.148s, 4.0%)

**Current Implementation**:
```python
def mapply_t(
    function: 'Callable',
    container: 'Tuple'
) -> 'Tuple':
    """ apply and merge for tuples"""
    return merge_t(apply_t(function, container))

def apply_t(
    function: 'Callable',
    container: 'Tuple'
) -> 'Tuple':
    """ apply function to each item in tuple """
    return tuple(function(e) for e in container)

def merge_t(
    containers: 'ContainerContainer'
) -> 'Container':
    """ merging """
    return type(containers)(e for c in containers for e in c)
```

**What it does**:
1. `apply_t`: Applies function to each element → returns tuple of results
2. `merge_t`: Flattens nested containers → merges all elements into one tuple

**Performance characteristics**:
- Called 700 times in 100 tasks
- ~3.07ms per call
- Composed of two operations: apply_t + merge_t
- Lots of tuple creation/destruction overhead

**Optimization opportunities**:

1. **Eliminate intermediate tuple** (Quick win):
   ```python
   def mapply_t_optimized(function, container):
       """Combined apply and merge - no intermediate tuple"""
       return tuple(e for item in container for e in function(item))
   ```
   - Saves one tuple allocation per call
   - Expected: 10-20% speedup (0.2-0.4s)

2. **Vectorize when possible** (Medium effort):
   - Detect if function is vectorizable
   - Process multiple items at once
   - Expected: 20-30% speedup if commonly vectorizable

3. **Cache results** (Medium effort):
   - Add LRU cache for pure functions
   - Check if function+container seen before
   - Expected: 30-50% speedup if high reuse

### 2. apply_t (2.106s, 3.9%)

**Current Implementation**:
```python
def apply_t(
    function: 'Callable',
    container: 'Tuple'
) -> 'Tuple':
    """ apply function to each item in tuple """
    return tuple(function(e) for e in container)
```

**What it does**:
- Maps function over tuple elements
- Returns new tuple with results

**Performance characteristics**:
- Called 700 times in 100 tasks
- ~3.01ms per call
- Simple but frequent

**Optimization opportunities**:

1. **Use list comprehension + tuple()** (Quick win):
   ```python
   def apply_t_optimized(function, container):
       """Slightly faster with list comprehension"""
       return tuple([function(e) for e in container])
   ```
   - List comprehension can be faster than generator
   - Expected: 5-10% speedup (0.1-0.2s)

2. **Parallel execution for expensive functions** (High effort):
   - Use multiprocessing for long-running functions
   - Only worth it if function takes >10ms
   - Expected: 2-4x speedup if parallelizable

3. **Memoization** (Medium effort):
   - Cache (function, element) → result mappings
   - Works best if same elements seen repeatedly
   - Expected: 20-40% speedup if high reuse

### 3. o_g (1.430s, 2.7%)

**Current Implementation**:
```python
def o_g(grid: 'Grid', type: 'R8') -> 'Objects':
    if type == 0:
        return objects(grid, False, False, False)
    elif type == 1:
        return objects(grid, False, False, True)
    # ... 6 more branches
```

**What it does**:
- Dispatcher function for `objects()` with different parameters
- Type encodes three boolean flags (univalued, diagonal, without_bg)
- Total: 8 different combinations (0-7)

**Performance characteristics**:
- Called 3,400 times in 100 tasks
- ~0.42ms per call
- Most time is in the `objects()` call itself

**Optimization opportunities**:

1. **Replace if-elif chain with array lookup** (Quick win):
   ```python
   # Pre-computed lookup table
   O_G_PARAMS = [
       (False, False, False),  # type 0
       (False, False, True),   # type 1
       (False, True, False),   # type 2
       (False, True, True),    # type 3
       (True, False, False),   # type 4
       (True, False, True),    # type 5
       (True, True, False),    # type 6
       (True, True, True),     # type 7
   ]
   
   def o_g_optimized(grid, type):
       params = O_G_PARAMS[type]
       return objects(grid, *params)
   ```
   - Eliminates 7 branches per call
   - Expected: 10-15% speedup on o_g (0.1-0.2s)

2. **GPU acceleration** (High effort):
   - Implement hybrid GPU strategy from GPU_O_G_IMPLEMENTATION.md
   - Complex flood-fill algorithm on GPU
   - Expected: 2-4x speedup based on benchmarks
   - **Note**: This is the main target from previous GPU work

### 4. objects (1.374s, 2.6%)

**Current Implementation**:
```python
def objects(grid, univalued, diagonal, without_bg):
    """objects occurring on the grid"""
    # Flood-fill algorithm to find connected components
    bg = mostcolor_t(grid) if without_bg else None
    objs = set()
    occupied = set()
    h, w = len(grid), len(grid[0])
    unvisited = asindices(grid)
    diagfun = neighbors if diagonal else dneighbors
    
    for loc in unvisited:
        if loc in occupied:
            continue
        val = grid[loc[0]][loc[1]]
        if val == bg:
            continue
        obj = {(loc[0], loc[1], val)}
        cands = {loc}
        while cands:
            neighborhood = set()
            for cand in cands:
                v = grid[cand[0]][cand[1]]
                if (val == v) if univalued else (v != bg):
                    obj.add((cand[0], cand[1], v))
                    occupied.add(cand)
                    neighborhood |= {
                        (i, j) for i, j in diagfun(cand) if 0 <= i < h and 0 <= j < w
                    }
            cands = neighborhood - occupied
        objs.add(frozenset(obj))
    return frozenset(objs)
```

**What it does**:
- Finds connected components (objects) in a grid
- Uses flood-fill algorithm
- Handles different connectivity rules (4-way, 8-way, uni-valued, etc.)

**Performance characteristics**:
- Called 3,400 times in 100 tasks
- ~0.40ms per call
- Complex algorithm with many set operations
- Most expensive DSL operation

**Optimization opportunities**:

1. **Use lists instead of sets during construction** (Quick win):
   ```python
   def objects_optimized(grid, univalued, diagonal, without_bg):
       # ... setup same ...
       objs = []  # Use list instead of set
       occupied = set()  # Keep set for membership testing
       
       for loc in unvisited:
           # ... flood fill logic ...
           obj = []  # Use list during construction
           # ... collect cells ...
           objs.append(frozenset(obj))  # Convert to frozenset at end
       return frozenset(objs)
   ```
   - List append faster than set add
   - Only convert to frozenset at the end
   - Expected: 10-15% speedup (0.1-0.2s)

2. **Optimize neighborhood calculation** (Medium effort):
   - Pre-compute neighbor offsets
   - Use array indexing instead of set comprehension
   - Cache diagfun lookup
   - Expected: 15-20% speedup (0.2-0.3s)

3. **Early termination** (Quick win):
   - Skip empty grids faster
   - Return early if no objects found
   - Expected: 5-10% speedup (0.05-0.1s)

4. **GPU acceleration** (High effort):
   - Implement parallel flood-fill on GPU
   - Complex but potentially high payoff
   - Expected: 2-4x speedup for large grids

### 5. apply (1.279s, 2.4%)

**Current Implementation**:
```python
def apply(function, container):
    """apply function to each element"""
    return type(container)(function(e) for e in container)
```

**What it does**:
- Generic apply function for any container type
- Maps function over elements

**Performance characteristics**:
- Called 7,772 times in 100 tasks (highest call count!)
- ~0.16ms per call (fastest per-call time)
- High frequency suggests it's used for small operations

**Optimization opportunities**:

1. **Inline for common cases** (Quick win):
   ```python
   # Specialized versions
   def apply_tuple(function, container):
       return tuple(function(e) for e in container)
   
   def apply_frozenset(function, container):
       return frozenset(function(e) for e in container)
   ```
   - Avoid type() call overhead
   - Expected: 5-10% speedup (0.05-0.1s)

2. **Batch small operations** (Medium effort):
   - Group multiple apply calls
   - Process in one pass
   - Expected: 10-20% speedup if batching is common

## Quick Win Summary

Low-hanging fruit that can be implemented in 1-2 days:

| Optimization | Target | Expected Speedup | Time | Lines of Code |
|--------------|--------|------------------|------|---------------|
| mapply_t: eliminate intermediate | 2.148s | 10-20% (0.2-0.4s) | 1 hour | 5 lines |
| o_g: array lookup | 1.430s | 10-15% (0.1-0.2s) | 30 min | 15 lines |
| objects: use lists | 1.374s | 10-15% (0.1-0.2s) | 1 hour | 10 lines |
| apply_t: list comprehension | 2.106s | 5-10% (0.1-0.2s) | 30 min | 3 lines |
| **Total Quick Wins** | **7.058s** | **~15-20%** (1.0-1.4s) | **3-4 hours** | **~30 lines** |

**Expected result after quick wins**: 6.64s → 5.2-5.6s for 100 tasks

## Medium Effort Optimizations (Week 1)

| Optimization | Target | Expected Speedup | Time | Complexity |
|--------------|--------|------------------|------|------------|
| objects: optimize neighborhood | 1.374s | 15-20% (0.2-0.3s) | 4-6 hours | Medium |
| mapply_t/apply_t: memoization | 4.254s | 20-30% (0.8-1.3s) | 1-2 days | Medium |
| Batch processing | Various | 10-15% (0.5-0.8s) | 2-3 days | High |
| **Total Medium Effort** | | **~30-40%** (1.5-2.4s) | **1 week** | |

**Expected result after Week 1**: 5.2-5.6s → 3.8-4.6s for 100 tasks

## High Effort Optimizations (Week 2-3)

| Optimization | Target | Expected Speedup | Time | Complexity |
|--------------|--------|------------------|------|------------|
| GPU o_g + objects | 2.804s | 2-4x (1.4-2.1s) | 1-2 weeks | Very High |
| Parallel apply_t | 2.106s | 2-3x (0.7-1.4s) | 3-5 days | High |
| **Total High Effort** | | **2-3x** (2.1-3.5s) | **2-3 weeks** | |

**Expected result after Weeks 2-3**: 3.8-4.6s → 1.3-2.5s for 100 tasks

## Recommendation: Staged Approach

### Stage 1: Quick Wins (Day 1)
1. Implement all 4 quick win optimizations
2. Test locally
3. Deploy to Kaggle
4. Profile and validate
5. **Expected**: 6.64s → 5.2-5.6s (1.2-1.3x)

### Stage 2: Medium Effort (Days 2-5)
1. Add memoization to mapply_t/apply_t
2. Optimize objects neighborhood calculation
3. Profile and measure
4. **Expected**: 5.2-5.6s → 3.8-4.6s (1.2-1.4x additional)

### Stage 3: Evaluate GPU Need (Day 6)
- If at 3.8-4.6s: **Consider GPU** (may not be needed!)
- If at >4.6s: **Definitely do GPU** (needed for target)
- Target: 2.5-3.5s (2-3x from Phase 1 baseline)

## Next Steps

1. ✅ **Archive old docs and scripts** (DONE)
2. ✅ **Create Phase 2 plan and analysis** (DONE)
3. 🔄 **Implement Stage 1 quick wins** (NEXT)
4. ⏳ **Deploy and validate on Kaggle**
5. ⏳ **Stage 2: Medium effort optimizations**
6. ⏳ **Stage 3: Evaluate GPU acceleration**

---

**Status**: Analysis complete, ready for implementation  
**Next action**: Implement Stage 1 quick wins  
**Target**: 6.64s → 5.2-5.6s (Day 1 goal)
