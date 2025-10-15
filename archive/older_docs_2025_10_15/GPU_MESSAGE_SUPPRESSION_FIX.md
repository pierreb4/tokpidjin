# GPU Message Suppression Fix

**Date**: October 14, 2025  
**Issue**: Unnecessary GPU warning messages when CPU mode explicitly requested  
**Status**: ✅ FIXED (commit b341324)

---

## Problem

When running `run_card.sh` with `-m` flag (force CPU mode), the following messages clutter the output:

```
run_batt.py:72: GPU Support: Disabled (CuPy not available)
CuPy not available, using CPU only
GPU not available - using CPU fallback
```

**Why This Is a Problem**:
- These messages are **expected** in CPU mode (not errors)
- User explicitly requested CPU mode with `-m` flag
- Messages add noise to logs when monitoring production
- Makes it harder to spot actual issues

---

## Solution

Implemented environment variable `EXPECT_GPU` to distinguish between:
1. **GPU expected but unavailable** (warning needed)
2. **CPU mode explicitly requested** (no warning needed)

### How It Works

**run_card.sh sets the expectation**:
```bash
# GPU mode (-g flag or auto-detected)
export EXPECT_GPU=1  # Show warnings if GPU unavailable

# CPU mode (-m flag)
export EXPECT_GPU=0  # Suppress warnings (expected behavior)
```

**Import sections check before printing**:
```python
# Only print warning if GPU was expected
if os.environ.get('EXPECT_GPU', '1') != '0':
    print("GPU unavailable message")
```

**Default behavior** (EXPECT_GPU not set):
- Assumes GPU might be expected → Shows warnings
- Preserves existing behavior for scripts run outside run_card.sh

---

## Files Modified

### 1. run_card.sh

**Lines 85-87** (GPU mode):
```bash
export EXPECT_GPU=1  # Signal that GPU is expected
```

**Lines 91** (CPU mode):
```bash
export EXPECT_GPU=0  # Signal that CPU mode is expected (no warnings needed)
```

### 2. run_batt.py

**Lines 70-75** (ImportError handler):
```python
except ImportError:
    GPU_AVAILABLE = False
    gpu_optimizer = None
    # Only print message if GPU was expected (not in forced CPU mode)
    if os.environ.get('EXPECT_GPU', '1') != '0':
        print_l("GPU Support: Disabled (CuPy not available)")
```

### 3. dsl.py

**Lines 34-38** (ImportError handler):
```python
except ImportError:
    GPU_AVAILABLE = False
    import numpy as np
    # Only print message if GPU was expected (not in forced CPU mode)
    import os
    if os.environ.get('EXPECT_GPU', '1') != '0':
        print("CuPy not available, using CPU only")
```

### 4. gpu_dsl_operations.py

**Lines 36-42** (ImportError handler):
```python
except ImportError:
    GPU_AVAILABLE = False
    cp = None
    # Only log warning if GPU was expected (not in forced CPU mode)
    import os
    if os.environ.get('EXPECT_GPU', '1') != '0':
        logger.warning("GPU not available - using CPU fallback")
```

---

## Testing

### Test 1: CPU Mode (Suppress Messages) ✅

**Command**:
```bash
EXPECT_GPU=0 python -c "import run_batt; import dsl; import gpu_dsl_operations"
```

**Expected Output**: No GPU warning messages  
**Result**: ✅ Pass (clean output)

### Test 2: GPU Expected (Show Warnings) ✅

**Command**:
```bash
EXPECT_GPU=1 python -c "import run_batt; import dsl; import gpu_dsl_operations"
```

**Expected Output**: 
```
CuPy not available, using CPU only
GPU not available - using CPU fallback
run_batt.py:74: GPU Support: Disabled (CuPy not available)
```
**Result**: ✅ Pass (warnings shown as expected)

### Test 3: Default Behavior (No EXPECT_GPU set) ✅

**Command**:
```bash
python -c "import run_batt; import dsl; import gpu_dsl_operations"
```

**Expected Output**: Same as Test 2 (warnings shown)  
**Result**: ✅ Pass (preserves existing behavior)

---

## Usage Examples

### With run_card.sh

**CPU Mode** (no GPU messages):
```bash
bash run_card.sh -o -c -32 -m
# Output: Clean, no GPU warnings ✓
```

**GPU Mode** (shows warnings if GPU unavailable):
```bash
bash run_card.sh -o -c -32 -g
# Output: Shows GPU warnings if CuPy not available ✓
```

**Auto-detect Mode** (default):
```bash
bash run_card.sh -o -c -32
# Output: Shows GPU warnings if GPU detected but CuPy unavailable ✓
```

### Direct Python Execution

**Suppress warnings**:
```bash
EXPECT_GPU=0 python run_batt.py -c -3
# No GPU messages
```

**Show warnings**:
```bash
EXPECT_GPU=1 python run_batt.py -c -3
# Shows GPU unavailable warnings
```

