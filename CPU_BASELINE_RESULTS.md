# CPU Baseline Performance Results

**Date**: October 13, 2025  
**Test**: CPU-only mode with 10 tasks, timing enabled  
**Command**: `bash run_card.sh -c 10 -T -m`

## Results Summary

### CPU-Only Performance (5 tasks sampled)

| Task ID  | Total Time | check_solver_speed | inline_variables | check_batt | batt (demo+test) |
|----------|------------|-------------------|------------------|------------|------------------|
| 0520fde7 | 0.504s     | 0.535s           | 0.253s (50%)     | 0.275s     | 0.032s (6%)      |
| 03560426 | 0.637s     | 0.618s           | 0.257s (40%)     | 0.411s     | 0.052s (8%)      |
| 00576224 | 0.451s     | 0.290s           | 0.313s (69%)     | 0.187s     | 0.012s (3%)      |
| 007bbfb7 | 0.744s     | 0.900s           | 0.447s (60%)     | 0.288s     | 0.046s (6%)      |
| 025d127b | ~0.6s*     | ~0.5s*           | ~0.3s* (50%)     | ~0.3s*     | ~0.04s* (7%)     |

*Estimated from partial output

### Component Breakdown (Average from 4 complete tasks)

```
Total per task:     0.584s (100%)

1. check_solver_speed: 0.586s (100%) ← BOTTLENECK!
   - 32 solvers validated
   - Average: 18.3ms per solver (was 87ms on GPU machine!)

2. inline_variables:   0.318s (54%)  ← SECONDARY
   - visit:    0.258s (81% of inlining)
   - unparse:  0.040s (13%)
   - parse:    0.020s (6%)

3. check_batt:         0.290s (50%)  ← TERTIARY
   - demo.parallel:   0.028s (9%)
   - test.call:       0.008s (3%)

4. phase2_inline_batch: 0.110s (19%)
5. phase4_differs:      0.081s (14%)
6. phase4_inline:       0.079s (14%)
7. generate_expanded:   0.054s (9%)
```

## 🎯 Key Discoveries

### 1. Solver Validation is DRAMATICALLY Different!

**GPU Machine (Kaggle)**: 87ms per solver × 32 = 2.770s total  
**CPU Machine (Local)**: 18ms per solver × 32 = 0.586s total

**Solver validation is 4.7x SLOWER on Kaggle GPU machine!**

This is HUGE and unexpected! Possible reasons:
- GPU machine has slower CPU?
- Different Python version/implementation?
- Network/filesystem latency on Kaggle?
- Different load/contention?

### 2. Variable Inlining is Much Faster Too

**GPU Machine**: 2.989s (69% of time)  
**CPU Machine**: 0.318s (54% of time)

**Inlining is 9.4x FASTER on local CPU!**

Again, suggests Kaggle CPU is significantly slower.

### 3. Batt Execution (CPU-only)

**CPU Machine (no GPU)**:
- demo.parallel: 28ms average (2-5 samples)
- test.call: 8ms average (1 sample)
- **Total batt: 36ms average**

**Kaggle GPU Machine**:
- demo.parallel: 315ms (2 samples) = 158ms per call with GPU
- test.call: 64ms (1 sample) with GPU
- **Total batt: 379ms with GPU**

Wait... **CPU-only is 10x FASTER than GPU-accelerated?!**

This doesn't make sense. Let me check...

### 4. The Real Comparison

Looking at the actual batt times:
- CPU local demo: 23-40ms for 2-5 samples
- GPU Kaggle demo: 315ms for 2 samples

**But wait!** The Kaggle GPU test had:
- 3 demo samples (not 2)
- Different task complexity

Let's look at per-sample times:
- CPU: 23ms / 3 samples = 7.7ms per sample (task 0520fde7)
- CPU: 40ms / 2 samples = 20ms per sample (task 03560426) 
- CPU: 8ms / 2 samples = 4ms per sample (task 00576224)
- CPU: 39ms / 5 samples = 7.8ms per sample (task 007bbfb7)

**Average CPU: ~10ms per batt() call**

**Kaggle GPU: 127ms per batt() call (from Week 5 testing)**

So GPU is actually **12.7x SLOWER than CPU!** 😱

## 🤯 SHOCKING REVELATION

### Week 5 Conclusion Was BACKWARDS!

We thought:
- GPU provides 3.3x speedup (127ms vs ~430ms estimated)
- GPU acceleration works great!

Reality:
- GPU is 12.7x SLOWER than CPU! (127ms vs 10ms actual)
- GPU "optimization" made batt 12x worse!

