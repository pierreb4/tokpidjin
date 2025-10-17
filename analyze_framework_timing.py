#!/usr/bin/env python3
"""
Phase 4 Framework Analysis - Enhanced Timing Profiler

Purpose: Break down the 74% framework overhead into specific components
         and identify where optimization effort should focus

This approach:
1. Adds detailed timing hooks to key framework functions
2. Captures what's taking time in each phase
3. Identifies bottleneck components
4. Guides optimization priorities

Usage: python analyze_framework_timing.py -c 10 --detailed
"""

import sys
from pathlib import Path
from collections import defaultdict
from time import perf_counter

sys.path.insert(0, str(Path(__file__).parent))


class TimingAnalyzer:
    """Analyze framework execution timing by component."""
    
    def __init__(self):
        self.timings = defaultdict(list)
        self.component_totals = defaultdict(float)
    
    def record(self, component, func_name, elapsed_time):
        """Record timing for a component function."""
        key = f"{component}.{func_name}"
        self.timings[key].append(elapsed_time)
        self.component_totals[component] += elapsed_time
    
    def report(self):
        """Generate timing analysis report."""
        total_time = sum(self.component_totals.values())
        
        print(f"\n{'='*80}")
        print("FRAMEWORK TIMING ANALYSIS")
        print(f"{'='*80}\n")
        
        print(f"Total Framework Time: {total_time:.3f}s\n")
        
        # By component
        print(f"{'Component':<30} {'Total (s)':>10} {'% of Total':>12} {'Calls':>8}")
        print("-" * 65)
        
        sorted_components = sorted(
            self.component_totals.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        for component, comp_time in sorted_components:
            pct = (comp_time / total_time * 100) if total_time > 0 else 0
            call_count = len([t for k, v in self.timings.items() 
                            if k.startswith(f"{component}.")
                            for t in v])
            print(f"{component:<30} {comp_time:>10.3f} {pct:>11.1f}% {call_count:>8}")
        
        print(f"\nOptimization Priority:")
        print("-" * 65)
        
        # Top 5 optimization targets
        print(f"\nTop 5 Components by Time Spent:\n")
        for i, (component, comp_time) in enumerate(sorted_components[:5], 1):
            pct = (comp_time / total_time * 100) if total_time > 0 else 0
            print(f"{i}. {component:.<35} {comp_time:>8.3f}s ({pct:>5.1f}%)")
        
        print(f"\nRecommended Optimization Sequence:")
        print(f"  1. Profile and optimize: {sorted_components[0][0]}")
        print(f"  2. Profile and optimize: {sorted_components[1][0]}")
        print(f"  3. Profile and optimize: {sorted_components[2][0]}")
        print(f"\nEven small optimizations (10-20%) would provide significant speedup:")
        
        for i, (component, comp_time) in enumerate(sorted_components[:3], 1):
            reduction_10 = comp_time * 0.1
            reduction_20 = comp_time * 0.2
            total_10 = total_time - reduction_10
            total_20 = total_time - reduction_20
            speedup_10 = total_time / total_10
            speedup_20 = total_time / total_20
            
            print(f"\n  {component}:")
            print(f"    -10% saves {reduction_10:.3f}s (total {total_10:.3f}s, {speedup_10:.2f}x speedup)")
            print(f"    -20% saves {reduction_20:.3f}s (total {total_20:.3f}s, {speedup_20:.2f}x speedup)")


# Global analyzer
_timing_analyzer = TimingAnalyzer()


def patch_timings_into_run_batt():
    """
    Patch run_batt.py to add detailed timing analysis.
    
    This adds profiler hooks to measure each phase.
    """
    import run_batt
    
    # Get the original functions we want to measure
    original_check_batt = run_batt.check_batt
    original_check_sample = run_batt.check_sample
    original_generate_expanded = run_batt.generate_expanded
    
    def timed_check_batt(*args, **kwargs):
        start = perf_counter()
        result = original_check_batt(*args, **kwargs)
        elapsed = perf_counter() - start
        _timing_analyzer.record('check_batt', 'execution', elapsed)
        return result
    
    def timed_check_sample(*args, **kwargs):
        start = perf_counter()
        result = original_check_sample(*args, **kwargs)
        elapsed = perf_counter() - start
        _timing_analyzer.record('check_sample', 'execution', elapsed)
        return result
    
    def timed_generate_expanded(*args, **kwargs):
        start = perf_counter()
        result = original_generate_expanded(*args, **kwargs)
        elapsed = perf_counter() - start
        _timing_analyzer.record('generate_expanded', 'execution', elapsed)
        return result
    
    # Patch the module
    run_batt.check_batt = timed_check_batt
    run_batt.check_sample = timed_check_sample
    run_batt.generate_expanded = timed_generate_expanded


def main():
    """Run framework timing analysis."""
    import argparse
    import run_batt
    
    parser = argparse.ArgumentParser(description='Analyze framework timing')
    parser.add_argument('-c', '--count', type=int, default=10,
                       help='Number of tasks to profile (default: 10)')
    
    args = parser.parse_args()
    
    print(f"\nAnalyzing framework timing for {args.count} tasks...")
    print(f"This will break down the 74% framework overhead into components.\n")
    
    # Patch timing into run_batt
    patch_timings_into_run_batt()
    
    # Run the test
    sys.argv = ['run_batt.py', '-c', str(args.count), '--timing']
    import asyncio
    asyncio.run(run_batt.main())
    
    # Print analysis
    _timing_analyzer.report()


if __name__ == '__main__':
    main()
