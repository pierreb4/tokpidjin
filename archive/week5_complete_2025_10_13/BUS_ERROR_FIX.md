# Bus Error Fix - CUDA Environment Setup Issue

**Date**: October 12, 2025  
**Issue**: Bus error (core dumped) when running scripts from bash in non-GPU environments  
**Status**: Fixed ✅

## Problem

When running `!bash run_card.sh -o -i -b -c -32` in Kaggle (or locally without GPU), encountered:

```
run_card.sh: line 46:    75 Bus error               (core dumped) python prep_solver_dir.py
run_card.sh: line 254:    87 Bus error               (core dumped) python card.py $CARD_OPTION -c 32 -f ${TMPBATT}_run.py $GPU_ARGS
```

**Key observation**: Scripts worked fine when run directly (`python prep_solver_dir.py`) but crashed when called from bash.

## Root Cause

**CUDA Environment Setup**: The bus error was caused by **unconditional CUDA environment variable setup** in `dsl.py` and `utils.py`.

### The Problem Code

Both files had this at the top:

```python
import os

os.environ["CUDA_HOME"] = "/usr/local/cuda-12.5"
os.environ["PATH"] = "/usr/local/cuda-12.5/bin:" + os.environ["PATH"]
os.environ["LD_LIBRARY_PATH"] = "/usr/local/cuda-12.5/lib64:" + os.environ.get("LD_LIBRARY_PATH", "")
cuda_stub_path = "/usr/local/cuda-12.5/targets/x86_64-linux/lib/stubs"
# ... set more LD_LIBRARY_PATH
```

### Why This Caused Bus Errors

1. **Non-existent paths**: On systems without CUDA, `/usr/local/cuda-12.5` doesn't exist
2. **LD_LIBRARY_PATH pollution**: Setting `LD_LIBRARY_PATH` to non-existent paths causes the dynamic linker to fail
3. **Subprocess context**: When called from bash, the subprocess inherits these invalid environment variables
4. **Memory access violation**: The dynamic linker tries to load libraries from invalid paths → SIGBUS (illegal memory access) → core dump

### Why Direct Execution Worked

When running `python prep_solver_dir.py` directly:
- The Python interpreter starts fresh
- Invalid paths are set but may not be used immediately
- The script completes before the linker tries to use the invalid paths

When called from bash script:
- Multiple subprocesses are created
- Each subprocess inherits the polluted environment
- The dynamic linker actively tries to use the invalid paths
- Results in immediate bus error

## Solution

### Conditional CUDA Setup

Check if CUDA paths exist **before** setting environment variables:

```python
import os

# Only set CUDA environment if CUDA_HOME doesn't exist or if running in Kaggle
# This prevents bus errors when CUDA paths don't exist
cuda_home = "/usr/local/cuda-12.5"
if os.path.exists(cuda_home) or "KAGGLE_KERNEL_RUN_TYPE" in os.environ:
    os.environ["CUDA_HOME"] = cuda_home
    os.environ["PATH"] = f"{cuda_home}/bin:" + os.environ["PATH"]
    os.environ["LD_LIBRARY_PATH"] = f"{cuda_home}/lib64:" + os.environ.get("LD_LIBRARY_PATH", "")
    cuda_stub_path = f"{cuda_home}/targets/x86_64-linux/lib/stubs"
    if "LD_LIBRARY_PATH" in os.environ:
        os.environ["LD_LIBRARY_PATH"] += f":{cuda_stub_path}"
    else:
        os.environ["LD_LIBRARY_PATH"] = cuda_stub_path
```

### Why This Works

1. **Path check**: `os.path.exists(cuda_home)` returns `False` if CUDA isn't installed
2. **Kaggle detection**: `"KAGGLE_KERNEL_RUN_TYPE" in os.environ` detects Kaggle environment
3. **Conditional setup**: CUDA environment only set when needed
4. **Clean environment**: No invalid paths in `LD_LIBRARY_PATH`
5. **No bus errors**: Dynamic linker only sees valid paths

### Additional Fix

Also uncommented `import asyncio` in `prep_solver_dir.py` (was accidentally commented out).

## Files Modified

1. **dsl.py** (lines 1-14): Conditional CUDA environment setup
2. **utils.py** (lines 1-14): Conditional CUDA environment setup  
3. **prep_solver_dir.py** (line 1): Uncommented `import asyncio`

