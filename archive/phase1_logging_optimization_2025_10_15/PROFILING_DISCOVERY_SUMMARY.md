# The Outlier Discovery: A Case Study in Data Analysis

**Date**: October 15, 2025  
**Summary**: How we discovered outliers, re-analyzed data, and confirmed our original insights

## The Journey

### Act 1: Initial Profiling (100 tasks)

Ran `profile_batt_batch.py` on Kaggle with `tmp_batt_onerun_run.py`:

```
Wall-clock: 110.33 seconds
cProfile total: 1054 seconds
Average per task: 10.54s

Framework: 93.9%
DSL: 6.4%
```

**Insight**: Framework is the bottleneck, not DSL operations.

### Act 2: The Outlier Question

User noticed extreme outliers in execution times:
- Task 16 (06df4c85): 239.5 seconds
- Task 50 (13f06aa5): 117.3 seconds
- Task 56 (15113be4): 101.9 seconds
- Task 79 (1b59e163): 180.3 seconds

**Question**: Are these outliers skewing our results? Do we need to re-profile?

### Act 3: The Investigation

Created `KAGGLE_PROFILING_OUTLIER_ANALYSIS.md`:
- Identified 4 outliers with infinite/near-infinite loops
- Root cause: Genetic mutations hitting edge cases
- Hypothesis: Outliers inflate DSL stats, hide real bottlenecks

**Concern**: Maybe DSL functions are actually 15-30% (not 1.3%) without outliers?

### Act 4: The Re-Analysis

Created `reanalyze_filtered.py` to remove outliers and recalculate:

```bash
python reanalyze_filtered.py
```

**Results (96 tasks, outliers removed)**:
```
Framework: 92.4%  (was 93.9%)
DSL: 7.6%         (was 6.4%)
```

### Act 5: The Discovery! 🎯

**The outliers were a RED HERRING!**

- Outliers inflated absolute times by 60% (632 seconds extra)
- But percentages barely changed (1.5 percentage points)
- Framework STILL dominates at 92.4%
- Original analysis was CORRECT!

## Key Insights

### 1. Absolute Time vs Percentage

**Outliers affected absolute time dramatically**:
- Total cProfile: 1054s → 422s (60% reduction)
- DSL functions: 64s → 32s (50% reduction)
- Framework: 990s → 390s (61% reduction)

**But percentages stayed nearly the same**:
- Framework: 93.9% → 92.4% (only 1.5 points!)
- DSL: 6.4% → 7.6% (only 1.2 points!)

### 2. Why Percentages Matter for Optimization

When optimizing, we care about **where time is spent**, not **how much time**.

Even with outliers:
- 93.9% framework → **Optimize framework**
- 6.4% DSL → **Secondary priority**

Without outliers:
- 92.4% framework → **Optimize framework** ✅ Same conclusion!
- 7.6% DSL → **Secondary priority** ✅ Same conclusion!

### 3. The Value of Filtering

Filtering outliers helped us:
- ✅ Understand data better
- ✅ Validate original findings
- ✅ Gain confidence in the analysis
- ✅ Confirm optimization priorities

But it **didn't change** our strategy!

## Lessons Learned

### About Data Analysis

1. **Outliers matter for absolute measurements**
   - Total time, average time, wall-clock
   - Remove outliers for accurate baselines

2. **Percentages are robust to outliers**
   - When outliers affect all categories proportionally
   - Framework and DSL both dropped by ~60%
   - Percentages stayed nearly constant

3. **Always validate suspicious data**
   - We were right to question extreme values
   - Investigation confirmed they were real outliers
   - Re-analysis validated original insights

### About Optimization

1. **Focus on percentages, not absolutes**
   - 93.9% framework → that's the target!
   - Whether it's 990s or 390s doesn't change priority

2. **Outliers can distract from real work**
   - We spent time investigating (valuable)
   - But original plan was already correct
   - Sometimes "good enough" data is sufficient

3. **Trust the analysis, but verify**
   - Original insights were sound
   - Verification gave us confidence
   - Now we can optimize without doubt

## The Numbers

### Optimization ROI (400 tasks, filtered data)

**Baseline**: 1757s (29.3 minutes)

| Optimization | Saves | New Total | Speedup |
|--------------|-------|-----------|---------|
| Framework (2-5x) | 812-1299s | 458-945s | 1.9-3.8x ⭐⭐⭐ |
| GPU DSL (3-6x) | 36-45s | 1711-1720s | 1.02-1.03x ⭐ |
| **Combined** | **848-1344s** | **413-909s** | **1.9-4.3x** ⭐⭐⭐ |

### Priorities (CONFIRMED)

1. **🔴 Framework optimization** (92.4% of time)
   - Saves 812-1299 seconds
   - 2-5x speedup potential
   - Highest impact

2. **🟡 GPU DSL acceleration** (7.6% of time)
   - Saves 36-45 seconds
   - 3-6x speedup on o_g/objects
   - Worthwhile with 8hr GPU budget

3. **🟢 Combined approach**
   - 1.9-4.3x overall speedup
   - 29 minutes → 7-15 minutes
   - Maximum performance

## Conclusion

### What We Learned

✅ **Original analysis was correct**
- Framework is the bottleneck (92.4% confirmed)
- DSL optimization is secondary (7.6% confirmed)
- Optimization priorities validated

✅ **Outliers were informative but not critical**
- They inflated times but not percentages
- Investigation was valuable for confidence
- But strategy remains unchanged

✅ **Ready to optimize with confidence**
- Know what to optimize (framework)
- Know the expected ROI (2-5x)
- Know it's worth doing (8hr GPU budget)

### The Takeaway

> **Sometimes the most valuable analysis is the one that confirms what you already knew.**

We spent time investigating outliers and re-analyzing data. This wasn't wasted effort - it gave us **confidence** in our original insights. Now we can proceed with optimization knowing our priorities are correct.

### Next Steps

The plan hasn't changed:

1. ✅ Profile Kaggle execution ← **DONE**
2. ✅ Identify bottlenecks ← **DONE** (framework 92.4%)
3. ✅ Validate findings ← **DONE** (filtered data confirms)
4. → **Profile framework with line_profiler** ← **NEXT**
5. → Optimize framework (2-5x target)
6. → GPU-accelerate o_g/objects (3-6x target)
7. → Measure combined speedup (1.9-4.3x expected)

---

**Status**: ✅ Analysis complete and validated  
**Confidence**: High - data confirms original insights  
**Next**: Profile batt() framework to identify specific bottlenecks  
**Expected**: 1.9-4.3x overall speedup from both optimizations
