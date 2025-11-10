# Server Deployment Steps - Cache Cleanup Fix

## Quick Summary

**What was fixed:**
- Stale `__pycache__/fluff.cpython-39.pyc` causing 38 import errors
- Tasks appearing to take 15-45s (actually execute in 1-2s)
- 9.5% timeout rate

**Expected improvement:**
- 0 fluff errors
- 1-2% timeout rate (80-90% reduction)
- P95 latency < 5s (was 19.3s)

## Deployment Commands (Simone Server)

```bash
# 1. Pull latest changes
cd ~/dsl/tokpidjin
git pull && date

# Expected output: 3 commits
# - d5942cf: Cache cleanup in run_card.sh
# - 83855da: t_call import fix
# - ac0ac26: Results documentation

# 2. Clean stale cache manually (one-time cleanup)
rm -rf __pycache__
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null

# 3. Verify no fluff files remain
find . -name "*fluff*" 2>/dev/null

# Expected output: Empty (no fluff files)

# 4. Run initial cache cleanup (now automatic)
bash run_card.sh -i

# This will:
# - Clean __pycache__ automatically
# - Create solver/differ directories
# - Ready for normal operation

# 5. Test on small batch (optional verification)
bash run_card.sh -c -32

# Expected: Zero "No module named 'fluff'" errors
# Expected: ~32s total time (was 60-90s)

# 6. Monitor with follow.sh
bash follow.sh -q -i 60
```

## Verification Checklist

After deployment, verify:

- [ ] `git pull` shows 3 new commits
- [ ] `find . -name "*fluff*"` returns nothing
- [ ] `bash run_card.sh -i` completes without errors
- [ ] No "__pycache__" directories in root (cleaned automatically)
- [ ] Test run shows 0 "No module named 'fluff'" errors
- [ ] Logs show improved timeout rate

## Expected Log Changes

**Before (in logs/):**
```
No module named 'fluff'
[Multiple import errors]
Task timeout after 15s, 20s, etc.
```

**After:**
```
[No fluff errors]
Inlining telemetry: 100% success
Tasks complete in 1-2s
```

## Rollback (if needed)

```bash
# Revert to previous version
git reset --hard HEAD~3
rm -rf __pycache__
find . -type d -name __pycache__ -exec rm -rf {} +
```

## Production Run

Once verified, run full production:

```bash
# Option A: Single instance
bash run_card.sh -c -400

# Option B: Multi-instance (Week 6D approach)
# Terminal 1:
bash run_card.sh -c -200 &
# Terminal 2:
bash run_card.sh -c -200 &
# Monitor:
bash follow.sh -q -i 60
```

## Notes

- Cache cleanup now runs automatically on `bash run_card.sh -i`
- No manual cache management needed going forward
- The fix prevents future stale .pyc accumulation
- Expected total time improvement: 30-40% (from eliminating timeout waits)

## Troubleshooting

**If fluff errors persist:**
```bash
# Nuclear option - clean everything
find . -type f -name "*.pyc" -delete
find . -type d -name __pycache__ -delete
python3 -c "import sys; print(sys.executable)"  # Verify Python
```

**If timeout rate doesn't improve:**
- Check logs for different error types
- May indicate real compute bottlenecks (not cache issue)
- Run profiler: `python profile_outlier_tasks.py`

## Contact

Deployed: 2025-11-10 19:12 CET
Commits: d5942cf, 83855da, ac0ac26
Verified locally: ✅ (9/10 tasks, 0 fluff errors)
