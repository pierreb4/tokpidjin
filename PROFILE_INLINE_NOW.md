# Profile inline_variables() Timeout - One Command

## The Command

```bash
bash run_card.sh -o -c -32 2>&1 | tee profile.log
```

Run this on the server. That's it.

**Time**: 2-5 minutes

## Then Check Results

```bash
# Any timeouts?
grep -i timeout profile.log

# Any errors?
grep -i "error.*inline" profile.log

# Summary stats?
tail -50 profile.log
```

## Decision

| What You See | What To Do |
|---|---|
| No timeouts, quick | ✅ Keep 1.0s timeout |
| Multiple timeouts | ⚠️ Increase to 2.0s: `sed -i 's/timeout_seconds=1/timeout_seconds=2/' utils.py` |
| All < 50ms | ✅ Can reduce to 0.5s: `sed -i 's/timeout_seconds=1/timeout_seconds=0.5/' utils.py` |

## If You Adjust

```bash
# Verify the change
grep "def inline_variables" utils.py

# Commit
git add utils.py && git commit -m "tune: Adjust inline_variables timeout"
git push
```

## Current Settings

- `utils.py:322` - `timeout_seconds=1`
- `run_batt.py:1560` - `timeout_per_item=1` (solver inlining)
- `run_batt.py:1808` - `timeout_per_item=1` (differ inlining)

That's all you need to know!
