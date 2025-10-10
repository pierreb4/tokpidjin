#!/usr/bin/env python3
"""
Quick test of optimized GPU-DSL module
Run this on Kaggle to verify the improvements
"""

print("="*70)
print("Testing Optimized GPU-DSL Module")
print("="*70)

# Import and run tests
from gpu_dsl import test_rot90_correctness, benchmark_rot90, GPU_AVAILABLE

if __name__ == "__main__":
    # First verify correctness
    if test_rot90_correctness():
        print("\n✓ Correctness tests passed!")
        
        # Then benchmark performance
        print("\n" + "="*70)
        print("Running optimized benchmark...")
        print("="*70)
        benchmark_rot90(sizes=[20, 50, 100, 200, 500], grid_size=(25, 25))
    else:
        print("\n✗ Correctness tests failed!")
    
    if GPU_AVAILABLE:
        print("\n" + "="*70)
        print("Key Optimizations Applied:")
        print("="*70)
        print("""
1. ✓ Single GPU memory allocation per batch
2. ✓ GPU warmup to trigger JIT compilation  
3. ✓ No intermediate CPU transfers
4. ✓ Minimum batch size threshold (20)
5. ✓ Best-of-3 timing for accuracy

Expected Results:
- Batch 20:    ~2-3x speedup
- Batch 50:    ~3-5x speedup
- Batch 100:   ~5-8x speedup
- Batch 200+:  ~8-12x speedup
        """)
