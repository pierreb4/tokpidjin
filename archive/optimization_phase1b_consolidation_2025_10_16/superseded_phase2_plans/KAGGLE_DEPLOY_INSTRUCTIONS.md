# Kaggle Deployment Instructions - Stage 1 Investigation

**Date**: October 15, 2025  
**Purpose**: Get full profiling data to investigate Stage 1 unexpected results

---

## What We Need to Find Out

1. **Where did mapply_t and apply_t go?** (disappeared from top 5)
2. **What are their actual times in Stage 1?** (expected 1.75-1.95s and 1.90-2.00s)
3. **Why did o_g and objects get slower?** (expected faster, got +5% slower)
4. **Why did framework overhead increase?** (+0.552s = +1.4%)

---

## Deployment Steps

### 1. Upload Files to Kaggle

Upload these files to your Kaggle notebook/kernel:

**Required files**:
- `profile_batt_framework.py` ⭐ **UPDATED** (fixed TypeError, added --search)
- `dsl.py` (with Stage 1 optimizations)
- `batt.py`
- `tmp_batt_onerun_run.py`
- `safe_dsl.py`
- `batt_gpu.py`
- All other dependencies

### 2. Run Enhanced Profiling

**Command 1: Search for Missing Functions** ⭐ **CRITICAL**
```bash
python profile_batt_framework.py --tasks 100 --search mapply_t apply_t o_g objects apply merge
```

This will show you:
```
================================================================================
FUNCTION SEARCH RESULTS
================================================================================

Pattern: 'mapply_t' (X matches)
--------------------------------------------------------------------------------
Function                                      Calls   Cum Time   Per Call
--------------------------------------------------------------------------------
mapply_t                                        700      ?.???s     ?.???ms

Pattern: 'apply_t' (X matches)
--------------------------------------------------------------------------------
Function                                      Calls   Cum Time   Per Call
--------------------------------------------------------------------------------
apply_t                                         700      ?.???s     ?.???ms

Pattern: 'o_g' (X matches)
--------------------------------------------------------------------------------
Function                                      Calls   Cum Time   Per Call
--------------------------------------------------------------------------------
o_g                                            3400      1.506s     0.443ms

Pattern: 'objects' (X matches)
--------------------------------------------------------------------------------
Function                                      Calls   Cum Time   Per Call
--------------------------------------------------------------------------------
objects                                        3400      1.449s     0.426ms
```

**Command 2: Get Complete Report**
```bash
python profile_batt_framework.py --tasks 100 --all > full_profile_output.txt
```

This creates:
- `profile_batt_framework_TIMESTAMP.txt` (complete file)
- Console output with search results

### 3. What to Look For

#### In Search Results (Console Output)

