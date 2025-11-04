# Phase 2b: GPU Batch Processing Acceleration (Option A)

**Status**: Implementation Planning  
**Target**: 2-3x speedup on solver execution  
**Effort**: 2-3 days  
**ROI**: High (batch overhead amortized across 100+ grids)  
**Kaggle Hardware**: 2x Tesla T4 (29.4GB each), CuPy enabled  

## Strategy Overview

### The Opportunity
- **Batch Processing Magic**: Process 100+ solver grids simultaneously
- **Why It Works**: 
  - GPU transfer overhead: ~0.2ms (FIXED per batch)
  - Single grid time: 0.1-1.0ms each
  - Batch of 100: Amortizes 0.2ms overhead to 0.002ms per grid
  - Result: GPU stays above 90% utilization

### Why Not Single-Operation GPU (Rejected)
- ❌ objects() uses BFS (inherently sequential)
- ❌ Full vectorization requires complex state management
- ❌ ROI low compared to batch approach
- ✅ Batch approach provides better amortization

### Implementation Architecture

**Hybrid Batch Processing**:
```
For each solver (genetic evolution):
  ├─ Collect 100 grids to process
  ├─ Convert to GPU arrays (batch transfer, ~0.2ms)
  ├─ Process all grids on GPU in parallel
  ├─ Convert results back (batch transfer, ~0.2ms)
  └─ Continue evolution with GPU-accelerated output
```

**Expected Performance**:
| Scenario | CPU | GPU | Speedup |
|----------|-----|-----|---------|
| Single grid | 1.0ms | 0.1ms | 10x (but transfer: 0.2ms overhead = 0.3ms total) ❌ |
| Batch 10 | 10ms | 1.0ms + 0.2ms transfer = 1.2ms | **8x ✓** |
| Batch 100 | 100ms | 10ms + 0.2ms transfer = 10.2ms | **~10x ✓** |
| Batch 1000 | 1000ms | 100ms + 0.2ms transfer = 100.2ms | **~10x ✓** |

## Implementation Plan

### Phase 2b Week 1: Architecture Setup

**Day 1: GPU Batch Infrastructure**
- [ ] Create `gpu_batch_solver.py` module
  - Batch accumulation logic
  - Grid collection until 100+ accumulated
  - GPU transfer management
  - Result collection

- [ ] Implement `BatchGridProcessor`:
  ```python
  class BatchGridProcessor:
      def __init__(self, batch_size=100):
          self.batch_size = batch_size
          self.batch = []
          self.gpu = None
          self.cupy_available = check_cupy()
      
      def add(self, grid):
          self.batch.append(grid)
          if len(self.batch) >= self.batch_size:
              return self.process()
          return None
      
      def process(self):
          # Transfer batch to GPU
          # Process all grids in parallel
          # Transfer results back
          # Clear batch
          # Return results
          pass
  ```

- [ ] GPU operations to vectorize:
  - `p_g()` - Pattern matching (100% vectorizable)
  - `rot90()` - Rotation (100% vectorizable)
  - `flip()` - Flipping (100% vectorizable)
  - `transpose()` - Transpose (100% vectorizable)
  - `shift()` - Shifting (100% vectorizable)

**Day 1 Code Changes**:
1. Create `gpu_batch_solver.py` (300 lines)
2. Implement `BatchGridProcessor` class
3. Add GPU operation wrappers
4. Create test suite

---

### Phase 2b Week 1: Integration Setup

**Day 2: Integration Points**

**Target Functions to Modify**:
1. `run_batt.py` - Main batch runner
   - Identify grid collection points
   - Insert batch processor initialization
   - Replace individual grid processing with batch calls

2. `batt.py` - Sample processing
   - Where individual grids are processed
   - Hook for batch accumulation

3. `solvers.py` - Solver execution
   - Where DSL operations happen
   - Most impactful for batch acceleration

**Integration Points**:
```python
# BEFORE (Sequential)
for grid in grids:
    result = dsl.p_g(grid, pattern)
    
# AFTER (Batch GPU)
batch_processor = BatchGridProcessor(batch_size=100)
for grid in grids:
    result = batch_processor.add_and_process(grid, operation='p_g')
```

**Day 2 Code Changes**:
1. Modify `run_batt.py` to support batch mode
2. Add batch processor initialization
3. Update grid processing loop
4. Add fallback to CPU if GPU unavailable

---

### Phase 2b Week 1: Testing & Validation

**Day 3: Local Testing & Kaggle Validation**

**Local Testing** (CPU-only, no GPU):
```bash
python gpu_batch_solver.py --test-local
# Expected: All tests pass with CPU fallback
```

