# GPU Viability Analysis: Solver Functions vs Individual DSL Operations

## Executive Summary

**CRITICAL DISCOVERY**: User revealed that solver functions in `solvers_pre.py` are ~50x longer than individual DSL operations and called 100s of times in sequence. This **completely changes the GPU viability calculus** from our failed p_g test.

## Current Status

### What We Know (Proven)
- ✅ Individual DSL operations (p_g, o_g, etc.) are **too fast for GPU** (0.1-0.5ms)
- ✅ GPU overhead dominates simple operations (0.2ms kernel launch + transfers)
- ✅ ARC grids are small (typically 30x30 = 900 elements)
- ✅ p_g GPU implementation is **3x slower** than CPU (0.34ms GPU vs 0.12ms CPU)
- ✅ Break-even requires >6060 elements or >0.2ms CPU time

### What We Just Discovered (Game Changer!)
- 💡 Solver functions compose **10-40 DSL operations** per solver
- 💡 Solvers are **~50x longer** than individual DSL ops → **6-25ms** execution time
- 💡 Each solver called **100s of times** with different arguments
- 💡 400 different solver functions in `solvers_pre.py` (6453 lines)

## The Math That Changes Everything

### Individual DSL Operation (p_g)
```
CPU time:           0.12ms
GPU overhead:       0.20ms (kernel launch + transfers)
Overhead ratio:     167% (GPU overhead > computation)
Result:             GPU 3x SLOWER ❌
```

### Solver Function (Estimated)
```
CPU time:           10ms (50x longer, composing 20 DSL ops @ 0.5ms each)
GPU overhead:       0.20ms (same kernel launch + one-time transfer)
Overhead ratio:     2% (negligible!)
Expected speedup:   2-4x (if operations stay on GPU) ✅
```

### Batch Execution (100 Solver Calls)
```
CPU time:           1000ms (100 calls @ 10ms each)
GPU time:           250ms (amortized, 4x speedup with batching)
Transfer overhead:  Amortized across 100 calls (0.002ms per call)
Result:             GPU 4x FASTER ✅
```

## Execution Pattern Analysis

### From run_test.py (lines 180-210)
```python
async def check_solvers_pre(data, task_id, timeout=1):
    task = data['demo'][task_id] + data['test'][task_id]  # Multiple samples
    S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in task)
    
    solver = getattr(solvers_pre, f'solve_{task_id}')
    solver.__globals__.update(globals())
    
    for sample in task:
        # Each solver called multiple times with different inputs
        result = await run_with_timeout(solver, [S, sample['input'], None], timeout)
        # Check if result matches expected output
```

**Key Insight**: Each `solve_*` function is called multiple times (once per training/test sample), typically 5-10 calls per task.

### Solver Function Complexity Examples

#### Simple Solver (4 operations)
```python
def solve_c9e6f938(S, I, C):
    x1 = mir_rot_t(I, R2)      # Mirror-rotate
    O = hconcat(I, x1)          # Horizontal concatenation
    return O
```
**Estimated CPU time**: 0.2ms (too fast for GPU)

#### Medium Solver (14 operations)
```python
def solve_045e512c(S, I, C):
    x1 = o_g(I, R5)            # Connected components (complex!)
    x2 = get_arg_rank_f(x1, size, F0)
    x3 = subgrid(x2, I)
    x4 = trim(x3)
    x5 = replace(I, FIVE, ZERO)
    x6 = center(x4)
    x7 = shift(x4, x6)
    x8 = paint(x5, x7)
    x9 = mir_rot_t(x4, R0)
    x10 = shift(x9, x6)
    x11 = paint(x8, x10)
    x12 = mir_rot_t(x4, R1)
    x13 = shift(x12, x6)
    O = paint(x11, x13)
    return O
```
**Estimated CPU time**: 5-10ms (GPU viable!)

#### Complex Solver (35+ operations)
```python
def solve_f8a8fe49(S, I, C):
    x1 = replace(I, FIVE, ZERO)
    x2 = compose(normalize, asobject)
    x3 = o_g(I, R5)            # Connected components
    x4 = colorfilter(x3, TWO)
    x5 = get_nth_f(x4, F0)
    x6 = portrait_f(x5)
    x7 = branch(x6, hsplit, vsplit)
    x8 = rbind(mir_rot_t, R2)
    x9 = rbind(mir_rot_t, R0)
    x10 = branch(x6, x8, x9)
    x11 = f_ofcolor(I, TWO)
    x12 = subgrid(x11, I)
    x13 = trim(x12)
    x14 = x10(x13)
    x15 = x7(x14, TWO)
    x16 = apply(x2, x15)
    x17 = get_nth_t(x16, L1)
    x18 = corner(x11, R0)
    x19 = increment(x18)
    x20 = shift(x17, x19)
    x21 = branch(x6, tojvec, toivec)
    x22 = compose(x21, increment)
    x23 = branch(x6, width_f, height_f)
    x24 = x23(x17)
    x25 = x22(x24)
    x26 = invert(x25)
    x27 = shift(x20, x26)
    x28 = paint(x1, x27)
    x29 = get_nth_f(x16, F0)
    x30 = shift(x29, x19)
    x31 = double(x24)
    x32 = x22(x31)
    x33 = shift(x30, x32)
    O = paint(x28, x33)
    return O
```
**Estimated CPU time**: 15-25ms (GPU highly viable!)