**Default** (no EXPECT_GPU):
```bash
python run_batt.py -c -3
# Shows GPU unavailable warnings (backward compatible)
```

---

## Design Decisions

### Why Environment Variable?

**Alternatives Considered**:
1. ❌ **Command-line flag**: Would need to pass through multiple scripts
2. ❌ **Config file**: Too heavy for simple on/off switch
3. ✅ **Environment variable**: 
   - Easy to set in run_card.sh
   - Inherited by all child processes
   - No code changes needed in intermediate scripts

### Why Default to Showing Warnings?

**Rationale**:
- Preserves existing behavior for scripts run outside run_card.sh
- Better to show unnecessary warning than hide important one
- Users running Python directly probably want to know about GPU availability

**Default behavior**:
```python
os.environ.get('EXPECT_GPU', '1')  # Default '1' = show warnings
```

### Why '0'/'1' String Values?

**Rationale**:
- Environment variables are always strings
- '0'/'1' is conventional (mimics boolean)
- Easy to check: `!= '0'` means "show warnings"

---

## Impact

### Before Fix

**Running**: `bash run_card.sh -o -c -32 -m`

**Output**:
```
Card.py: Generating standard batt for CPU
Timeout: 10.0s
Running: python run_batt.py -t 10.0 -c -32 -b tmp_batt_xxx
run_batt.py:72: GPU Support: Disabled (CuPy not available)  ← Noise
CuPy not available, using CPU only                            ← Noise
GPU not available - using CPU fallback                        ← Noise
-- Processing 32 tasks...
```

### After Fix

**Running**: `bash run_card.sh -o -c -32 -m`

**Output**:
```
Card.py: Generating standard batt for CPU
Timeout: 10.0s
Running: python run_batt.py -t 10.0 -c -32 -b tmp_batt_xxx
-- Processing 32 tasks...                                    ← Clean!
```

**Benefits**:
- ✅ Cleaner production logs
- ✅ Easier to spot actual issues
- ✅ Less cognitive load when monitoring
- ✅ Preserves warnings when GPU expected

---

## Related Issues

### Similar Warnings in Other Files

These files also have GPU unavailable messages but are **not modified** because:

1. **test_kaggle_gpu_optimized.py**: Test script, warnings are informative
2. **kaggle_gpu_benchmark.py**: Benchmark script, warnings expected
3. **validate_local.py**: Validation script, warnings useful
4. **gpu_env.py**: Environment check script, warnings are the point
5. **benchmark_gpu_solvers.py**: GPU-specific benchmark, warnings appropriate

**Principle**: Only suppress warnings when:
- User explicitly requested CPU mode (via `-m` flag)
- Warnings add noise without value
- Context is production/operational (not testing/debugging)

---

## Backward Compatibility

### Scripts Affected
- ✅ run_card.sh: Explicitly sets EXPECT_GPU
- ✅ Direct run_batt.py: Uses default behavior (shows warnings)
- ✅ Direct dsl.py import: Uses default behavior (shows warnings)
- ✅ Test scripts: Unaffected (no EXPECT_GPU set)

### Existing Workflows
- ✅ Kaggle submissions: Unaffected (no run_card.sh)
- ✅ Local testing: Unaffected (direct Python execution)
- ✅ CI/CD pipelines: Unaffected (no EXPECT_GPU set)
- ✅ Production: Improved (cleaner logs with -m flag)

**Migration Required**: None (fully backward compatible)

---

## Future Considerations

### Potential Enhancements

1. **Logging Levels**: Use proper logging levels (INFO vs WARNING)
   ```python
   if EXPECT_GPU:
       logger.warning("GPU expected but not available")
   else:
       logger.debug("GPU not available (CPU mode)")
   ```

2. **Explicit GPU Check Flag**: Add `--no-gpu-warnings` command-line flag
   ```bash
   python run_batt.py --no-gpu-warnings -c -32
   ```

3. **Structured Logging**: Use JSON for machine-readable logs
   ```python
   logger.info(json.dumps({
       "event": "gpu_check",
       "available": False,
       "expected": EXPECT_GPU,
       "mode": "CPU"
   }))
   ```

### Not Needed For Now

- Current solution is simple and effective
- Covers 95% of use cases
- Easy to understand and maintain
- Minimal code changes

---

## Summary

**Problem**: Unnecessary GPU warnings clutter logs in CPU mode  
**Solution**: Environment variable `EXPECT_GPU` to distinguish expected vs unexpected GPU unavailability  
**Impact**: Cleaner production logs, easier monitoring, better UX  
**Compatibility**: Fully backward compatible, no migration needed  

**Status**: ✅ Fixed and tested (commit b341324)

---

**Related Documentation**:
- WEEK6B_PRODUCTION_DEPLOYMENT_SUMMARY.md
- WEEK6B_THREAD_EXHAUSTION_FIX.md
- WEEK6B_PRODUCTION_MONITORING.md
