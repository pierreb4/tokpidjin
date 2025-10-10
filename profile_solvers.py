#!/usr/bin/env python3
"""
Profile slow solver functions to identify expensive DSL operations.

This script instruments DSL operations to measure their execution time
within solver functions, helping us identify which operations to GPU-accelerate.

Target solvers:
- solve_36d67576: 120.674 ms (33 ops) - THE HOLY GRAIL
- solve_36fdfd69: 58.314 ms (16 ops) - EXCELLENT CANDIDATE
"""

import time
import sys
from typing import Dict, List, Tuple
from collections import defaultdict
from utils import get_data, print_l
import solvers_pre
from dsl import *
from constants import *


class DSLProfiler:
    """Profile DSL operation execution times within solver functions."""
    
    def __init__(self):
        self.operation_times = defaultdict(list)
        self.operation_calls = defaultdict(int)
        self.wrapped_functions = {}
        self.original_functions = {}
        
    def wrap_dsl_operations(self, operation_names: List[str]):
        """Wrap DSL operations with timing instrumentation."""
        import dsl
        
        for op_name in operation_names:
            if not hasattr(dsl, op_name):
                continue
            
            original_op = getattr(dsl, op_name)
            self.original_functions[op_name] = original_op
            
            def make_wrapper(name, func):
                def wrapper(*args, **kwargs):
                    start = time.perf_counter()
                    result = func(*args, **kwargs)
                    elapsed = (time.perf_counter() - start) * 1000  # ms
                    
                    self.operation_times[name].append(elapsed)
                    self.operation_calls[name] += 1
                    return result
                
                return wrapper
            
            wrapped = make_wrapper(op_name, original_op)
            setattr(dsl, op_name, wrapped)
            self.wrapped_functions[op_name] = wrapped
            
            # Also update solvers_pre module
            if hasattr(solvers_pre, op_name):
                setattr(solvers_pre, op_name, wrapped)
    
    def restore_dsl_operations(self):
        """Restore original DSL operations."""
        import dsl
        
        for op_name, original_func in self.original_functions.items():
            setattr(dsl, op_name, original_func)
            if hasattr(solvers_pre, op_name):
                setattr(solvers_pre, op_name, original_func)
    
    def get_stats(self) -> Dict[str, Dict]:
        """Get profiling statistics."""
        stats = {}
        
        for op_name in self.operation_times:
            times = self.operation_times[op_name]
            calls = self.operation_calls[op_name]
            total_time = sum(times)
            avg_time = total_time / calls if calls > 0 else 0
            
            stats[op_name] = {
                'calls': calls,
                'total_ms': total_time,
                'avg_ms': avg_time,
                'min_ms': min(times) if times else 0,
                'max_ms': max(times) if times else 0,
            }
        
        return stats
    
    def reset(self):
        """Reset profiling data."""
        self.operation_times.clear()
        self.operation_calls.clear()


def get_dsl_operations() -> List[str]:
    """Get list of DSL operations to profile."""
    import dsl
    
    # Get all functions from dsl module
    all_names = dir(dsl)
    
    # Filter to actual DSL operations (exclude builtins, types, etc.)
    dsl_ops = []
    for name in all_names:
        if name.startswith('_'):
            continue
        if name[0].isupper():  # Constants like ZERO, ONE, etc.
            continue
        
        obj = getattr(dsl, name)
        if callable(obj):
            dsl_ops.append(name)
    
    return dsl_ops


def profile_solver(
    profiler: DSLProfiler,
    solver_func,
    S: tuple,
    I: tuple,
    C: None,
    iterations: int = 10
) -> Tuple[Dict[str, Dict], float, bool]:
    """
    Profile a solver function.
    
    Returns:
        (stats, avg_total_time_ms, success)
    """
    profiler.reset()
    
    total_times = []
    success = True
    
    for _ in range(iterations):
        try:
            start = time.perf_counter()
            result = solver_func(S, I, C)
            elapsed = (time.perf_counter() - start) * 1000
            total_times.append(elapsed)
        except Exception as e:
            success = False
            break
    
    if not success or len(total_times) == 0:
        return {}, -1.0, False
    
    stats = profiler.get_stats()
    avg_total_time = sum(total_times) / len(total_times)
    
    return stats, avg_total_time, True


