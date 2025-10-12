# GPU Execution Engine Design

**Date:** October 10, 2025  
**Status:** Planning Phase  
**Goal:** GPU-accelerate the entire `batt()` execution pipeline for 2-4x speedup

## Problem Analysis

### Current Architecture
- **Execution Model**: DAG (Directed Acyclic Graph) with 600+ sequential operations per `batt()` call
- **Operation Pattern**: `t1 → t2 → t3 → ...` with dependencies between steps
- **Data Flow**: Single grid transformations with intermediate results cached
- **Bottleneck**: CPU execution + repeated type conversions (Grid ↔ FrozenSet ↔ Tuple)

### Why Individual Operation GPU Acceleration Failed
1. **Transfer overhead** dominates for single operations (23x slower for fgpartition)
2. **No batch processing** - operations called one at a time
3. **Sequential dependencies** - can't parallelize across operations

## Solution: GPU-Resident Execution

### Core Strategy
**Keep all grids on GPU for entire `batt()` execution, only transfer final results**

```
┌─────────────────────────────────────────────────────────┐
│                    CPU (Control Flow)                    │
│  • DAG execution order                                   │
│  • Operation dispatch                                    │
│  • Dependency tracking                                   │
└────────────┬────────────────────────────────┬───────────┘
             │ transfer once                  │ transfer once
             ↓                                ↓
┌─────────────────────────────────────────────────────────┐
│                GPU (Data & Computation)                  │
│  • All grids cached on GPU (gpu_cache)                  │
│  • Hot operations run on GPU (o_g, mapply, difference)  │
│  • Cold operations fall back to CPU                      │
│  • Minimize GPU ↔ CPU transfers                         │
└─────────────────────────────────────────────────────────┘
```

## Implementation Plan

### Phase 1: GPU Cache Infrastructure (Week 1)

**File:** `gpu_env.py`

```python
class GPUEnv(Env):
    """GPU-accelerated execution environment"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gpu_available = self._check_gpu()
        self.gpu_cache = {}  # {step_id: gpu_array}
        self.transfer_count = 0
        self.stats = {'gpu_ops': 0, 'cpu_ops': 0, 'transfers': 0}
        
    def do_pile(self, t_num, t, isok=True):
        """GPU-aware operation execution"""
        if not isok or t is None:
            return OKT(False, None)
            
        func = t[0]
        args = t[1:]
        
        # Try GPU execution for hot operations
        if self.gpu_available and self._is_gpu_eligible(func):
            try:
                result = self._execute_on_gpu(func, args, t_num)
                self.stats['gpu_ops'] += 1
                return OKT(True, result)
            except Exception as e:
                # Fallback to CPU on GPU error
                pass
        
        # CPU execution (original behavior)
        self.stats['cpu_ops'] += 1
        return super().do_pile(t_num, t, isok)
```

**Key Features:**
- ✅ Transparent GPU usage - no changes to generated `batt()` code
- ✅ Automatic fallback to CPU if GPU fails
- ✅ Statistics tracking for performance analysis
- ✅ Compatible with evolutionary changes

### Phase 2: GPU Operation Registry (Week 1-2)

**File:** `gpu_ops_registry.py`

```python
# Priority 1: High-frequency grid operations (implement first)
GPU_OPS_PRIORITY_1 = {
    'o_g': gpu_o_g,              # Objects on grid (30+ calls)
    'p_g': gpu_p_g,              # Partition grid (every differ block)
    'fgpartition': gpu_fgpartition,  # Foreground partition
}

# Priority 2: High-frequency set operations
GPU_OPS_PRIORITY_2 = {
    'difference': gpu_difference,      # Set difference (100+ calls)
    'difference_tuple': gpu_diff_tuple,  # Tuple difference
    'mapply': gpu_mapply,              # Map apply (50+ calls)
    'apply': gpu_apply,                # Apply function
}

# Priority 3: Color operations (if time permits)
GPU_OPS_PRIORITY_3 = {
    'f_ofcolor': gpu_f_ofcolor,    # Filter by color
    'colorfilter': gpu_colorfilter,  # Color filtering
    'replace': gpu_replace,          # Replace color
    'fill': gpu_fill,                # Fill region
}

def get_gpu_implementation(func_name: str):
    """Get GPU implementation if available"""
    for registry in [GPU_OPS_PRIORITY_1, GPU_OPS_PRIORITY_2, GPU_OPS_PRIORITY_3]:
        if func_name in registry:
            return registry[func_name]
    return None
```

