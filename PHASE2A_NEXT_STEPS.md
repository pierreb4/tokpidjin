# 🎯 ACTION PLAN - PHASE 2A FULL VALIDATION

**Current Status**: ✅ Single-task test passed  
**Next Action**: Run 100-task validation  
**Commit**: 8eaea6da (results documented)  
**Expected Timeline**: 1-2 hours on Kaggle

---

## What We Know So Far

### ✅ Single-Task Test Results (0.858s)

**Code Status**:
- ✅ Compiles without errors
- ✅ Runs successfully
- ✅ Generates solvers (32 created)
- ✅ No crashes or exceptions
- ✅ GPU detected and initialized (2x L100)

**Cache Performance**:
- Inlining cache: **80% hit rate**
- Time saved: **19.2s** on single task
- Validation cache: 32 entries (first run)

**Framework Breakdown** (0.858s total):
- asyncio overhead: 50% (framework)
- JSON/file I/O: 23% (I/O)
- Solver expansion: 12% (code gen)
- DSL operations: 5% (too small to measure on 1 task)
- Other: 2%

### ⚠️ Limitation

**Why we need 100 tasks**:

On 1 task:
- objects() calls: ~40 (too small to measure)
- Phase 2a saves: ~50ms (hidden in noise)
- DSL overhead: ~5% (too small to see improvements)

On 100 tasks:
- objects() calls: ~3,400 (large enough to measure)
- Phase 2a saves: ~50-100ms per batch (visible)
- DSL overhead: ~30-35% (clearly visible)

---

## 🚀 FULL VALIDATION COMMAND

### Run This on Kaggle

```bash
cd /Users/pierre/dsl/tokpidjin
git pull origin main  # Get latest (commit 8eaea6da)
python run_batt.py -c 100 --cprofile --cprofile-top 30
```

### Expected Duration

- Task generation: ~30-40s
- Solver evaluation: ~40-50s
- Profiling overhead: ~5-10s
- **Total**: ~80-100s (with profiler)
- **Without profiler** (`--timing`): ~50-60s

### What to Expect in Output

```
Kaggle GPU Support: True (2 devices)
✓ Kaggle GPU Optimizer initialized

... progress output ...

Solvers generated: 13,200
Errors: 0

[cProfile output - 100 tasks]
ncalls  cumtime  function
 3400   ~1.2-1.3s  objects()    ← IMPROVED from 1.402s
 3400   ~1.35-1.4s  o_g()
  700   ~0.36-0.39s  objects_t()  ← IMPROVED from 0.425s
  ...

Wall-clock: 3.08-3.15s  (target vs 3.23s baseline)
```

---

## 📊 EXPECTED RESULTS

### Success Criteria

| Metric | Target | Success |
|--------|--------|---------|
| Wall-clock | < 3.23s | ✅ Any improvement |
| Solvers | 13,200 | ✅ Exact count |
| Errors | 0 | ✅ None |
| Success | 100% | ✅ All pass |

### Performance Expectations

| Scenario | Wall-Clock | Assessment |
|----------|-----------|-----------|
| **Conservative** | 3.18s | ✅ -0.05s minimum |
| **Target** | 3.10s | ✅ -0.13s good |
| **Optimistic** | 3.05s | ✅ -0.18s excellent |

### Per-Function Improvements

| Function | Current | Expected | Improvement |
|----------|---------|----------|-------------|
| objects() | 1.402s | 1.20-1.30s | -8-15% ✅ |
| objects_t() | 0.425s | 0.36-0.39s | -8-15% ✅ |
| o_g() | 1.427s | 1.35-1.40s | -2-5% ✅ |
| **Total DSL** | 4.648s | 4.40-4.50s | -3-5% ✅ |

---

## 📋 CAPTURE THESE METRICS

When you run the 100-task test, capture:

```
1. Wall-clock time
   - Total execution time (target: 3.08-3.15s)
   - Compare with Phase 1b baseline (3.23s)
   
2. Per-function times (from cProfile output)
   - objects() cumtime (look for line with dsl.py:3089)
   - o_g() cumtime (look for line with dsl.py:508)
   - objects_t() cumtime (look for line with dsl.py:3149)
   
3. Correctness metrics
   - Solvers generated (target: 13,200)
   - Error count (target: 0)
   - Success rate (target: 100%)
   
4. Environment
   - GPU info (should show 2x L100)
   - Profiler run (--cprofile --cprofile-top 30)
```

---

## 🔄 AFTER YOU GET RESULTS

### If Results Are Good (≥ -0.05s improvement)

