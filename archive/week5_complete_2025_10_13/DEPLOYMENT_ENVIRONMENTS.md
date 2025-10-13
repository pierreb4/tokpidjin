# Deployment Environment Analysis

**Date**: October 13, 2025  
**Context**: Understanding real performance requirements across deployments

## Three Different Environments

### 1. Local Development (Laptop)
```
Hardware: Fast MacBook Pro
CPU: High single-core performance (~10x faster than Kaggle)
Use Case: Development, testing, quick iterations
Constraints: Single instance, interactive use
Performance: batt ~10ms, inlining ~318ms, validation ~586ms

NOT REPRESENTATIVE OF PRODUCTION!
```

### 2. Kaggle Competition (GPU Container)
```
Hardware: 4x NVIDIA L4 + Shared CPU
CPU: Containerized, slower single-core (~10x slower than laptop)
GPU: 4x L4 (22.3GB each) but high overhead for small batches
Use Case: Competition submission, batch scoring
Constraints: 9-hour runtime limit, shared resources
Performance: batt ~127ms (with GPU!), inlining ~2.989s, validation ~2.770s

CURRENT BOTTLENECK: Slow containerized CPU
```

### 3. Production Server (Future)
```
Hardware: Multi-core CPU servers (TBD)
CPU: Moderate single-core, many cores available
Use Case: Multiple concurrent run_card.sh instances
Constraints: Multiple processes competing for CPU
Performance: Unknown (likely between laptop and Kaggle)

KEY CONSTRAINT: Multiple concurrent instances!
```

## Critical Insight: Kaggle CPU is Slow!

### Local vs Kaggle Performance Comparison
```
Operation           Local (Laptop)  Kaggle (Container)  Ratio
─────────────────────────────────────────────────────────────
Batt (CPU-only)     10ms           127ms (GPU!)        12.7x
                                   ~40ms (CPU fallback) 4.0x
Variable Inlining   318ms          2,989ms             9.4x
Solver Validation   586ms          2,770ms             4.7x
Inline Batch        ~100ms         976ms               9.8x
─────────────────────────────────────────────────────────────
Total per Task      ~1.0s          ~6.9s               6.9x
```

**Discovery**: Kaggle's containerized CPU is 5-10x slower than laptop!

### Why is Kaggle CPU So Slow?

1. **Containerization Overhead**
   - Docker/Kubernetes virtualization
   - Shared kernel with other containers
   - Resource throttling

