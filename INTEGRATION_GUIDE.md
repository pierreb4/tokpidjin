# Integration Guide: GPU Acceleration in Production

## Quick Start

### 1. Add GPU Support to Your DSL Functions

Pick your most-used functions and create GPU versions. Here's the pattern:

```python
# In dsl.py or new file gpu_dsl.py

import cupy as cp
import numpy as np
from gpu_optimizations import KaggleGPUOptimizer

# Initialize optimizer (do this once at module level)
_gpu_optimizer = KaggleGPUOptimizer() if GPU_AVAILABLE else None

# Example: Convert 'rot90' function
def rot90(grid):
    """Original CPU version"""
    return tuple(tuple(row) for row in np.rot90(grid))

def rot90_vectorized(batch):
    """GPU version - works on 3D tensor (batch_size, h, w)"""
    if isinstance(batch, cp.ndarray):
        return cp.rot90(batch, axes=(1, 2))
    return np.rot90(batch, axes=(1, 2))

def rot90_batch(grids):
    """Batch processor - automatically uses GPU or CPU"""
    if _gpu_optimizer and len(grids) >= 30:
        return _gpu_optimizer.batch_grid_op_optimized(
            grids,
            rot90_vectorized,
            vectorized=True,
            operation_single=lambda g: np.rot90(g)
        )
    else:
        return [rot90(g) for g in grids]
```

### 2. Convert High-Priority DSL Functions

Based on your timing analysis, convert these first:

#### Priority 1: fgpartition (~60s total time)
```python
def fgpartition_vectorized(batch):
    """
    Partition foreground/background on GPU
    batch: (batch_size, h, w) CuPy array
    """
    if isinstance(batch, cp.ndarray):
        # Find background (most common color per grid)
        # This is complex - may need custom kernel
        # For now, use per-grid on GPU
        results = []
        for i in range(batch.shape[0]):
            grid = batch[i]
            # Your partitioning logic here
            result = your_gpu_partition_logic(grid)
            results.append(result)
        return cp.stack(results)
    else:
        # CPU version
        return np.array([fgpartition_cpu(batch[i]) for i in range(batch.shape[0])])

def fgpartition_batch(grids):
    """Batch version"""
    if _gpu_optimizer and len(grids) >= 50:
        return _gpu_optimizer.batch_grid_op_optimized(
            grids,
            fgpartition_vectorized,
            vectorized=True,
            operation_single=fgpartition
        )
    return [fgpartition(g) for g in grids]
```

#### Priority 2: gravitate (physics simulation)
```python
def gravitate_vectorized(batch, direction):
    """
    Gravitate pixels in batch
    Highly parallelizable on GPU!
    """
    if isinstance(batch, cp.ndarray):
        # Example: gravity down
        if direction == 'down':
            # Iterate until stable (vectorized)
            for _ in range(batch.shape[1]):  # max iterations
                # Find movable pixels (non-zero with space below)
                movable = (batch[:, :-1, :] != 0) & (batch[:, 1:, :] == 0)
                # Shift them down
                batch[:, 1:, :] = cp.where(movable, batch[:, :-1, :], batch[:, 1:, :])
                batch[:, :-1, :] = cp.where(movable, 0, batch[:, :-1, :])
        return batch
    return np.array([gravitate_cpu(batch[i], direction) for i in range(batch.shape[0])])

def gravitate_batch(grids, direction):
    if _gpu_optimizer and len(grids) >= 50:
        return _gpu_optimizer.batch_grid_op_optimized(
            grids,
            lambda b: gravitate_vectorized(b, direction),
            vectorized=True,
            operation_single=lambda g: gravitate(g, direction)
        )
    return [gravitate(g, direction) for g in grids]
```

#### Priority 3: shift (simple operation)
```python
def shift_vectorized(batch, direction, amount=1):
    """
    Shift entire batch in direction
    Very fast on GPU!
    """
    if isinstance(batch, cp.ndarray):
        if direction == 'up':
            result = cp.roll(batch, -amount, axis=1)
            result[:, -amount:, :] = 0
        elif direction == 'down':
            result = cp.roll(batch, amount, axis=1)
            result[:, :amount, :] = 0
        elif direction == 'left':
            result = cp.roll(batch, -amount, axis=2)
            result[:, :, -amount:] = 0
        elif direction == 'right':
            result = cp.roll(batch, amount, axis=2)
            result[:, :, :amount] = 0
        return result
    return np.array([shift_cpu(batch[i], direction, amount) for i in range(batch.shape[0])])

def shift_batch(grids, direction, amount=1):
    if _gpu_optimizer and len(grids) >= 50:
        return _gpu_optimizer.batch_grid_op_optimized(
            grids,
            lambda b: shift_vectorized(b, direction, amount),
            vectorized=True,
            operation_single=lambda g: shift(g, direction, amount)
        )
    return [shift(g, direction, amount) for g in grids]
```

