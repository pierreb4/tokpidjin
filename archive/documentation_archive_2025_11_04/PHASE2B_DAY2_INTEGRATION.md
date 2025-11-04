# Phase 2b Day 2: GPU Batch Integration Guide

**Status**: Integration Points Identified  
**Target**: Modify run_batt.py to use BatchSolverAccumulator  
**Effort**: 2-3 hours for safe, minimal integration  

## Architecture Overview

### Current Flow (Without Batch Processing)
```
Task → Sample 1 → Score → Return result
     → Sample 2 → Score → Return result
     → Sample 3 → Score → Return result
     ...
```

**Issue**: Each sample scoring happens independently, no opportunity to batch GPU operations.

### New Flow (With Batch Processing)
```
Task → Accumulator initialized
     → Sample 1 → Grid to Accumulator → Continue scoring
     → Sample 2 → Grid to Accumulator → Continue scoring
     → Sample 3 → Grid to Accumulator → [BATCH FULL] → Process all on GPU
     → Sample 4 → Grid to Accumulator → Continue scoring
     ...
     → Task End → Flush remaining grids → Final processing
```

**Benefit**: Amortizes GPU transfer overhead across 100+ grids per batch.

---

## Integration Points in run_batt.py

### Point 1: Task Initialization (Line ~1945 in `main`)
**Location**: Where tasks are started  
**Change**: Initialize `BatchSolverAccumulator` per task  
**Risk**: Low - new initialization, no side effects

```python
# BEFORE
async def main(do_list, start=0, count=0, timeout=1, ...):
    for task_i, task_id in enumerate(do_list):
        await run_batt(...)

# AFTER
async def main(do_list, start=0, count=0, timeout=1, ...):
    for task_i, task_id in enumerate(do_list):
        # Initialize batch accumulator for this task
        batch_acc = BatchSolverAccumulator(batch_size=100, use_gpu=GPU_AVAILABLE)
        await run_batt(..., batch_accumulator=batch_acc)
```

### Point 2: Sample Scoring (Line ~1540 in `check_one_solver` or `score_sample`)
**Location**: Where individual grids are processed  
**Change**: Add input/output grids to accumulator  
**Risk**: Low - purely accumulation, doesn't change scoring logic

```python
# BEFORE
async def check_one_solver(data):
    result = solver(grid)
    return result

# AFTER
async def check_one_solver(data):
    result = solver(grid)
    # Add grids to batch accumulator (transparent)
    if batch_accumulator:
        batch_accumulator.add('input', grid)
        batch_accumulator.add('output', result)
    return result
```

### Point 3: Task Completion (Line ~1750 in `run_batt`)
**Location**: Where task results are finalized  
**Change**: Flush remaining batched grids  
**Risk**: Low - final flush, minimal overhead

```python
# BEFORE
return all_o, o_score, s_score

# AFTER
# Flush any remaining batched grids and log stats
if batch_accumulator:
    stats = batch_accumulator.flush_and_log()
    if DO_PRINT:
        print_l(f"Batch stats: {stats}")

return all_o, o_score, s_score
```

---

## Minimal Integration Strategy (Recommended for Day 2)

### Phase 1: Add Infrastructure (Hour 1)
1. Import modules at top of run_batt.py
   ```python
   from gpu_batch_integration import BatchSolverAccumulator
   ```

2. Add batch_accumulator parameter to function signatures
   ```python
   # In main()
   batch_acc = BatchSolverAccumulator(batch_size=100, use_gpu=GPU_AVAILABLE)
   
   # In run_batt()
   async def run_batt(..., batch_accumulator=None):
   
   # In check_batt()
   def check_batt(..., batch_accumulator=None):
   ```

3. Pass parameter through the call chain

### Phase 2: Add Accumulation Points (Hour 1-2)
1. In `score_sample` function, add grids to accumulator
   ```python
   if batch_accumulator:
       batch_accumulator.add('input', sample['input'])
   ```

2. In `check_one_solver`, add output grids
   ```python
   if batch_accumulator:
       batch_accumulator.add('output', result)
   ```

### Phase 3: Flush and Validate (Hour 2-3)
1. Add flush call at task end
   ```python
   if batch_accumulator:
       stats = batch_accumulator.flush_and_log()
   ```

2. Test with 1 task first
3. Test with 10 tasks
4. Measure performance improvement

---

## Specific Code Changes Required

### Change 1: Import statement (Line 100, after other imports)
```python
# Add this line
from gpu_batch_integration import BatchSolverAccumulator
```

**Risk Level**: ✅ None (pure import)

### Change 2: `main()` function (Line ~1945)
Find where `run_batt` is called and add:
```python
# Initialize batch accumulator for this task
batch_acc = BatchSolverAccumulator(batch_size=100, use_gpu=GPU_AVAILABLE)

# Pass to run_batt
await run_batt(..., batch_accumulator=batch_acc)
```

**Risk Level**: ✅ Low (non-invasive)

