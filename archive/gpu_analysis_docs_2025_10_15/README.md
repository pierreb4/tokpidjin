# GPU Analysis Docs Archive

**Date**: October 15, 2025  
**Reason**: Superseded by consolidated documentation

## What's Here

Recent GPU analysis documents from October 15, 2025:
- `ACTION_PLAN.md` - GPU optimization action plan
- `PIPELINE_PROFILING_RESULTS.md` - Pipeline profiling results (10 tasks)
- `GPU_OPTIMIZATION_ROADMAP.md` - Optimization roadmap
- `KAGGLE_VALIDATION_RESULTS.md` - Kaggle validation results
- `KAGGLE_GPU_EVALUATION.md` - GPU evaluation on Kaggle
- `RUN_BATT_GPU_ANALYSIS.md` - run_batt.py GPU analysis
- `GPU_STATUS_REALITY_CHECK.md` - GPU status check
- `WEEK4_QUICKSTART.md` - Week 4 quickstart guide
- `GPU_ACCELERATION_STRATEGY.md` - Acceleration strategy
- `GPU_MODE_BROKEN.md` - GPU mode issues

## Why Archived

These documents represented intermediate analysis and discoveries that are now consolidated into:

### Current Active Documentation
1. **PROFILING_README.md** - Complete Kaggle profiling guide
2. **PROFILING_SESSION_SUMMARY.md** - Session summary with scale analysis
3. **.github/copilot-instructions.md** - Development guidelines with profiling workflow

### Key Insights Preserved
- Pipeline profiling: Code gen 9%, Solver 91%
- Scale analysis: GPU ROI increases 25x from testing to production
- Competition resources: 8hr L4x4 GPU budget
- Profiling workflow: Must use Kaggle, not local

## What Changed

**Old approach**: Try to profile locally, optimize code generation  
**New approach**: Profile on Kaggle with GPU, optimize DSL operations

**Discovery**: Local profiling unreliable due to threading, code generation not the bottleneck

## Status

All valid insights from these documents are now in:
- Profiling guides (workflow, tools, expectations)
- Session summary (what we learned, scale analysis)
- Copilot instructions (development guidelines)

---

**Next**: Deploy profilers to Kaggle, identify real DSL bottlenecks
