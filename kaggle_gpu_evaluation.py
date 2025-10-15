#!/usr/bin/env python3
"""
Kaggle GPU Evaluation - Test what actually works

This script tests:
1. GPU detection and initialization
2. CPU-only baseline performance (run_card.sh without -g)
3. DSL operations (check if any use GPU)
4. Batch operations (gpu_optimizations.py)
5. Run a few actual solvers and measure time

Usage on Kaggle:
    python kaggle_gpu_evaluation.py
"""

import time
import sys
import os
from utils import print_l

def test_gpu_detection():
    """Test if GPU is detected and CuPy works"""
    print_l("=" * 100)
    print_l("TEST 1: GPU DETECTION")
    print_l("=" * 100)
    
    try:
        import cupy as cp
        print_l("✅ CuPy imported successfully")
        
        gpu_available = cp.cuda.is_available()
        print_l(f"GPU Available: {gpu_available}")
        
        if gpu_available:
            gpu_count = cp.cuda.runtime.getDeviceCount()
            print_l(f"GPU Count: {gpu_count}")
            
            for i in range(gpu_count):
                device = cp.cuda.Device(i)
                compute = device.compute_capability
                mem_total = device.mem_info[1] / (1024**3)
                print_l(f"  GPU {i}: Compute {compute}, Memory: {mem_total:.1f}GB")
            
            # Test simple GPU operation
            try:
                a = cp.array([1, 2, 3])
                b = cp.array([4, 5, 6])
                c = a + b
                result = cp.asnumpy(c)
                print_l(f"✅ GPU computation works: {result}")
                return True, gpu_count
            except Exception as e:
                print_l(f"❌ GPU computation failed: {e}")
                return False, 0
        else:
            print_l("⚠️  No GPU detected")
            return False, 0
            
    except ImportError:
        print_l("❌ CuPy not available")
        return False, 0
    except Exception as e:
        print_l(f"❌ GPU detection failed: {e}")
        return False, 0