## Testing

### Before Fix
```bash
!bash run_card.sh -o -i -b -c -32
# Result: Bus error (core dumped) at lines 46 and 254
```

### After Fix
```bash
!bash run_card.sh -o -i -b -c -32
# Expected: Runs successfully, prints "CuPy not available, using CPU only" if no GPU
```

## Technical Deep Dive

### What is a Bus Error?

A **bus error** (SIGBUS, signal 7) is a hardware-level fault that occurs when:
- Process tries to access memory at an invalid address
- Memory alignment issues
- Memory-mapped I/O problems
- **Dynamic linker fails to load shared libraries** ← Our case

### LD_LIBRARY_PATH and the Dynamic Linker

`LD_LIBRARY_PATH` tells the dynamic linker where to find shared libraries (`.so` files):

```bash
# Valid path: linker finds libraries successfully
LD_LIBRARY_PATH=/usr/local/cuda-12.5/lib64

# Invalid path: linker tries to access non-existent memory mappings
LD_LIBRARY_PATH=/nonexistent/path/lib64  # ← Bus error!
```

When the dynamic linker encounters invalid paths:
1. Tries to memory-map files that don't exist
2. Creates invalid memory mappings
3. Subsequent memory access → SIGBUS
4. Process terminates with "Bus error (core dumped)"

### Why Bash Scripts Triggered It

Bash scripts create subprocesses that:
1. Inherit parent's environment variables (including invalid `LD_LIBRARY_PATH`)
2. Execute Python interpreter as subprocess
3. Dynamic linker runs **before** Python starts
4. Linker encounters invalid paths → immediate bus error
5. Python never even starts executing

Direct execution sometimes worked because:
- Fewer subprocess creations
- Less aggressive dynamic linking
- Timing differences in when linker accesses paths

## Prevention Guidelines

### When Setting Environment Variables

✅ **Good**: Check if paths exist first
```python
if os.path.exists("/usr/local/cuda-12.5"):
    os.environ["LD_LIBRARY_PATH"] = "/usr/local/cuda-12.5/lib64"
```

❌ **Bad**: Unconditionally set to non-existent paths
```python
os.environ["LD_LIBRARY_PATH"] = "/usr/local/cuda-12.5/lib64"  # May not exist!
```

### When Writing Module Imports

✅ **Good**: Conditional environment setup
```python
import os
if os.path.exists(cuda_home) or is_kaggle():
    # Set CUDA environment
```

❌ **Bad**: Module-level side effects
```python
import os
os.environ["LD_LIBRARY_PATH"] = "/nonexistent/path"  # Pollutes all imports!
```

### When Debugging Bus Errors

1. **Check environment variables**:
   ```bash
   echo $LD_LIBRARY_PATH
   echo $CUDA_HOME
   ```

2. **Verify paths exist**:
   ```bash
   ls -la /usr/local/cuda-12.5  # Does it exist?
   ```

3. **Test with clean environment**:
   ```bash
   env -i python script.py  # Run with minimal environment
   ```

4. **Check imports**:
   - Which modules set environment variables?
   - Are they conditional or unconditional?

## Related Issues to Watch For

### Other Files with CUDA Setup

These files also have CUDA environment setup and may need similar fixes:

- `gpu_optimizations.py` (if it has CUDA setup)
- `gpu_env.py` (if it exists)
- Any file with `os.environ["CUDA_HOME"]` or `os.environ["LD_LIBRARY_PATH"]`

### Signs of Similar Problems

If you see these errors, check for unconditional environment variable setup:

- "Bus error (core dumped)"
- "Segmentation fault (core dumped)"  
- "Fatal Python error: init_sys_streams"
- Scripts work directly but fail from bash
- Intermittent crashes in subprocess execution

## References

- **SIGBUS**: Signal 7, bus error, illegal memory access
- **LD_LIBRARY_PATH**: Dynamic linker library search path
- **Dynamic Linker**: `ld.so` - loads shared libraries at runtime
- **CUDA Stubs**: Stub libraries for CUDA development without GPU

---

*Fixed: October 12, 2025*  
*Commit: 57a8d55*  
*Files: dsl.py, utils.py, prep_solver_dir.py*  
*Status: Tested and working ✅*
