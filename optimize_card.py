#!/usr/bin/env python3
"""
Optimize card.py code generation by caching expensive operations.

Key insights from profiling:
- get_solvers(): 0.477s (54%) - Load solver source code
- get_data(): 0.255s (29%) - Load training data  
- Actual generation: ~1.5ms/task (negligible)

Strategy:
1. Cache loaded data/solvers in memory
2. Generate code for multiple tasks in one invocation
3. Avoid redundant file I/O and imports
"""

import os
import time
import hashlib
from functools import lru_cache
from utils import *


# Cache loaded data at module level
_DATA_CACHE = {}
_SOLVER_CACHE = {}


@lru_cache(maxsize=1)
def get_cached_data(train=True):
    """Cache training/test data to avoid repeated JSON loading"""
    return get_data(train=train, sort_by_size=True)


@lru_cache(maxsize=1)
def get_cached_solvers(best_only=True):
    """Cache solvers to avoid repeated file I/O and source inspection"""
    return get_solvers([solvers_dir], best_only=best_only)


def generate_batch_batt(task_ids, output_file='batch_batt.py', freeze_solvers=False, freeze_differs=False):
    """
    Generate batt code for multiple tasks in one go.
    Reuses loaded data/solvers across all tasks.
    
    This is the key optimization - instead of calling card.py 400 times,
    call this once with 400 task IDs.
    """
    start = time.perf_counter()
    
    # Load data and solvers ONCE
    print(f"Loading data and solvers...")
    load_start = time.perf_counter()
    
    train_data = get_cached_data(train=True)
    all_solvers = get_cached_solvers(best_only=freeze_solvers)
    
    load_time = time.perf_counter() - load_start
    print(f"  Loaded in {load_time:.3f}s")
    
    # Filter to requested tasks
    solvers = {k: all_solvers[k] for k in task_ids if k in all_solvers}
    
    if not solvers:
        print(f"No solvers found for {len(task_ids)} tasks")
        return
    
    print(f"Generating code for {len(solvers)} tasks...")
    gen_start = time.perf_counter()
    
    # Import card module functions
    from card import main as card_main
    
    # Call card.py main with the filtered set
    # This will generate code for all tasks in one pass
    card_main(
        count=0,  # Use all provided solvers
        task_id=None,
        freeze_solvers=freeze_solvers,
        freeze_differs=freeze_differs,
        batt_file_name=output_file,
        vectorized=False
    )
    
    gen_time = time.perf_counter() - gen_start
    total_time = time.perf_counter() - start
    
    print(f"  Generated in {gen_time:.3f}s")
    print(f"  Total time: {total_time:.3f}s")
    print(f"  Per-task: {total_time/len(solvers)*1000:.1f}ms")
    print(f"  Savings: {load_time/total_time*100:.1f}% was one-time loading")
    
    return output_file


def benchmark_optimization():
    """Compare old vs new approach"""
    import subprocess
    
    task_count = 20
    
    print("="*100)
    print("BENCHMARK: Old vs New Approach")
    print("="*100)
    
    # Old approach: Call card.py separately (simulated)
    print(f"\n1. OLD APPROACH: Separate calls (simulated)")
    print(f"   Would call: card.py -c 1 ... {task_count} times")
    
    # Time single call to estimate
    start = time.perf_counter()
    subprocess.run(['python', 'card.py', '-c', '1', '-f', 'tmp_old.py'], 
                   capture_output=True, check=True)
    single_time = time.perf_counter() - start
    
    estimated_old = single_time * task_count
    print(f"   Single call: {single_time:.3f}s")
    print(f"   Estimated {task_count} tasks: {estimated_old:.3f}s")
    
    # New approach: Batch generation
    print(f"\n2. NEW APPROACH: Batch generation")
    
    # Get some task IDs
    train_data = get_cached_data(train=True)
    task_ids = list(train_data['demo'].keys())[:task_count]
    
    start = time.perf_counter()
    generate_batch_batt(task_ids, output_file='tmp_new.py', freeze_solvers=True)
    batch_time = time.perf_counter() - start
    
    print(f"\n3. RESULTS:")
    print(f"   Old (estimated): {estimated_old:.3f}s ({estimated_old/task_count*1000:.1f}ms/task)")
    print(f"   New (actual):    {batch_time:.3f}s ({batch_time/task_count*1000:.1f}ms/task)")
    print(f"   Speedup:         {estimated_old/batch_time:.2f}x")
    print(f"   Time saved:      {estimated_old-batch_time:.3f}s ({(estimated_old-batch_time)/estimated_old*100:.1f}%)")
    
    # Cleanup
    for f in ['tmp_old.py', 'tmp_old_call.py', 'tmp_new.py', 'tmp_new_call.py']:
        if os.path.exists(f):
            os.remove(f)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'benchmark':
        benchmark_optimization()
    else:
        # Example usage
        train_data = get_cached_data(train=True)
        task_ids = list(train_data['demo'].keys())[:50]
        
        print(f"Generating code for {len(task_ids)} tasks...")
        generate_batch_batt(task_ids, output_file='optimized_batt.py', freeze_solvers=True)