def test_dsl_gpu():
    """Test if DSL operations use GPU"""
    print_l("\n" + "=" * 100)
    print_l("TEST 2: DSL GPU OPERATIONS")
    print_l("=" * 100)
    
    try:
        from dsl import o_g_t, GPU_AVAILABLE
        print_l(f"GPU_AVAILABLE in dsl: {GPU_AVAILABLE}")
        
        # Simple test grid
        test_grid = (
            (1, 1, 0, 0),
            (1, 1, 0, 0),
            (0, 0, 2, 2),
            (0, 0, 2, 2),
        )
        
        # Test o_g_t
        start = time.perf_counter()
        result = o_g_t(test_grid, 0)
        elapsed = (time.perf_counter() - start) * 1000
        
        print_l(f"o_g_t execution: {elapsed:.3f}ms")
        print_l(f"Result type: {type(result)}")
        print_l(f"Result length: {len(result)}")
        
        # Check if GPU was actually used by looking for CuPy in stack
        import inspect
        source = inspect.getsource(o_g_t)
        has_cupy = 'cupy' in source.lower() or 'cp.' in source
        has_gpu_check = 'GPU_AVAILABLE' in source or 'gpu' in source.lower()
        
        print_l(f"\nCode Analysis:")
        print_l(f"  Contains CuPy calls: {has_cupy}")
        print_l(f"  Contains GPU checks: {has_gpu_check}")
        
        if has_cupy:
            print_l("✅ o_g_t appears to have GPU code")
        else:
            print_l("❌ o_g_t is CPU-only (no CuPy found)")
        
        return has_cupy
        
    except Exception as e:
        print_l(f"❌ DSL test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_batch_operations():
    """Test gpu_optimizations.py batch operations"""
    print_l("\n" + "=" * 100)
    print_l("TEST 3: BATCH GPU OPERATIONS")
    print_l("=" * 100)
    
    try:
        from gpu_optimizations import auto_select_optimizer
        
        print_l("✅ gpu_optimizations imported")
        
        optimizer = auto_select_optimizer()
        
        if optimizer is not None:
            print_l(f"✅ Optimizer created: {optimizer.__class__.__name__}")
            
            # Test with simple grids
            test_grids = [
                ((1, 2), (3, 4)),
                ((5, 6), (7, 8)),
                ((9, 0), (1, 2)),
            ]
            
            def identity(grid):
                return grid
            
            start = time.perf_counter()
            results = optimizer.batch_grid_op_optimized(
                test_grids,
                identity,
                vectorized=False
            )
            elapsed = (time.perf_counter() - start) * 1000
            
            print_l(f"Batch operation: {elapsed:.3f}ms")
            print_l(f"Results: {len(results)} grids processed")
            print_l("✅ Batch operations working")
            return True
        else:
            print_l("⚠️  No optimizer available (CPU fallback)")
            return False
            
    except Exception as e:
        print_l(f"❌ Batch operations test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_run_batt_gpu():
    """Test if run_batt.py uses GPU"""
    print_l("\n" + "=" * 100)
    print_l("TEST 4: RUN_BATT GPU USAGE")
    print_l("=" * 100)
    
    try:
        import run_batt
        
        # Check for GPU optimizer
        has_gpu_optimizer = hasattr(run_batt, 'gpu_optimizer')
        print_l(f"Has gpu_optimizer: {has_gpu_optimizer}")
        
        if has_gpu_optimizer:
            gpu_opt = getattr(run_batt, 'gpu_optimizer')
            print_l(f"gpu_optimizer value: {gpu_opt}")
            print_l(f"gpu_optimizer type: {type(gpu_opt)}")
            
            if gpu_opt is not None:
                print_l("✅ gpu_optimizer initialized")
            else:
                print_l("⚠️  gpu_optimizer is None")
        
        # Check for GPU_AVAILABLE
        has_gpu_available = hasattr(run_batt, 'GPU_AVAILABLE')
        print_l(f"Has GPU_AVAILABLE: {has_gpu_available}")
        
        if has_gpu_available:
            gpu_avail = getattr(run_batt, 'GPU_AVAILABLE')
            print_l(f"GPU_AVAILABLE value: {gpu_avail}")
        
        # Check if GPUBatchProcessor exists
        has_gpu_batch = hasattr(run_batt, 'GPUBatchProcessor')
        print_l(f"Has GPUBatchProcessor class: {has_gpu_batch}")
        
        return has_gpu_optimizer and gpu_opt is not None
        
    except Exception as e:
        print_l(f"❌ run_batt GPU check failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_actual_solver():
    """Test running an actual solver"""
    print_l("\n" + "=" * 100)
    print_l("TEST 5: ACTUAL SOLVER EXECUTION")
    print_l("=" * 100)
    
    try:
        from utils import get_data
        import solvers_pre
        
        # Load data
        print_l("Loading ARC data...")
        train_data = get_data(train=True)
        
        # Pick a simple solver
        task_id = '007bbfb7'  # From your earlier test
        
        if task_id not in train_data['demo']:
            print_l(f"⚠️  Task {task_id} not found, trying another...")
            task_id = list(train_data['demo'].keys())[0]
        
        print_l(f"Testing with task: {task_id}")
        
        solver_name = f'solve_{task_id}'
        if not hasattr(solvers_pre, solver_name):
            print_l(f"❌ Solver {solver_name} not found")
            return False
        
        solver_func = getattr(solvers_pre, solver_name)
        
        # Get task data
        task = train_data['demo'][task_id]
        sample = task[0]
        S = tuple((tuple(s['input']), tuple(s['output'])) for s in task)
        I = sample['input']
        
        # Time execution
        print_l(f"Running {solver_name}...")
        start = time.perf_counter()
        result = solver_func(S, I, None)
        elapsed = (time.perf_counter() - start) * 1000
        
        print_l(f"✅ Solver executed in {elapsed:.3f}ms")
        print_l(f"Result type: {type(result)}")
        
        # Check correctness
        expected = sample['output']
        matches = result == expected
        print_l(f"Correct: {matches}")
        
        return True
        
    except Exception as e:
        print_l(f"❌ Solver test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_performance_baseline():
    """Run a few solvers to get performance baseline"""
    print_l("\n" + "=" * 100)
    print_l("TEST 6: PERFORMANCE BASELINE")
    print_l("=" * 100)
    
    try:
        from utils import get_data
        import solvers_pre
        
        train_data = get_data(train=True)
        
        # Test on 5 random tasks
        task_ids = list(train_data['demo'].keys())[:5]
        
        total_time = 0
        successful = 0
        
        for task_id in task_ids:
            solver_name = f'solve_{task_id}'
            
            if not hasattr(solvers_pre, solver_name):
                continue
            
            solver_func = getattr(solvers_pre, solver_name)
            task = train_data['demo'][task_id]
            
            if len(task) == 0:
                continue
            
            sample = task[0]
            S = tuple((tuple(s['input']), tuple(s['output'])) for s in task)
            I = sample['input']
            
            try:
                start = time.perf_counter()
                result = solver_func(S, I, None)
                elapsed = (time.perf_counter() - start) * 1000
                
                total_time += elapsed
                successful += 1
                
                print_l(f"  {task_id}: {elapsed:.3f}ms")
            except Exception as e:
                print_l(f"  {task_id}: FAILED ({e})")
        
        if successful > 0:
            avg_time = total_time / successful
            print_l(f"\n✅ Average execution time: {avg_time:.3f}ms ({successful}/{len(task_ids)} solvers)")
            return avg_time
        else:
            print_l(f"❌ No solvers succeeded")
            return None
            
    except Exception as e:
        print_l(f"❌ Performance baseline failed: {e}")
        import traceback
        traceback.print_exc()
        return None


def main():
    print_l("=" * 100)
    print_l("KAGGLE GPU EVALUATION")
    print_l("Testing what actually works in current implementation")
    print_l("=" * 100)
    print_l("")
    
    results = {}
    
    # Test 1: GPU Detection
    gpu_works, gpu_count = test_gpu_detection()
    results['gpu_detected'] = gpu_works
    results['gpu_count'] = gpu_count
    
    # Test 2: DSL GPU
    dsl_gpu = test_dsl_gpu()
    results['dsl_has_gpu'] = dsl_gpu
    
    # Test 3: Batch Operations
    batch_gpu = test_batch_operations()
    results['batch_gpu_works'] = batch_gpu
    
    # Test 4: run_batt GPU
    run_batt_gpu = test_run_batt_gpu()
    results['run_batt_has_gpu'] = run_batt_gpu
    
    # Test 5: Actual Solver
    solver_works = test_actual_solver()
    results['solver_works'] = solver_works
    
    # Test 6: Performance Baseline
    avg_time = test_performance_baseline()
    results['avg_solver_time_ms'] = avg_time
    
    # Summary
    print_l("\n" + "=" * 100)
    print_l("EVALUATION SUMMARY")
    print_l("=" * 100)
    print_l("")
    
    print_l("Infrastructure Status:")
    print_l(f"  GPU Detected: {results['gpu_detected']} ({results['gpu_count']} GPUs)")
    print_l(f"  DSL has GPU code: {results['dsl_has_gpu']}")
    print_l(f"  Batch GPU works: {results['batch_gpu_works']}")
    print_l(f"  run_batt has GPU: {results['run_batt_has_gpu']}")
    print_l("")
    
    print_l("Execution Status:")
    print_l(f"  Solvers work: {results['solver_works']}")
    if results['avg_solver_time_ms']:
        print_l(f"  Average solver time: {results['avg_solver_time_ms']:.3f}ms")
    print_l("")
    
    # Overall assessment
    print_l("Overall Assessment:")
    
    if not results['gpu_detected']:
        print_l("  ⚠️  NO GPU AVAILABLE - Running on CPU only")
    elif results['dsl_has_gpu'] and results['batch_gpu_works']:
        print_l("  ✅ GPU FULLY FUNCTIONAL - Both DSL and batch operations have GPU support")
    elif results['batch_gpu_works']:
        print_l("  ⚠️  PARTIAL GPU - Batch operations work, but DSL is CPU-only")
    elif results['dsl_has_gpu']:
        print_l("  ⚠️  PARTIAL GPU - DSL has GPU code, but batch operations don't work")
    else:
        print_l("  ❌ GPU INFRASTRUCTURE ONLY - GPU detected but no acceleration implemented")
    
    print_l("")
    print_l("Next Steps:")
    if not results['dsl_has_gpu']:
        print_l("  1. Implement GPU-accelerated DSL operations (o_g_t, objects_t, etc)")
    if not results['run_batt_has_gpu'] or not run_batt_gpu:
        print_l("  2. Connect gpu_optimizer to run_batt.py execution pipeline")
    if results['batch_gpu_works'] and not results['dsl_has_gpu']:
        print_l("  3. OR: Focus on integrating working batch operations into production")
    
    print_l("")
    print_l("=" * 100)
    print_l("EVALUATION COMPLETE")
    print_l("=" * 100)


if __name__ == '__main__':
    main()
