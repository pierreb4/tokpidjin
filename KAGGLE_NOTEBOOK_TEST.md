# Kaggle Notebook Test Cell

**Copy-paste this into a Kaggle notebook to test the cache!**

## Cell 1: Setup
```python
# Clone and setup
!git clone https://github.com/pierreb4/tokpidjin.git
%cd tokpidjin
!ls -la

# Check GPU availability
!nvidia-smi
```

## Cell 2: First Run (Cold Cache)
```bash
%%bash
echo "=== RUN 1: COLD CACHE ==="
date
bash run_card.sh -o -i -c 20 -T -g 2>&1 | tee run1.log
date
echo ""
echo "=== EXTRACTING METRICS ==="
echo "Cache Stats:"
grep -A 15 "Cache Statistics" run1.log | tail -16
echo ""
echo "Top Timing Items:"
grep "utils.inline_variables.total\|run_batt.check_solver_speed\|run_batt.phase2_inline_batch" run1.log
```

## Cell 3: Second Run (Warm Cache)
```bash
%%bash
echo "=== RUN 2: WARM CACHE ==="
date
bash run_card.sh -o -c 20 -T -g 2>&1 | tee run2.log
date
echo ""
echo "=== EXTRACTING METRICS ==="
echo "Cache Stats:"
grep -A 15 "Cache Statistics" run2.log | tail -16
echo ""
echo "Top Timing Items:"
grep "utils.inline_variables.total\|run_batt.check_solver_speed\|run_batt.phase2_inline_batch" run2.log
```

## Cell 4: Third Run (Hot Cache)
```bash
%%bash
echo "=== RUN 3: HOT CACHE ==="
date
bash run_card.sh -o -c 20 -T -g 2>&1 | tee run3.log
date
echo ""
echo "=== EXTRACTING METRICS ==="
echo "Cache Stats:"
grep -A 15 "Cache Statistics" run3.log | tail -16
echo ""
echo "Top Timing Items:"
grep "utils.inline_variables.total\|run_batt.check_solver_speed\|run_batt.phase2_inline_batch" run3.log
```

## Cell 5: Compare Results
```bash
%%bash
echo "=== COMPARISON SUMMARY ==="
echo ""
echo "Run 1 (Cold Cache):"
grep "Hit Rate" run1.log
grep "Time Saved" run1.log
echo ""
echo "Run 2 (Warm Cache):"
grep "Hit Rate" run2.log
grep "Time Saved" run2.log
echo ""
echo "Run 3 (Hot Cache):"
grep "Hit Rate" run3.log
grep "Time Saved" run3.log
echo ""
echo "=== TIMING COMPARISON ==="
echo "Inlining time:"
grep "utils.inline_variables.total" run*.log
echo ""
echo "Validation time:"
grep "run_batt.check_solver_speed" run*.log
```

## Cell 6: Check Cache Size
```bash
%%bash
echo "=== CACHE ANALYSIS ==="
echo "Validation cache entries:"
ls .cache/validation/ | wc -l
echo ""
echo "Inlining cache entries:"
ls .cache/inlining/ | wc -l
echo ""
echo "Cache disk usage:"
du -sh .cache/
echo ""
echo "Sample validation cache:"
ls -lh .cache/validation/ | head -5
echo ""
echo "Sample inlining cache:"
ls -lh .cache/inlining/ | head -5
```

## Expected Output Pattern

### Run 1 (Cold Cache):
```
Inlining Cache:
  Hits: ~400-600
  Misses: ~150-250
  Hit Rate: 60-75%
  Time Saved: ~60-90s

utils.inline_variables.total    2.500-3.000
run_batt.check_solver_speed     2.500-2.800
```

### Run 2 (Warm Cache):
```
Inlining Cache:
  Hits: ~700-900
  Misses: ~20-50
  Hit Rate: 90-95%
  Time Saved: ~120-150s

utils.inline_variables.total    0.500-1.000  ← 3-5x FASTER!
run_batt.check_solver_speed     1.000-1.500  ← 2x FASTER!
```

### Run 3 (Hot Cache):
```
Inlining Cache:
  Hits: ~800-1000
  Misses: ~0-10
  Hit Rate: 98-100%
  Time Saved: ~150-180s

utils.inline_variables.total    0.100-0.300  ← 10-30x FASTER!
run_batt.check_solver_speed     0.500-0.800  ← 3-5x FASTER!
```

## Quick Test (5 tasks, faster)

If you want a faster test:

```bash
%%bash
echo "=== QUICK TEST (5 tasks) ==="
bash run_card.sh -o -i -c 5 -T -g
echo "=== RUN 2 ==="
bash run_card.sh -o -c 5 -T -g

# Compare
echo "=== RESULTS ==="
grep "Hit Rate" *.log
grep "Time Saved" *.log
```

## Success Indicators

✅ **Cache is working if**:
- Hit rate increases from run 1 → run 2 → run 3
- Time saved increases each run
- Inlining time decreases dramatically
- Cache files appear in .cache/ directory

⚠️ **Issues if**:
- Hit rate stays at 0%
- Time saved doesn't increase
- No .cache/ directory created
- Errors about missing batt_cache module

## After Testing

Copy the final comparison summary and update:
- WEEK6A_CACHE_SUCCESS.md with Kaggle results
- Create commit with actual performance data
- Share results!

🚀 **Ready to test on Kaggle!**
