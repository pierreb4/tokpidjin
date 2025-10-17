#!/usr/bin/env python3
"""
Phase 4 Framework Analysis - Profile DSL Operations Usage

Purpose: Understand which DSL operations are called most frequently
         and how much time they consume during solver execution

This is a lighter-weight analysis than full cProfile that focuses on:
1. Which DSL functions are called most frequently
2. Which operations take the most time
3. Which operations should be optimized

Usage: python profile_dsl_usage.py -c 10
"""

import sys
import asyncio
from pathlib import Path
from collections import defaultdict
from time import perf_counter
import importlib

sys.path.insert(0, str(Path(__file__).parent))


class DSLProfiler:
    """Profile DSL operation usage during solver execution."""
    
    def __init__(self):
        self.call_counts = defaultdict(int)
        self.call_times = defaultdict(float)
        self.call_details = defaultdict(list)
        self.active = False
    
    def enable(self):
        """Enable DSL operation tracking."""
        self.active = True
    
    def disable(self):
        """Disable DSL operation tracking."""
        self.active = False
    
    def record(self, func_name, elapsed_time):
        """Record a DSL operation call."""
        if not self.active:
            return
        
        self.call_counts[func_name] += 1
        self.call_times[func_name] += elapsed_time
        self.call_details[func_name].append(elapsed_time)
    
    def report(self, top_n=20):
        """Generate profiling report."""
        print(f"\n{'='*80}")
        print("DSL OPERATION PROFILING REPORT")
        print(f"{'='*80}\n")
        
        total_time = sum(self.call_times.values())
        total_calls = sum(self.call_counts.values())
        
        print(f"Total DSL operations: {total_calls}")
        print(f"Total time in DSL: {total_time:.3f}s")
        print(f"Average per call: {total_time/total_calls*1000:.3f}ms\n")
        
        # Sort by total time
        sorted_ops = sorted(
            self.call_times.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        print(f"{'Operation':<30} {'Calls':>8} {'Total (s)':>10} {'Per Call (ms)':>12} {'% of Time':>10}")
        print("-" * 75)
        
        for op_name, total_op_time in sorted_ops[:top_n]:
            count = self.call_counts[op_name]
            per_call = total_op_time / count * 1000 if count > 0 else 0
            pct = (total_op_time / total_time * 100) if total_time > 0 else 0
            
            print(f"{op_name:<30} {count:>8} {total_op_time:>10.3f} {per_call:>12.3f} {pct:>9.1f}%")
        
        print(f"\n{'Optimization Opportunities:':<30}")
        print("-" * 75)
        
        # Show top 5 opportunities
        for op_name, total_op_time in sorted_ops[:5]:
            count = self.call_counts[op_name]
            pct = (total_op_time / total_time * 100) if total_time > 0 else 0
            print(f"  • {op_name}: {count} calls, {total_op_time:.3f}s ({pct:.1f}% of total)")


# Global profiler instance
_dsl_profiler = DSLProfiler()


def instrument_dsl_module(dsl_module):
    """
    Wrap DSL functions to track their execution time.
    
    This replaces DSL functions with timing wrappers that record:
    - How many times each function is called
    - How much time each function takes
    """
    original_functions = {}
    
    # Get all callable attributes from dsl module
    for name in dir(dsl_module):
        if name.startswith('_'):
            continue
        
        obj = getattr(dsl_module, name)
        
        # Only wrap functions
        if not callable(obj):
            continue
        
        if name in ['print', 'len', 'list', 'dict', 'set', 'tuple']:
            continue
        
        # Store original
        original_functions[name] = obj
        
        # Create wrapper
        def make_wrapper(func_name, original_func):
            def wrapper(*args, **kwargs):
                start = perf_counter()
                try:
                    result = original_func(*args, **kwargs)
                    return result
                finally:
                    elapsed = perf_counter() - start
                    _dsl_profiler.record(func_name, elapsed)
            
            wrapper.__name__ = func_name
            return wrapper
        
        # Replace with wrapped version
        setattr(dsl_module, name, make_wrapper(name, obj))
    
    return original_functions


async def run_profiled_test(count=10):
    """Run the solver pipeline with DSL profiling enabled."""
    import run_batt
    
    # Import and instrument DSL module
    import dsl
    instrument_dsl_module(dsl)
    
    # Enable profiler
    _dsl_profiler.enable()
    
    try:
        # Run the test
        sys.argv = ['run_batt.py', '-c', str(count), '--timing']
        await run_batt.main()
    finally:
        _dsl_profiler.disable()


def main():
    """Run DSL profiling."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Profile DSL operation usage')
    parser.add_argument('-c', '--count', type=int, default=10,
                       help='Number of tasks to profile (default: 10)')
    parser.add_argument('--top', type=int, default=20,
                       help='Show top N operations (default: 20)')
    
    args = parser.parse_args()
    
    print(f"\nStarting DSL profiling for {args.count} tasks...")
    print(f"This will track which DSL operations are called most frequently.\n")
    
    # Run profiling
    asyncio.run(run_profiled_test(count=args.count))
    
    # Print report
    _dsl_profiler.report(top_n=args.top)


if __name__ == '__main__':
    main()