## Why Solvers Are Different from DSL Operations

| Aspect | DSL Operation (p_g) | Solver Function |
|--------|---------------------|-----------------|
| **Execution Time** | 0.12ms | 6-25ms (50x longer) |
| **GPU Overhead** | 0.20ms (167% of compute) | 0.20ms (0.8-3% of compute) |
| **Call Frequency** | 1 call in solver | 5-10 calls per task |
| **Composition** | Single operation | 10-40 DSL operations |
| **GPU Strategy** | CPU fallback | Keep data on GPU |
| **Expected Speedup** | 0.34x (SLOWER) | 2-4x (FASTER) |

## GPU Acceleration Strategy for Solvers

### Option 1: GPU-Resident Solver Execution (RECOMMENDED)
**Approach**: Convert entire solver function to run on GPU, keeping all intermediate results on GPU.

**Pros**:
- Maximum speedup potential (2-4x)
- Eliminates intermediate CPU↔GPU transfers
- Works for medium-complex solvers (14+ operations)
- Batching across multiple samples compounds speedup

**Cons**:
- Need to GPU-accelerate called DSL operations (o_g, paint, shift, etc.)
- More complex implementation
- Not all DSL operations may benefit from GPU

**Implementation**:
```python
def solve_045e512c_gpu(S, I_cpu, C):
    # Transfer input to GPU once
    I = cp.asarray(I_cpu)
    
    # All operations on GPU (no intermediate transfers)
    x1 = gpu_o_g(I, R5)
    x2 = gpu_get_arg_rank_f(x1, size, F0)
    x3 = gpu_subgrid(x2, I)
    # ... 11 more GPU operations ...
    O_gpu = gpu_paint(x11, x13)
    
    # Transfer result to CPU once
    return cp.asnumpy(O_gpu)
```

**Expected Performance**:
- Single call: 2-3x speedup (10ms → 3-5ms)
- Batched (10 calls): 3-4x speedup (100ms → 25-33ms)

### Option 2: Selective GPU Acceleration
**Approach**: GPU-accelerate only the most expensive DSL operations within solvers.

**Pros**:
- Simpler implementation
- Focus on high-impact operations (o_g, fgpartition, gravitate)
- Gradual rollout possible

**Cons**:
- CPU↔GPU transfers at each operation (overhead adds up)
- Lower speedup potential (1.5-2x)
- May not be worth the complexity

### Option 3: Batch Solver Calls
**Approach**: Execute multiple solver calls in parallel on GPU.

**Pros**:
- Highest speedup potential (4-6x with batching)
- Amortizes transfer overhead across many calls
- Natural fit for ARC evaluation (multiple samples per task)

**Cons**:
- Requires parallelizing solver execution
- Memory overhead (multiple grids on GPU simultaneously)
- More complex implementation

## Key Questions to Answer

### 1. What is the actual CPU execution time for typical solvers?
**Action**: Benchmark 20-30 representative solvers from `solvers_pre.py`
**Why**: Need real data to validate 50x estimate and identify GPU candidates

### 2. Which DSL operations are called most frequently in solvers?
**Action**: Profile solver execution, count operation frequency
**Why**: Focus GPU acceleration on high-impact operations

### 3. Can we batch solver calls effectively?
**Action**: Analyze ARC evaluation pattern (how many samples per task?)
**Why**: Batching could multiply speedup (2x → 8x)

### 4. What's the memory footprint of keeping intermediate grids on GPU?
**Action**: Measure GPU memory usage for typical solver execution
**Why**: Ensure we don't run out of GPU memory

## Immediate Next Steps

### Step 1: Benchmark Solver Functions (PRIORITY)
**Goal**: Measure actual CPU execution time for 20-30 solvers

**Approach**:
```python
import time
import solvers_pre

def benchmark_solver(solver_func, S, I, C, iterations=100):
    start = time.perf_counter()
    for _ in range(iterations):
        result = solver_func(S, I, C)
    elapsed = time.perf_counter() - start
    return elapsed / iterations * 1000  # ms per call

# Test solvers of varying complexity
solvers_to_test = [
    'solve_c9e6f938',     # Simple (2 ops)
    'solve_045e512c',     # Medium (14 ops)
    'solve_f8a8fe49',     # Complex (35 ops)
    # ... add 17 more
]
```

