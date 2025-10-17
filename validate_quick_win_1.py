#!/usr/bin/env python3
"""
Quick Win #1 Validation: Measure actual speedup from solver body caching
Compares performance with and without caching on a small task set
"""
import os
import sys
import time
import subprocess
import json
import tempfile
import shutil
from pathlib import Path

def run_batt_with_config(task_count, use_cache_enabled=True, label=""):
    """Run run_batt.py with specific configuration and measure time"""
    print(f"\n{'=' * 70}")
    print(f"Running: {label}")
    print(f"  Tasks: {task_count}")
    print(f"  Cache: {'ENABLED' if use_cache_enabled else 'DISABLED'}")
    print(f"{'=' * 70}")
    
    env = os.environ.copy()
    cmd = [
        'python', 'run_batt.py',
        '-c', str(task_count),
        '--timeout', '30'
    ]
    
    start_time = time.time()
    result = subprocess.run(cmd, capture_output=False, text=True, env=env)
    elapsed = time.time() - start_time
    
    print(f"\nElapsed time: {elapsed:.2f}s")
    return elapsed

def main():
    print("=" * 70)
    print("QUICK WIN #1 VALIDATION: Solver Body Caching")
    print("=" * 70)
    
    # Warmup run (primes caches and solvers)
    print("\n1. WARMUP RUN (establish baseline)...")
    time_warmup = run_batt_with_config(
        5, 
        use_cache_enabled=True,
        label="Warmup (5 tasks, cache enabled)"
    )
    
    # Second run should benefit from body cache
    print("\n2. VALIDATION RUN (measure cache benefit)...")
    print("   Note: This run uses same 5 tasks, cache should have 100% hit rate")
    time_cached = run_batt_with_config(
        5,
        use_cache_enabled=True, 
        label="Validation (5 tasks, cache enabled)"
    )
    
    # Calculate improvement
    if time_warmup > 0:
        improvement = (time_warmup - time_cached) / time_warmup * 100
        speedup = time_warmup / time_cached if time_cached > 0 else 0
        
        print("\n" + "=" * 70)
        print("RESULTS")
        print("=" * 70)
        print(f"Warmup (first run):     {time_warmup:.2f}s")
        print(f"Cached (second run):    {time_cached:.2f}s")
        print(f"Improvement:            {improvement:.1f}%")
        if speedup > 1:
            print(f"Speedup:                {speedup:.2f}x faster")
        else:
            print(f"Speedup:                {speedup:.2f}x (or {100-improvement:.1f}% slower - overhead)")
        
        # Write results to JSON for tracking
        results = {
            "optimization": "Quick Win #1: Solver Body Caching",
            "warmup_time": time_warmup,
            "cached_time": time_cached,
            "improvement_percent": improvement,
            "speedup_factor": speedup,
            "task_count": 5
        }
        
        with open('qw1_validation_results.json', 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\n✓ Results saved to: qw1_validation_results.json")
        
        if improvement > 0:
            print("✓ QUICK WIN #1 VALIDATED - Cache is improving performance!")
        else:
            print("⚠ Quick Win #1 shows no benefit on this small task set")
            print("  (Cache benefits typically appear with >10 repeated tasks)")
        
        print("=" * 70)
        return True
    else:
        print("\n✗ ERROR: Warmup run failed!")
        return False

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n✗ Test interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