### 3. Integrate with run_batt.py

```python
# In run_batt.py

from gpu_optimizations import KaggleGPUOptimizer

class GPUBatchProcessor:
    def __init__(self, batch_size=100, use_gpu=True):
        self.batch_size = batch_size
        self.use_gpu = use_gpu and GPU_AVAILABLE
        
        if self.use_gpu:
            self.optimizer = KaggleGPUOptimizer()
            # Warmup
            print("Warming up GPU...")
            warmup_grids = [np.random.randint(0, 10, (25, 25)) for _ in range(50)]
            def warmup_op(b):
                return cp.rot90(b, axes=(1, 2)) if isinstance(b, cp.ndarray) else np.rot90(b, axes=(1, 2))
            _ = self.optimizer.batch_grid_op_optimized(
                warmup_grids, warmup_op, vectorized=True, operation_single=lambda g: np.rot90(g)
            )
            print("GPU ready")
    
    def process_solver_batch(self, solvers, test_cases):
        """
        Evaluate multiple solvers on test cases using GPU
        
        Args:
            solvers: List of solver functions
            test_cases: List of (input_grid, expected_output) tuples
        
        Returns:
            List of (solver, score) tuples
        """
        results = []
        
        # Batch test cases for GPU processing
        for solver in solvers:
            input_grids = [tc[0] for tc in test_cases]
            expected = [tc[1] for tc in test_cases]
            
            # Apply solver (may use GPU internally if solver is GPU-enabled)
            predictions = [solver(grid) for grid in input_grids]
            
            # Score
            correct = sum(1 for pred, exp in zip(predictions, expected) if np.array_equal(pred, exp))
            score = correct / len(test_cases)
            results.append((solver, score))
        
        return results
```

### 4. Update run_card.sh Workflow

```python
# In card.py or similar

from run_batt import GPUBatchProcessor

def evaluate_mutations(base_solver, test_cases, num_mutations=100):
    """
    Generate and evaluate solver mutations
    """
    # Generate mutations
    mutations = [mutate_solver(base_solver) for _ in range(num_mutations)]
    
    # Process in batches
    processor = GPUBatchProcessor(batch_size=100, use_gpu=True)
    
    all_results = []
    for i in range(0, len(mutations), 100):
        batch = mutations[i:i+100]
        batch_results = processor.process_solver_batch(batch, test_cases)
        all_results.extend(batch_results)
    
    # Return best
    return max(all_results, key=lambda x: x[1])
```

### 5. Gradual Migration Strategy

Don't convert everything at once. Use this phased approach:

#### Phase 1: Test with Simple Operations (Week 1)
```python
# Add GPU versions of rot90, flip, shift
# Run existing workflow with GPU acceleration
# Measure speedup (expect 2-3x)
```

#### Phase 2: Add Complex Operations (Week 2)
```python
# Add fgpartition, gravitate GPU versions
# Measure speedup (expect 5-7x)
# Monitor GPU memory usage
```

#### Phase 3: Batch-Aware Workflow (Week 3)
```python
# Modify workflow to accumulate batches of 100-200
# Process entire batches on GPU
# Measure end-to-end speedup (expect 5-10x)
```

#### Phase 4: Optimize Hot Paths (Week 4)
```python
# Profile to find remaining bottlenecks
# Convert additional functions as needed
# Fine-tune batch sizes
```

## Common Patterns

### Pattern 1: Simple Element-wise Operations
```python
def threshold_vectorized(batch, value):
    """Works on entire batch at once"""
    if isinstance(batch, cp.ndarray):
        return (batch > value).astype(cp.int32)
    return (batch > value).astype(np.int32)
```

### Pattern 2: Neighbor-based Operations
```python
def count_neighbors_vectorized(batch):
    """Count non-zero neighbors for each pixel"""
    if isinstance(batch, cp.ndarray):
        # Pad batch
        padded = cp.pad(batch, ((0,0), (1,1), (1,1)), constant_values=0)
        # Count neighbors (vectorized)
        neighbors = (
            padded[:, :-2, 1:-1] +  # top
            padded[:, 2:, 1:-1] +    # bottom
            padded[:, 1:-1, :-2] +   # left
            padded[:, 1:-1, 2:]      # right
        )
        return (neighbors > 0).astype(cp.int32)
    # CPU version
    return np.array([count_neighbors_cpu(batch[i]) for i in range(batch.shape[0])])
```

