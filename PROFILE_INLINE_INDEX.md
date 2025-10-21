# inline_variables() Timeout Profiling - Documentation Index

## Quick Links

| What You Need | File | Time |
|---------------|------|------|
| **Just want the commands?** | [`PROFILE_INLINE_TL_DR.md`](PROFILE_INLINE_TL_DR.md) | 5 min read |
| **Need a quick reference?** | [`PROFILE_INLINE_QUICK_START.md`](PROFILE_INLINE_QUICK_START.md) | 10 min read |
| **Want comprehensive guide?** | [`PROFILE_INLINE_VARIABLES.md`](PROFILE_INLINE_VARIABLES.md) | 20 min read |
| **Just run this script** | `python profile_inline_isolated.py` | 30 sec run |
| **Need stress testing** | `python profile_inline_stress.py` | 1 min run |
| **All commands reference** | [`profile_inline_commands.sh`](profile_inline_commands.sh) | Reference |

## What to Run on Server

**Recommended workflow:**

```bash
# 1. Generate batt (only if first run)
timeout 120 bash run_card.sh -c -1

# 2. Profile inline_variables timeout
python profile_inline_isolated.py 2>&1 | tee profile.log
tail -50 profile.log

# 3. Based on output, optionally stress test
python profile_inline_stress.py 2>&1 | tee stress.log
```

## Current Settings

| Location | Setting | Default | Why |
|----------|---------|---------|-----|
| `utils.py:322` | `timeout_seconds` | `1` | Catch infinite loops while allowing normal solvers |
| `run_batt.py:1560` | `timeout_per_item` | `1` | Batch solver inlining |
| `run_batt.py:1808` | `timeout_per_item` | `1` | Batch differ inlining |

## Documentation Structure

### For Different Audiences

**Developers:**
- Start with [`PROFILE_INLINE_TL_DR.md`](PROFILE_INLINE_TL_DR.md) - Quick commands and decision tree
- Run `python profile_inline_isolated.py` - Get real timing data
- Use output to decide if timeout needs adjustment
- Use `sed` one-liner to adjust if needed

**System Administrators:**
- Start with [`PROFILE_INLINE_QUICK_START.md`](PROFILE_INLINE_QUICK_START.md) - Detailed reference
- Run profilers on production machines
- Monitor timeout patterns
- Document changes for team

**Researchers/Advanced Users:**
- Read [`PROFILE_INLINE_VARIABLES.md`](PROFILE_INLINE_VARIABLES.md) - Comprehensive analysis
- Run both isolated and stress tests
- Analyze percentile distributions
- Profile different workload types

### Files in This Package

| File | Type | Purpose |
|------|------|---------|
| `profile_inline_isolated.py` | Script | Profile inline_variables on real solvers |
| `profile_inline_stress.py` | Script | Test optimal timeout with stress testing |
| `profile_inline_commands.sh` | Reference | All commands in one place |
| `PROFILE_INLINE_VARIABLES.md` | Guide | Comprehensive profiling strategy |
| `PROFILE_INLINE_QUICK_START.md` | Reference | Quick reference with examples |
| `PROFILE_INLINE_TL_DR.md` | Summary | Commands and decision guide |
| `PROFILE_INLINE_INDEX.md` | This file | Navigation and structure |

## How to Use This Package

### Step 1: Choose Your Starting Point

- **5 minutes available?** → [`PROFILE_INLINE_TL_DR.md`](PROFILE_INLINE_TL_DR.md)
- **15 minutes available?** → [`PROFILE_INLINE_QUICK_START.md`](PROFILE_INLINE_QUICK_START.md)
- **30+ minutes available?** → [`PROFILE_INLINE_VARIABLES.md`](PROFILE_INLINE_VARIABLES.md)

### Step 2: Run the Profilers

```bash
# Isolated profiling (RECOMMENDED - START HERE)
python profile_inline_isolated.py | tee profile.log

# Read the output summary
tail -50 profile.log
```

### Step 3: Make a Decision

Based on profiling output, use decision tree to choose timeout:
- All < 50ms → reduce to 0.5s
- All < 100ms → keep 1.0s
- Some timeouts → increase to 2.0s

### Step 4: Adjust and Verify

```bash
# Adjust if needed
sed -i 's/timeout_seconds=1/timeout_seconds=0.5/' utils.py

# Verify
grep "def inline_variables" utils.py

# Commit
git add utils.py && git commit -m "tune: Adjust inline_variables timeout"
```

## Expected Outputs

### Good Profile Result
```
SOLVER STATISTICS:
  Completed:  20/20
  Mean time:  45.23ms
  Max time:   120.34ms
  Min time:    0.98ms

OVERALL SUMMARY
Total tests:    30
Success:        30 (100.0%)
```

### Stress Test Result
```
Timeout | Success | Timeout | Error | Success% | Avg Time
  0.1s |      20 |       5 |     0 |    66.7% |    15.23ms
  0.5s |      28 |       2 |     0 |    93.3% |    25.15ms
  1.0s |      30 |       0 |     0 |   100.0% |    30.23ms
  2.0s |      30 |       0 |     0 |   100.0% |    35.45ms

RECOMMENDATIONS
✓ 1.0s timeout is working well
  Recommendation: Keep at 1.0s unless profiling shows otherwise
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Script says "Could not find tmp_batt_onerun_run.py" | Run `bash run_card.sh -c -1` first to generate a batt module |
| Profiling shows many timeouts | Run stress test to see if increasing timeout helps; might be AST errors |
| Profiling shows all very fast (< 20ms) | Can reduce timeout to 0.5s for faster error detection |
| Want to profile different task | Modify script to load specific batt module or task ID |

## Performance Baseline

Based on testing:
- **Normal solvers**: 20-100ms
- **Complex solvers**: 100-200ms
- **Edge cases**: 200-500ms
- **Pathological**: > 500ms (usually AST errors)

Current 1.0s timeout is conservative and handles all normal cases.

## Related Files

- `utils.py` - Contains `inline_variables()` function
- `run_batt.py` - Uses inlining in batch operations
- `batt_cache.py` - Caches inlined results
- `.cache/` - Cache directory (can get large)

## Key Takeaway

**One command gives you all the information:**
```bash
python profile_inline_isolated.py 2>&1 | tee profile.log && tail -50 profile.log
```

The output will tell you whether to:
1. Keep current 1.0s timeout ✓
2. Reduce to 0.5s (if all < 50ms) 
3. Increase to 2.0s (if seeing timeouts)

## Next Steps After Profiling

1. **If timeout is good**: No action needed, you're done
2. **If timeout should change**: 
   - Use `sed` one-liner to adjust
   - Commit change with rationale
   - Verify with `bash run_card.sh -c -32`
3. **If many AST errors**: 
   - Report error patterns
   - May need upstream fix in inlining logic
   - Can use `SKIP_INLINING=1` while investigating

## Questions?

- How do I run this? → See [`PROFILE_INLINE_TL_DR.md`](PROFILE_INLINE_TL_DR.md)
- What does the output mean? → See [`PROFILE_INLINE_QUICK_START.md`](PROFILE_INLINE_QUICK_START.md)
- Deep dive analysis? → See [`PROFILE_INLINE_VARIABLES.md`](PROFILE_INLINE_VARIABLES.md)
- All commands in one place? → See [`profile_inline_commands.sh`](profile_inline_commands.sh)