1. ✅ Document in PHASE2A_FULL_RESULTS.md
2. ✅ Calculate actual speedup percentage
3. ✅ Verify objects() improved as expected
4. ✅ **Proceed to Phase 2a Step 2** (loop optimization)
   - Add early termination for edge cases
   - Expected: -2-5% additional
   - Total Phase 2a target: -1-3% → can reach -3-8%

### If Results Are Excellent (≥ -0.15s improvement)

1. ✅ Document results
2. ✅ Verify Phase 2a success
3. ✅ Consider **Phase 2b GPU acceleration** immediately
   - Expected: -5-15% additional
   - Could reach -8-20% total for Phase 2
   - Highest ROI per effort

### If Results Disappoint (< -0.05s)

1. ⚠️ Debug the difference
2. Check if profiler overhead masks improvement
3. Run **without profiler** to get true wall-clock
4. Verify objects() was actually called in profiler output
5. Consider alternative optimization approaches

---

## 🛠️ COMMAND OPTIONS

### Option 1: Full Profiling (Recommended)
```bash
python run_batt.py -c 100 --cprofile --cprofile-top 30
```
- Detailed function-level data
- Perfect for validating improvements
- ~0.3-0.5s profiler overhead

### Option 2: Quick Wall-Clock
```bash
python run_batt.py -c 100 --timing
```
- Lightweight timing breakdown
- Less overhead than profiler
- Good for quick validation

### Option 3: Just Run (No Profiling)
```bash
python run_batt.py -c 100
```
- Fastest execution
- No profiler overhead
- Just wall-clock time

**Recommendation**: Use Option 1 first (full profiling), then Option 3 if you want to see true wall-clock without profiler overhead.

---

## 📝 DOCUMENTATION WORKFLOW

1. **Run the test**
   ```bash
   python run_batt.py -c 100 --cprofile --cprofile-top 30 > results.txt 2>&1
   ```

2. **Save the output**
   - Copy cProfile output
   - Note wall-clock time
   - Note solvers/errors

3. **Document results**
   - Create PHASE2A_FULL_RESULTS.md
   - Include: command, output, metrics, comparison
   - Assessment: success/excellent/investigate

4. **Decide next phase**
   - Phase 2a Step 2 (loop optimization)
   - Phase 2b (GPU acceleration)
   - Hybrid (both)

---

## 🎯 SUCCESS DEFINITION

### Phase 2a is SUCCESSFUL if:

```
✅ Wall-clock time:    < 3.23s
✅ Solvers generated:  13,200
✅ Errors:            0
✅ Success rate:      100%
✅ objects() improved: 1.402s → 1.20-1.30s (visible in profiler)
```

### Phase 2a is EXCELLENT if:

```
✅ Wall-clock time:    < 3.15s (-0.08s or better)
✅ objects() improved: 1.402s → 1.15-1.25s (-15% or better)
✅ All 4 success criteria met
```

---

## 📞 QUICK REFERENCE

| Need | Action |
|------|--------|
| Run test | `python run_batt.py -c 100 --cprofile --cprofile-top 30` |
| Just measure | `python run_batt.py -c 100 --timing` |
| See wall-clock | `python run_batt.py -c 100` |
| Check code | Look at commit abb3b604 (Phase 2a optimization) |
| Review results | See PHASE2A_VALIDATION_RESULTS.md (single task results) |
| Next steps | After 100-task run, create PHASE2A_FULL_RESULTS.md |

---

## ⏰ TIMELINE

```
Now:       Ready to run 100-task validation
+30min:    Test should complete
+35min:    Results documented
+40min:    Assessment and decision on Phase 2a Step 2 or Phase 2b
+2-3hrs:   Phase 2a Step 2 implementation (if chosen)
```

---

## 💡 KEY INSIGHTS FROM SINGLE-TASK TEST

1. **Code is solid**: No errors, compiles cleanly
2. **GPU ready**: 2x L100 detected and initialized
3. **Cache effective**: 80% inlining cache hit rate
4. **Framework dominant**: Framework takes 80%+ on small tasks, DSL will be visible on 100 tasks
5. **Ready to scale**: Infrastructure is solid for 100-task validation

---

## 🚀 READY TO PROCEED?

### Next Step:

**Run on Kaggle**:
```bash
python run_batt.py -c 100 --cprofile --cprofile-top 30
```

**Capture**:
- Wall-clock time
- objects() cumtime
- Solver count
- Error count

**Then**:
- Compare wall-clock with 3.23s baseline
- Calculate speedup percentage
- Decide Phase 2a Step 2 or Phase 2b

---

**Status**: ✅ READY FOR FULL 100-TASK VALIDATION

**Expected**: -1 to -3% improvement (0.08-0.15s savings on 3.23s baseline)

**Timeline**: ~30-50 seconds on Kaggle