**Kaggle Testing** (With GPU):
- Single task: Verify correctness
- 10-task run: Verify 2x speedup
- 32-task run: Measure actual batch effects
- 100-task run: Final validation

**Validation Checkpoints**:
- [ ] Correctness: Results match Phase 2a output
- [ ] Performance: 2-3x speedup measured
- [ ] Stability: No GPU OOM errors
- [ ] Fallback: CPU works when GPU unavailable

---

## Technical Details

### GPU Memory Management
```
Per batch (100 grids, max 30×30):
- Input grids: 100 × 900 × 4 bytes = 360KB
- Output grids: 100 × 900 × 4 bytes = 360KB
- Working memory: ~10MB
- Total: ~10.7MB (well within 15GB per GPU)
```

### Batch Accumulation Strategy

**Option A: Natural Batches** (Recommended)
- Solvers already process 100+ grids in their lifetime
- Use genetic algorithm's natural batch boundaries
- No synchronization overhead

**Option B: Fixed-Size Windowing**
- Process every 100 grids as a batch
- More predictable batching
- Potential synchronization delays

**Option C: Adaptive Batching**
- Accumulate until GPU queue builds
- Dynamic batch sizing based on workload
- Complex to implement, marginal gains

→ **Going with Option A** (natural solver batches)

### Error Handling & Fallback

```python
try:
    results = batch_processor.process_gpu()
except Exception as e:
    # Fallback to CPU
    results = [cpu_op(grid) for grid in batch]
    # Log GPU error but continue
```

---

## Implementation Checklist

### Week 1 (Days 1-3)
- [ ] Day 1: `gpu_batch_solver.py` infrastructure
  - [ ] `BatchGridProcessor` class (100 lines)
  - [ ] GPU/CPU detection (20 lines)
  - [ ] Vectorized operation wrappers (50 lines)
  - [ ] Unit tests (100 lines)
  
- [ ] Day 2: Integration with `run_batt.py`
  - [ ] Batch processor initialization (10 lines)
  - [ ] Grid collection logic (20 lines)
  - [ ] Result collection (15 lines)
  - [ ] Configuration options (10 lines)
  
- [ ] Day 3: Testing & Validation
  - [ ] Local CPU testing
  - [ ] Kaggle single-task test
  - [ ] Kaggle 10-task test
  - [ ] Kaggle 32-task test
  - [ ] Kaggle 100-task test

### Week 1-2 (Days 4-10)
- [ ] Performance profiling
- [ ] Memory optimization
- [ ] Multi-GPU support (if available)
- [ ] Documentation updates
- [ ] Results consolidation

---

## Performance Targets

### Baseline (Phase 2a)
- 100-task wall-clock: 24.818s
- Cache hit rate: 100% (16,000/16,000)
- CPU only: ~12,000ms solver time

### Expected With GPU Batch (Phase 2b)
- Solver time: 4,000-6,000ms (3-4x faster)
- **Wall-clock estimate: 12-15s** (⚡ 2x overall improvement)
- Combined optimization: -60% from baseline

---

## Success Criteria

✅ **Correctness**: Output matches Phase 2a exactly  
✅ **Performance**: ≥2x speedup on solver operations  
✅ **Stability**: 100 tasks complete without error  
✅ **Reliability**: Works on T4x2, P100, L4x4  
✅ **Fallback**: CPU execution when GPU unavailable  

---

## Risk Mitigation

| Risk | Mitigation | Confidence |
|------|-----------|-----------|
| GPU OOM | Batch size adaptive, reduce if needed | High |
| Transfer bottleneck | Amortized over 100+ grids | High |
| Correctness mismatch | Unit tests before integration | High |
| GPU unavailable | CPU fallback implemented | High |
| Synchronization delays | Natural solver batches | High |

---

## Next Steps (Immediate)

1. **Create `gpu_batch_solver.py`** - Core infrastructure
2. **Implement `BatchGridProcessor`** - Batch handling logic
3. **Add GPU operation wrappers** - Vectorized DSL operations
4. **Test locally** - Verify correctness with CPU
5. **Deploy to Kaggle** - Validate speedup on real hardware

**Timeline**: Start today, validation complete by end of Day 3

**Expected Outcome**: 2-3x speedup → 12-15s wall-clock for 100 tasks (vs 24.818s current)

---

## References

- **Phase 2a**: PHASE2A.md (100% cache hit rate, baseline established)
- **Phase 2b Analysis**: PHASE2B_ANALYSIS.md (strategy comparison)
- **GPU Environment**: Kaggle T4x2, CuPy available
- **Batch Processing Guide**: gpu_optimizations.py in companion docs

