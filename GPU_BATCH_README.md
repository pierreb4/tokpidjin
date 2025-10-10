# GPU Batch Processing for Kaggle

This implementation provides GPU-accelerated batch processing optimized for Kaggle's GPU environments:
- **NVIDIA T4 x2**: 16GB memory, Compute 7.5
- **NVIDIA P100**: 16GB memory, Compute 6.0  
- **NVIDIA L4 x4**: 24GB memory, Compute 8.9

## Features

### 1. Intelligent Batch Processing (`GPUBatchProcessor`)
- Automatic GPU detection and configuration
- Dynamic batch size adjustment based on available memory
- Graceful fallback to CPU when GPU is unavailable or encounters errors
- Memory cleanup between batches to prevent OOM

### 2. GPU Memory Management
- `configure_gpu_memory()`: Configure memory pool for Kaggle constraints
- `gpu_memory_cleanup()`: Clean up memory between batches
- `get_optimal_batch_size()`: Calculate optimal batch size based on grid size and available memory

### 3. Batch Grid Operations
- `batch_grid_operations()`: Process multiple grids in parallel on GPU
- `gpu_grid_transform()`: Apply transformations to individual grids with GPU acceleration
- Automatic format conversion (tuple ↔ numpy/cupy)
- Same-shape optimization for efficient batching

## Usage

### Basic Batch Processing

```python
from run_batt import GPUBatchProcessor, configure_gpu_memory

# Configure GPU
configure_gpu_memory(device_id=0, memory_fraction=0.8)

# Create processor
processor = GPUBatchProcessor(batch_size=32, use_gpu=True)

# Process tasks
tasks = [...]  # Your tasks
results = processor.process_tasks_batch(tasks)
```

### Batch Grid Operations

```python
from dsl import batch_grid_operations

# Define operation
def my_operation(grid):
    return grid + 1

# Process multiple grids
grids = [grid1, grid2, grid3, ...]
results = batch_grid_operations(grids, my_operation)
```

### Optimal Batch Sizing

```python
from run_batt import get_optimal_batch_size

# Get optimal batch size for your workload
batch_size = get_optimal_batch_size(
    grid_size=400,  # 20x20 grids
    num_samples=100
)
```

## Memory Guidelines

### T4/P100 (16GB)
- **Small grids** (10x10): batch_size = 64
- **Medium grids** (20x20): batch_size = 32
- **Large grids** (30x30): batch_size = 16

### L4 (24GB)
- **Small grids** (10x10): batch_size = 128
- **Medium grids** (20x20): batch_size = 64
- **Large grids** (30x30): batch_size = 32

## Performance Tips

1. **Use Same-Shape Batches**: Grids with the same shape can be stacked for maximum efficiency
2. **Clean Memory Regularly**: Call `gpu_memory_cleanup()` between large batches
3. **Monitor Memory**: The processor automatically adjusts batch size when memory is low
4. **Profile First**: Run `test_gpu_batch.py` to see actual performance on your Kaggle instance

## Testing

Run the comprehensive test suite:

```bash
python test_gpu_batch.py
```

This will test:
1. GPU detection and configuration
2. Memory management
3. Batch size optimization
4. Batch operations performance
5. Processor functionality
6. Memory cleanup

## Expected Speedups (on Kaggle GPUs)

### T4
- Small batches (10-20 grids): 2-3x
- Medium batches (50-100 grids): 5-8x
- Large batches (100+ grids): 10-15x

### P100
- Similar to T4 but with higher memory bandwidth
- Better for large grid operations

### L4
- Best performance for large batches
- 1.5-2x faster than T4 for compute-intensive operations

## Integration with run_card.sh

The batch processor is designed to work seamlessly with the existing workflow:

```bash
# GPU will be automatically detected and used
./run_card.sh -c 100 -t 1.0
```

The processor will:
1. Detect available GPU(s)
2. Configure memory appropriately
3. Process tasks in batches
4. Clean up memory automatically
5. Fall back to CPU if needed

## Troubleshooting

### Out of Memory (OOM)
- Reduce batch size manually
- Increase memory cleanup frequency
- Check for memory leaks in custom operations

### Slow Performance
- Ensure grids are being converted to GPU arrays
- Check if operations are GPU-compatible
- Profile with `test_gpu_batch.py` to identify bottlenecks

### GPU Not Detected
- Verify CuPy installation: `pip install cupy-cuda12x` (or appropriate CUDA version)
- Check CUDA paths in `dsl.py`
- Ensure Kaggle notebook has GPU enabled

## Future Enhancements

1. Multi-GPU support for L4x4 configurations
2. Async batch processing with asyncio
3. GPU-accelerated specific DSL functions (fgpartition, gravitate, etc.)
4. Automatic kernel compilation for custom operations
5. Memory-mapped arrays for very large datasets

## Notes for Kaggle

- Kaggle provides 30 hours/week of GPU time
- T4 is most common, L4 is newest
- GPU memory is shared across all operations
- Set `memory_fraction=0.8` to leave room for system operations
- Monitor with `nvidia-smi` command in Kaggle terminal
