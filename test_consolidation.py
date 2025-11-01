#!/usr/bin/env python3
"""
Consolidation Validation Test Script

This script validates that the DSL consolidation (removing _t/_f variants)
produces identical results to the original code.

Strategy:
1. Run solvers_pre.py solvers against demo/test samples
2. Compare results with expected outputs
3. Verify all 138 tasks pass (same as before consolidation)
4. Report any regressions

Usage:
  python test_consolidation.py                    # Quick validation (10 samples)
  python test_consolidation.py --full             # Full validation (all samples)
  python test_consolidation.py --task 00d62c1b    # Single task test
"""

import sys
import argparse
from pathlib import Path
import inspect

# Import required modules
from grid import *
from dsl import *
from constants import *
from utils import *
import solvers_pre
import asyncio

# Import the validation infrastructure from run_test.py
import run_test


def validate_solvers_pre(task_limit=None, task_id=None, quiet=False):
    """
    Validate that solvers_pre.py produces correct output.
    
    Args:
        task_limit: Max number of tasks to test (None = all)
        task_id: Specific task to test (None = all)
        quiet: If True, only show summary
    
    Returns:
        tuple: (total_passed, total_tested)
    """
    # Get data
    total_data = run_test.get_data(train=True)
    
    # Get list of tasks to test
    all_tasks = list(total_data['demo'].keys())
    if task_id:
        if task_id not in all_tasks:
            print(f"❌ Task {task_id} not found in dataset")
            return 0, 1
        tasks_to_test = [task_id]
    else:
        tasks_to_test = all_tasks[:task_limit] if task_limit else all_tasks
    
    total_passed = 0
    total_tested = 0
    failed_tasks = []
    
    print(f"Validating {len(tasks_to_test)} tasks from solvers_pre.py")
    print("=" * 70)
    
    for task_idx, task in enumerate(tasks_to_test):
        total_tested += 1
        
        # Get demo and test samples
        demo_samples = total_data['demo'][task]
        test_samples = total_data['test'][task]
        all_samples = demo_samples + test_samples
        
        # Prepare training tuple S
        S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in demo_samples)
        
        # Check if solver exists
        if not hasattr(solvers_pre, f'solve_{task}'):
            if not quiet:
                print(f"  [{task_idx+1}/{len(tasks_to_test)}] {task}: ⚠️  No solver")
            continue
        
        # Get the solver function
        try:
            solver = getattr(solvers_pre, f'solve_{task}')
            # Ensure solver has access to DSL functions
            solver.__globals__.update(globals())
            
            # Test on all samples (demo + test)
            task_passed = True
            samples_correct = 0
            
            for sample_idx, sample in enumerate(all_samples):
                try:
                    expected = sample['output']
                    actual = solver(S, sample['input'], None)
                    
                    if actual == expected:
                        samples_correct += 1
                    else:
                        task_passed = False
                        if task_id:  # Show details for specific task
                            print(f"\n  Sample {sample_idx} mismatch:")
                            print(f"    Expected: {expected}")
                            print(f"    Got:      {actual}")
                except Exception as e:
                    task_passed = False
                    if task_id:
                        print(f"\n  Sample {sample_idx} error: {e}")
            
            # Report result
            if task_passed:
                total_passed += 1
                if not quiet:
                    print(f"  [{task_idx+1}/{len(tasks_to_test)}] {task}: ✅ Pass ({samples_correct}/{len(all_samples)})")
            else:
                failed_tasks.append((task, samples_correct, len(all_samples)))
                if not quiet:
                    print(f"  [{task_idx+1}/{len(tasks_to_test)}] {task}: ❌ Fail ({samples_correct}/{len(all_samples)})")
        
        except NameError as e:
            failed_tasks.append((task, 0, len(all_samples)))
            if not quiet:
                print(f"  [{task_idx+1}/{len(tasks_to_test)}] {task}: ❌ NameError: {e}")
        except Exception as e:
            failed_tasks.append((task, 0, len(all_samples)))
            if not quiet:
                print(f"  [{task_idx+1}/{len(tasks_to_test)}] {task}: ❌ Error: {e}")
    
    # Summary
    print()
    print("=" * 70)
    print(f"VALIDATION SUMMARY")
    print("=" * 70)
    print(f"Passed: {total_passed}/{total_tested}")
    print(f"Success rate: {100*total_passed/total_tested:.1f}%")
    
    if failed_tasks:
        print(f"\n❌ {len(failed_tasks)} Failed tasks:")
        for task, correct, total in failed_tasks:
            print(f"   {task}: {correct}/{total}")
    else:
        print(f"\n✅ ALL {total_tested} TASKS PASSED!")
    
    return total_passed, total_tested


