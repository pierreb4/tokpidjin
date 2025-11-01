# DSL Type Consolidation - Detailed Implementation Plan

## Functions to Consolidate (100+ total)

### Tier 1: Critical Collection Operations (HIGHEST PRIORITY)
These are the most frequently used in solvers:

1. **apply** - _t, _f → single tuple version
2. **rapply** - _t, _f → single version  
3. **mapply** - _t, _f → single version
4. **papply** - (no _f variant yet)
5. **mpapply** - (no _f variant yet)
6. **prapply** - (no _f variant yet)
7. **sfilter** - _t, _f → single version
8. **mfilter** - _t, _f → single version
9. **merge** - _t, _f → single version
10. **combine** - _t, _f → single version
11. **first** - _t, _f → single version
12. **last** - _t, _f → single version
13. **remove** - _t, _f → single version
14. **other** - _t, _f → single version

### Tier 2: Selection/Ranking Operations
15. **get_nth** - _t, _f → single version
16. **get_nth_by_key** - _t, _f → single version
17. **get_arg_rank** - _t, _f → single version
18. **get_val_rank** - _t, _f → single version
19. **get_common_rank** - _t, _f → single version
20. **get_color_rank** - _t, _f (for Grid/Object)

### Tier 3: Statistical Operations
21. **size** - _t, _f → single version
22. **valmax** - _t, _f → single version
23. **valmin** - _t, _f → single version
24. **argmax** - _t, _f → single version
25. **argmin** - _t, _f → single version
26. **mostcommon** - _t, _f → single version
27. **leastcommon** - _t, _f → single version
28. **mostcolor** - _t, _f → single version
29. **leastcolor** - _t, _f → single version

### Tier 4: Geometric Operations
30. **height** - _t, _f, _i, _o → consolidate
31. **width** - _t, _f, _i, _o → consolidate
32. **shape** - _t, _f → single version
33. **palette** - _t, _f → single version
34. **square** - _t, _f → single version
35. **normalize** - _t, _i, _o → consolidate
36. **hmirror** - _t, _f, _i, _o → consolidate
37. **vmirror** - _t, _f, _i, _o → consolidate
38. **dmirror** - _t, _f, _i, _o → consolidate
39. **cmirror** - _t, _f, _i, _o → consolidate
40. **portrait** - _t, _f → single version
41. **colorcount** - _t, _f → single version

### Tier 5: Filter Operations  
42. **colorfilter** - _t (only)
43. **sizefilter** - _t (only)

### Tier 6: Special Cases
44. **p_f** - Return type changes (FrozenSet → Tuple)
45. **o_g_t** - Keep (Grid-specific)
46. **mir_rot_t/f** - Keep (semantics differ)
47. **initset** - Change return from frozenset({v}) to (v,)
48. **product** - Return FrozenSet → Tuple

## Implementation Strategy

### Phase 2A: Core Collection Operators (Tier 1)
Focus on most-used functions first. Each consolidation:
1. Delete _f variant
2. Keep _t variant but rename to base name
3. Update docstring
4. Update type annotations
5. Handle edge cases (empty containers)

### Phase 2B: Selection/Ranking (Tier 2)
Same process as 2A

### Phase 2C: Statistics (Tier 3)  
Same process

### Phase 2D: Geometric (Tier 4)
May need special handling for different input types

### Phase 2E: Filters & Special (Tier 5-6)
Handle as needed

## Files to Update After dsl.py Consolidation

1. **solvers_pre.py** - Replace _f calls with non-suffixed versions
2. **constants.py** - Update HINT_OVERLAPS 
3. **card.py** - Update type handling
4. **Any test files**

## Validation Steps

1. Compile dsl.py
2. Run solvers_pre.py solver (check correctness)
3. Verify no performance regression
4. Update solvers_pre.py to use new API
5. Re-validate solvers work correctly

---

## Notes

- Total functions to modify: 100+
- Lines to remove: ~2000
- Estimated time: 3-4 hours for full implementation
- Best approach: Automated script + manual review
