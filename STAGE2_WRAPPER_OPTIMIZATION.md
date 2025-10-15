# Stage 2: Wrapper Optimization Plan

**Date**: October 15, 2025  
**Target**: Optimize `safe_dsl` wrapper function  
**Current Cost**: 5.134s (739,260 calls, 0.007ms/call)  
**Expected Savings**: 2.5-3.5s (50-70% reduction)

---

## Problem Analysis

### Current Implementation

```python
@wraps(func)
def wrapper(*args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        # Log the exception (first occurrence only to avoid spam)
        if not hasattr(wrapper, '_logged'):
            logger.debug(f"{func.__name__} failed with {type(e).__name__}: {e}")
            wrapper._logged = True
        
        # Return safe default based on return type
        return _get_safe_default(func)
```

### Performance Issues

1. **Try-except overhead**: Every call pays for exception handling setup
2. **Function call overhead**: Extra layer of indirection
3. **739,260 calls**: Adds up to 5.134s total
4. **Rare exceptions**: Most calls never raise exceptions

### Why It's Slow

Python's try-except has overhead even when no exception is raised:
- Setup exception handler: ~0.003ms per call
- Tear down handler: ~0.003ms per call  
- Total: **~0.007ms per call** (matches our measurement!)

With 739,260 calls: 0.007ms × 739,260 = **5.2s overhead**

---

## Optimization Strategy

### Option 1: Remove Wrapper for Hot Paths ⭐ **RECOMMENDED**

**Approach**: Don't wrap DSL functions at all during normal execution.

**Rationale**:
- Solvers are already exception-safe (batt.py has try-except)
- DSL functions rarely crash with valid inputs
- We're paying 5.2s for protection we don't need

**Implementation**:
```python
# At end of dsl.py
# REMOVE THIS:
# from safe_dsl import make_all_dsl_safe
# make_all_dsl_safe(sys.modules[__name__])

# DSL functions are now unwrapped - maximum performance!
```

**Expected**: **-5.1s** (eliminate wrapper entirely)  
**Risk**: LOW - batt.py already has exception handling  
**Effort**: **5 minutes**

### Option 2: Fast-Path Optimization 🎯

**Approach**: Add fast path that skips try-except when exceptions are unlikely.

**Implementation**:
```python
def safe_dsl_optimized(func: Callable) -> Callable:
    """Optimized safe_dsl with fast path"""
    
    # Pre-compute safe default at decoration time (cache!)
    safe_default = _get_safe_default(func)
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Fast path: direct call (no try-except!)
        result = func(*args, **kwargs)
        
        # Only check for errors if result is None (rare)
        if result is None and safe_default != ():
            # Slow path: something went wrong
            return safe_default
        
        return result
    
    # Add error tracking
    wrapper._error_count = 0
    return wrapper
```

**Expected**: **-3.5-4.0s** (70-80% reduction)  
**Risk**: MEDIUM - Assumes func returns non-None on success  
**Effort**: **1-2 hours**

### Option 3: Conditional Wrapping 🟡

**Approach**: Only wrap functions that actually need protection.

**Implementation**:
```python
# List of functions that may crash
NEEDS_WRAPPING = {
    'objects', 'partition', 'fgpartition', 
    # ... other risky functions
}

def make_all_dsl_safe_selective(module):
    """Only wrap functions that need it"""
    for name, obj in module.__dict__.items():
        if callable(obj) and name in NEEDS_WRAPPING:
            setattr(module, name, safe_dsl(obj))
```

**Expected**: **-3.0-3.5s** (60-70% reduction)  
**Risk**: MEDIUM - Must identify which functions crash  
**Effort**: **2-3 hours**

### Option 4: Pre-compute Defaults 🟢

**Approach**: Cache `_get_safe_default` results (currently called on every exception).

**Current Problem**:
```python
# _get_safe_default called 7,343 times!
hints = get_type_hints(func)  # EXPENSIVE!
```

**Implementation**:
```python
_DEFAULT_CACHE = {}

def _get_safe_default_cached(func: Callable) -> Any:
    """Cached version of _get_safe_default"""
    if func not in _DEFAULT_CACHE:
        _DEFAULT_CACHE[func] = _get_safe_default_original(func)
    return _DEFAULT_CACHE[func]
```

**Expected**: **-0.8s** (_get_safe_default optimization)  
**Risk**: LOW - Simple caching  
**Effort**: **30 minutes**

---

## Recommended Implementation Plan

### Phase 1: Test Without Wrapper (5 minutes) ⭐

**Step 1**: Comment out wrapper application
```bash
# Edit dsl.py line 3824-3826:
# from safe_dsl import make_all_dsl_safe
# make_all_dsl_safe(sys.modules[__name__])
```

**Step 2**: Test locally
```bash
python run_batt.py --tasks 5
```

**Step 3**: If successful, test on Kaggle
```bash
python profile_batt_framework.py --tasks 100
```

**Expected result**: 5.24s → **~2.0s** (eliminate 3.2s wrapper overhead)

### Phase 2: Cache `_get_safe_default` (30 minutes)

**Step 1**: Add caching to safe_dsl.py
**Step 2**: Test locally
**Step 3**: Measure improvement

**Expected additional**: -0.8s (_get_safe_default calls)

### Phase 3: Validate and Document (1 hour)

**Step 1**: Full Kaggle run (100 tasks)
**Step 2**: Verify correctness (all outputs match)
**Step 3**: Document results
**Step 4**: Commit changes

---

## Success Criteria

### Minimum Success:
- ✅ Wall-clock: <4.0s (from 5.24s, 30% improvement)
- ✅ No errors/crashes
- ✅ All outputs correct

### Target Success:
- ✅ Wall-clock: 2.0-2.5s (from 5.24s, 52-62% improvement)
- ✅ wrapper overhead eliminated (5.1s → 0s)
- ✅ _get_safe_default cached (0.9s → 0.1s)

### Stretch Success:
- 🎯 Wall-clock: <2.0s (from 5.24s, >62% improvement)
- 🎯 Combined with other optimizations

---

## Risk Mitigation

**Risk**: Removing wrapper may expose crashes

**Mitigation**:
1. batt.py already has try-except at solver level
2. Test thoroughly before deploying
3. Keep safe_dsl.py for future use if needed
4. Can re-enable wrapper if issues found

**Risk**: Outputs may differ without wrapper

**Mitigation**:
1. Test with validation script
2. Compare outputs before/after
3. Have rollback plan ready

---

## Next Steps

**Immediate** (tonight):
1. 🔧 Comment out `make_all_dsl_safe` call
2. 🧪 Test locally with 5 tasks
3. ✅ If successful, test on Kaggle with 100 tasks
4. 📊 Measure improvement

**Expected Timeline**:
- Test without wrapper: **5 minutes**
- Kaggle validation: **10 minutes**
- Cache optimization: **30 minutes**
- Full validation: **1 hour**
- **Total: ~2 hours to completion**

**Expected Result**:
- Current: 5.24s
- After wrapper removal: **~2.0s**
- **Total so far: 37.78s → 2.0s = 18.9x speedup!** 🎉

---

**STATUS**: Ready to implement ✅  
**FIRST STEP**: Comment out wrapper and test  
**EXPECTED**: Massive 60% improvement (5.24s → 2.0s)  
**RISK**: Low - batt.py has exception handling