2. **Older/Slower CPU Architecture**
   - Xeon CPUs optimized for throughput, not single-core speed
   - Lower clock speeds (1.8-2.5 GHz vs laptop's 3-4 GHz)

3. **Resource Competition**
   - Multiple containers on same host
   - CPU time slicing
   - Cache contention

4. **No Turbo Boost**
   - Server CPUs don't boost as aggressively
   - Thermal limits in data center

## Revised Optimization Strategy

### ❌ WRONG Approach (What We Almost Did)
```
"GPU is 10x slower, disable it!"
"Optimize for laptop performance!"
"Single-threaded is best!"
```

### ✅ RIGHT Approach (What We Should Do)

#### 1. GPU Threshold is Actually Correct!
```python
# Current threshold: len(S) < 3
# We thought: Raise to len(S) < 100

# BUT WAIT - On Kaggle:
# - Small batches (2-5): CPU 40ms, GPU 127ms → CPU wins ✓
# - Large batches (100+): CPU 400ms, GPU 100ms → GPU wins ✓

# The problem: We're never getting large batches!
# Solution: Keep threshold, but engineer for large batches
```

**Key Insight**: GPU code is fine. We just need batch sizes > 100.

#### 2. Multi-Instance Server Considerations
```python
# Server will run multiple run_card.sh concurrently
# Each instance competes for:
# - CPU cores
# - Memory
# - I/O bandwidth

# Optimization Priorities:
# 1. Minimize CPU usage per instance
# 2. Use multiprocessing CAREFULLY (don't starve other instances)
# 3. Cache aggressively (share across instances)
# 4. Efficient memory usage (avoid copies)
```

**Multi-Instance Strategy**:
- Each instance: 2-4 worker processes (not 8+)
- Shared cache (Redis/disk) for validation results
- Efficient resource allocation
- Monitor and throttle if needed

#### 3. Kaggle-Specific Optimizations
```python
# Kaggle CPU is SLOW but we're stuck with it
# Can't make CPU faster, so:

# Strategy A: Reduce CPU work
# - Cache everything possible
# - Skip redundant operations
# - Simplify algorithms

# Strategy B: Better use slow CPU
# - Multiprocessing (4-6 workers, not too many)
# - Parallel validation
# - Parallel inlining where possible

# Strategy C: Better leverage GPU
# - Batch operations when possible
# - Keep GPU code for future mega-batching
# - Don't disable GPU yet!
```

## Revised Week 6 Priorities

### Priority 1: Cache Everything (HIGH IMPACT, LOW RISK)
**Impact**: 30-50% speedup on Kaggle, helps all environments

```python
# Cache validation results
validation_cache = {}  # Or Redis for multi-instance

def check_solver_speed(solver):
    cache_key = hash(solver)
    if cache_key in validation_cache:
        return validation_cache[cache_key]
    
    result = _do_validation(solver)
    validation_cache[cache_key] = result
    return result

# Expected Impact on Kaggle:
# Validation: 2.770s → 0.5s (5.5x) on repeated runs
# First run unchanged, but subsequent runs much faster
```

**Benefits**:
- Works on laptop, Kaggle, and server
- No risk (pure optimization)
- Helps multi-instance server (shared cache)
- Solves slow Kaggle CPU indirectly

### Priority 2: Parallel Validation (MEDIUM IMPACT, LOW RISK)
**Impact**: 2-4x speedup on Kaggle

```python
# Use ProcessPoolExecutor with 4 workers
# (Not too many - leave CPU for other instances on server)

from concurrent.futures import ProcessPoolExecutor

def validate_all_solvers(solvers):
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(check_solver_speed, solvers))
    return results

# Expected Impact on Kaggle:
# Validation: 2.770s → 0.7-1.0s (3-4x)
# Uses slow Kaggle CPU cores in parallel
```

**Benefits**:
- Bypasses single-core slowness
- 4 workers reasonable for server (won't starve other instances)
- Works on all environments

### Priority 3: Parallel Inlining (HIGH IMPACT, MEDIUM RISK)
**Impact**: 2-3x speedup on Kaggle

```python
# Inlining is 9.4x slower on Kaggle (2.989s vs 318ms)
# Multiprocessing can help but must be careful

# Strategy: Process multiple solvers in parallel
# Each worker does full inlining for one solver

from concurrent.futures import ProcessPoolExecutor

def inline_all_solvers(solvers):
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(inline_variables, solvers))
    return results

# Expected Impact on Kaggle:
# Inlining: 2.989s → 1.0-1.5s (2-3x)
```

**Risks**:
- Memory usage (each worker has copy of data)
- Process startup overhead
- May not parallelize well if bottleneck is AST library

**Mitigation**:
- Profile first to confirm CPU-bound
- Start with 4 workers (conservative)
- Add memory monitoring

### Priority 4: Algorithm Optimization (MEDIUM IMPACT, MEDIUM RISK)
**Impact**: 20-50% speedup on specific operations

```python
# Profile and optimize hot paths in:
# - utils.inline_variables (slow AST traversal)
# - check_solver_speed (redundant checks)
# - AST parsing/unparsing (use faster libraries)

# Example: Skip inlining for simple cases
def inline_variables(code):
    if is_simple_case(code):
        return code  # Skip expensive inlining
    
    return _full_inline(code)
```

### Priority 5: GPU Batch Architecture (FUTURE)
**Impact**: Potentially huge, but requires architectural changes

```python
# Current: Process samples individually
# batt(task_id, S, I, C) where S has 2-5 samples

# Future: Mega-batch architecture
# collect_samples_from_multiple_tasks() → 100+ samples
# batch_process_all_samples_gpu() → 10-35x speedup
# distribute_results_to_tasks()

# This is HARD - requires major refactoring
# But could unlock true GPU potential
```

## Server Multi-Instance Strategy

### Resource Allocation Per Instance
```bash
# Server with 32 cores, 64GB RAM
# Running 8 concurrent instances

# Per instance:
# - Max 4 worker processes (32 cores / 8 instances)
# - 6-8 GB memory limit
# - Shared cache (Redis or filesystem)
# - Nice level to prevent starvation
```

### Monitoring and Throttling
```python
# Each instance monitors:
# - CPU usage (stay under 50% of allocated cores)
# - Memory usage (stay under limit)
# - I/O bandwidth

# If over limit:
# - Reduce worker count
# - Increase sleep between operations
# - Wait for other instances to finish
```

### Shared Cache Architecture
```python
# Redis cache shared across instances
# - Validation results (solver → pass/fail)
# - Inlining results (code → inlined_code)
# - Known good/bad patterns

# Benefits:
# - First instance does work
# - Other instances get cached results
# - Warm cache helps all instances
```

## Testing Strategy for Each Environment

### Local Development (Laptop)
```bash
# Fast iteration, correctness testing
bash run_card.sh -c 5 -T -m  # CPU mode
bash run_card.sh -c 5 -T -g  # GPU mode (if available)

# Focus: Correctness, algorithm validation
# Don't optimize for laptop performance!
```

### Kaggle Competition
```bash
# Full scale testing with slow CPU
bash run_card.sh -c 50 -T -g  # Auto-detect GPU
bash run_card.sh -c 50 -T -m  # Force CPU (comparison)

# Focus: 
# - Cache effectiveness
# - Parallel processing on slow CPU
# - GPU threshold correctness
# - Total runtime under 9 hours
```

### Server Deployment (Simulation)
```bash
# Simulate multiple instances
for i in {1..8}; do
  bash run_card.sh -c 20 -T &
done
wait

# Focus:
# - Resource sharing
# - No instance starvation
# - Cache benefits across instances
# - Total throughput
```

## Key Metrics for Each Environment

### Laptop (Development)
- Correctness: 100%
- Fast iteration: < 2s per test
- Memory usage: < 2GB

### Kaggle (Competition)
- Total runtime: < 9 hours for 400 tasks
- Per-task time: < 1.5-2.0s (target)
- Cache hit rate: > 80% on subsequent runs
- GPU utilization: > 50% if batches large enough

### Server (Production)
- Throughput: 8 instances × 400 tasks = 3200 tasks
- Per-instance resources: < 4 cores, < 8GB RAM
- Completion time: < 12 hours for all instances
- No instance starvation: All complete within 2x of best
- Cache effectiveness: > 90% hit rate across instances

## Revised Action Plan

### Week 6A: Caching (Days 1-2)
1. Implement validation result cache
2. Implement inlining result cache  
3. Test on Kaggle (expect 30-50% improvement)
4. Add Redis/filesystem cache for server

### Week 6B: Parallel Processing (Days 3-4)
1. Parallel solver validation (4 workers)
2. Test on Kaggle (expect 3-4x validation speedup)
3. Parallel inlining (4 workers, careful with memory)
4. Test on Kaggle (expect 2-3x inlining speedup)

### Week 6C: Algorithm Optimization (Day 5)
1. Profile hot paths on Kaggle
2. Skip inlining for simple cases
3. Optimize AST operations
4. Test end-to-end improvement

### Week 6D: Multi-Instance Testing (Day 6-7)
1. Simulate 8 concurrent instances locally
2. Test resource sharing and cache
3. Monitor for starvation
4. Tune worker counts and limits

### Future: Mega-Batch Architecture
1. Design sample collection across tasks
2. Batch processing with 100+ samples
3. Result distribution
4. Test on Kaggle (expect 10-35x GPU speedup)

## Expected Results

### After Week 6A-C (Kaggle)
```
Operation           Current    After Opt   Speedup
──────────────────────────────────────────────────
Variable Inlining   2.989s     1.0-1.5s    2-3x
Solver Validation   2.770s     0.5-1.0s    3-5x
Inline Batch        0.976s     0.5-0.7s    1.5-2x
Batt (keep GPU)     0.379s     0.379s      1x
──────────────────────────────────────────────────
Total per Task      6.9s       2.4-3.7s    1.9-2.9x
```

### Server Multi-Instance (8 concurrent)
```
Metric                  Without Opt    With Opt
─────────────────────────────────────────────────
Per-task time           ~10-15s        ~3-5s
Total time (400 tasks)  ~40-60s        ~15-25s
Per instance (serial)   ~6-8 hours     ~2-3 hours
All instances (8x)      ~6-8 hours     ~2-3 hours
Cache hit rate          0%             90%+
```

## Key Decisions

### ✅ DO
1. Implement aggressive caching (validation, inlining)
2. Use conservative multiprocessing (4 workers)
3. Optimize for Kaggle's slow CPU specifically
4. Keep GPU code (threshold is correct)
5. Design for multi-instance server deployment
6. Test in all three environments

### ❌ DON'T
1. Disable GPU (we need it for future mega-batches)
2. Optimize for laptop (not representative)
3. Use too many workers (starves other instances)
4. Ignore memory usage (server constraint)
5. Make changes without profiling on Kaggle first

## Success Criteria

### Week 6 Success
- ✅ Kaggle: 6.9s → 2.5-3.5s per task (2-3x faster)
- ✅ Server: 8 instances run without starvation
- ✅ Cache: 80%+ hit rate on repeated runs
- ✅ Correct: All results match sequential baseline

### Long-term Success
- ✅ Kaggle: < 9 hours for 400 tasks with margin
- ✅ Server: High throughput with multiple instances
- ✅ Maintainable: Clear code, good documentation
- ✅ Flexible: Easy to adjust for different deployments
