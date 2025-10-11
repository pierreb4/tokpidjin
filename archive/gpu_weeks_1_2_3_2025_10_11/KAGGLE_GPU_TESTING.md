# Kaggle GPU Testing Instructions

## Week 1 Deliverable: GPU o_g Implementation

This folder contains the Week 1 implementation of GPU-accelerated `o_g` operation (connected components).

### 📁 Files to Upload to Kaggle

**Core Implementation:**
- `gpu_dsl_core.py` - GPU o_g implementation
- `test_gpu_dsl_core.py` - Comprehensive unit tests

**Dependencies (from repo):**
- `dsl.py` - CPU reference implementation
- `arc_types.py` - Type definitions
- `utils.py` - Utility functions (if needed)

**Test Script:**
- `kaggle_test_gpu_o_g.py` - Main Kaggle test runner

### 🚀 Kaggle Setup Steps

1. **Create New Notebook**
   - Go to Kaggle.com
   - Click "Create" → "New Notebook"
   - Name it: "GPU o_g Testing - Week 1"

2. **Enable GPU**
   - Click "Settings" (right panel)
   - Accelerator: **GPU L4** (preferred) or GPU T4
   - Persistence: On (optional)
   - Internet: On

3. **Upload Files**
   - Click "File" → "Upload"
   - Upload all 6 files listed above
   - Wait for upload to complete

4. **Run Test Script**
   ```python
   !python kaggle_test_gpu_o_g.py
   ```

### ✅ Expected Results

**Correctness Tests:**
- Total tests: 128 (16 grids × 8 modes)
- Expected: 100% pass rate
- All GPU results should match CPU exactly

**Performance Tests:**
- CPU baseline: 4-7ms per o_g call
- GPU (frozenset): 1.45-2.15ms (2.3-4.8x speedup)
- GPU (tuple): 0.95-1.65ms (2.5-7.8x speedup)

### 🎯 Success Criteria

✅ **Pass:** All correctness tests pass (128/128)  
✅ **Pass:** Frozenset speedup ≥ 2.3x  
✅ **Pass:** Tuple speedup ≥ 2.5x  

### 📊 What to Report Back

After running on Kaggle, report:

1. **GPU Type:** (L4, T4, or P100)
2. **Correctness:** X/128 tests passed
3. **Performance:**
   - CPU median time: X.XXX ms
   - GPU (frozenset) median time: X.XXX ms (X.XXx speedup)
   - GPU (tuple) median time: X.XXX ms (X.XXx speedup)
4. **Any errors or warnings**

### 🐛 Troubleshooting

**CuPy not available:**
- Check GPU is enabled in notebook settings
- Run: `!pip install cupy-cuda12x`

**Import errors:**
- Verify all 6 files are uploaded
- Check files are in the correct directory
- Run: `!ls -la` to list files

**Tests failing:**
- Check output for specific failures
- Report the failure details
- May need to adjust implementation

**Performance below expectations:**
- Check GPU type (L4 > T4 > P100)
- Ensure JIT warmup completed
- Try increasing number of warmup runs

### 📝 Next Steps After Kaggle Testing

If all tests pass:
- ✅ **Week 1 Complete**
- → Proceed to **Week 2: Solver Integration**
- Integrate `gpu_o_g` into 3 profiled solvers
- Measure end-to-end solver speedup

If tests fail:
- Debug and fix issues
- Re-test on Kaggle
- Don't proceed to Week 2 until tests pass

### 🔗 Documentation References

- **GPU_O_G_IMPLEMENTATION.md** - Complete implementation guide
- **GPU_SOLVER_STRATEGY.md** - Strategic overview
- **profile_solvers.py results** - Shows o_g is 75-92% bottleneck

---

**Status:** Ready for Kaggle testing  
**Week:** 1 of 4  
**Goal:** Validate GPU o_g correctness and performance  
**Expected Outcome:** 2.3-7.8x speedup with 100% correctness