**Adaptive Strategy:**
- Start with Priority 1 (highest impact)
- Measure speedup after each priority level
- Stop adding operations when speedup plateaus
- ✅ **Evolution-proof:** New operations automatically fall back to CPU

### Phase 3: Smart Transfer Management (Week 2)

```python
class GPUTransferManager:
    """Minimize CPU ↔ GPU transfers"""
    
    def __init__(self):
        self.gpu_cache = {}
        self.cpu_cache = {}
        self.access_count = {}  # Track hot data
        
    def get_data(self, step_id, cpu_data):
        """Get data, prefer GPU cache"""
        if step_id in self.gpu_cache:
            return self.gpu_cache[step_id], 'gpu'
        
        # Transfer to GPU if accessed frequently
        if self._is_hot_data(step_id):
            gpu_data = cp.asarray(cpu_data)
            self.gpu_cache[step_id] = gpu_data
            return gpu_data, 'gpu'
            
        return cpu_data, 'cpu'
    
    def _is_hot_data(self, step_id):
        """Determine if data should be GPU-resident"""
        return self.access_count.get(step_id, 0) > 2
```

**Key Optimizations:**
- Keep frequently accessed grids on GPU
- Transfer cold data only when needed
- Lazy CPU→GPU transfer (only if operation is GPU-accelerated)
- Batch cleanup at end of `batt()` execution

## Expected Performance

### Baseline (Current CPU)
- **Total `batt()` time:** ~200-300ms for 650 operations
- **Per-operation average:** ~0.3-0.5ms
- **Hot operations (o_g, difference):** ~1-5ms each

### Target (GPU-Accelerated)
- **Initial transfer (I, C grids):** ~1-2ms (one-time cost)
- **GPU operations:** ~0.1-0.2ms each (2-3x faster than CPU)
- **Hot operations on GPU:** ~0.3-1ms (3-5x faster)
- **Final transfer (results):** ~1ms (one-time cost)
- **Total `batt()` time:** ~80-150ms
- **Expected speedup:** **2-4x overall**

### Breakdown by Operation Category

| Category | CPU Time | GPU Time | Speedup | Count | Impact |
|----------|----------|----------|---------|-------|--------|
| Grid ops (o_g, p_g) | 30-50ms | 8-15ms | 3-4x | 30-50 | 🔥 HIGH |
| Set ops (difference) | 40-60ms | 20-30ms | 2x | 100+ | 🔥 HIGH |
| Color ops | 20-30ms | 10-15ms | 2x | 50+ | ⚡ MEDIUM |
| Simple ops (size, nth) | 80-100ms | 80-100ms | 1x | 400+ | ❌ NO GPU |
| **Total** | **200-300ms** | **80-150ms** | **2-4x** | **650+** | ✅ **WIN** |

## Risk Mitigation

### Challenge 1: GPU Memory Limits
**Solution:** 
- Implement LRU cache eviction for old grids
- Monitor GPU memory usage
- Fallback to CPU if GPU memory exhausted

### Challenge 2: Type Conversion Overhead
**Problem:** Grid ↔ FrozenSet conversions on CPU
**Solution:** 
- Implement GPU-native set representations
- Use boolean masks instead of explicit sets where possible
- Keep common data structures on GPU

### Challenge 3: Complex Python Operations
**Problem:** Some operations involve complex Python logic (Callables, nested structures)
**Solution:**
- Only GPU-accelerate numerical/array operations
- Let complex operations run on CPU naturally
- Don't force everything onto GPU

