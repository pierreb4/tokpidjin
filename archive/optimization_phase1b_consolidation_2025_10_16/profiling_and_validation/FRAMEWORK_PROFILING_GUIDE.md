# Framework Profiling Guide

**Status**: Using detailed cProfile analysis to identify specific bottlenecks within 92.4% framework overhead

**Date**: October 15, 2025

## Background

Previous profiling revealed:
- **Framework overhead**: 92.4% of execution time (validated with outlier filtering)
- **DSL operations**: 7.6% of execution time
- **Line profiler**: Failed to collect timing data (function didn't execute properly)
- **Next step**: Use cProfile with detailed function categorization

## Profiling Script: profile_batt_framework.py

### Purpose
Identify specific framework bottlenecks using cProfile with automatic function categorization:
- GPU batch processing (`batch_process_samples_gpu`)
- Dedupe operations
- Tuple/Frozenset operations
- Candidate generation
- Result collection

### Usage

**Local testing** (quick validation):
```bash
# Test with small number of tasks
python profile_batt_framework.py --tasks 10
```

**Kaggle profiling** (production data):
```bash
# Profile 100 tasks (matches previous profiling)
python profile_batt_framework.py --tasks 100

# Full profiling (400 tasks)
python profile_batt_framework.py --tasks 400
```

### Output

**Console output**:
1. Framework Bottlenecks by Category (ranked by time)
2. Top Functions in each major category
3. Summary statistics

**File output**: `profile_batt_framework_TIMESTAMP.txt`
- Category summary with percentages
- Detailed function listings for each category
- Full profiling stats (top 100 functions)

### Expected Bottlenecks

Based on 92.4% framework overhead, expect to find:

**High probability** (likely >20% each):
1. **GPU batch processing**: 
   - `batch_process_samples_gpu` - GPU memory transfers
   - 7 calls per execution (found in code analysis)

2. **Dedupe operations**:
   - `dedupe` - Set deduplication after batch processing
   - Called 14 times per execution (2x per batch)

**Medium probability** (likely 5-15% each):
3. **Tuple operations**:
   - `difference_tuple` - Finding differences between tuples
   - `get_nth_t` - Extracting elements from tuples
   - `astuple` - Creating tuples

4. **Candidate management**:
   - `_get_safe_default` - Error handling fallbacks
   - List append operations (`o.append`, `s.append`)

**Lower probability** (likely <5% each):
5. **Frozenset operations**:
   - `difference` - Frozenset differences
   - `get_nth_f` - Extracting from frozensets

## Analysis Workflow

### Step 1: Run profiling on Kaggle
```bash
# Upload profile_batt_framework.py to Kaggle
# Enable GPU (T4x2 or L4x4)
# Run profiling
python profile_batt_framework.py --tasks 100
```

### Step 2: Analyze results
Look for:
1. **Categories >10% of total time** - Priority targets
2. **Functions with high per-call time** - Expensive operations
3. **Functions with many calls** - Optimization opportunities

### Step 3: Prioritize optimizations

**For GPU bottlenecks**:
- Reduce memory transfers (batch multiple operations)
- Optimize batch size
- Pipeline GPU operations

**For dedupe bottlenecks**:
- Use faster data structures (dict vs set)
- Implement caching
- Reduce duplicate generation

**For tuple/frozenset bottlenecks**:
- Use arrays instead of tuples where possible
- Cache frequently accessed elements
- Batch tuple operations

### Step 4: Implement optimizations

Target 2-5x speedup:
- **Conservative**: 2x speedup → 1624s → 812s (saves 812s)
- **Aggressive**: 5x speedup → 1624s → 325s (saves 1299s)

With DSL optimizations (3-6x on 7.6%):
- **Combined**: 1.9-4.3x overall speedup
- **Result**: 1757s → 413-909s (7-15 minutes vs 29 minutes)

## Expected Findings

Based on code analysis (7 GPU batch patterns found):

### GPU Batch Processing Pattern
```python
# Pattern repeated 7 times in batt()
t687, t688, t689, t690 = batch_process_samples_gpu(S)
t691 = dedupe(t689)
t692 = dedupe(t690)
t693 = difference_tuple(t692, t691)
t694 = get_nth_t(t693, F0)
```

**Expected time breakdown**:
1. `batch_process_samples_gpu`: 30-50% (GPU transfers)
2. `dedupe`: 20-30% (set operations)
3. `difference_tuple`: 10-20% (tuple comparison)
4. `get_nth_t`: 5-10% (element extraction)

### Optimization Opportunities

**Immediate** (low-hanging fruit):
1. **Batch dedupe operations** - Process multiple dedupe calls together
2. **Cache dedupe results** - Avoid redundant deduplication
3. **Reduce GPU transfers** - Keep data on GPU longer

**Medium-term** (requires restructuring):
4. **Pipeline GPU operations** - Chain operations without CPU transfer
5. **Optimize tuple operations** - Use arrays internally
6. **Lazy evaluation** - Defer expensive operations

**Long-term** (major refactor):
7. **Rewrite framework** - Design for GPU-first architecture
8. **Eliminate redundancy** - Generate fewer candidates

## Success Criteria

✅ **Profiling complete** when:
- Clear bottleneck identification (functions >10% of time)
- Category breakdown available
- Per-call timing data collected

✅ **Analysis complete** when:
- Top 3-5 bottlenecks identified
- Optimization strategy defined
- Expected speedup estimated

✅ **Ready for implementation** when:
- Optimization priorities ranked
- Technical approach validated
- Test cases defined

## Next Steps After Profiling

1. **Create optimization plan** based on profiling data
2. **Implement highest-impact optimizations** (>20% time savings)
3. **Validate correctness** (test on known tasks)
4. **Measure speedup** (re-profile to confirm gains)
5. **Iterate** until 2-5x framework speedup achieved

## Files

- **Profiling script**: `profile_batt_framework.py`
- **Previous analysis**: 
  - `KAGGLE_PROFILING_ANALYSIS.md` (original findings)
  - `KAGGLE_PROFILING_FILTERED_ANALYSIS.md` (validated priorities)
  - `PROFILING_DISCOVERY_SUMMARY.md` (outlier investigation)
- **Output**: `profile_batt_framework_TIMESTAMP.txt` (generated by script)

## Notes

- **Line profiler failed**: No timing data collected (function didn't execute)
- **cProfile works**: Function-level profiling with detailed categorization
- **Focus**: Framework functions (92.4% of time)
- **Goal**: 2-5x speedup (saves 812-1299s at 400 tasks)
- **Budget**: 8 hours of L4x4 GPU time (28,800 seconds) - all optimizations worthwhile!
