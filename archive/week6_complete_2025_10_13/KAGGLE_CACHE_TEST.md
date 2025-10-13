# Kaggle Cache Testing Instructions

**Date**: October 13, 2025  
**Goal**: Validate Week 6A cache performance on Kaggle

## Test Setup

### 1. Upload Latest Code to Kaggle
```bash
# Ensure latest code is pushed
git status
git push

# On Kaggle notebook:
!git clone https://github.com/pierreb4/tokpidjin.git
cd tokpidjin
```

### 2. Test Configuration
```bash
# Test with 20 tasks to see cache effectiveness
# Run THREE times to observe cache warming

# First run: Cold cache (builds cache)
bash run_card.sh -o -i -c 20 -T -g

# Second run: Warm cache (should see cache hits)
bash run_card.sh -o -c 20 -T -g

# Third run: Hot cache (best performance)
bash run_card.sh -o -c 20 -T -g
```

## What to Look For

### Cache Statistics (at end of each run)
```
=== Cache Statistics ===

Validation Cache:
  Hits: ???        # Should increase run 1 → run 2 → run 3
  Misses: ???      # Should decrease
  Hit Rate: ???%   # Target: 80%+ by run 3
  
Inlining Cache:
  Hits: ???        # Should increase dramatically
  Misses: ???      # Should decrease to near 0
  Hit Rate: ???%   # Target: 90%+ by run 2, 100% by run 3
  Time Saved: ???  # Should be 100+ seconds
```

### Timing Summary
Look for these key metrics:
```
Timing summary (seconds):
  utils.inline_variables.total    # Should DROP dramatically
  run_batt.check_solver_speed     # Should DROP on repeated solvers
  run_batt.phase2_inline_batch    # Should approach 0 with cache
```

## Expected Results

### Run 1 (Cold Cache)
```
Cache:
  Validation hits: 0-20%
  Inlining hits: 50-70% (common patterns)
  
Performance:
  Inlining: ~2.5-3.0s (building cache)
  Validation: ~2.5-2.8s (building cache)
  Total per task: ~5-6s
```

### Run 2 (Warm Cache)
```
Cache:
  Validation hits: 70-80%
  Inlining hits: 85-95%
  
Performance:
  Inlining: ~0.5-1.0s (cache hits!)
  Validation: ~0.8-1.2s (cache hits!)
  Total per task: ~2-3s (2-3x faster!)
```

### Run 3 (Hot Cache)
```
Cache:
  Validation hits: 90-95%
  Inlining hits: 95-100%
  
Performance:
  Inlining: ~0.1-0.3s (mostly cache)
  Validation: ~0.3-0.5s (mostly cache)
  Total per task: ~1.5-2.5s (3-5x faster!)
```

## Success Criteria

### ✅ Cache is Working If:
- [ ] Inlining cache hit rate increases each run
- [ ] Inlining time decreases dramatically (>50%)
- [ ] Validation cache builds up over runs
- [ ] Cache stats show "Time Saved" growing
- [ ] Total runtime improves run 1 → run 2 → run 3

### ⚠️ Issues to Watch For:
- Cache hit rate doesn't increase → Check cache disk storage
- Inlining time doesn't decrease → Check cache is being used
- Validation cache always 0% → Need more repeated solvers
- Disk cache not persisting → Check .cache/ directory permissions

## Data Collection

### Collect These Metrics:

**Run 1 (Cold Cache)**:
```
Total tasks: 20
Total time: ___ seconds
Avg per task: ___ seconds

Validation cache hits: ___
Inlining cache hits: ___
Time saved: ___ seconds
```

**Run 2 (Warm Cache)**:
```
Total tasks: 20
Total time: ___ seconds
Avg per task: ___ seconds (improvement: ___x)

Validation cache hits: ___
Inlining cache hits: ___
Time saved: ___ seconds
```

**Run 3 (Hot Cache)**:
```
Total tasks: 20
Total time: ___ seconds
Avg per task: ___ seconds (improvement: ___x)

Validation cache hits: ___
Inlining cache hits: ___
Time saved: ___ seconds
```

## Analysis Commands

### Check Cache Directory Size
```bash
# See what's being cached
ls -lh .cache/validation/ | wc -l
ls -lh .cache/inlining/ | wc -l

# Check disk usage
du -sh .cache/
```

### Extract Key Metrics
```bash
# From run output, extract:
grep "Hit Rate" <output>
grep "Time Saved" <output>
grep "utils.inline_variables.total" <output>
grep "run_batt.check_solver_speed" <output>
```

## Troubleshooting

### If Cache Not Working:

1. **Check cache directory**:
   ```bash
   ls -la .cache/
   ls -la .cache/validation/
   ls -la .cache/inlining/
   ```

2. **Verify imports**:
   ```bash
   python -c "from batt_cache import init_cache; init_cache(); print('OK')"
   ```

3. **Check permissions**:
   ```bash
   chmod -R 755 .cache/
   ```

4. **Force cache clear** (if needed):
   ```bash
   rm -rf .cache/
   python -c "from batt_cache import init_cache; init_cache()"
   ```

## Quick Test (Alternative)

If time-constrained, run quick test:
```bash
# 5 tasks, 2 runs
bash run_card.sh -o -i -c 5 -T -g
bash run_card.sh -o -c 5 -T -g

# Should see dramatic improvement even with 5 tasks
```

## Post-Test Actions

### If Successful (✅):
1. Update WEEK6A_CACHE_SUCCESS.md with Kaggle results
2. Mark Week 6A as complete in todo list
3. Start Week 6B: Parallel processing
4. Share results in commit message

### If Issues (⚠️):
1. Document specific issue
2. Check error messages
3. Verify cache file creation
4. Test with simpler case (2 tasks)
5. Report findings for debugging

## Expected Commit Message

After successful test:
```
test: Validate cache on Kaggle - Week 6A SUCCESS! 🎉

Kaggle Test Results (20 tasks):
- Run 1 (cold): X.Xs per task
- Run 2 (warm): X.Xs per task (Xx faster!)
- Run 3 (hot):  X.Xs per task (Xx faster!)

Cache Statistics:
- Validation hit rate: X% → Y% → Z%
- Inlining hit rate: X% → Y% → Z%
- Total time saved: X seconds

Conclusion:
- Cache working as expected on Kaggle ✓
- Performance improvement validated ✓
- Ready for Week 6B parallel processing ✓

Files: WEEK6A_CACHE_SUCCESS.md updated with Kaggle data
```

## Ready to Test! 🚀

Upload to Kaggle and run the three-test sequence. The cache should show dramatic improvements!