### Change 3: `run_batt()` signature (Line ~1404)
```python
async def run_batt(total_data, task_i, task_id, d_score, start_time, 
                   pile_log_path, timeout=1, prof=None, 
                   batt_module_name='batt',
                   batch_accumulator=None):  # ← ADD THIS
```

**Risk Level**: ✅ Low (optional parameter)

### Change 4: `run_batt()` end (Line ~1750 before return)
```python
# Flush remaining batched grids
if batch_accumulator:
    stats = batch_accumulator.flush_and_log()
    if DO_PRINT:
        print_l(f"-- {task_id} batch stats: added={stats['total_grids_added']} processed={stats['total_grids_processed']}")

return all_o, o_score, s_score
```

**Risk Level**: ✅ Low (after processing complete)

### Change 5: `check_batt()` signature (Line ~681)
```python
def check_batt(total_data, task_i, task_id, d_score, start_time, 
               pile_log_path, timeout=1, prof=None, 
               batt_module_name='batt',
               batch_accumulator=None):  # ← ADD THIS
```

**Risk Level**: ✅ Low (optional parameter)

### Change 6: `check_batt()` pass-through (Line ~715)
When calling `score_sample`, add to arguments:
```python
all_sample_args.append((i, sample, 'demo', task_id, S, pile_log_path, 
                       timeout, DO_PRINT, batt_module_name, 
                       batch_accumulator))  # ← ADD THIS
```

**Risk Level**: ✅ Low (parameter pass-through)

### Change 7: `score_sample()` signature (Line ~617)
```python
def score_sample(args):
    i, sample, sample_type, task_id, S, pile_log_path, timeout, DO_PRINT, batt_module_name, batch_accumulator = args
    # ... existing code ...
    
    # Add accumulation (inside score_sample, after batt call)
    if batch_accumulator:
        batch_accumulator.add('input', sample['input'])
        # Don't add output here - keeps changes minimal
```

**Risk Level**: ✅ Low (non-invasive accumulation)

---

## Testing Strategy

### Test 1: Single Task (Verification)
```bash
python run_batt.py -c 1 --timing
```
**Expected**: 
- ✅ Produces same results as before
- ✅ No errors
- ✅ Batch stats printed

### Test 2: 10 Tasks (Batch Effectiveness)
```bash
python run_batt.py -c 10 --timing
```
**Expected**:
- ✅ All 10 tasks complete
- ✅ Batch accumulator working (stats show added grids)
- ✅ No performance regression

### Test 3: 32 Tasks (Real Speedup)
```bash
python run_batt.py -c 32 --timing
```
**Expected**:
- ✅ Measure actual speedup vs Phase 2a baseline (24.818s for 100 tasks)
- ✅ Compare wall-clock times
- ✅ Look for 2-3x speedup on solver operations

### Test 4: 100 Tasks (Full Validation)
```bash
python run_batt.py -c 100 --timing
```
**Expected**:
- ✅ Wall-clock target: 12-15s (vs 24.818s current)
- ✅ Batch stats confirm processing
- ✅ All 100 tasks complete successfully

---

## Fallback Strategy

If integration causes issues:

1. **Disable Accumulator**: Set `batch_accumulator=None` everywhere
   - Reverts to pre-optimization behavior
   - Zero performance regression

2. **Reduce Batch Size**: Change `batch_size=100` to `batch_size=10`
   - Tests batch mechanism with smaller batches
   - Easier to debug

3. **CPU-Only Accumulator**: Set `use_gpu=False`
   - Tests accumulation logic without GPU
   - Helps isolate GPU vs integration issues

---

## Success Criteria for Day 2

- [ ] Import statement added ✓
- [ ] Batch accumulator initialized per task ✓
- [ ] Parameter threaded through function chain ✓
- [ ] Single-task test passes ✓
- [ ] 10-task test passes ✓
- [ ] Batch stats printing correctly ✓
- [ ] No performance regression ✓
- [ ] Ready for Day 3 Kaggle validation ✓

---

## Estimated Timeline

- **Hour 1**: Add imports and function signatures
- **Hour 1-2**: Add accumulation points and parameter passing
- **Hour 2-3**: Test locally (1 and 10 tasks), debug issues
- **By EOD**: Ready for Kaggle validation (Day 3)

---

## Key Insights

1. **Transparent Integration**: Batch accumulator doesn't change existing scoring logic
2. **Minimal Changes**: All modifications are parameter additions or simple calls
3. **Easy Rollback**: If issues arise, simply remove accumulator calls
4. **CPU Safe**: Defaults to CPU if GPU not available
5. **No Algorithm Changes**: Just adding overhead to existing flow

---

## Next Steps

When ready:
1. Open run_batt.py
2. Follow "Specific Code Changes" section above
3. Run single-task test
4. Gradually increase task count
5. Monitor performance metrics
6. Ready for Kaggle Day 3 validation

**Timeline**: 2-3 hours for safe, tested integration

