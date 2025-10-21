# Quick Reference: Profile inline_variables() Timeout

## Current Settings
- **utils.py:322**: `timeout_seconds=1` (default)
- **run_batt.py:1560, 1808**: `timeout_per_item=1` (batch operations)
- **Performance target**: Catch infinite loops while allowing normal solvers (<100ms)

## Commands to Run on Server

### Step 1: Generate a batt module (if needed)
```bash
timeout 120 bash run_card.sh -c -1
```
This creates `tmp_batt_onerun_run.py` needed by the profilers.

### Step 2: Run isolated profiling (RECOMMENDED - START HERE)
```bash
python profile_inline_isolated.py | tee profile_inline_isolated.log
```

**What it does:**
- Tests 20 random solvers with current timeout
- Tests 10 random differs with current timeout
- Shows timing distribution and statistics
- **Duration**: ~10-30 seconds

**Expected output:**
```
Found 50 solvers and 20 differs
solve_36d67576        :  120.34ms - OK
solve_36fdfd69        :   58.31ms - OK
...
SOLVER STATISTICS:
  Completed:  20/20
  Mean time:  45.23ms
  Max time:   120.34ms
  Min time:    0.98ms
```

### Step 3: Run stress test (if you need to find optimal timeout)
```bash
python profile_inline_stress.py | tee profile_inline_stress.log
```

**What it does:**
- Tests all solvers with timeouts: 0.1s, 0.5s, 1.0s, 2.0s, 5.0s
- Shows success rate at each timeout level
- Recommends optimal timeout
- **Duration**: ~30-60 seconds

**Expected output:**
```
Timeout | Success | Timeout | Error | Success% | Avg Time
  0.1s |      20 |       5 |     0 |    66.7% |    15.23ms
  0.5s |      28 |       2 |     0 |    93.3% |    25.15ms
  1.0s |      30 |       0 |     0 |   100.0% |    30.23ms
  2.0s |      30 |       0 |     0 |   100.0% |    35.45ms

RECOMMENDATIONS:
✓ 1.0s timeout is working well
  Recommendation: Keep at 1.0s unless profiling shows otherwise
```

### Step 4: Verify with real run
```bash
bash run_card.sh -c -32 2>&1 | tee profile_inline_verify.log
```

Check for inlining errors:
```bash
grep -i "timeout\|error.*inline" profile_inline_verify.log
```

## Decision Tree: What Timeout to Use?

| Observation | Decision |
|-------------|----------|
| All solvers < 50ms, no timeouts | ✅ Reduce to **0.5s** (faster error detection) |
| All solvers < 100ms, no timeouts | ✅ Keep **1.0s** (current, safe) |
| Some solvers 100-200ms, no timeouts | ✅ Keep **1.0s** or try **0.5s** |
| Some solvers 200-500ms, no timeouts | ✅ Keep **1.0s** (reasonable) |
| Solvers > 500ms, no timeouts | ⚠️ Increase to **2.0s** or investigate |
| Multiple timeouts at 1.0s | 🔍 Check if AST errors or legitimate slow inlining |
| Timeouts disappear at 2.0s | ✅ Increase to **2.0s** |

## Adjusting the Timeout

### Option 1: Change in utils.py (affects everything)
```bash
# Reduce to 0.5 seconds
sed -i 's/timeout_seconds=1/timeout_seconds=0.5/' utils.py

# Or increase to 2 seconds
sed -i 's/timeout_seconds=1/timeout_seconds=2/' utils.py

# Then verify
grep "def inline_variables" utils.py
```

### Option 2: Change in run_batt.py (affects batch operations only)
```bash
# Increase batch timeout to 2 seconds
sed -i 's/timeout_per_item=1/timeout_per_item=2/' run_batt.py

# Then verify
grep "timeout_per_item=" run_batt.py
```

### Option 3: Manual editing
```bash
# Edit the file directly
vim utils.py
# Find line 322, change timeout_seconds value

vim run_batt.py
# Find lines 1560, 1808, change timeout_per_item value
```

## Analysis Commands

### Quick analysis
```bash
# Show timing distribution
grep -E '[0-9]+\.[0-9]+ms' profile_inline_*.log | head -20

# Count timeouts
grep -c 'TIMEOUT' profile_inline_*.log

# Count errors
grep -c 'ERROR' profile_inline_*.log
```

### Detailed analysis
```bash
# Show statistics
grep -A 10 'STATISTICS:' profile_inline_*.log

# Show percentiles (from stress test)
grep -A 3 'Percentiles:' profile_inline_*.log

# Show recommendations
grep -A 5 'RECOMMENDATIONS' profile_inline_*.log
```

## Typical Results

### Good result (current timeout is fine)
```
Isolated profiling:
  All < 100ms: ✓ OK
  Max: 120ms
  Mean: 45ms
  
Stress test:
  1.0s timeout: 100% success rate
  
Recommendation: Keep 1.0s
```

### Shows we can be more aggressive
```
Isolated profiling:
  All < 50ms: ✓ OK
  Max: 48ms
  Mean: 20ms
  
Stress test:
  0.5s timeout: 100% success rate
  1.0s timeout: 100% success rate
  
Recommendation: Reduce to 0.5s for faster error detection
```

### Shows we need to be more conservative
```
Isolated profiling:
  Some 200-500ms: ⚠️ Borderline
  Max: 485ms
  Mean: 150ms
  
Stress test:
  1.0s timeout: 90% success (3 timeouts)
  2.0s timeout: 100% success
  
Recommendation: Increase to 2.0s
```

## Files Modified by Profiling

- `PROFILE_INLINE_VARIABLES.md` - Comprehensive documentation
- `profile_inline_isolated.py` - Isolated profiling tool
- `profile_inline_stress.py` - Stress test with different timeouts
- `profile_inline_commands.sh` - Quick reference commands

## Summary Workflow (5 minutes on server)

1. **Generate batt** (if needed): `timeout 120 bash run_card.sh -c -1` (1-2 min)
2. **Profile**: `python profile_inline_isolated.py | tee log.txt && tail -50 log.txt` (30 sec)
3. **Analyze**: Check if all < 100ms and no errors
4. **Decide**: Use decision tree above to choose new timeout (if needed)
5. **Adjust**: `sed -i 's/timeout_seconds=1/timeout_seconds=X/' utils.py` (optional)
6. **Verify**: `git diff utils.py` to confirm change, commit

Done! You now know the optimal timeout for your workload.