def print_profile_report(
    task_id: str,
    op_count: int,
    total_time: float,
    stats: Dict[str, Dict]
):
    """Print formatted profile report."""
    print_l("=" * 100)
    print_l(f"PROFILE REPORT: solve_{task_id}")
    print_l("=" * 100)
    print_l(f"Total operations: {op_count}")
    print_l(f"Total execution time: {total_time:.3f} ms")
    print_l("")
    
    # Sort operations by total time (descending)
    sorted_ops = sorted(stats.items(), key=lambda x: x[1]['total_ms'], reverse=True)
    
    print_l(f"{'Operation':<20} {'Calls':<8} {'Total (ms)':<12} {'Avg (ms)':<12} {'% of Total':<12} {'GPU Viable'}")
    print_l("=" * 100)
    
    for op_name, op_stats in sorted_ops:
        calls = op_stats['calls']
        total_ms = op_stats['total_ms']
        avg_ms = op_stats['avg_ms']
        percent = (total_ms / total_time) * 100 if total_time > 0 else 0
        
        # Determine GPU viability
        if avg_ms >= 1.0:
            gpu_viable = "✅ Yes"
        elif avg_ms >= 0.5:
            gpu_viable = "⚠️  Maybe"
        else:
            gpu_viable = "❌ No"
        
        print_l(f"{op_name:<20} {calls:<8} {total_ms:>10.3f}  {avg_ms:>10.3f}  {percent:>10.1f}%  {gpu_viable}")
    
    print_l("=" * 100)
    print_l("")
    
    # Summary of top GPU candidates
    print_l("TOP GPU CANDIDATES (avg time ≥ 0.5ms)")
    print_l("-" * 100)
    
    gpu_candidates = [(name, s) for name, s in sorted_ops if s['avg_ms'] >= 0.5]
    
    if len(gpu_candidates) > 0:
        for op_name, op_stats in gpu_candidates[:10]:  # Top 10
            print_l(f"  {op_name:<20} {op_stats['avg_ms']:>8.3f} ms/call  ({op_stats['calls']} calls, {op_stats['total_ms']:.1f} ms total)")
    else:
        print_l("  No operations with avg time ≥ 0.5ms")
    
    print_l("")


def main():
    print_l("=" * 100)
    print_l("DSL OPERATION PROFILER")
    print_l("Identifying expensive operations in slow solvers")
    print_l("=" * 100)
    print_l("")
    
    # Load ARC data
    print_l("Loading ARC data...")
    train_data = get_data(train=True)
    eval_data = get_data(train=False)
    total_data = {k: {**train_data[k], **eval_data[k]} for k in ['demo', 'test']}
    print_l(f"Loaded {len(total_data['demo'])} tasks")
    print_l("")
    
    # Get DSL operations to profile
    print_l("Identifying DSL operations to profile...")
    dsl_ops = get_dsl_operations()
    print_l(f"Found {len(dsl_ops)} DSL operations")
    print_l("")
    
    # Create profiler and wrap operations
    print_l("Wrapping DSL operations with timing instrumentation...")
    profiler = DSLProfiler()
    profiler.wrap_dsl_operations(dsl_ops)
    print_l("Ready to profile!")
    print_l("")
    
    # Target solvers (from benchmark results)
    target_solvers = [
        ('36d67576', 33, 120.674),  # THE HOLY GRAIL
        ('36fdfd69', 16, 58.314),   # EXCELLENT
        ('1a07d186', 16, 11.004),   # GOOD
        ('09629e4f', 7, 6.379),     # GOOD
        ('272f95fa', 22, 7.857),    # GOOD
        ('29623171', 22, 5.170),    # GOOD
        ('23b5c85d', 3, 7.594),     # GOOD
        ('1f85a75f', 3, 5.011),     # GOOD
    ]
    
    for task_id, op_count, expected_time in target_solvers:
        # Check if solver exists
        if task_id not in total_data['demo']:
            print_l(f"⚠️  Task {task_id} not found in data, skipping...")
            print_l("")
            continue
        
        # Get solver function
        solver_func = getattr(solvers_pre, f'solve_{task_id}', None)
        if solver_func is None:
            print_l(f"⚠️  Solver solve_{task_id} not found, skipping...")
            print_l("")
            continue
        
        # Get task data
        task = total_data['demo'][task_id]
        if len(task) == 0:
            print_l(f"⚠️  Task {task_id} has no samples, skipping...")
            print_l("")
            continue
        
        # Use first sample
        sample = task[0]
        S = tuple((tuple(s['input']), tuple(s['output'])) for s in task)
        I = sample['input']
        
        # Profile solver
        print_l(f"Profiling solve_{task_id} (expected: {expected_time:.1f} ms)...")
        stats, actual_time, success = profile_solver(profiler, solver_func, S, I, None, iterations=10)
        
        if not success:
            print_l(f"❌ Profiling failed for solve_{task_id}")
            print_l("")
            continue
        
        # Print report
        print_profile_report(task_id, op_count, actual_time, stats)
    
    # Restore original DSL operations
    print_l("Restoring original DSL operations...")
    profiler.restore_dsl_operations()
    print_l("Done!")


if __name__ == '__main__':
    main()
