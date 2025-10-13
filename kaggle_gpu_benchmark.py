"""
Kaggle GPU Benchmark - Week 5 Day 3

This script benchmarks the mega-batch coordinator with GPU operations
on Kaggle's GPU infrastructure (T4, P100, or L4x4).

Expected speedups:
- Sequential (CPU baseline): 1.0x
- Parallel (4 workers, CPU): 3.5-4x
- Parallel + GPU (Tier 1): 7-12x

Usage:
    python kaggle_gpu_benchmark.py

Requirements:
    - Kaggle notebook with GPU enabled
    - Files: gpu_dsl_operations.py, mega_batch_batt.py, batt_gpu_operations_test.py, dsl.py, arc_types.py
    - Note: Uses batt_gpu_operations_test.py (calls actual GPU ops) not batt_mega_test.py (calls old GPU system)

Author: Pierre
Date: October 13, 2025
Week: 5 Day 3
"""

import sys
import logging
import json
from timeit import default_timer as timer
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def check_environment():
    """Check Kaggle environment and GPU availability"""
    print("\n" + "="*70)
    print("KAGGLE ENVIRONMENT CHECK")
    print("="*70)
    
    # Check if running on Kaggle (check for /kaggle directory instead of API)
    import os
    if os.path.exists('/kaggle'):
        print("✅ Running on Kaggle")
    else:
        print("⚠️  Not running on Kaggle (this is OK for local testing)")
    
    # Check GPU availability
    try:
        import cupy as cp
        gpu_count = cp.cuda.runtime.getDeviceCount()
        print(f"✅ CuPy available")
        print(f"✅ GPU count: {gpu_count}")
        
        for i in range(gpu_count):
            props = cp.cuda.runtime.getDeviceProperties(i)
            print(f"   GPU {i}: {props['name'].decode()}")
            print(f"   Memory: {props['totalGlobalMem'] / 1e9:.1f} GB")
        
        return True, gpu_count
    except Exception as e:
        print(f"❌ GPU not available: {e}")
        print("   Will use CPU fallback")
        return False, 0


def create_test_data():
    """Create test dataset for benchmarking"""
    # Simple test grids
    grid1 = ((0, 1, 0), (1, 0, 1), (0, 1, 0))
    grid2 = ((1, 1, 1), (1, 0, 1), (1, 1, 1))
    grid3 = ((2, 2), (2, 2))
    grid4 = ((3, 3, 3), (3, 3, 3), (3, 3, 3))
    
    # Create multiple tasks for better benchmarking
    mock_data = {
        'demo': {},
        'test': {}
    }
    
    # Generate 20 test tasks (80+ samples total)
    for task_num in range(20):
        task_id = f'bench_task_{task_num:03d}'
        
        # Vary the grids to make it more realistic
        grids = [grid1, grid2, grid3, grid4]
        demo_samples = []
        test_samples = []
        
        for i in range(2):  # 2 demo samples per task
            idx = (task_num + i) % len(grids)
            demo_samples.append({
                'input': grids[idx],
                'output': grids[(idx + 1) % len(grids)]
            })
        
        for i in range(2):  # 2 test samples per task
            idx = (task_num + i + 2) % len(grids)
            test_samples.append({
                'input': grids[idx],
                'output': None
            })
        
        mock_data['demo'][task_id] = demo_samples
        mock_data['test'][task_id] = test_samples
    
    return mock_data, [f'bench_task_{i:03d}' for i in range(20)]


def run_benchmark(mode='sequential', enable_gpu=False, parallel=True, max_workers=4):
    """Run benchmark with specified configuration"""
    from mega_batch_batt import MegaBatchCoordinator
    
    # Create test data
    mock_data, task_list = create_test_data()
    total_samples = sum(len(mock_data['demo'][t]) + len(mock_data['test'][t]) 
                       for t in task_list)
    
    print(f"\n{'='*70}")
    print(f"BENCHMARK: {mode.upper()}")
    print(f"{'='*70}")
    print(f"Tasks: {len(task_list)}")
    print(f"Total samples: {total_samples}")
    print(f"GPU enabled: {enable_gpu}")
    print(f"Parallel: {parallel}")
    print(f"Max workers: {max_workers}")
    print(f"{'='*70}\n")
    
    # Create coordinator
    # NOTE: Using batt_gpu_operations_test.py which actually calls our GPU operations
    # (batch_mapply, batch_o_g, batch_apply) instead of old batch_process_samples_gpu
    coordinator = MegaBatchCoordinator(
        batt_module_name='batt_gpu_operations_test',
        batch_size=20,
        enable_gpu=enable_gpu,
        parallel=parallel,
        max_workers=max_workers
    )
    
    # Run benchmark
    start_time = timer()
    try:
        results, elapsed = coordinator.process_all(mock_data, task_list)
        
        # Calculate metrics
        throughput = total_samples / elapsed
        
        print(f"\n{'='*70}")
        print(f"RESULTS - {mode.upper()}")
        print(f"{'='*70}")
        print(f"Total time: {elapsed:.3f}s")
        print(f"Throughput: {throughput:.1f} samples/s")
        print(f"Average per sample: {elapsed/total_samples*1000:.2f}ms")
        print(f"Tasks processed: {len(results)}")
        print(f"{'='*70}\n")
        
        return {
            'mode': mode,
            'elapsed': elapsed,
            'throughput': throughput,
            'samples': total_samples,
            'tasks': len(results),
            'avg_per_sample_ms': elapsed/total_samples*1000,
            'gpu_enabled': enable_gpu,
            'parallel': parallel,
            'max_workers': max_workers
        }
    
    except Exception as e:
        print(f"❌ Benchmark failed: {e}")
        import traceback
        traceback.print_exc()
        return None


