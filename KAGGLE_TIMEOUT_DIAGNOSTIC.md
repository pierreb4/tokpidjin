# Kaggle Timeout Diagnostic

**Issue**: All batt() calls timing out at 10 seconds on Kaggle

## Problem Analysis

### What's Happening:
```
run_batt.py:398: -- 007bbfb7 - demo[0] timed out
run_batt.py:398: -- 007bbfb7 - demo[1] timed out
run_batt.py:398: -- 007bbfb7 - demo[2] timed out
run_batt.py:398: -- 007bbfb7 - demo[3] timed out
run_batt.py:398: -- 007bbfb7 - demo[4] timed out
run_batt.py:568: -- 007bbfb7 - test[0] timed out
```

### What This Means:
- **EVERY sample** timing out at 10s
- Happens on BOTH tasks tested (007bbfb7, 00d62c1b)
- No candidates generated (0 outputs)
- Cache never used (no solvers validated)

### This is NOT a Cache Issue!
The cache would only help AFTER solvers complete. Here, solvers never finish!

## Root Causes (Most Likely)

### 1. Infinite Loop in Generated Solver Code ⚠️
**Most Likely**: Generated batt.py has an infinite loop or extremely slow operation.

```python
# Possible issues in generated code:
- Infinite while loop
- Recursive call without base case
- Extremely expensive operation (e.g., massive grid processing)
- GPU code deadlock (though GPU disabled for small batches)
```

### 2. Missing or Broken DSL Functions
**Possible**: DSL functions not available or broken on Kaggle.

```python
# Check if DSL imports work:
from pile import *
from dsl import *
```

### 3. Thread/Process Deadlock
**Less Likely**: call_with_timeout() deadlocking.

## Diagnostic Steps

### Step 1: Test Simple Batt
```bash
# Generate simpler batt with fewer solvers
python card.py -c 5 -f test_batt.py

# Test it
python -c "
from test_batt import batt
S = (((0,0), (1,1)),)  # Trivial sample
I = (0,0)
result = batt('test', S, I, None, 'test.log')
print('SUCCESS:', result)
"
```

### Step 2: Check Vectorized Flag Issue
The timeout might be related to --vectorized flag generating broken code.

```bash
# Test WITHOUT vectorized
bash run_card.sh -o -i -c 5 -T -m  # Force CPU mode (no --vectorized)
```

### Step 3: Test Specific Task Locally
```bash
# Test the exact tasks that timed out
python run_batt.py -c 1 -b batt -t 30 --timing

# If that works locally, Kaggle-specific issue
```

### Step 4: Add Debug Output
```python
# Add to generated batt start:
def batt(task_id, S, I, C, log_path):
    print(f"BATT START: {task_id}, {len(S)} samples")
    import sys
    sys.stdout.flush()
    
    # ... existing code
```

## Quick Fixes to Try

### Fix 1: Increase Timeout
```bash
# Maybe 10s not enough on slow Kaggle CPU
bash run_card.sh -o -i -c 5 -t 30 -T -g  # 30 second timeout
```

### Fix 2: Disable Vectorized Mode
```bash
# Test without GPU batch calls
bash run_card.sh -o -i -c 5 -T -m  # Force CPU, no vectorized
```

### Fix 3: Reduce Solver Count
```bash
# Maybe 32 solvers too many
# Edit run_card.sh line: -c 32 → -c 10
bash run_card.sh -o -i -c 5 -T -g
```

### Fix 4: Check Generated Code
```bash
# Look at what was generated
less tmp_batt_onerun_run.py

# Search for obvious issues:
# - while True without break
# - Recursive calls
# - Huge operations
```

## Most Likely Solution

Based on the pattern, I suspect **--vectorized flag is generating broken code**.

### Test This:
```bash
# 1. Force CPU mode (disables --vectorized)
bash run_card.sh -o -i -c 5 -T -m

# If that works, the issue is vectorized code generation
# If that ALSO times out, issue is in base solver logic
```

### Check card.py Vectorized Logic
```python
# In card.py, check what --vectorized does:
if args.vectorized:
    # What code does this generate?
    # Is it valid?
    # Does it import correctly?
```

## Expected vs Actual

### Expected (Working):
```
demo[0] - 007bbfb7 - 32    # 32 outputs generated
demo[1] - 007bbfb7 - 32
...
-- Demo scoring: 64 outputs, X matches
```

### Actual (Broken):
```
demo[0] timed out           # Never completes
demo[1] timed out
...
-- Demo scoring: 0 outputs  # No results!
```

## Action Plan

1. **IMMEDIATE**: Test without --vectorized flag
   ```bash
   bash run_card.sh -o -i -c 5 -T -m
   ```

2. **IF THAT WORKS**: Issue is in vectorized code generation
   - Fix card.py --vectorized logic
   - Or disable --vectorized on Kaggle

3. **IF THAT FAILS**: Issue is in base solver logic
   - Reduce solver count (-c 10 instead of 32)
   - Increase timeout (30s instead of 10s)
   - Check specific solvers for infinite loops

4. **DEBUG**: Add print statements
   ```python
   # Add to batt start:
   print("BATT CALLED")
   sys.stdout.flush()
   ```

## Hypothesis

**Most likely**: The vectorized code generation (--vectorized flag) is creating broken code that hangs or has an infinite loop. Test with -m flag (CPU mode, no vectorized) to confirm.

**Second most likely**: 32 solvers too many, generating extremely slow code. Test with -c 10.

**Least likely**: Cache or GPU issue (GPU already disabled for small batches, cache never reached).

## Next Steps for User

**Try this on Kaggle**:
```bash
# Test 1: Without vectorized (most likely fix)
bash run_card.sh -o -i -c 3 -T -m

# Test 2: Fewer solvers
bash run_card.sh -o -i -c 3 -T -g

# Test 3: Longer timeout
bash run_card.sh -o -i -c 3 -t 30 -T -g

# Test 4: Check generated code
head -100 tmp_batt_onerun_run.py | grep -A 10 "def batt"
```

The timeout issue is **blocking cache testing**. We need to fix the generated code first!