### Pattern 3: Iterative Operations
```python
def flood_fill_vectorized(batch, seed_mask):
    """Iterative flood fill on entire batch"""
    if isinstance(batch, cp.ndarray):
        filled = seed_mask.copy()
        for _ in range(max(batch.shape[1], batch.shape[2])):  # max iterations
            # Expand to neighbors
            padded = cp.pad(filled, ((0,0), (1,1), (1,1)), constant_values=0)
            expanded = (
                (padded[:, :-2, 1:-1] > 0) |
                (padded[:, 2:, 1:-1] > 0) |
                (padded[:, 1:-1, :-2] > 0) |
                (padded[:, 1:-1, 2:] > 0)
            )
            # Stay within same-color regions
            filled = expanded & (batch == batch)  # Your condition here
        return filled.astype(cp.int32)
    # CPU version
    return np.array([flood_fill_cpu(batch[i], seed_mask[i]) for i in range(batch.shape[0])])
```

## Testing Strategy

### Unit Tests
```python
# test_gpu_dsl.py

def test_rot90_equivalence():
    """Ensure GPU and CPU versions produce same results"""
    grids = [np.random.randint(0, 10, (25, 25)) for _ in range(100)]
    
    # CPU results
    cpu_results = [rot90(g) for g in grids]
    
    # GPU results
    gpu_results = rot90_batch(grids)
    
    # Compare
    for cpu, gpu in zip(cpu_results, gpu_results):
        assert np.array_equal(cpu, gpu), "GPU/CPU mismatch!"
```

### Performance Tests
```python
def benchmark_operation(operation_name, grids, cpu_func, gpu_func):
    """Benchmark CPU vs GPU"""
    import time
    
    # CPU
    start = time.time()
    cpu_results = [cpu_func(g) for g in grids]
    cpu_time = time.time() - start
    
    # GPU
    start = time.time()
    gpu_results = gpu_func(grids)
    gpu_time = time.time() - start
    
    speedup = cpu_time / gpu_time
    print(f"{operation_name}: {speedup:.2f}x speedup ({cpu_time*1000:.2f}ms → {gpu_time*1000:.2f}ms)")
    
    return speedup
```

## Monitoring & Debugging

### GPU Memory Usage
```python
import cupy as cp

def check_gpu_memory():
    """Monitor GPU memory"""
    device = cp.cuda.Device()
    mem_info = device.mem_info
    used = (mem_info[1] - mem_info[0]) / 1024**3
    total = mem_info[1] / 1024**3
    print(f"GPU Memory: {used:.1f}GB / {total:.1f}GB ({used/total*100:.1f}%)")

# Call periodically
check_gpu_memory()
```

### Performance Profiling
```python
def profile_gpu_operation(func, *args):
    """Profile GPU operation"""
    import cupy as cp
    from timeit import default_timer as timer
    
    # Warmup
    _ = func(*args)
    
    # Profile
    start = timer()
    result = func(*args)
    cp.cuda.Stream.null.synchronize()  # Wait for GPU to finish
    elapsed = timer() - start
    
    print(f"Operation took {elapsed*1000:.2f}ms")
    return result
```

## Troubleshooting

### Issue: Out of Memory
```python
# Reduce batch size
processor = GPUBatchProcessor(batch_size=50, use_gpu=True)  # Instead of 100

# Or process in smaller chunks
def process_large_batch(grids, chunk_size=100):
    results = []
    for i in range(0, len(grids), chunk_size):
        chunk = grids[i:i+chunk_size]
        chunk_results = gpu_process(chunk)
        results.extend(chunk_results)
    return results
```

### Issue: Slower than Expected
```python
# Check if operations are too simple
# Use CPU for simple ops, GPU for complex ones

def smart_batch_process(grids, operation):
    complexity = estimate_complexity(operation)
    
    if complexity > 100:  # Complex operation
        return gpu_process(grids)
    else:  # Simple operation
        return cpu_process(grids)
```

### Issue: Inconsistent Results
```python
# Ensure deterministic operations
cp.random.seed(42)
np.random.seed(42)

# Check for floating point precision issues
# Use int32, not float32, for grid operations
```

## Expected Performance

Based on Kaggle P100 results:

| Your Workflow | Typical Size | Expected Speedup | Time Saved |
|---------------|--------------|------------------|------------|
| Single solver test | 10 test cases | 1-2x | Minimal |
| Mutation batch | 100 mutations | 5-7x | Significant |
| Full optimization | 1000+ evals | 5-7x | 5-10 minutes per run |

## Summary

✅ **Start with simple operations** (rot90, flip, shift)  
✅ **Use batch size 100-200** for best speedup  
✅ **Gradually convert complex functions** (fgpartition, gravitate)  
✅ **Test thoroughly** (GPU/CPU equivalence)  
✅ **Monitor memory usage** (P100 has 16GB)  
✅ **Profile end-to-end** (measure actual workflow speedup)  

With these patterns, you can integrate GPU acceleration into your ARC solver workflow and achieve **5-7x speedup** on Kaggle P100! 🚀
