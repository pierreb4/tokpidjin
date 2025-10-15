# Action Plan - Let's Go! 🚀

## Current Status

✅ **Phase 1 Complete**: Pipeline profiled, bottlenecks identified  
🔴 **Blocker Found**: 0% accuracy issue  
🎯 **New Strategy**: Fix accuracy, then optimize code generation (not just solvers!)

---

## Immediate Actions (Priority Order)

### 1. 🔴 Investigate 0% Accuracy (ACTIVE NOW)

**Problem**: Profiling showed 0/35 samples correct

**Tool Created**: `diagnose_accuracy.py`

**Run on Kaggle**:
```bash
python diagnose_accuracy.py
```

**What it tests**:
1. ✅ Import: Can tmp_batt_onerun_run module be imported?
2. ✅ Execution: Do solvers run without errors?
3. ✅ Type compatibility: Is it a tuple vs list issue?
4. ✅ Function signature: Does batt() have correct parameters?
5. ✅ Validation logic: Are comparisons working correctly?

**Expected findings**:
- Type mismatch (tuple vs list)?
- Generated code has bugs?
- Solver import issues?
- Comparison logic broken?

**Next steps after diagnosis**:
- If type issue: Fix comparison in profiler or generated code
- If execution issue: Debug specific solver
- If import issue: Fix module generation
- If validation issue: Fix comparison logic

---

### 2. 🔴 Optimize Code Generation (Once accuracy fixed)

**Problem**: Code generation is 67% of pipeline time (78s at 400 tasks)

**Phase 2A: Profile card.py** (1 hour)
```bash
python -m cProfile -o card.profile card.py -c 10 -f test_batt.py
python -c "import pstats; p = pstats.Stats('card.profile'); p.sort_stats('cumulative').print_stats(20)"
```

**What to look for**:
- Which functions take most time?
- Is it solver loading? Code generation? Template processing?
- File I/O overhead?
- String operations?

**Phase 2B: Implement Optimizations** (2-3 days)

**Option A: Caching** (Quickest win)
- Cache generated code for known tasks
- Only regenerate if solver changed
- Store in `.cache/` directory
- Expected: 50-80% reduction

**Option B: Parallelization** (Medium effort)
- Generate 4-8 tasks simultaneously
- Use ProcessPoolExecutor
- Expected: 4-8x speedup

**Option C: Incremental Generation** (Higher effort)
- Only regenerate changed solvers
- Keep previously generated code
- Expected: 70-90% reduction on repeat runs

**Expected total savings**: 78s → 8-39s (39-70 seconds saved!)

---

### 3. 🔴 Integrate Batch Operations (After code gen optimization)

**Problem**: Solver execution is 33% of pipeline time (38.5s at 400 tasks)

**What to do**: Modify run_batt.py to use GPUBatchProcessor

**Implementation** (1-2 days):

**Step 1: Remove unused initialization**
```python
# run_batt.py line 87
# REMOVE: gpu_optimizer = KaggleGPUOptimizer(device_id=0)
```

**Step 2: Instantiate GPUBatchProcessor in check_batt()**
```python
if GPU_AVAILABLE and len(samples) >= 10:
    processor = GPUBatchProcessor(gpu_optimizer=KaggleGPUOptimizer())
    results = processor.process_batch(samples, batt_func)
else:
    # CPU fallback
    results = [process_sample_cpu(s, batt_func) for s in samples]
```

**Step 3: Test and validate**
- Test on 10 tasks
- Verify correctness
- Measure speedup
- Scale to 100+ tasks

**Expected savings**: 38.5s → 1.1-3.9s (34-37 seconds saved!)

---

### 4. 🟡 GPU DSL Operations (Complementary optimization)

**Timeline**: 4-6 weeks (start after batch ops working)

**Expected additional savings**: 2-4 seconds

**Still worth doing** with 8hr L4x4 budget, but lower priority than code gen optimization.

---

## Timeline

### Today (Oct 15)
- ✅ Created diagnostic tool
- 🔄 Run `diagnose_accuracy.py` on Kaggle
- 🔄 Identify and fix accuracy issue

### Tomorrow (Oct 16)
- ✅ Verify accuracy fixed
- 🔄 Profile card.py with cProfile
- 🔄 Analyze hotspots

