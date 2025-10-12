# Summary: Using _get_safe_default from safe_dsl.py

## Changes Made

Successfully refactored the mutation safety system to use the centralized `_get_safe_default()` function from `safe_dsl.py` instead of duplicating code in generated files.

## Files Modified

### 1. **safe_dsl.py** (lines 66-120)
- Updated `_get_safe_default()` to return `()` for `Any` and unknown types (was returning `None`)
- Updated to return `()` on exception (was returning `None`)
- Now provides consistent fallback behavior across all cases

### 2. **card.py** (lines 638-645)
- Removed duplicated `_safe_default()` function definition
- Changed from generating helper function to importing it:
  ```python
  from safe_dsl import _get_safe_default
  ```

### 3. **card.py** (line 229)
- Updated exception handler to use imported function:
  ```python
  t{self.t_num} = _get_safe_default({func_name})
  ```

### 4. **MUTATION_SAFETY.md**
- Updated documentation to reflect single source of truth
- Clarified that both layers use same function
- Updated type mapping table (added `Any/Unknown → ()`)
- Updated status section with correct line numbers

## Benefits

✅ **No code duplication** - Single implementation in `safe_dsl.py`  
✅ **Easier maintenance** - Update logic in one place  
✅ **Consistency guaranteed** - Both safety layers use identical function  
✅ **Cleaner generated code** - Just an import instead of 30-line function  
✅ **Same behavior** - All tests pass with centralized function  

## Type Mapping

| Return Type | Default Value | Example Functions |
|-------------|---------------|-------------------|
| FrozenSet types | `frozenset()` | `objects`, `o_g`, `indices` |
| Tuple types | `()` | `shape_t`, `IJ` |
| Integer types | `0` | `size`, `count_colors`, `width` |
| Boolean types | `False` | Boolean operations |
| Callable types | `lambda: ()` | `rbind`, `lbind` |
| **Any/Unknown** | **`()`** | `identity`, fallback ⭐ |

## Testing

All tests pass:
- ✅ `test_safe_default.py` - Tests `_get_safe_default()` with various DSL functions
- ✅ `test_generated_pattern.py` - Tests complete mutation safety pattern
- ✅ Validates type-aware defaults for all type categories
- ✅ Confirms no code duplication

## Next Steps

When you regenerate batch files (e.g., via `bash run_card.sh`), they will:
1. Import `_get_safe_default` from `safe_dsl.py`
2. Use it in all exception handlers
3. Get consistent type-aware defaults
4. Have cleaner, more maintainable code

## Architecture

```
safe_dsl.py
  ├─ _get_safe_default(func) → type-aware default
  │
  ├─ Used by @safe_dsl decorator (Layer 1)
  │   └─ Protects DSL function internals
  │
  └─ Imported by generated files (Layer 2)
      └─ Protects function calls in mutations
```

Both layers call the same function - single source of truth! 🎯
