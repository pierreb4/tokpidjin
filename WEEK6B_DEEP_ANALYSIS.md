# Week 6B Optimization Analysis

## What We've Learned

### Optimization 1: ✅ Unified Sample Scoring (IMPLEMENTED)

**Problem:** Demo and test samples processed separately
- Demo: 2 samples in parallel (4 workers, 50% utilization)
- Test: 1 sample sequential

**Solution:** Process all samples together
- Combined: 3 samples in parallel (4 workers, 75% utilization)
- Single ProcessPoolExecutor batch
- Eliminated sequential test processing

**Impact:** Better worker utilization, reduced overhead

### Optimization 2: ❌ Candidate Caching (NOT NEEDED)

**Initial assumption:** Candidates regenerated for each task
**Reality:** Candidates already reused!

**How it works:**
1. `card.py` generates batt() function once (32 random solver candidates)
2. Same batt() used for ALL tasks in the run
3. batt() returns same 32 candidates for each sample
4. Filtering happens post-batt (dedup, score check, etc.)

**Evidence from output:**
```
Test 1: 86 total candidates → 32 unique after filtering
Test 2: 82 total candidates → 32 unique after filtering  
Test 3: 77 total candidates → 32 unique after filtering
```

**Conclusion:** The batt() function is already shared! No caching needed.

## Real Performance Analysis

### Where is the time going?

Looking at Test 3 (best performance):
```
Component                    Time     % of Total   What it does
─────────────────────────────────────────────────────────────────
main.run_batt                3.079s   100%         Everything
├─ run_batt.check_solver_speed  4.810s   CPU time   Validation (parallelized)
│  └─ phase3a_validate_batch    0.244s   Wall-clock Actual time (20x parallelized!)
├─ run_batt.check_batt          2.173s   71%        Batt + overhead
│  ├─ batt.demo.parallel         0.114s    4%       Demo+test scoring ✓
│  └─ UNKNOWN OVERHEAD          ~2.0s    67%       ??? ← THE REAL BOTTLENECK!
├─ inline_variables              0.437s   14%        AST operations (cached)
├─ phase2_inline_batch           0.377s   12%        Inlining coordination
├─ phase3b_file_ops              0.178s    6%        File I/O
└─ Other                         0.138s    4%        Misc
```

### The Mystery: 2 seconds of unknown overhead in check_batt!

**What we know:**
- `check_batt` total: 2.173s (wall-clock)
- `batt.demo.parallel`: 0.114s (actual batt execution)
- **Missing**: ~2.0s (92% of check_batt time!)

**What could this be?**
1. Score aggregation logic?
2. Result processing loops?
3. Python object creation/manipulation?
4. Something not being profiled?

Let me check the check_batt code more carefully...

## Deep Dive: check_batt Function

```python
def check_batt(...):
    # 1. Setup (negligible)
    demo_task = total_data['demo'][task_id]
    test_task = total_data['test'][task_id]
    o = {'demo': {}, 'test': {}}
    s = {'demo': {}, 'test': {}}
    S = tuple(...)  # Convert to tuple
    
    # 2. Parallel sample scoring (0.114s - FAST!)
    with ProcessPoolExecutor(max_workers=4):
        all_results = [score_sample(...) for all samples]
    
    # 3. Result aggregation (NOT PROFILED!)
    for result in demo_results:
        o['demo'][i] = result['outputs']
        s['demo'][i] = result['solver_scores']
        all_o = all_o.union(result['outputs'])  # Set union!
        for output in result['outputs']:
            o_score.update(...)  # Score updates
        for s_item in result['solver_scores']:
            d_score.update(...)  # More updates
    
    for result in test_results:
        # Same as above
    
    # 4. Score consolidation (NOT PROFILED!)
    for o_solver_id in d_score.score.keys():
        for name in d_score.score[o_solver_id].keys():
            if name not in s_score:
                s_score[name] = {'iz': S_Score(), 'zo': S_Score()}
            for score_type in ['iz', 'zo']:
                s_score[name][score_type].update(...)
    
    return all_o, o_score, s_score
```

**Hypothesis:** The result aggregation loops (step 3 & 4) are taking ~2 seconds!

## Potential Issues

### Issue 1: Set Union Operations
```python
all_o = all_o.union(result['outputs'])  # Called for each result
```
- 3 samples × 32 outputs = 96 candidates
- Each union creates a new set (Python sets are immutable for this operation)
- Could be expensive!

### Issue 2: Nested Score Updates
```python
for result in demo_results + test_results:  # 3 iterations
    for output in result['outputs']:  # ~32 per result = 96 total
        o_score.update(...)
    for s_item in result['solver_scores']:  # Variable count
        d_score.update(...)
```

### Issue 3: Score Consolidation Triple Loop
```python
for o_solver_id in d_score.score.keys():  # ~32 solvers
    for name in d_score.score[o_solver_id].keys():  # Multiple names
        for score_type in ['iz', 'zo']:  # 2 types
            s_score[name][score_type].update(...)
```

This could be O(n²) or O(n³) depending on how many names there are!

## Action Items

### Week 6B Optimization 2: Profile check_batt internals

Add profiling to:
1. Result aggregation loops
2. Set union operations
3. Score update calls
4. Score consolidation loop

### Week 6B Optimization 3: If loops are slow, optimize them

Potential optimizations:
1. Use `all_o.update()` instead of `all_o.union()` (in-place)
2. Batch score updates instead of one-by-one
3. Optimize triple loop in score consolidation
4. Consider caching score lookups

## Expected Impact

If the 2 seconds is in aggregation loops:
- Optimize set operations: Save 0.5s
- Optimize score updates: Save 0.5s  
- Optimize consolidation: Save 0.5s
- **Total savings: 1.5s (from 3.079s → 1.6s per task)**

## Summary

1. ✅ **Optimization 1 (Unified Samples)**: Implemented, improves worker utilization
2. ❌ **Optimization 2 (Candidate Cache)**: Not needed, already done by design
3. 🔍 **Next Step**: Profile check_batt internals to find the missing 2 seconds
4. 🎯 **Goal**: Identify and optimize the score aggregation bottleneck

The real win is in finding where that 2 seconds of overhead is hiding!