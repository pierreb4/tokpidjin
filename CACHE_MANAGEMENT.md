# Cache Management Guide

## Overview

The caching system has built-in **automatic expiration** to prevent invalid or stale cache entries from causing issues.

### Current Status
- **Cache Directory**: `.cache/` (~20 MB)
- **TTL (Time-to-Live)**: 7 days (default)
- **Auto-expiration**: Enabled ✓
- **Invalid Entry Risk**: Minimal (expires automatically)

## How It Works

### Automatic Expiration on Startup
Every time `run_batt.py` starts:
1. Checks cache file modification times
2. Removes entries older than 7 days
3. Reports expiration stats

### TTL Configuration
Located in `batt_cache.py`:
```python
CACHE_TTL_SECONDS = 7 * 24 * 60 * 60  # 7 days

# To disable expiration:
CACHE_TTL_SECONDS = 0

# To change to 3 days:
CACHE_TTL_SECONDS = 3 * 24 * 60 * 60
```

## Management Commands

### View Cache Status
```bash
python cache_manage.py status
```
Shows:
- Cache statistics (hits, misses, hit rate)
- Disk usage (MB)
- TTL configuration
- Expiration status

### View Cache Size
```bash
python cache_manage.py size
```
Output:
```
Validation: 7.97 MB (8,353,421 bytes)
Inlining:   12.67 MB (13,289,452 bytes)
Total:      20.64 MB (21,642,873 bytes)
```

### Manually Expire Old Entries
```bash
# Use default TTL (7 days)
python cache_manage.py expire
```

### Refresh Cache (Keep Recent Only)
```bash
# Keep only entries less than 3 days old
python cache_manage.py refresh 3

# Keep only entries less than 1 day old
python cache_manage.py refresh 1
```

### Clear Entire Cache
```bash
# Clear all caches
python cache_manage.py clear

# Clear only validation cache
python cache_manage.py clear validation

# Clear only inlining cache
python cache_manage.py clear inlining
```

### Show Configuration
```bash
python cache_manage.py config
```
Output:
```
Cache Directory: .cache
TTL (Time-to-Live): 7.0 days (604800 seconds)
Status: Auto-expiration ENABLED
```

## When to Refresh Cache

### Refresh If:
1. **Solver logic changed** - Invalidates cached validation results
2. **Inlining logic changed** - Invalidates cached inlined code
3. **DSL functions modified** - Previous results may be incorrect
4. **Seeing unexpected timeouts** - May indicate stale cache
5. **After major bug fixes** - Ensure fresh data

### Keep Cache If:
1. **Running multiple times** - Same task_ids benefit from cache
2. **Small changes** - Only bug fixes in non-core logic
3. **Performance critical** - Avoiding re-computation

## Workflow Examples

### Development Workflow
```bash
# Run some tasks (cache builds up)
bash run_card.sh -c 10

# Make code changes
# ... edit dsl.py or expand_solver.py ...

# Refresh cache to invalidate affected entries
python cache_manage.py refresh 1

# Run again with fresh cache
bash run_card.sh -c 10
```

### Production Workflow
```bash
# Check cache status
python cache_manage.py status

# Run solver generation
bash run_card.sh -c 100

# Monitor cache growth
python cache_manage.py size

# Refresh if cache gets too large (>100 MB)
python cache_manage.py refresh 3
```

### Troubleshooting
```bash
# If seeing unexpected behavior:
python cache_manage.py status          # Check current state
python cache_manage.py refresh 1       # Keep only 1-day-old entries
bash run_card.sh -c 5                  # Re-run with fresh cache

# If cache is suspected corrupted:
python cache_manage.py clear           # Nuke everything
bash run_card.sh -c 5                  # Rebuild from scratch
```

## Cache Expiration Details

### What Gets Expired
- Validation results >7 days old
- Inlined code >7 days old
- Based on file modification time

### What Doesn't Get Expired
- In-memory cache (cleared on restart)
- Files <7 days old
- Files with invalid timestamps

### Auto-Expiration Trigger
Happens automatically when:
1. Python process imports `batt_cache.py`
2. First time `bash run_card.sh` runs each day
3. Manually via `python cache_manage.py expire`

## Preventing Invalid Cache Issues

### Root Cause
Previous issue where invalid cache entries caused score mismatches:
- Old entries stayed in cache indefinitely
- Code changes invalidated assumptions
- Stale data used for validation

### Solution
1. **TTL-based expiration**: Auto-delete old entries
2. **Manual refresh**: Remove specific old data
3. **Status monitoring**: Check cache health
4. **Clear option**: Complete wipe if needed

### Detection
If you suspect invalid cache:
```bash
# Check if entries are too old
python cache_manage.py config

# Look at file timestamps
ls -lt .cache/validation/ | head -10
ls -lt .cache/inlining/ | head -10

# If old, refresh
python cache_manage.py refresh 1
```

## Performance Impact

### Cache Benefits
- **Validation**: 87x faster (0.087s vs 0.001s)
- **Inlining**: 150x faster (0.150s vs 0.001s)
- **Typical run**: 5-10x faster with warm cache

### Expiration Impact
- **Startup time**: +100ms to check and delete files
- **One-time**: Happens first run per day (or manual)
- **Negligible**: Compared to actual work

## Debugging Cache Issues

### Monitor Expiration
```bash
# Check what's being expired
python -c "
from batt_cache import expire_old_cache_entries
stats = expire_old_cache_entries()
print(f'Expired: {stats}')
"
```

### Check Cache Size Growth
```bash
# Track size over time
for i in {1..7}; do
  echo "Day $i:"
  python cache_manage.py size | grep Total
  sleep 86400  # Wait 24 hours
done
```

### Validate Cache Entries
```bash
# Check if validation files are valid JSON
python -c "
import json
from pathlib import Path
for f in Path('.cache/validation').glob('*.json'):
    try:
        json.load(open(f))
    except:
        print(f'Invalid: {f}')
"
```

## Summary

| Command | Purpose | When to Use |
|---------|---------|------------|
| `status` | View cache health | Daily/weekly check |
| `size` | Check disk usage | Monitor growth |
| `expire` | Auto-expire old | Auto-run on startup |
| `refresh N` | Keep recent only | After code changes |
| `clear` | Full wipe | Troubleshooting |
| `config` | Show settings | Verify TTL config |

**Default behavior**: Automatic expiration on startup, no action needed. Manual commands available for specific needs.
