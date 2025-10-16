# Stage 3 Optimization Planning

**Date:** 2025-10-16

## Objective
Push for 15-20x+ speedup by targeting remaining bottlenecks after Stage 2 (wrapper removal, exception fix). Focus: framework, DSL, GPU, and caching optimizations.

---

## 1. Current State (Post-Stage 2)
- **Wall-clock:** 2.82s (13.4x speedup, all outputs correct)
- **Bottleneck breakdown:**
  - Framework: ~63%
  - DSL: ~32%
  - get_type_hints/_get_safe_default: ~0.4s each
- **GPU:** MultiGPUOptimizer, CuPy enabled, batch ops in place
- **Exception handling:** Robust (IndexError/KeyError included)

---

## 2. Stage 3 Optimization Options

### A. Framework Refactoring
- **Goal:** Reduce 63% "Other Framework" overhead
- **Actions:**
  - Profile with cProfile to identify top time sinks
  - Refactor slow functions (batching, async, algorithmic improvements)
  - Remove redundant checks, minimize Python overhead

### B. DSL Operation Optimization
- **Goal:** Further reduce 32% DSL time
- **Actions:**
  - Profile top DSL ops (o_g, objects, etc.)
  - GPU-accelerate long-running ops (if not already)
  - Batch DSL calls where possible

### C. GPU Utilization
- **Goal:** Maximize GPU speedup for eligible workloads
- **Actions:**
  - Ensure all batch/grid ops use GPU (auto_select_optimizer)
  - Profile solver functions for GPU viability (>5ms CPU time)
  - Add/expand hybrid GPU strategy (arrays on GPU, frozenset at boundaries)

### D. Caching & Memoization
- **Goal:** Eliminate redundant computation
- **Actions:**
  - Profile for repeated calls (type hints, DSL ops)
  - Add LRU or custom caching for expensive pure functions
  - Consider grid-level or solver-level memoization

### E. Algorithmic Improvements
- **Goal:** Reduce complexity of hot-path functions
- **Actions:**
  - Analyze top framework/DSL functions for O(n^2) or worse patterns
  - Replace with more efficient algorithms where possible

---

## 3. Immediate Next Steps

## 3. Framework Profiling Results (Kaggle, 2025-10-16)

**Wall-clock:** 4.00s (100 tasks, 2 GPUs)
**Outputs:** 3200 outputs, 13200 solvers

### Bottleneck Breakdown
| Category              | Cum Time (s) | % Time | Calls    | Functions |
|---------------------- | ------------ | ------ | -------- | --------- |
| Other Framework       | 11.91        | 67.5%  | 5,491,459| 233       |
| DSL Operations        | 5.07         | 28.8%  | 510,444  | 50        |
| Candidate Management  | 0.43         | 2.4%   | 236,752  | 2         |
| GPU Batch Processing  | 0.14         | 0.8%   | 1,700    | 1         |
| Tuple Operations      | 0.03         | 0.2%   | 32,100   | 5         |
| Dedupe Operations     | 0.03         | 0.2%   | 3,400    | 1         |
| Frozenset Operations  | 0.02         | 0.1%   | 16,000   | 4         |

### Top Functions (by Category)
**Other Framework:**
- `batt` (3.96s cum, 100 calls)
- `f` (2.03s cum, 71,126 calls)
- `<genexpr>` (0.74s cum, 1,048,811 calls)
- `shoot` (0.56s cum, 23,511 calls)
- `connect` (0.54s cum, 23,739 calls)

**DSL Operations:**
- `o_g` (1.38s cum, 3,400 calls)
- `objects` (1.35s cum, 3,400 calls)
- `mapply_t` (0.84s cum, 1,100 calls)
- `fill` (0.25s cum, 2,100 calls)
- `apply` (0.22s cum, 10,114 calls)

---

## 4. Stage 3 Optimization Plan (Draft)