### This Week (Oct 16-18)
- 🔄 Implement code generation caching
- 🔄 Test parallelization
- 🔄 Measure improvements
- 🎯 Target: 78s → 8-39s

### Next Week (Oct 19-20)
- 🔄 Integrate batch operations
- 🔄 Test and validate
- 🔄 Measure speedup
- 🎯 Target: 38.5s → 1.1-3.9s

### Week After (Oct 21+)
- ✅ Re-profile full pipeline
- ✅ Measure combined improvements
- ✅ Document results
- 🎯 Target: 116.8s → 10-50s total

---

## Success Metrics

### Phase 0: Accuracy Fix ✅
- 🎯 >90% accuracy on validation
- ✅ All solvers execute correctly
- ✅ No type mismatch issues

### Phase 1: Code Generation ✅
- 🎯 50-90% reduction (78s → 8-39s)
- ✅ Caching works correctly
- ✅ Parallelization stable
- ✅ No correctness regressions

### Phase 2: Batch Operations ✅
- 🎯 10-35x speedup (38.5s → 1.1-3.9s)
- ✅ GPU acceleration working
- ✅ CPU fallback works
- ✅ 100% accuracy maintained

### Combined ✅
- 🎯 116.8s → 10-50s total (58-91% reduction)
- 🎯 14x more iterations in 8hr budget
- ✅ Production-ready performance

---

## Files Ready to Use

1. ✅ `diagnose_accuracy.py` - Investigate 0% accuracy
2. ✅ `profile_pipeline.py` - Full pipeline profiling
3. ✅ `kaggle_gpu_evaluation.py` - GPU validation
4. ✅ `gpu_optimizations.py` - Batch operations (ready to integrate)

**Documentation**:
- ✅ `PIPELINE_PROFILING_RESULTS.md` - Detailed findings
- ✅ `PIPELINE_SCALE_ANALYSIS.md` - Scale projections
- ✅ `GPU_OPTIMIZATION_ROADMAP.md` - Full roadmap
- ✅ `KAGGLE_VALIDATION_RESULTS.md` - GPU testing results

---

## Commands to Run on Kaggle

### 1. Diagnose Accuracy
```bash
python diagnose_accuracy.py
```

### 2. Profile Code Generation (after accuracy fixed)
```bash
python -m cProfile -o card.profile card.py -c 20 -f test_batt.py
python -c "import pstats; p = pstats.Stats('card.profile'); p.sort_stats('cumulative').print_stats(30)"
```

### 3. Test Optimizations
```bash
# Test code generation speed
time python card.py -c 10 -f test_batt.py

# Test with caching (after implementing)
time python card.py -c 10 -f test_batt.py --use-cache

# Full pipeline test
python profile_pipeline.py --tasks 32
```

---

## Quick Wins Available

### Win 1: Code Generation Caching
- **Effort**: 2-4 hours
- **Savings**: 50-80% of 78s = 39-62s
- **Implementation**: Cache generated code, check MD5 before regenerating

### Win 2: Batch Operations Integration
- **Effort**: 6-12 hours
- **Savings**: 97% of 38.5s = 37s
- **Implementation**: Use existing gpu_optimizations.py code

### Win 3: Parallel Code Generation
- **Effort**: 4-8 hours
- **Savings**: 4-8x speedup on generation = 50-68s
- **Implementation**: ProcessPoolExecutor for card.py

**Total quick wins: 126-167 seconds saved from 116.8s baseline = 86-143% faster!**

---

## Key Insights to Remember

1. **Code generation (67%) > Solver execution (33%)**
   - Optimize generation first!
   - Bigger impact than GPU acceleration

2. **0% accuracy must be fixed first**
   - Can't optimize a broken pipeline
   - Run diagnostic tool to identify issue

3. **Quick wins are available**
   - Caching: 2-4 hours for 50-80% reduction
   - Batch ops: 6-12 hours for 97% solver speedup

4. **With 8 hours of L4x4, everything is worth optimizing**
   - Don't stop at "good enough"
   - Even 1% improvements valuable

---

## Next Command to Run

**On Kaggle right now**:
```bash
python diagnose_accuracy.py
```

This will tell us why accuracy is 0% and what to fix!

---

**Date**: October 15, 2025  
**Status**: Ready to execute  
**Priority**: Fix accuracy → Optimize code gen → Integrate batch ops  
**Expected outcome**: 116.8s → 10-50s (58-91% faster) 🚀