def check_function_availability():
    """
    Verify that all consolidated functions are available in dsl.py
    (no _f variants remaining, only base names and _t variants for special cases)
    """
    print("Checking DSL function availability...")
    print("=" * 70)
    
    # Get all functions that should exist after consolidation
    expected_functions = [
        # Tier 1 - Collection Operations
        'apply', 'rapply', 'mapply', 'first', 'last', 'remove', 'other',
        'sfilter', 'mfilter', 'merge', 'combine',
        
        # Tier 2 - Selection Operations
        'get_nth', 'get_nth_by_key', 'get_arg_rank', 'get_val_rank', 'get_common_rank',
        
        # Tier 3 - Statistics Operations
        'size', 'valmax', 'valmin', 'argmax', 'argmin',
        'mostcommon', 'leastcommon', 'mostcolor', 'leastcolor',
        
        # Tier 4 - Geometric Operations
        'shape', 'palette', 'square', 'hmirror', 'vmirror',
        'dmirror', 'cmirror', 'portrait', 'colorcount',
    ]
    
    # Functions that should NOT exist (old _f variants)
    forbidden_functions = [
        'apply_f', 'rapply_f', 'mapply_f', 'first_f', 'last_f', 'remove_f', 'other_f',
        'sfilter_f', 'mfilter_f', 'merge_f', 'combine_f',
        'get_nth_f', 'get_nth_by_key_f', 'get_arg_rank_f', 'get_val_rank_f', 'get_common_rank_f',
        'size_f', 'valmax_f', 'valmin_f', 'argmax_f', 'argmin_f',
        'mostcommon_f', 'leastcommon_f', 'mostcolor_f', 'leastcolor_f',
        'shape_f', 'palette_f', 'square_f', 'hmirror_f', 'vmirror_f',
        'dmirror_f', 'cmirror_f', 'portrait_f', 'colorcount_f',
    ]
    
    missing = []
    present_forbidden = []
    
    # Check for expected functions
    for func in expected_functions:
        if not hasattr(dsl, func):
            missing.append(func)
    
    # Check for forbidden functions
    for func in forbidden_functions:
        if hasattr(dsl, func):
            present_forbidden.append(func)
    
    # Report
    if not missing and not present_forbidden:
        print(f"✅ All {len(expected_functions)} consolidated functions found")
        print(f"✅ No _f variants remain")
        return True
    else:
        if missing:
            print(f"❌ Missing {len(missing)} expected functions:")
            for f in missing:
                print(f"   - {f}")
        if present_forbidden:
            print(f"❌ Found {len(present_forbidden)} forbidden _f variants:")
            for f in present_forbidden:
                print(f"   - {f}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Validate DSL consolidation")
    parser.add_argument("--full", help="Test all tasks (default: first 10)", action="store_true")
    parser.add_argument("--task", help="Test specific task_id", type=str, default=None)
    parser.add_argument("-q", "--quiet", help="Minimal output", action="store_true")
    args = parser.parse_args()
    
    print("DSL CONSOLIDATION VALIDATION")
    print("=" * 70)
    print()
    
    # Step 1: Check function availability
    funcs_ok = check_function_availability()
    print()
    
    if not funcs_ok:
        print("❌ Function availability check failed!")
        print("   Consolidation may be incomplete.")
        return False
    
    # Step 2: Validate solvers_pre.py
    print()
    task_limit = None if args.full else 10
    passed, tested = validate_solvers_pre(task_limit=task_limit, task_id=args.task, quiet=args.quiet)
    
    success = (passed == tested)
    
    print()
    print("=" * 70)
    if success:
        print("✅ CONSOLIDATION VALIDATION PASSED")
        print(f"   {passed}/{tested} tasks passed")
        if not args.full:
            print("   (Run with --full to test all 138 tasks)")
    else:
        print("❌ CONSOLIDATION VALIDATION FAILED")
        print(f"   {passed}/{tested} tasks passed")
    
    return success


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