### Priority 1: "Other Framework" (67.5%)
- **Target:** Refactor or batch top functions: `batt`, `f`, `<genexpr>`, `shoot`, `connect`
- **Actions:**
  - Analyze and refactor `batt` for unnecessary overhead, batch processing, or async
  - Investigate `f` and `<genexpr>` for possible vectorization or inlining
  - Profile `shoot` and `connect` for algorithmic improvements or batching
  - Consider Cython or Numba for hot-paths if pure Python is limiting

### Priority 2: DSL Operations (28.8%)
- **Target:** Further optimize `o_g`, `objects`, `mapply_t`, `fill`, `apply`
- **Actions:**
  - GPU-accelerate or batch `o_g` and `objects` if not already
  - Profile and refactor `mapply_t` for further batching
  - Explore caching/memoization for pure DSL ops

### Priority 3: Candidate Management & GPU
- **Target:** Reduce `_get_safe_default` and maximize GPU batch utilization
- **Actions:**
  - Cache results of `_get_safe_default` if possible
  - Ensure all eligible grid/solver ops use MultiGPUOptimizer

### Priority 4: Minor Categories
- **Tuple/Dedupe/Frozenset:** Only optimize if found to be a bottleneck in specific tasks

---

## 5. Next Steps

## 6. Action Plan: Batching/Vectorizing `batt` Main Loop

### Goal
Reduce Python overhead and maximize GPU utilization by batching or vectorizing repeated operations in the generated `batt` function (`batt.py`).

### Approach
- **Identify**: Find repeated patterns in `batt` (e.g., DSL op calls, appends to `s` and `o`).
- **Batch**: Replace per-sample/object loops with batch operations using NumPy/CuPy or `batch_process_samples_gpu`.
- **Refactor Generator**: Update `card.py` to emit batched code for these patterns.

### Concrete Steps
1. Review the generated `batt.py` for repeated DSL calls and list/tuple operations.
2. For each repeated operation:
  - If it processes a list/tuple of grids, objects, or indices, replace with a batch call (preferably via GPU).
  - Use `batch_process_samples_gpu` or similar for grid/object ops.
  - For simple list comprehensions or generator expressions, use NumPy/CuPy vectorization if possible.
3. Update the code generator in `card.py` to emit batched/vectorized code for these cases.
4. Validate correctness and measure speedup on Kaggle.


### Generalized Refactor Plan
- **Pattern:** Any repeated DSL call or append in a loop (e.g., `for x in X: y = f(x); o.append(y)`).
- **Refactor:** Replace with a batch call: `o.extend(batch_f(X))` or `o.extend(batch_process_samples_gpu(X, f))`.
- **Codegen Template (card.py):**
  - Detect when a block of code is repeated for a list/tuple.
  - Instead of emitting a loop, emit:
    ```python
    # Old:
    for x in X:
      y = f(x)
      o.append(y)
    # New:
    o.extend(batch_f(X))
    # Or, for GPU:
    o.extend(batch_process_samples_gpu(X, f))
    ```
- **Fallback:** If batch op not available, fall back to loop (for correctness).
- **Scope:** Apply to all repeated DSL patterns, not just specific ops.

### Next Action
- [ ] Update `card.py` codegen logic to emit batch/extend patterns for all repeated DSL calls and appends, with fallback to loop if batching is not possible.

---

---

---

**All findings and changes will be tracked in this file.**

---

## 4. Documentation & Workflow
- All findings and plans go in this file (STAGE3_PLANNING.md)
- Archive intermediate scripts/results after documenting
- Update .github/copilot-instructions.md if process changes

---

## 5. References
- [STAGE2_VALIDATION_RESULTS.md](STAGE2_VALIDATION_RESULTS.md)
- [PHASE2_STAGE1_RESULTS.md](PHASE2_STAGE1_RESULTS.md)
- [GPU_PROJECT_SUMMARY.md](GPU_PROJECT_SUMMARY.md)
- [COMPLETE_GPU_COMPARISON.md](COMPLETE_GPU_COMPARISON.md)
- [INTEGRATION_GUIDE.md](INTEGRATION_GUIDE.md)

---

**Next: Begin detailed profiling of framework bottleneck.**
