# Week 6B - Loky Installation Guide

## 🔧 Required Package

Week 6B parallel processing requires the `loky` library to handle DSL closures properly.

## 📦 Installation

### On Kaggle:
```python
# In a notebook cell:
!pip install loky==3.4.1
```

### Locally:
```bash
pip install loky==3.4.1
```

## ❓ Why Loky?

**Problem:**
- ProcessPoolExecutor uses `pickle` for serialization
- DSL functions like `rbind` return closures (nested functions)
- Standard `pickle` can't serialize closures
- Results in error: "Can't pickle local object 'rbind.<locals>.f'"

**Solution:**
- `loky` is a drop-in replacement for ProcessPoolExecutor
- Uses `cloudpickle` internally (handles closures!)
- No code changes needed
- Automatic fallback to standard ProcessPoolExecutor if unavailable

## ✅ Verification

After installation, you should see:
```
# No warning message = loky working
bash run_card.sh -o -c 1 -T

# With loky unavailable, you'd see:
Warning: loky not available, using standard ProcessPoolExecutor (may fail on closures)
```

## 📊 Performance Impact

With loky working correctly:
- All DSL functions work (including rbind, lbind, etc.)
- No pickle errors
- Full parallel processing across all sample types
- Expected: 20-30% speedup over baseline

## 🎯 Test Results (With Loky)

**Test 1 (3 samples):** 4.698s (22% faster) ✓
**Test 2 (6 samples):** 3.378s (28% faster) ✓
**Test 3:** Should work (no pickle errors)

## 🚨 Fallback Behavior

If loky is not available:
- Standard ProcessPoolExecutor is used
- Most functions work fine
- Functions returning closures (rbind, lbind, etc.) will fail
- Fallback to sequential processing on error

## 📝 Summary

Install loky for full Week 6B functionality:
```bash
pip install loky==3.4.1
```

Then test on Kaggle:
```bash
bash run_card.sh -o -c 3 -T
```

Expected: No pickle errors, 20-30% speedup!
