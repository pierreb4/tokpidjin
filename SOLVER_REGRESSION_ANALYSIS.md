# Solver Regression Analysis

## Current Status
- **Current Score**: 301/1000 solvers passing
- **Target Score**: 352/1000 solvers passing  
- **Regression**: 51 solvers still failing

## Timeline
1. **Original state (before consolidation)**: 352/1000 ✅
2. **After consolidation broke it**: 68/1000 ❌
3. **After consolidation fix (commit a64c9ff9)**: 286/1000 (partial recovery)
4. **After adding _f functions**: 301/1000 (15 more solvers fixed)

## Root Cause Analysis

### Issue 1: Missing _f Functions (FIXED ✅)
- **Problem**: Consolidation removed 48 frozenset-specific (_f) variants
- **Symptoms**: NameError for `palette_f`, `mir_rot` 
- **Solution**: Added 5 critical _f functions (p_f, palette_f, mir_rot_f, get_nth_f, get_nth_by_key_f)
- **Impact**: Fixed 15 solvers (286 → 301)

### Issue 2: Type Preservation in Container Operations (PARTIALLY FIXED ✅)
- **Problem**: `merge()` uses `type(containers)` which returns tuple type instead of frozenset when given (frozenset, frozenset)
- **Example**: `merge((frozenset([1,2]), frozenset([3,4])))` returns `(1,2,3,4)` instead of `frozenset({1,2,3,4})`
- **Solution**: Added frozenset detection in merge()
- **Status**: Fix applied but may not have resolved all failures

### Issue 3: Unknown Behavioral Differences (NOT YET FIXED ❌)
- **Remaining**: 51 solvers still failing despite above fixes
- **Likely Causes**:
  1. Other container operations with type preservation issues (combine, remove, sfilter, etc.)
  2. Subtle logic changes in consolidated versions of DSL functions
  3. Functions that should return frozensets but return tuples (or vice versa)
  4. Edge cases in type preservation for nested containers

## Investigation Findings

### Solvers using _t functions (from solvers_pre.py)
Most frequently used:
- `o_g_t`: 237 occurrences - returns tuple of tuples
- `mapply_t`: 185 occurrences
- `mir_rot_t`: 119 occurrences
- `get_nth_t`: 93 occurrences
- `get_arg_rank_t`: 79 occurrences
- `merge_t`: 60 occurrences
- `colorfilter_t`: 58 occurrences
- `get_color_rank_t`: 56 occurrences

### Functions with Type Preservation Issues
Candidates for investigation:
1. `merge()` - Fixed, but may not cover all cases
2. `combine()` - Uses `type(a)` pattern, may need similar fix
3. `remove()` - Operates on containers
4. `sfilter()` - Operates on containers  
5. `rapply()` - Applies function to container
6. `mapply()` - Maps function over container

## Comparison: Original vs Consolidated

### Original (dsl_arc.py)
- 160 functions total
- Single function per operation
- Explicit frozenset/tuple handling

### Consolidated (dsl.py)
- 261 functions total
- Added _t, _f, _i, _o variants for type specialization
- Generic Container-based functions with type preservation via `type()`
- Consolidated from ~36 types to 18 types

## Next Steps to Reach 352

### High Priority (likely to fix multiple solvers)
1. **Audit container operations** - Check all functions using `type(container)` pattern
   - Ensure frozensets return frozensets
   - Ensure tuples return tuples
   - Add frozenset detection similar to merge() fix

2. **Add missing _f function variants** - Extract remaining 40+ _f functions from git history
   - Currently only have 5 critical ones
   - Others may be called by internal DSL operations
   - File: `/tmp/f_functions.py` was partially generated

3. **Test with original dsl_arc.py logic** - Verify if specific functions should use different logic
   - Identify functions where consolidation changed semantics
   - May need to revert some functions to original implementation

### Medium Priority
1. Review test data - Understand what the 51 failing solvers are actually testing
2. Profile execution - Identify which DSL operations are bottlenecks
3. Check for empty container edge cases - May fail in min/max operations

### Testing Strategy
1. Create minimal test case that reproduces the 51-solver regression
2. Isolate which DSL function(s) are causing the issue
3. Compare implementation between dsl_arc.py and dsl.py for that function
4. Apply targeted fix

## Files
- `dsl_arc.py` - Original single-version DSL (1524 lines, 160 functions)
- `dsl.py` - Consolidated DSL with variants (3244 lines, 261 functions)
- `dsl_current.py` - Current working version with _f functions
- `_f_functions.txt` - Partially extracted _f functions from git history

## Key Insight
The consolidation was too aggressive in relying on `type()` for type preservation.
Container-of-containers operations need special handling because:
- `type(tuple_of_frozensets)` returns `tuple`, not `frozenset`
- Generic functions can't always preserve both structure and element types simultaneously
- Some operations fundamentally change cardinality (merge, combine, difference)