### Challenge 4: Evolution Changes Operation Frequencies
**Solution:**
- ✅ **Adaptive registry:** Easy to add/remove GPU operations
- ✅ **Automatic CPU fallback:** No crash if GPU op unavailable
- ✅ **Statistics tracking:** Measure which ops actually help
- ✅ **No code changes:** Generated `batt()` files unchanged

## Testing Strategy

### Unit Tests (Phase 1)
```python
def test_gpu_env_correctness():
    """GPU results must match CPU exactly"""
    cpu_env = Env(seed, task_id, S)
    gpu_env = GPUEnv(seed, task_id, S)
    
    for step in range(650):
        cpu_result = cpu_env.do_pile(step, operations[step])
        gpu_result = gpu_env.do_pile(step, operations[step])
        assert cpu_result.t == gpu_result.t  # Exact match required
```

### Integration Tests (Phase 2)
```python
def test_gpu_batt_speedup():
    """Measure actual speedup on real batt() execution"""
    import time
    
    # CPU baseline
    start = time.perf_counter()
    cpu_result = batt_cpu(task_id, S, I, C, log_path)
    cpu_time = time.perf_counter() - start
    
    # GPU version
    start = time.perf_counter()
    gpu_result = batt_gpu(task_id, S, I, C, log_path)
    gpu_time = time.perf_counter() - start
    
    print(f"CPU: {cpu_time*1000:.1f}ms, GPU: {gpu_time*1000:.1f}ms")
    print(f"Speedup: {cpu_time/gpu_time:.2f}x")
    
    assert gpu_result == cpu_result  # Correctness
    assert gpu_time < cpu_time  # Speedup
```

### Kaggle Validation (Phase 3)
- Test on all 3 GPU types (T4x2, P100, L4x4)
- Verify speedup across 100+ different `batt()` executions
- Ensure no memory leaks over long runs

## Implementation Timeline

### Week 1: Foundation
- ✅ Create `gpu_env.py` with basic GPU cache
- ✅ Implement `GPUTransferManager`
- ✅ Add Priority 1 operations (o_g, p_g, fgpartition)
- ✅ Unit tests for correctness

### Week 2: Expansion
- ✅ Add Priority 2 operations (difference, mapply, apply)
- ✅ Optimize transfer strategy
- ✅ Integration tests with real `batt()` files
- ✅ Measure and document speedup

### Week 3: Polish & Deploy
- ⚡ Add Priority 3 operations (if needed)
- ⚡ Kaggle testing on all GPU types
- ⚡ Performance profiling and optimization
- ✅ Update documentation and integration guide

## Success Criteria

### Minimum (Must Have)
- ✅ **2x speedup** on full `batt()` execution
- ✅ **100% correctness** - all results match CPU exactly
- ✅ **Transparent usage** - no changes to generated code
- ✅ **Automatic fallback** - works even without GPU

### Target (Should Have)
- 🎯 **3x speedup** on typical workloads
- 🎯 **Works on all Kaggle GPU types** (T4x2, P100, L4x4)
- 🎯 **< 5% memory overhead** compared to CPU
- 🎯 **Statistics tracking** for optimization

### Stretch (Nice to Have)
- 🌟 **4x speedup** on grid-heavy workloads
- 🌟 **Multi-GPU support** for parallel `batt()` executions
- 🌟 **Adaptive operation selection** based on profiling
- 🌟 **GPU operation fusion** for common patterns

## Next Steps

1. **Create `gpu_env.py`** - Basic GPUEnv class with cache infrastructure
2. **Port `o_g` to GPU** - Highest impact operation (30+ calls)
3. **Test correctness** - Ensure GPU matches CPU exactly
4. **Measure baseline** - Get actual speedup numbers
5. **Iterate** - Add more operations based on profiling

---

## Questions for Review

1. **Architecture:** Does the GPU-resident execution model make sense for your DAG execution?
2. **Priorities:** Agree with Priority 1/2/3 operation classification?
3. **Evolution:** Is the adaptive registry sufficient for handling evolution changes?
4. **Testing:** Any additional test scenarios to consider?
5. **Timeline:** 3 weeks reasonable for initial implementation?

Let me know if you want to proceed with creating `gpu_env.py` or if you'd like to adjust the design! 🚀
