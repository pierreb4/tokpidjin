# Week 3/4: Dual-Return API Optimization

## Goal
Optimize GPU solvers by using tuple format internally, avoiding frozenset conversion overhead.

## Current Performance (Week 2 Results)

```
Solver       CPU (ms)   GPU (ms)   Speedup    
----------------------------------------------
23b5c85d     3.369      6.406      0.53x
09629e4f     2.190      2.338      0.94x
1f85a75f     3.399      6.401      0.53x
----------------------------------------------
AVERAGE      2.986      5.048      0.59x
```

**Issue**: GPU frozenset conversion adds ~0.3-0.4ms per operation.

## Strategy: GPU-Resident Solvers

### Concept
When a solver uses multiple o_g operations or chains GPU operations together, keep data as tuples (GPU-native) until the final output.

**Example Solver**:
```python
def solve_example(I):
    x1 = o_g(I, R7)           # Returns frozenset
    x2 = get_arg_rank_f(x1, size, L1)  # Works on frozenset
    O = subgrid(x2, I)        # Returns grid
    return O
```

**GPU-Optimized Version**:
```python
def gpu_solve_example_optimized(I):
    # Keep as tuple internally
    x1 = gpu_o_g(I, R7, return_format='tuple')  # Returns tuple (faster!)
    
    # Problem: get_arg_rank_f expects frozenset!
    # Need GPU-native version or convert at boundary
    x1_fs = frozenset(frozenset(obj) for obj in x1)
    x2 = get_arg_rank_f(x1_fs, size, L1)
    
    O = subgrid(x2, I)
    return O
```

**Optimization**: Not much benefit if we convert immediately anyway!

## The Real Optimization: Chain Multiple GPU Ops

### Target: Solvers with Multiple o_g Calls

Look for solvers that do:
```python
x1 = o_g(I, R7)
x2 = o_g(x1_processed, R4)  # Another o_g on processed result
x3 = combine(x1, x2)
```

For these, we can:
1. Keep x1 as tuple
2. Process x1 (tuple operations)
3. Call gpu_o_g(processed, R4, return_format='tuple')
4. Combine as tuples
5. Convert to frozenset only at final output

**Benefit**: Save 0.3-0.4ms per intermediate o_g call!

## Week 3 Tasks

### Task 1: Identify Candidate Solvers ✓
From `profile_solvers.py` results, find solvers with:
- Multiple o_g calls (benefit from tuple chaining)
- Long execution time (>10ms) where savings matter
- High o_g percentage (>80%)

**Already identified** (from Week 2):
- `solve_36d67576`: 120ms, 33 ops, multiple o_g likely
- `solve_36fdfd69`: 58ms, 16 ops
- `solve_1a07d186`: 11ms, 16 ops

### Task 2: Analyze Solver Structure
For each candidate, check:
```python
# How many o_g calls?
# Are there intermediate conversions we can skip?
# What operations happen between o_g calls?
```

### Task 3: Create Optimized Versions
Implement GPU-resident versions that:
- Use `return_format='tuple'` for intermediate results
- Chain GPU operations without frozenset conversion
- Convert to frozenset only at DSL boundaries

### Task 4: Benchmark
Measure:
- Original CPU time
- GPU (frozenset) time  
- GPU (tuple-optimized) time
- Calculate savings

**Expected savings**: 0.3-0.4ms per o_g call avoided

## Week 4: Convert More Solvers

Based on Week 3 results:
- If tuple format shows 20-30% speedup: Convert 10-20 solvers
- Document patterns for easy conversion
- Create helper functions for common chains

## Expected Impact

### Conservative Estimate
- Convert 10 solvers with 2 o_g calls each
- Save 0.3ms per intermediate conversion
- Total savings: 10 × 0.3ms = 3ms per solver
- If these solvers run 10x each: **30ms saved**

### Optimistic Estimate  
- Convert 20 solvers with 3-4 o_g calls each
- Save 0.4ms per conversion
- Complex solvers benefit more
- Total potential: **100-200ms saved** in full ARC evaluation

## Implementation Priority

### High Priority (Week 3)
1. ✅ Analyze `solve_36d67576` (120ms - biggest target!)
2. ✅ Analyze `solve_36fdfd69` (58ms)
3. Implement optimized versions
4. Benchmark and validate

### Medium Priority (Week 4)  
5. Analyze 5-10 more candidates
6. Create conversion patterns
7. Document best practices

### Low Priority (Future)
8. Batch processing multiple puzzles on GPU
9. Full GPU-resident solver chains
10. Custom GPU kernels for complex operations

## Success Criteria

### Week 3 Success
- ✅ 2-3 optimized solvers implemented
- ✅ Correctness: 100% match CPU results
- ✅ Performance: 20-40% faster than GPU frozenset version
- ✅ Documentation of optimization patterns

### Week 4 Success  
- ✅ 10-20 solvers converted
- ✅ Measurable improvement in full ARC benchmark
- ✅ Reusable patterns for future conversions

## Next Steps

1. **Read solver source** for the 3 candidate solvers
2. **Identify o_g usage patterns** (how many calls, what happens between them)
3. **Create optimized versions** using tuple format
4. **Benchmark on Kaggle** with L4 GPU
5. **Document findings** for Week 4 scaling

---

**Status**: Starting Week 3
**Goal**: Prove tuple format optimization value
**Target**: 20-40% speedup on multi-o_g solvers
**Commit**: df0cf94 (Week 2 complete)

Let's begin by analyzing the three candidate solvers! 🚀
