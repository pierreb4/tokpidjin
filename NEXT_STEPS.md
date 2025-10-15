# Next Steps: Framework Profiling

**Current Status**: ✅ Bottleneck identified and validated (framework = 92.4%)  
**Next Action**: Profile batt() framework to find specific bottlenecks  
**Expected Result**: Identify where 92.4% of time is spent

---

## Quick Start

### On Kaggle (Recommended)

```bash
# 1. Install line_profiler
pip install line_profiler

# 2. Add @profile decorators to batt functions
# Edit batt_gpu.py or tmp_batt_onerun_run.py:
@profile
def batt(...):
    # existing code

# 3. Run line_profiler
kernprof -l -v tmp_batt_onerun_run.py

# 4. Save output
kernprof -l -v tmp_batt_onerun_run.py > line_profile_output.txt 2>&1
```

### What to Profile

Focus on these functions (where 92.4% likely lives):

1. **batt() execution loop**
   - Candidate generation
   - Sample validation
   - Result collection

2. **GPU batch processing**
   - CPU→GPU transfers
   - GPU→CPU transfers  
   - Batch size impact

3. **Framework overhead**
   - Module imports
   - Function wrapping
   - Error handling

---

## Expected Bottlenecks

Based on the 92.4% framework overhead, likely culprits:

### High Priority (probably 40-60% of time)

- **GPU memory transfers**: CPU↔GPU data movement
- **Batch processing overhead**: Setup/teardown per batch
- **Candidate generation**: Creating test inputs

### Medium Priority (probably 20-30% of time)

- **Validation logic**: Checking if solutions work
- **Result collection**: Gathering and formatting outputs
- **Module imports**: Loading DSL and helpers

### Low Priority (probably 5-10% of time)

- **Error handling**: Try/except overhead
- **Logging**: Print statements and debugging
- **Framework initialization**: Setup code

---

## Analysis Checklist

When you get line_profiler results:

- [ ] Identify functions taking >10% of time (HIGH priority)
- [ ] Identify functions taking 5-10% of time (MEDIUM priority)  
- [ ] Look for repeated operations (can they be batched?)
- [ ] Check for CPU↔GPU transfers (can they be reduced?)
- [ ] Find initialization overhead (can it be moved out of loops?)

---

## Optimization Ideas

### Reduce GPU Transfers

```python
# Bad: Transfer on every operation
for op in operations:
    data_gpu = cp.array(data_cpu)  # ❌ Transfer
    result_gpu = op(data_gpu)
    data_cpu = result_gpu.get()     # ❌ Transfer

# Good: Keep data on GPU
data_gpu = cp.array(data_cpu)       # ✅ Transfer once
for op in operations:
    data_gpu = op(data_gpu)         # Stay on GPU
result_cpu = data_gpu.get()         # ✅ Transfer once
```

### Batch Candidate Processing

```python
# Bad: Process candidates one by one
for candidate in candidates:
    result = test_candidate(candidate)  # ❌ Serial

# Good: Batch process candidates
results = test_candidates_batch(candidates)  # ✅ Parallel
```

### Pre-compute Common Values

```python
# Bad: Recompute in loop
for sample in samples:
    grid = sample['input']
    neighbors = get_neighbors(grid)  # ❌ Recompute
    
# Good: Compute once
neighbor_cache = {
    i: get_neighbors(sample['input'])
    for i, sample in enumerate(samples)
}
for i, sample in enumerate(samples):
    neighbors = neighbor_cache[i]    # ✅ Cached
```

---

## Success Criteria

After framework optimization, you should see:

- ✅ Framework overhead: 92.4% → 35-50% (2-5x improvement)
- ✅ DSL operations: 7.6% → 15-25% (now more visible)
- ✅ GPU utilization: Higher (less idle time)
- ✅ Total time: 1757s → 350-900s at 400 tasks

---

## Files to Check

**Profiling tools** (already created):
- `profile_batt_dsl.py` - DSL function profiler ✅
- `profile_batt_batch.py` - Multi-task profiler ✅
- `reanalyze_filtered.py` - Outlier filtering ✅

**Analysis results**:
- `KAGGLE_PROFILING_ANALYSIS.md` - Original findings ✅
- `KAGGLE_PROFILING_FILTERED_ANALYSIS.md` - Validated findings ✅
- `PROFILING_DISCOVERY_SUMMARY.md` - Journey recap ✅

**Next to create**:
- Line profiler output for batt() framework
- Framework optimization implementation
- Combined optimization validation

---

## Timeline Estimate

**Framework profiling**: 1-2 hours
- Run line_profiler on Kaggle
- Analyze results
- Identify top 3 bottlenecks

**Framework optimization**: 3-7 days
- Reduce GPU transfers (1-2 days)
- Batch candidate processing (1-2 days)  
- Optimize initialization (1 day)
- Test and validate (1-2 days)

**GPU DSL implementation**: 3-5 days
- Implement GPU o_g (2-3 days)
- Implement GPU objects (1-2 days)
- Test and validate (1 day)

**Total**: 1-2 weeks for 1.9-4.3x speedup

---

## Ready to Go!

You have:
✅ Identified the bottleneck (framework = 92.4%)
✅ Validated with filtered data (still 92.4%)
✅ Confirmed optimization priorities
✅ Set clear success criteria

Next: **Run line_profiler on Kaggle to find specific bottlenecks!**

```bash
# On Kaggle
kernprof -l -v tmp_batt_onerun_run.py > line_profile_output.txt 2>&1
```
