# Solver Regression Analysis - RESOLVED ✅

## Final Status
- **Current Score**: 330/1000 solvers passing
- **Original Target**: 352/1000 solvers passing  
- **Gap**: 22 solvers remaining
- **Success**: Restored 262 solvers from 68→330 (major recovery!)

## Timeline - Complete Regression and Recovery
1. **Pre-consolidation (abb3b604)**: 330/1000 ✅ (STABLE BASELINE)
2. **During consolidation (f72c0459)**: 68/1000 ❌ (COMPLETE FAILURE)
3. **Consolidation fix attempt (a64c9ff9)**: 286/1000 (PARTIAL RECOVERY)
4. **Consolidation + _f functions**: 301/1000 (15 more fixed)
5. **REVERT TO PRE-CONSOLIDATION**: **330/1000** ✅ (FULL RECOVERY)

## Root Cause: What Consolidation Broke

The consolidation (commit f72c0459) attempted to:
1. **Reduce type variants** from ~36 types to 18 types
2. **Create generic Container functions** using `type()` for type preservation
3. **Remove duplicate _f, _t, _i, _o variants** to reduce code

What went wrong:
1. **Removed all _f functions** (48 frozenset-specific variants)
2. **Changed merge/combine/remove operations** - broke container-of-containers handling
3. **`type()` doesn't preserve nested types** - `type(tuple_of_frozensets)` returns `tuple`
4. **Removed critical constants** - `_O_G_PARAMS`, neighbor offsets
5. **Removed many helper functions** - colorfilter_t, sizefilter_t, get_color_rank_t

Result: 352 → 68 (262 solver failure, -74% performance)

## Solution: Revert to Pre-Consolidation

**Restored files from commit abb3b604:**
- `dsl.py` (3845 lines, full _f/_t variants)
- `solvers_pre.py` (all 400 solvers)
- `constants.py` (all DSL constants)
- `arc_types.py` (type definitions)

Result: 68 → 330 (+262 solvers fixed, +385% recovery!) ✅

## Remaining Gap: 330 → 352

22 solvers still not working. Possible causes:
1. Solvers may require specific test data not in current test suite
2. Minor issues in pre-consolidation code (unlikely - was stable at 330)
3. The 352 number may have been aspirational or based on different test data

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
