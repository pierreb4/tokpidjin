# Profiling Guide - Quick Reference

## Updated: October 15, 2025

This guide covers the improved `profile_batt_framework.py` with enhanced search and reporting capabilities.

---

## Quick Commands

### 1. Standard Profiling (Top 100 functions)
```bash
python profile_batt_framework.py --tasks 100
```
- Profiles 100 tasks
- Generates report with top 100 functions
- Output: `profile_batt_framework_TIMESTAMP.txt`

### 2. Search for Specific Functions ⭐ **NEW**
```bash
python profile_batt_framework.py --tasks 100 --search mapply_t apply_t o_g objects
```
- Profiles 100 tasks
- **Searches for specific function names** (mapply_t, apply_t, o_g, objects)
- **Shows times even if not in top 100!**
- Useful for finding "missing" functions

### 3. Get ALL Functions (Complete Data)
```bash
python profile_batt_framework.py --tasks 100 --all
```
- Profiles 100 tasks
- Includes **ALL functions** in report (not just top 100)
- WARNING: Large output file (~10MB+)
- Use for comprehensive analysis

### 4. Combination: Search + Full Report
```bash
python profile_batt_framework.py --tasks 100 --search mapply_t apply_t --all
```
- Shows search results immediately
- Saves complete report with all functions

### 5. Custom Top N
```bash
python profile_batt_framework.py --tasks 100 --top 200
```
- Profiles 100 tasks
- Shows top 200 functions (instead of default 100)

---

## For Stage 1 Investigation

### Finding Missing mapply_t and apply_t

**Problem**: These functions disappeared from top 5 DSL functions after Stage 1 optimizations.

**Solution**: Use search mode!

```bash
python profile_batt_framework.py --tasks 100 --search mapply_t apply_t
```

This will show:
- Exact times for mapply_t and apply_t
- Call counts
- Per-call time
- **Even if they're not in top 100 anymore!**

### Comparing Multiple Functions

```bash
python profile_batt_framework.py --tasks 100 --search mapply_t apply_t o_g objects apply merge
```

Shows all DSL functions we care about in one view.

### Full Investigation

```bash
python profile_batt_framework.py --tasks 100 --search mapply_t apply_t o_g objects --all
```

- Immediate console output with search results
- Complete file with all function data
- Best for thorough investigation

---

## Understanding Output

### Console Output (Search Results)

```
================================================================================
FUNCTION SEARCH RESULTS
================================================================================

Pattern: 'mapply_t' (2 matches)
--------------------------------------------------------------------------------
Function                                      Calls   Cum Time   Per Call
--------------------------------------------------------------------------------
mapply_t                                        700      1.234s     1.763ms
mapply_t_helper                                 700      0.045s     0.064ms

Pattern: 'apply_t' (1 matches)
--------------------------------------------------------------------------------
Function                                      Calls   Cum Time   Per Call
--------------------------------------------------------------------------------
apply_t                                         700      1.567s     2.239ms
```

### File Output Structure

1. **Category Summary**: Time by category (Framework, DSL, etc.)
2. **Detailed Function Listings**: Top functions per category
3. **Full Profiling Stats**: Complete pstats output

---

## Tips for Stage 1 Investigation

### 1. Get Baseline and Stage 1 Data

**Baseline (Phase 1 code)**:
```bash
git checkout <phase1_commit>
python profile_batt_framework.py --tasks 100 --search mapply_t apply_t o_g objects
# Save output as baseline_search.txt
```

**Stage 1 (current code)**:
```bash
git checkout main
python profile_batt_framework.py --tasks 100 --search mapply_t apply_t o_g objects
# Save output as stage1_search.txt
```

### 2. Compare Times Directly

Create a comparison table:

| Function | Baseline | Stage 1 | Change | Expected |
|----------|----------|---------|--------|----------|
| mapply_t | 2.148s | ??? | ??? | 1.75-1.95s |
| apply_t | 2.106s | ??? | ??? | 1.90-2.00s |
| o_g | 1.430s | 1.506s | +5% | 1.23-1.29s |
| objects | 1.374s | 1.449s | +5% | 1.17-1.24s |

### 3. Check Call Counts

Use search to verify:
- Did call counts change?
- Baseline: 700 calls to mapply_t
- Stage 1: ??? calls (should be same)

### 4. Multiple Runs for Variance

```bash
# Run 3 times, check consistency
for i in 1 2 3; do
    python profile_batt_framework.py --tasks 100 --search mapply_t apply_t o_g objects
    sleep 5
done
```

---

## Common Questions

### Q: Function not showing in top 100, is it gone?
**A**: No! Use `--search` to find it:
```bash
python profile_batt_framework.py --tasks 100 --search <function_name>
```

### Q: How to get complete data for analysis?
**A**: Use `--all` flag:
```bash
python profile_batt_framework.py --tasks 100 --all
```

### Q: Search returns no matches?
**A**: Check spelling, try partial names:
```bash
python profile_batt_framework.py --tasks 100 --search apply map merge
```

### Q: Output file too large with --all?
**A**: Use `--top 200` or `--top 500` instead:
```bash
python profile_batt_framework.py --tasks 100 --top 200
```

---

## Next Steps for Stage 1 Investigation

1. **Run search mode on Kaggle**:
   ```bash
   python profile_batt_framework.py --tasks 100 --search mapply_t apply_t o_g objects apply
   ```

2. **Compare with baseline**: Get exact times for "missing" functions

3. **Analyze results**: Determine if optimizations worked or failed

4. **Update PHASE2_STAGE1_RESULTS.md** with actual data

---

## Troubleshooting

### Error: "TypeError: Cannot create or construct a pstats.Stats object"
**Fixed!** Updated script to pass `stats` directly (not `stats.stats`)

### Error: "No module named 'pstats'"
```bash
# Shouldn't happen (standard library), but if it does:
pip install --upgrade python
```

### Output file not created
Check permissions in current directory:
```bash
ls -la profile_batt_framework_*.txt
```

---

**Updated**: October 15, 2025  
**For**: Phase 2 Stage 1 investigation  
**Key Feature**: `--search` flag to find "missing" optimized functions
