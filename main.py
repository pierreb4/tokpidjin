#!/usr/bin/env python3
"""
ARC Solver Testing Framework
===========================

This script provides a framework for testing and evaluating solvers for the Abstraction and
Reasoning Corpus (ARC). It includes functionality for validating solver formatting, testing 
correctness against example tasks, and measuring performance.

Features:
---------
- Test DSL primitives against their test implementations
- Validate the formatting of solver functions
- Test solver correctness against ARC tasks
- Measure and report execution time performance
- Optional function call tracking for optimization
- Support for focused testing of specific solvers
- Support for testing alternative solver implementations

Usage:
------
# Basic testing of all solvers
python main.py

# Test a specific solver by key
python main.py -k 88a62173

# Test solvers from an alternative module
python main.py --solvers solvers_evo.py

# Test with performance tracking enabled
python main.py --track --stats-output stats/my_stats.json

# Quick testing with minimal output
python main.py -q

# Performance-focused testing
python main.py -t 0.1 -w

Arguments:
---------
  -q, --quiet           Suppress verbose output and progress bars
  -k, --key KEY         Test only a specific task key
  -t, --timeout SEC     Warning threshold in seconds (default: 0.2s)
  -w, --wait            Wait for user input when timeout is exceeded
  --track               Enable function call statistics tracking
  --sample-rate RATE    Sampling rate for tracking (default: 0.01)
  --max-samples NUM     Maximum samples to collect per argument (default: 10)
  --stats-output FILE   File to save statistics output (default: module_stats.json)
  --solvers MODULE      Path to alternative solvers module (default: solvers.py)
"""


import os
import json
import inspect
import tqdm
import argparse
import contextlib
import time
import sys
import traceback
import glob
import math

from func_timeout import func_timeout, FunctionTimedOut

import arc_types
import constants
import dsl
import tests
import solvers_pre
import run_batt

from utils import *
from batt import batt


def get_data(train=True):
    path = f'../data/{"training" if train else "evaluation"}'
    data = {}
    for fn in os.listdir(path):
        with open(f'{path}/{fn}') as f:
            data[fn.rstrip('.json')] = json.load(f)
    ast = lambda g: tuple(tuple(r) for r in g)
    return {
        'train': {k: [{
            'input': ast(e['input']),
            'output': ast(e['output']),
        } for e in v['train']] for k, v in data.items()},
        'test': {k: [{
            'input': ast(e['input']),
            'output': ast(e['output']),
        } for e in v['test']] for k, v in data.items()}
    }


def get_functions(path):
    """ returns a list of available functions """
    with open(path, 'r') as f:
        code = f.read()
    functions = []
    for row in code.split('\n'):
        if row.startswith('def '):
            function = row.split('def ')[1].split('(')[0]
            functions.append(function)
    return functions


def run_dsl_tests(dsl_module, test_module, quiet=False):
    """ test DSL primitives """
    dsl_functions = get_functions(dsl_module.__file__)
    test_functions = get_functions(test_module.__file__)
    expected = {f'test_{f}' for f in dsl_functions}

    try:
        assert set(test_functions) == expected
    except AssertionError:
        if not quiet:
            print(f'Error: {len(test_functions)} test functions found, expected {len(expected)}')

    for fun in test_functions:
        getattr(test_module, fun)()

    if not quiet:
        print(f"All {len(test_functions)} DSL tests passed.")


def check_solvers_formatting(solvers_module, dsl_module, quiet=False):
    """ tests the implemented solvers for formatting """
    with open('constants.py', 'r') as f:
        constants = [c.split(' = ')[0] for c in f.readlines() if ' = ' in c]

    module_file = solvers_module.__file__
    functions = get_functions(module_file)

    # Filter out non-solver functions
    solver_functions = [f for f in functions if f.startswith('solve_')]

    definitions = {
        function: inspect.getsource(getattr(solvers_module, function)) \
            for function in solver_functions
    }
    dsl_interface = get_functions(dsl_module.__file__)
    n_correct = 0
    n = len(definitions)

    if not quiet:
        print(f"Testing {n} solver(s) in {os.path.basename(module_file)} for formatting...")

    for key, definition in definitions.items():
        try:
            lines = definition.split('\n')
            params_line = lines[0]
            # Check if the solver has the right signature (might be solve_xxx(I) or solve_xxx(S, I))
            assert params_line.startswith(f'def {key}(') and params_line.endswith(':')
            assert lines[-1] == ''
            variables = set()
            calls = set()
            for i, line in enumerate(lines[1:-2], 1):
                if '=' not in line.strip():
                    continue  # Skip non-assignment lines
                if 'x ==' in line:
                    continue # Skip comparison lines
                if 'return x' in line:
                    continue # Skip return statements
                variable, call = line.lstrip().split(' = ', 1)
                if '(' not in call:
                    continue  # Skip simple assignments
                function, args = call.split('(', 1)
                assert variable not in dsl_interface
                assert variable not in variables
                # Example troubleshooting assertion
                # try:
                assert call not in calls
                # except AssertionError:
                #     print(f'{key = } - {i = } - {call = } - {line = }')
                variables.add(variable)
                calls.add(call)
                assert function in dsl_interface or function in variables
                assert args[-1] == ')'
                args_str = args[:-1]
                args = [args_str] if ',' not in args_str else args_str.split(', ')
                for arg in args:
                    assert any([
                        arg in variables, arg in dsl_interface,
                        arg in constants, arg == 'I', arg == 'S'
                    ])
            for v in variables:
                assert (
                    sum(
                        definition.count(vs)
                        for vs in [
                            f'({v})',
                            f'({v}, ',
                            f', {v})',
                            f', {v}, ',
                            f' {v} = ',
                            f' {v}(',
                        ]
                    )
                    > 1
                    or v == 'O'
                )
            n_correct += 1
        except Exception as e:
            if quiet:
                # Add line number information to the error message
                line_number = getattr(e, 'lineno', None)
                line_info = f" at line {line_number}" if line_number else ""
                print_l(f"Error in {key}{line_info}: {len(lines)} lines")
            else:
                # Determine line number from traceback if available
                import sys, traceback
                exc_type, exc_obj, exc_tb = sys.exc_info()
                frame = traceback.extract_tb(exc_tb)[-1]
                line_number = frame.lineno if frame else "unknown"
                print_l(f'Exception at line {line_number}: {e}')
                print_l(f'Error in {key}:\n{definition}')

    print(f'{n_correct} out of {n} solvers in {os.path.basename(module_file)} formatted correctly.')