**mapply_t**:
- ✅ **Success**: Time ~1.75-1.95s (10-20% faster than 2.148s)
- ⚠️ **Concern**: Time >2.0s (optimization didn't work)
- ❌ **Failure**: Time >2.148s (got slower!)

**apply_t**:
- ✅ **Success**: Time ~1.90-2.00s (5-10% faster than 2.106s)
- ⚠️ **Concern**: Time >2.0s (optimization didn't work)
- ❌ **Failure**: Time >2.106s (got slower!)

**o_g**:
- Current: 1.506s (was 1.430s, +5%)
- ✅ **Success**: Time <1.430s (optimization worked)
- ❌ **Failure**: Still >1.430s (optimization failed)

**objects**:
- Current: 1.449s (was 1.374s, +5%)
- ✅ **Success**: Time <1.374s (optimization worked)
- ❌ **Failure**: Still >1.374s (optimization failed)

#### In Full Report File

Look for:
1. **Total DSL time**: Should be ~8-9s (was 10.094s baseline)
2. **Framework time**: Should be ~40s (is 40.693s, was 40.141s)
3. **Call counts**: Verify they match baseline (628k DSL calls)

### 4. Copy Results Back

**Copy these outputs**:
1. Search results from console (paste into issue/comment)
2. `profile_batt_framework_TIMESTAMP.txt` (download file)
3. `full_profile_output.txt` (if created)

---

## Analysis Template

Fill this in with your results:

```markdown
## Stage 1 Kaggle Results - Full Data

### Search Results

**mapply_t**:
- Calls: ???
- Cumulative time: ?.???s
- Per call: ?.???ms
- Baseline: 2.148s (3.07ms/call)
- **Change**: [+X% / -X%]
- **Expected**: 1.75-1.95s
- **Status**: [✅ SUCCESS / ⚠️ PARTIAL / ❌ FAILED]

**apply_t**:
- Calls: ???
- Cumulative time: ?.???s
- Per call: ?.???ms
- Baseline: 2.106s (3.01ms/call)
- **Change**: [+X% / -X%]
- **Expected**: 1.90-2.00s
- **Status**: [✅ SUCCESS / ⚠️ PARTIAL / ❌ FAILED]

**o_g**:
- Calls: 3400
- Cumulative time: 1.506s
- Per call: 0.443ms
- Baseline: 1.430s (0.42ms/call)
- **Change**: +5.3%
- **Expected**: 1.23-1.29s
- **Status**: ❌ FAILED (got slower)

**objects**:
- Calls: 3400
- Cumulative time: 1.449s
- Per call: 0.426ms
- Baseline: 1.374s (0.40ms/call)
- **Change**: +5.5%
- **Expected**: 1.17-1.24s
- **Status**: ❌ FAILED (got slower)

### Summary

**Total DSL time**: ?.???s (baseline: 10.094s)
**Framework time**: 40.693s (baseline: 40.141s, +1.4%)
**Wall-clock**: 6.73s (baseline: 6.64s, +1.4%)

**Overall**: [✅ SUCCESS / ⚠️ MIXED / ❌ FAILED]
```

---

## Expected Outcomes

### Scenario A: Hidden Success ✅
```
mapply_t: 1.8s (-16% ✅)
apply_t: 1.95s (-7% ✅)
o_g: 1.25s (-13% ✅)
objects: 1.20s (-13% ✅)
Total DSL: 8.0s (-19% ✅) <- We saw this!
Framework: 40.7s (+1.4% ❌) <- This masked it
```
**Conclusion**: Optimizations WORKED, but framework overhead increased

### Scenario B: Partial Success ⚠️
```
mapply_t: 1.85s (-14% ✅)
apply_t: 2.05s (-3% ⚠️)
o_g: 1.48s (+3% ❌)
objects: 1.42s (+3% ❌)
Total DSL: 9.0s (-11% ⚠️)
```
**Conclusion**: Some optimizations worked, others didn't

### Scenario C: Implementation Error ❌
```
mapply_t: 2.25s (+5% ❌)
apply_t: 2.18s (+4% ❌)
o_g: 1.51s (+6% ❌)
objects: 1.45s (+6% ❌)
Total DSL: 10.5s (+4% ❌)
```
**Conclusion**: Optimizations introduced overhead

---

## Next Steps Based on Results

### If Scenario A (Hidden Success)
1. ✅ **Stage 1 optimizations are GOOD - keep them!**
2. 🔍 Investigate framework overhead increase
3. 📊 Profile framework bottlenecks specifically
4. ➡️ Proceed to Stage 2 (optimize framework if needed)

### If Scenario B (Partial Success)
1. ⚠️ Keep working optimizations (mapply_t, apply_t)
2. ❌ Revert failed optimizations (o_g, objects)
3. 🔍 Debug why o_g/objects got slower
4. 🔧 Re-implement with different approach

### If Scenario C (Implementation Error)
1. ❌ Revert ALL Stage 1 optimizations
2. 🐛 Debug implementation issues
3. 🧪 Test each optimization individually locally
4. 🔄 Re-implement one at a time

---

## Commands Summary

```bash
# On Kaggle - Critical command!
python profile_batt_framework.py --tasks 100 --search mapply_t apply_t o_g objects

# For complete data
python profile_batt_framework.py --tasks 100 --all

# Both together
python profile_batt_framework.py --tasks 100 --search mapply_t apply_t o_g objects --all
```

---

**Key Insight**: The `--search` flag will find mapply_t and apply_t even if they're not in top 100 anymore (because they got faster!). This is the critical data we need.

**Status**: Ready to deploy ✅  
**Expected time**: 5-10 minutes on Kaggle  
**Deliverable**: Complete profiling data with times for ALL 4 optimized functions