def main():
    """Main benchmark routine"""
    print("\n" + "="*70)
    print("KAGGLE GPU BENCHMARK - WEEK 5 DAY 3")
    print("="*70)
    print("Testing mega-batch coordinator with GPU acceleration")
    print("Expected: 7-12x speedup vs sequential baseline")
    print("="*70 + "\n")
    
    # Check environment
    gpu_available, gpu_count = check_environment()
    
    # Run benchmarks
    results = []
    
    # Benchmark 1: Sequential (baseline)
    print("\n[1/4] Running Sequential Baseline...")
    result = run_benchmark(
        mode='sequential',
        enable_gpu=False,
        parallel=False,
        max_workers=1
    )
    if result:
        results.append(result)
        baseline_time = result['elapsed']
    else:
        print("❌ Sequential benchmark failed, aborting")
        return
    
    # Benchmark 2: Parallel (CPU only)
    print("\n[2/4] Running Parallel (CPU only)...")
    result = run_benchmark(
        mode='parallel_cpu',
        enable_gpu=False,
        parallel=True,
        max_workers=4
    )
    if result:
        results.append(result)
    
    # Benchmark 3: Parallel + GPU (if available)
    if gpu_available:
        print("\n[3/4] Running Parallel + GPU...")
        result = run_benchmark(
            mode='parallel_gpu',
            enable_gpu=True,
            parallel=True,
            max_workers=4
        )
        if result:
            results.append(result)
    else:
        print("\n[3/4] Skipping GPU benchmark (GPU not available)")
    
    # Benchmark 4: GPU with more workers (if available)
    if gpu_available and gpu_count >= 2:
        print("\n[4/4] Running Parallel + GPU (8 workers)...")
        result = run_benchmark(
            mode='parallel_gpu_8workers',
            enable_gpu=True,
            parallel=True,
            max_workers=8
        )
        if result:
            results.append(result)
    else:
        print("\n[4/4] Skipping multi-worker GPU benchmark")
    
    # Generate comparison report
    print("\n" + "="*70)
    print("BENCHMARK COMPARISON")
    print("="*70)
    print(f"{'Mode':<25} {'Time (s)':<12} {'Throughput':<15} {'Speedup':<10}")
    print("-"*70)
    
    for r in results:
        speedup = baseline_time / r['elapsed']
        print(f"{r['mode']:<25} {r['elapsed']:>10.3f}  {r['throughput']:>12.1f} s/s  {speedup:>8.2f}x")
    
    print("="*70)
    
    # Find best result
    if len(results) > 1:
        best = max(results, key=lambda x: x['throughput'])
        speedup = baseline_time / best['elapsed']
        
        print(f"\n🏆 BEST PERFORMANCE: {best['mode'].upper()}")
        print(f"   Speedup: {speedup:.2f}x vs sequential baseline")
        print(f"   Throughput: {best['throughput']:.1f} samples/s")
        
        # Compare to expectations
        print(f"\n📊 PERFORMANCE ANALYSIS:")
        print(f"   Expected (parallel CPU): 3.5-4x")
        print(f"   Expected (parallel + GPU): 7-12x")
        
        if 'gpu' in best['mode']:
            if speedup >= 7:
                print(f"   ✅ GPU performance EXCELLENT ({speedup:.1f}x >= 7x)")
            elif speedup >= 5:
                print(f"   ⚠️  GPU performance GOOD ({speedup:.1f}x, target 7-12x)")
            else:
                print(f"   ❌ GPU performance BELOW TARGET ({speedup:.1f}x < 5x)")
        else:
            if speedup >= 3.5:
                print(f"   ✅ CPU parallel performance GOOD ({speedup:.1f}x)")
            else:
                print(f"   ⚠️  CPU parallel performance BELOW TARGET ({speedup:.1f}x < 3.5x)")
    
    # Save results to JSON
    output_file = 'kaggle_gpu_benchmark_results.json'
    with open(output_file, 'w') as f:
        json.dump({
            'results': results,
            'baseline_time': baseline_time,
            'gpu_available': gpu_available,
            'gpu_count': gpu_count,
            'timestamp': str(timer())
        }, f, indent=2)
    
    print(f"\n💾 Results saved to {output_file}")
    print("\n" + "="*70)
    print("✅ BENCHMARK COMPLETE")
    print("="*70)
    
    # Return best speedup for programmatic use
    if len(results) > 1:
        return baseline_time / best['elapsed']
    return 1.0


if __name__ == '__main__':
    try:
        speedup = main()
        print(f"\nFinal speedup: {speedup:.2f}x")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Benchmark failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
