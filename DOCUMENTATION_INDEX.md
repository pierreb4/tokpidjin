# Documentation Index - November 4, 2025

## Current Active Documentation

### Core Status Documents
- **SOLVER_REGRESSION_ANALYSIS.md** - Complete analysis of solver regression (68→352 recovery)
- **TIMEOUT_ANALYSIS.md** - Root cause analysis of timeout issues (exceptions being masked)

### Quick Reference
- **README.md** - Main project documentation
- **QUICK_REFERENCE.md** - Quick lookup guide

### GPU Optimization (Batch Operations)
- **GPU_DOCS_INDEX.md** - GPU documentation index
- **GPU_README.md** - GPU optimization overview

### Configuration & Setup
- **RUN_BATT_ARGUMENTS.md** - Command-line arguments for run_batt.py
- **CACHE_MANAGEMENT.md** - Cache system documentation

### Archive Directory
All other documentation has been archived to `archive/` subdirectories organized by date and purpose:
- `archive/dsl_consolidation_2025_10_31/` - DSL consolidation attempts and analysis
- `archive/phase_1_2_3_4_2025_10_20/` - Phase-based optimization work
- `archive/quick_win_1_2025_10_18/` - Quick win optimization attempts
- `archive/profiling_analysis_2025_10_15/` - Profiling and analysis work

## Key Issues Resolved

1. **Solver Regression (68→352)**
   - Root cause: Phase 3 tuple conversion + consolidation
   - Solution: Restored to ff140d60 baseline
   - Status: ✅ RESOLVED

2. **Timeout Masking**
   - Root cause: Exceptions in call_with_timeout() treated as timeouts
   - Solution: Enabled exception logging in utils.py
   - Status: ✅ FIXED

3. **get_nth Function Error**
   - Root cause: card.py calling undefined get_nth() function
   - Solution: Changed to get_nth_t() in card.py
   - Status: ✅ FIXED

## Current Codebase Status

### Aligned with ff140d60 (Oct 14 working baseline)
- ✅ dsl.py (with TTT_iii type hints)
- ✅ arc_types.py (with TTT_iii type alias)
- ✅ constants.py (with INT_TYPE_RANGES, HINT_OVERLAPS)
- ✅ solvers_pre.py (400 solvers)

### Recent Fixes
- ✅ Enable exception logging in utils.py
- ✅ Replace undefined get_nth with get_nth_t in card.py

## For Next Session

When starting work:
1. Read SOLVER_REGRESSION_ANALYSIS.md for regression context
2. Read TIMEOUT_ANALYSIS.md for exception masking details
3. Check GPU_DOCS_INDEX.md for GPU optimization status
4. Use RUN_BATT_ARGUMENTS.md for run_batt.py options

For historical context, consult archived documentation organized by date and topic.