def check_solvers_correctness(data, solvers_module, task_id=None, quiet=False, timeout_warning=1.0, wait=False):
    """ checks the implemented solvers for correctness """
    functions = get_functions(solvers_module.__file__)
    solver_functions = [f for f in functions if f.startswith('solve_')]

    definitions = {
        function: inspect.getsource(getattr(solvers_module, function)) \
            for function in solver_functions
    }

    solve_func = {}
    solve_path = {}
    solve_score = {}

    if task_id:
        task_ids = [task_id]
        solve_func[task_id] = f'solve_{task_id}'
        solve_path[task_id] = None
        solve_score[task_id] = -math.inf
    else:
        task_ids = data["train"].keys()
        for task_id in task_ids:
            module = None
            files = glob.glob(f'solver_dir/solve_{task_id}/[0-9]*/[0-9]*/[0-9]*/[0-9a-f]*.py')
            for file in files:
                sections = file.split('/')
                score = int(sections[2])
                if module is None or score > module['score']:
                    t_log = int(sections[3])
                    module = {
                        'path': file,
                        'score': score,
                        't_log': t_log,
                        'name': sections[-1][:-3]}

            if module is None:
                continue

            solve_func[task_id] = module['name']
            solve_path[task_id] = module['path']
            solve_score[task_id] = module['score']


    n_correct = 0
    n_checked = 0
    n = len(solve_func)

    # Track execution times
    total_execution_time = 0.0
    total_examples = 0
    slow_solvers = []

    if quiet:
        # Without progress bar in quiet mode
        solver_iterator = tqdm.tqdm(solve_func.keys(), total=n)
    else:
        # With progress bar in normal mode
        print(f"Testing {n} tasks for correctness using {os.path.basename(solvers_module.__file__)}...")
        solver_iterator = solve_func.keys()

    fluff_log_path = 'fluff.log'
    if os.path.isfile(fluff_log_path):
        os.remove(fluff_log_path)
    for task_id in solver_iterator:
        task = data['train'][task_id] + data['test'][task_id]
        num_train = len(data['train'][task_id])

        S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in task)
        solver_execution_time = 0.0
        success = True

        correct_sample = 0
        remove_solve_path = False
        for i, sample in enumerate(task):
            start_time = time.time()
            I = sample['input']
            O = sample['output']
            flags = Flags(True, False)

            # NOTE This looks like the test in run_batt.py but:
            #      Here we check for a single top ranking non-mutated solution 
            #      from solver_dir/solve_{task_id}
            #      - Maybe we could check all top ranking solutions
            #      In run_batt.py we accept (mutated) solutions from any solver
            timed_out, run_result = run_with_timeout(batt, 
                    (task_id, S, I, O, flags, fluff_log_path), timeout_warning)

            execution_time = time.time() - start_time
            total_execution_time += execution_time
            total_examples += 1
            solver_execution_time += execution_time

            # Check if execution took too long
            if execution_time > timeout_warning:
                print(f"WARNING: {solve_func[task_id]} sample {i} took {execution_time:.2f}s - {timed_out = }")
                slow_solvers.append((task_id, i, execution_time))
                remove_solve_path = True

                # If wait is enabled, pause for user inspection
                if wait:
                    input("Press Enter to continue...")

                break

            if run_result is None:
                success = False
                break
            
            success = any(tid == task_id for _, _, tid, _ in run_result[0])
            if success:
                correct_sample += 1

        if correct_sample < solve_score[task_id] or remove_solve_path:
            print_l(f'rm {solve_path[task_id]}')
            if os.path.exists(solve_path[task_id]):
                os.remove(solve_path[task_id])

        if correct_sample == len(task):
            n_correct += 1
        n_checked += 1

        print_l(f'{n_correct}/{n_checked} - {n_correct / n_checked:.2f} - {total_examples}')

    # Calculate average execution time
    avg_time = total_execution_time / max(total_examples, 1)

    # Print summary with execution time statistics
    print(f'{n_correct} out of {n} tasks solved correctly using {os.path.basename(solvers_module.__file__)}.')
    print(f'Average execution time: {avg_time:.4f}s per example')

    # Print top slow solvers if any
    if slow_solvers:
        print(f'Found {len(slow_solvers)} examples exceeding the {timeout_warning}s threshold.')
        if not quiet and len(slow_solvers) <= 5:  # Show details only if not in quiet mode and not too many slow solvers
            print("Slowest examples:")
            for task_id, example, time_taken in sorted(slow_solvers, task_id=lambda x: x[2], reverse=True)[:5]:
                print(f"  - solve_{task_id} example {example}: {time_taken:.2f}s")

    return n_correct, avg_time, n


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test ARC solvers")
    parser.add_argument("-q", "--quiet", help="Suppress verbose output and progress bars",
                        action="store_true")
    parser.add_argument("--solvers", help="Use this instead of solvers_pre", type=str, default='solvers_pre')
    parser.add_argument("-i", "--task_id", help="Specific task_id to test", type=str)
    parser.add_argument("--check-dsl", help="Do DSL checks", action="store_true")
    parser.add_argument("--check-format", help="Do format checks", action="store_true")
    parser.add_argument("-t", "--timeout", help="Warning threshold in seconds (default: 1.0)",
                        type=float, default=1.0)
    parser.add_argument("-w", "--wait", help="Wait for user input when timeout is exceeded",
                        action="store_true")
    parser.add_argument("--track", help="Enable function call statistics tracking",
                        action="store_true")
    parser.add_argument("--sample-rate", help="Sampling rate for tracking (default: 0.01)",
                        type=float, default=0.01)
    parser.add_argument("--max-samples", help="Maximum number of samples to collect per argument (default: 10)",
                        type=int, default=10)
    parser.add_argument("--stats-output", help="File to save statistics output (default: module_stats.json)",
                        type=str, default="module_stats.json")
    args = parser.parse_args()

    # Load the specified solver module or use default
    if args.solvers:
        try:
            solvers_module = load_module(args.solvers)
            print(f"Using custom solver module: {args.solvers}")
        except Exception as e:
            print(f"Error loading solver module {args.solvers}: {e}")
            return
    else:
        solvers_module = solvers_pre  # Use default module

    # Configure and enable function tracking if requested
    if args.track:
        try:
            import patch_module
            from stats import configure, enable, print_stats, export_stats

            # Configure statistics collection
            configure(
                sampling_rate=args.sample_rate,
                max_samples=args.max_samples
            )

            print(f"Enabling function call tracking with sampling rate: {args.sample_rate}")
            # patch_module.enable_tracking()
            # patch_module.enable_dsl_tracking()
            # patch_module.enable_solvers_tracking()
            # patch_module.enable_all_tracking()
        except ImportError:
            print("Warning: Could not import tracking modules. Function tracking will be disabled.")
            args.track = False

    # Load data
    # data = get_data(train=True)
    train_data = get_data(train=True)
    eval_data = get_data(train=False)
    total_data = {k: {**train_data[k], **eval_data[k]} for k in train_data.keys()}

    # Filter data if a specific task_id was provided
    if args.task_id:
        if args.task_id in total_data['train']:
            total_data = {
                'train': {args.task_id: total_data['train'][args.task_id]},
                'test': {args.task_id: total_data['test'][args.task_id]}
            }
        else:
            print(f"Task '{args.task_id}' not found in training data.")
            return

    if args.check_dsl:
        run_dsl_tests(dsl, tests, args.quiet)
    if args.check_format:
        check_solvers_formatting(solvers_module, dsl, args.quiet)
    n_correct, avg_time, n_tasks = check_solvers_correctness(total_data, solvers_module, args.task_id, args.quiet, args.timeout, args.wait)

    # Final summary
    print(f"Summary: {n_correct}/{n_tasks} tasks solved correctly with average execution time {avg_time:.4f}s")

    # Export statistics if tracking was enabled
    if args.track:
        from stats import export_stats, print_stats
        try:
            # Print summary of most called functions
            if not args.quiet:
                print("\nFunction Statistics Summary:")
                print_stats()

            # Export statistics to a file
            export_stats(args.stats_output)
            print(f"Function call statistics exported to {args.stats_output}")

            # Disable tracking
            patch_module.disable_tracking()
        except Exception as e:
            print(f"Error exporting statistics: {e}")


if __name__ == '__main__':
    main()
