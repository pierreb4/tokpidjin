# Superseded GPU Documentation

This directory contains GPU documentation files that have been superseded by more comprehensive guides.

## Files in This Archive

### QUICK_REF.md
- **Created**: October 10, 2025
- **Superseded by**: GPU_PROJECT_SUMMARY.md
- **Content**: Quick reference for rot90 failure and fgpartition strategy
- **Why superseded**: Content consolidated into GPU_PROJECT_SUMMARY.md with more comprehensive analysis

### SUMMARY.md
- **Created**: October 10, 2025
- **Superseded by**: GPU_PROJECT_SUMMARY.md + INTEGRATION_GUIDE.md
- **Content**: Detailed explanation of rot90 failure, fgpartition strategy, and next steps
- **Why superseded**: Split into executive summary (GPU_PROJECT_SUMMARY.md) and integration guide (INTEGRATION_GUIDE.md)

### GPU_STRATEGY.md
- **Created**: October 10, 2025
- **Superseded by**: INTEGRATION_GUIDE.md
- **Content**: Which operations to accelerate, transfer cost analysis, implementation plan
- **Why superseded**: Content integrated into INTEGRATION_GUIDE.md with better structure

### GPU_OPTIMIZATION_APPLIED.md
- **Created**: October 10, 2025
- **Superseded by**: GPU_OPTIMIZATION_SUCCESS.md
- **Content**: Lessons learned from rot90 failure, what operations benefit from GPU
- **Why superseded**: Replaced by comprehensive GPU_OPTIMIZATION_SUCCESS.md covering the entire journey

## Historical Context

These files were created during the GPU optimization exploration phase when:
- rot90 GPU implementation showed 0.5x speedup (GPU 2x slower than CPU)
- Analysis revealed simple operations don't benefit from GPU due to transfer overhead
- Strategy shifted to focus on complex operations (fgpartition, gravitate)

The key insights from these files are now consolidated in:
- **GPU_PROJECT_SUMMARY.md** - Executive summary
- **INTEGRATION_GUIDE.md** - Practical integration guide
- **GPU_OPTIMIZATION_SUCCESS.md** - Complete optimization journey

## When to Reference These Files

These files are kept for historical reference and should be used only when:
- Understanding the evolution of GPU optimization strategy
- Researching why certain approaches were abandoned
- Learning from early mistakes (per-element transfers, no warmup, wrong thresholds)

For current GPU optimization work, always refer to the main documentation listed in **GPU_DOCS_INDEX.md**.

## Consolidation Date

**October 10, 2025** - Files moved to archive to reduce documentation clutter and avoid confusion.

---

**Note**: Do not update these files. If you need to document GPU optimization work, update the main documentation files instead.
