# Profile inline_variables() Timeout - Final Answer

## The Simple Truth

The `inline_variables()` function **already has built-in profiling**. To profile it:

### One Command on Server

```bash
bash run_card.sh -o -T -c -32 2>&1 | tee profile.log
```

That's it. Just run the pipeline with 32 tasks, single optimization loop, with timing enabled. The profiling happens automatically.

## Time Investment

- **Runtime**: 2-5 minutes (to run 32 tasks)
- **Analysis**: 1 minute (look at logs)
- **Total**: ~5-10 minutes

## What You Get

After running that command, check the results:

```bash
# Check for any timeout issues
grep -i timeout profile.log

# Check for any errors
grep -i "error.*inline" profile.log

# See summary statistics
tail -50 profile.log
```

## Decision Tree

| Observation | Action |
|-------------|--------|
| No timeouts, all quick | ✅ Keep 1.0s timeout |
| Multiple timeouts | ⚠️ Increase to 2.0s |
| All inline < 50ms | ✅ Can reduce to 0.5s |
| All inline < 100ms | ✅ Keep 1.0s |

## Adjust Timeout (if needed)

```bash
# Reduce to 0.5s
sed -i 's/timeout_seconds=1/timeout_seconds=0.5/' utils.py

# Increase to 2s
sed -i 's/timeout_seconds=1/timeout_seconds=2/' utils.py

# Verify
grep "def inline_variables" utils.py

# Commit
git add utils.py && git commit -m "tune: Adjust inline_variables timeout"
```

## Current Settings

| File | Line | Setting |
|------|------|---------|
| `utils.py` | 322 | `timeout_seconds=1` |
| `run_batt.py` | 1560 | `timeout_per_item=1` |
| `run_batt.py` | 1808 | `timeout_per_item=1` |

## Files Available

- `profile_inline_timeout.sh` - Bash script to run profiling
- `profile_inline_guide.py` - Quick reference guide
- `PROFILE_INLINE_TL_DR.md` - Original quick reference
- `PROFILE_INLINE_QUICK_START.md` - Detailed reference
- Other docs archived or deprecated

## That's All You Need

1. **Run**: `bash run_card.sh -o -T -c -32 2>&1 | tee profile.log`
2. **Check**: `grep -i timeout profile.log`
3. **Decide**: Use decision tree above
4. **Adjust** (if needed): One `sed` command
5. **Verify**: `git commit`

The inline_variables() profiling is built in. Just run the pipeline with -T flag!
