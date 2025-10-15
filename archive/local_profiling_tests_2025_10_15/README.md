# Local Profiling Tests Archive

**Date**: October 15, 2025  
**Reason**: Local profiling tests archived while deploying to Kaggle

## What's Here

### Test Files (Generated during local development)
- `test_100_tasks.py` / `test_100_tasks_call.py` - 100-task test generation
- `test_batt.py` / `test_batt_call.py` - Single batt test file
- `test_prof_batt.py` / `test_prof_batt_call.py` - Profiling test file
- `tmp_old.py` / `tmp_old_call.py` - Old temporary batt files

### Profiling Artifacts
- `card.profile` - cProfile output from card.py profiling
- `optimize_card.py` - Attempted code generation optimization (obsolete)

## Why Archived

These files were created during local development to test:
1. Code generation performance (card.py)
2. Local profiling attempts (found unreliable due to threading)
3. Scale testing (100 tasks)

**Key Finding**: Local profiling unreliable due to threading/multiprocessing obscuring DSL function times.

**Decision**: Profile on Kaggle with GPU instead (see PROFILING_README.md)

## What Replaced This

- **profile_batt_dsl.py**: Single-task profiler (works on Kaggle)
- **profile_batt_batch.py**: Multi-task aggregate profiler (primary tool)
- **tmp_batt_onerun_run.py**: Production batt file for Kaggle profiling

## Status

These files served their purpose in discovering that:
- Code generation is NOT the bottleneck (4s at 400 tasks)
- Solver execution IS the bottleneck (38.5s at 400 tasks)
- Must profile on Kaggle for accurate DSL timing data

All insights preserved in:
- `PROFILING_SESSION_SUMMARY.md`
- `PROFILING_README.md`
- `.github/copilot-instructions.md`

---

**Next**: Kaggle profiling with GPU to identify real DSL bottlenecks
