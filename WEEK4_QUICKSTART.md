# Week 4: GPU Conversion Quick Start Guide

## 🎯 Goal
Convert 20-50 solvers from `o_g()` to `o_g_t()` to enable GPU acceleration on large grids.

**Expected Result**: 2-6x speedup on individual solvers, 2.0-2.5x average speedup across all tasks.

## 📋 Prerequisites

✅ Week 1-3 completed:
- Hybrid GPU o_g_t() implemented
- 100% correctness validated on Kaggle
- 70-cell threshold optimized

✅ Current status:
- CPU mode working (no -g flag)
- Generated batt imports gpu_env
- Ready for solver conversion

## 🚀 Three Ways to Convert

### Option 1: Fully Automated (Recommended)

Convert and test top 20 candidates in one command:

```bash
python week4_gpu_workflow.py --convert 20 --test
```

This will:
1. Analyze all solvers
2. Convert top 20 high-priority candidates
3. Test each conversion
4. Generate success report

### Option 2: Manual Selection

Convert specific solvers you've identified:

```bash
python week4_gpu_workflow.py --solvers solve_36d67576 solve_36fdfd69 solve_1a07d186 --test
```

### Option 3: Step by Step

```bash
# 1. Analyze all solvers
python analyze_solvers_for_gpu.py

# 2. Convert high-priority solvers
python convert_solver_to_gpu.py solve_36d67576 solve_36fdfd69

# 3. Test each one
python run_test.py -q -i 36d67576
python run_test.py -q -i 36fdfd69
```

## 📊 Analysis Tool

Find the best candidates for GPU conversion:

```bash
# Show top 50 candidates
python analyze_solvers_for_gpu.py

# Show top 20 only
python analyze_solvers_for_gpu.py --top 20
```

Output shows:
- **GPU Score**: Higher = better candidate
- **Mean Size**: Grid size in cells (70+ = GPU beneficial, 100+ = high priority)
- **o_g Count**: Number of o_g calls to convert
- **Status**: Priority level

Example output:
```
Task ID      Score  Mean Size    o_g    o_g_t    Samples  Status
---------------------------------------------------------------------------
36d67576     31     168.5        3      0        4        🎯 HIGH PRIORITY
36fdfd69     28     145.2        2      0        3        🎯 HIGH PRIORITY
1a07d186     15     95.3         1      0        3        ⭐ GOOD CANDIDATE
```

## 🔧 Conversion Tool

Convert individual solvers:

```bash
# Dry run (preview changes)
python convert_solver_to_gpu.py solve_36d67576 --dry-run

# Convert
python convert_solver_to_gpu.py solve_36d67576

# Convert and test
python convert_solver_to_gpu.py solve_36d67576 --test

# Convert multiple
python convert_solver_to_gpu.py solve_36d67576 solve_36fdfd69 solve_1a07d186
```

What it does:
- Finds `o_g(` calls in solver
- Replaces with `o_g_t(`
- Creates backup (`.bak` file)
- Optionally runs tests

## 🧪 Testing

After conversion, always test:

```bash
# Test single solver
python run_test.py -q -i 36d67576

# Expected output:
# 1 out of 1 tasks solved correctly (0 new).
```

If test fails:
1. Check the conversion wasn't applied to non-o_g functions
2. Verify the solver logic is correct
3. Restore from `.bak` file if needed

## 📈 Tracking Progress

### Current Status
```bash
# Check how many solvers already use o_g_t
grep -c "o_g_t(" solvers_pre.py

# Check how many still use o_g
grep -c "o_g(" solvers_pre.py | grep -v "o_g_t"
```

### Week 4 Todo List Progress

Track your conversions:

```markdown
Week 4 Progress:
- [ ] Phase 1: Convert 10 high-priority solvers (mean ≥100 cells)
- [ ] Phase 2: Test all conversions on laptop
- [ ] Phase 3: Deploy to Kaggle, measure speedup
- [ ] Phase 4: Convert 10 more good candidates (70-99 cells)
- [ ] Phase 5: Final validation and performance report
```