### Why Did We Think GPU Helped?

1. **Never measured CPU baseline** - Just estimated ~430ms
2. **GPU seemed fast** - 127ms felt good compared to timeout
3. **Measurement beats theory** - But we didn't measure correctly!

### The Architecture Problem

Looking at batt execution times:
- **Local CPU**: 36ms total for demo+test
- **Kaggle GPU**: 379ms total for demo+test

The issue is NOT the GPU acceleration itself, but:
1. **Kaggle CPU is much slower** (4-10x slower!)
2. **GPU overhead on Kaggle** (initialization, transfers)
3. **Small batch sizes** (2-5 samples) don't benefit from GPU

## 📊 Corrected Performance Analysis

### Total Time Breakdown (Local CPU)

```
Component              Local CPU    Kaggle GPU    Notes
──────────────────────────────────────────────────────────
Solver Validation      0.586s       2.770s        4.7x slower on Kaggle!
Variable Inlining      0.318s       2.989s        9.4x slower on Kaggle!
Batt Execution         0.036s       0.379s        10.5x slower on Kaggle!
Phase 2 Inline         0.110s       0.976s        8.9x slower on Kaggle!
──────────────────────────────────────────────────────────
TOTAL                  ~1.05s       ~7.1s         6.8x slower on Kaggle!
```

**The Kaggle CPU is 6-10x SLOWER than local CPU!**

This explains everything:
- Why GPU "seemed fast" (compared to slow Kaggle CPU)
- Why we need 10s timeout (Kaggle is slow)
- Why all operations take 3-10x longer on Kaggle

## 🎯 Week 6 Strategy REVISED

### The Real Problem: Kaggle CPU is Slow

**Option 1: Accept Kaggle slowness, optimize for it**
- Focus on Week 6 optimizations (still valid)
- Use multiprocessing to work around slow CPU
- Cache expensive operations
- Expected: 7.1s → 2.5s on Kaggle (still 2x slower than local!)

**Option 2: GPU is actually HURTING us!**
- Current GPU batt: 379ms (10x slower than CPU would be)
- If we remove GPU batching on Kaggle: 7.1s → 6.8s
- Save 300ms by REMOVING GPU acceleration!

**Option 3: Fix GPU to not hurt performance**
- GPU batch operations have overhead
- Small batches (2-5 samples) too small for GPU
- Need threshold: Use GPU only for batches >= 20 samples
- Or: Skip GPU batching entirely for batt

### Recommendation

**REMOVE GPU acceleration from batt** on Kaggle!
- GPU making it 10x slower, not faster
- Small batch sizes don't benefit
- Better to just use (slow) Kaggle CPU

Then focus on Week 6 optimizations:
1. Solver validation: 2.770s → 0.7s (4x speedup)
2. Variable inlining: 2.989s → 1.0s (3x speedup)
3. Inline batch: 0.976s → 0.5s (2x speedup)
4. **Remove GPU from batt**: 0.379s → 0.036s (10x speedup!)

**Total impact**: 7.1s → 2.2s (3.2x speedup on Kaggle)

## 🔥 Action Items

1. **Immediate**: Disable GPU batching in batt_gpu.py for small batches
   - Change threshold from 3 to 100+ samples
   - Or: Force CPU fallback always

2. **Week 6A**: Implement shared optimizations
   - Solver validation parallelization
   - Variable inlining caching + multiprocessing
   - Inline batch optimization

3. **Week 6B**: Re-evaluate GPU strategy
   - GPU might help for MEGA batch operations (1000+ samples)
   - But hurts for normal batt execution (2-5 samples)
   - Keep GPU code, but disable by default

## 📝 Lessons Learned (Again!)

1. **Always measure baseline** - Don't estimate!
2. **GPU isn't always faster** - Small batches have overhead
3. **Environment matters** - Kaggle CPU is surprisingly slow
4. **Question assumptions** - "3.3x speedup" was wrong!
5. **Measure, don't assume** - Even after measuring, verify!

## Next Steps

1. ✅ **Update batt_gpu.py** - Disable GPU for small batches
2. ⏳ Test on Kaggle with GPU disabled
3. ⏳ Confirm batt time drops from 379ms to ~100-200ms
4. ⏳ Then proceed with Week 6 optimizations

**Expected final performance**: 
- Kaggle without GPU overhead: ~6.8s
- After Week 6 optimizations: ~2.2s (3x faster!)
- Still 2x slower than local (Kaggle CPU is just slow)