**Expected Outcome**:
- Confirm solvers are 10-100x longer than individual DSL ops
- Identify which solvers are GPU candidates (>5ms CPU time)
- Validate 50x estimate from user

### Step 2: Profile Operation Frequency
**Goal**: Determine which DSL operations are called most in solvers

**Approach**:
```python
import ast
import inspect

def count_dsl_operations(solver_func):
    source = inspect.getsource(solver_func)
    tree = ast.parse(source)
    
    operation_counts = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                op_name = node.func.id
                operation_counts[op_name] = operation_counts.get(op_name, 0) + 1
    
    return operation_counts

# Analyze all 400 solvers
all_op_counts = {}
for solver_name in dir(solvers_pre):
    if solver_name.startswith('solve_'):
        solver = getattr(solvers_pre, solver_name)
        counts = count_dsl_operations(solver)
        for op, count in counts.items():
            all_op_counts[op] = all_op_counts.get(op, 0) + count
```

**Expected Outcome**:
- List of top 10-20 most-called DSL operations
- Priority list for GPU acceleration (focus on high-frequency ops)

### Step 3: Test GPU Strategy on One Solver
**Goal**: Prove GPU viability by implementing one medium-complexity solver on GPU

**Approach**:
1. Pick `solve_045e512c` (14 operations, uses o_g which is complex)
2. Implement GPU version with all operations on GPU
3. Benchmark: CPU vs GPU for single call and batched calls
4. Measure correctness (results must match CPU exactly)

**Expected Outcome**:
- If >2x speedup: GPU viable, proceed to full implementation
- If <2x speedup: Re-evaluate strategy, maybe stick to CPU + Numba

### Step 4: Batch Execution Analysis
**Goal**: Determine if we can batch solver calls for higher speedup

**Questions**:
- How many samples per task in ARC evaluation?
- Can we run multiple solvers in parallel?
- What's the memory overhead?

**Expected Outcome**:
- Design for batched GPU execution (if viable)
- Potential for 4-8x speedup instead of 2-3x

## Risk Assessment

### High Risk (Show Stoppers)
- ❌ **Solvers may not actually be 50x longer** - Need to verify with benchmarks
- ❌ **Memory constraints** - Keeping 10-20 grids on GPU simultaneously
- ❌ **Complex DSL operations may not GPU-accelerate well** - o_g uses frozensets, scanning

### Medium Risk (Manageable)
- ⚠️ **Not all solvers will benefit** - Simple solvers (2-5 ops) stay on CPU
- ⚠️ **Implementation complexity** - Need to GPU-accelerate 20-30 DSL operations
- ⚠️ **Correctness validation** - Extensive testing required

### Low Risk (Acceptable)
- ✓ **GPU overhead still exists** - But becomes negligible for long solvers
- ✓ **Some solvers will be CPU-bound** - Adaptive fallback handles this

## Success Criteria

### Minimum Viable Product
- [ ] Benchmark proves solvers are >5ms CPU time (on average)
- [ ] One GPU solver shows >2x speedup vs CPU
- [ ] Correctness matches CPU exactly (100% test pass rate)
- [ ] Automatic CPU fallback for simple solvers

### Full Success
- [ ] 50+ solver functions GPU-accelerated
- [ ] Average speedup >2.5x for medium-complex solvers
- [ ] Batched execution shows >4x speedup
- [ ] Memory footprint <50% of available GPU memory
- [ ] Zero correctness regressions

### Stretch Goals
- [ ] 200+ solver functions GPU-accelerated
- [ ] Average speedup >3x
- [ ] Batched execution shows >6x speedup
- [ ] Automatic profiling identifies GPU candidates

## Conclusion

**The user's insight about solver functions being 50x longer completely changes the GPU viability calculation.**

While individual DSL operations like p_g are too fast for GPU (overhead dominates), solver functions that compose 10-40 operations are **perfect GPU candidates**:

1. **Long enough**: 6-25ms CPU time → GPU overhead becomes negligible (0.8-3%)
2. **Called frequently**: 5-10 times per task → amortizes transfer cost
3. **Composable**: Can keep all data on GPU across operations
4. **Batchable**: Can run multiple samples in parallel

**Immediate Action**: Benchmark 20-30 solver functions to validate 50x estimate and confirm GPU viability.

If benchmarks confirm solvers are >5ms CPU time, we should **pivot from individual DSL operation GPU acceleration to solver-level GPU execution**. Expected outcome: **2-4x speedup** for ARC evaluation, with potential for 4-8x with batching.