## 🎯 Prioritization

### High Priority (Convert First)
- Mean grid size ≥100 cells
- Multiple o_g calls (3+)
- Multiple samples (3+ demos)

**Example**: `solve_36d67576` - 168.5 mean cells, 3 o_g calls

### Good Candidates (Convert Next)
- Mean grid size 70-99 cells
- 1-2 o_g calls
- 2+ samples

**Example**: `solve_1a07d186` - 95.3 mean cells, 1 o_g call

### Low Priority (Skip for Now)
- Mean grid size <70 cells (CPU faster)
- No o_g calls
- Already uses o_g_t

## 🏁 Validation on Kaggle

After converting 20-50 solvers locally:

```bash
# 1. Commit changes
git add solvers_pre.py
git commit -m "Week 4: Convert 20 solvers to GPU o_g_t"
git push

# 2. On Kaggle, run validation
bash run_card.sh -i -b -c -32

# 3. Measure execution time
# Before: ~80 seconds for 32 tasks
# After:  ~40-50 seconds for 32 tasks (expected)
```

## 📊 Expected Results

Based on Week 3 validation (8,616 real grids):

### Grid Size Distribution
- Mean: 168 cells
- Median: 100 cells
- 65% are ≥70 cells (GPU beneficial)
- 57% are ≥100 cells (strong GPU speedup)

### Speedup Expectations
- **Individual solvers**: 2-6x faster on large grids
- **Average across tasks**: 2.0-2.5x faster
- **run_batt.py**: 40-50% reduction in execution time

### Success Criteria
- ✅ 100% correctness maintained (no wrong answers)
- ✅ All converted solvers pass tests
- ✅ Measurable speedup on Kaggle (30-40 seconds saved per 32 tasks)

## 🔄 Workflow Summary

```
1. Analyze      →  python week4_gpu_workflow.py --convert 20 --test
2. Review       →  Check test results, fix failures
3. Validate     →  git commit && git push
4. Deploy       →  Run on Kaggle: bash run_card.sh -i -b -c -32
5. Measure      →  Compare before/after execution time
6. Iterate      →  Convert more solvers if needed
```

## 🆘 Troubleshooting

### Problem: Conversion tool can't find solver
**Solution**: Check solver name format (must be `solve_TASKID`)
```bash
grep "def solve_36d67576" solvers_pre.py
```

### Problem: Test fails after conversion
**Solution**: Check if conversion was correct
```bash
# Restore backup
cp solvers_pre.py.bak solvers_pre.py

# Try dry run first
python convert_solver_to_gpu.py solve_36d67576 --dry-run
```

### Problem: No solvers found with high priority
**Solution**: Already optimized! Check current status:
```bash
python analyze_solvers_for_gpu.py --top 10
# Look for "Already optimized" status
```

### Problem: Tests pass locally but fail on Kaggle
**Solution**: GPU availability issue
```bash
# On Kaggle, check GPU status
python -c "import cupy; print('GPU available' if cupy.cuda.is_available() else 'No GPU')"

# Check if gpu_env is loaded
grep "from gpu_env" solvers_pre.py
```

## 📚 Related Documentation

- `GPU_ACCELERATION_STRATEGY.md` - Why this approach works
- `GPU_MODE_BROKEN.md` - Why NOT to use -g flag
- `.github/copilot-instructions.md` - Complete GPU status
- Week 1-3 documentation in archive

## 🎉 Success Metrics

After completing Week 4:

✅ **Correctness**: All solvers pass tests (100% maintained)
✅ **Coverage**: 20-50 solvers converted
✅ **Performance**: 2.0-2.5x average speedup
✅ **Production**: 40-50% faster run_batt.py
✅ **Validation**: Tested on Kaggle with real GPU

**Goal**: Cut solver execution time in half with zero risk to correctness!
