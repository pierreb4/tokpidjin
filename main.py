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
import sys
import json
import inspect
import importlib.util
import tqdm
import argparse
import time

import arc_types
import constants
import dsl
import tests
import solvers_pre

from utils import print_l


def load_module_from_file(file_path):
    """
    Dynamically load a Python module from a file path
    
    Args:
        file_path: Path to the Python file to load
        
    Returns:
        Loaded module object
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Module file not found: {file_path}")
        
    module_name = os.path.basename(file_path).replace('.py', '')
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


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
    expected = set([f'test_{f}' for f in dsl_functions])

    try:
        assert set(test_functions) == expected
    except AssertionError:
        if not quiet:
            print(f'Error: {len(test_functions)} test functions found, expected {len(expected)}')

    for fun in test_functions:
        getattr(test_module, fun)()
    
    if not quiet:
        print(f"All {len(test_functions)} DSL tests passed.")


def test_solvers_formatting(solvers_module, dsl_module, quiet=False):
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
                assert sum([
                    definition.count(vs) for vs in [
                        f'({v})', f'({v}, ', f', {v})',
                        f', {v}, ', f' {v} = ', f' {v}('
                    ]
                ]) > 1 or v == 'O'
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


def test_solvers_correctness(data, solvers_module, quiet=False, timeout_warning=1.0, wait=False):
    """ tests the implemented solvers for correctness """
    functions = get_functions(solvers_module.__file__)
    solver_functions = [f for f in functions if f.startswith('solve_')]
    
    definitions = {
        function: inspect.getsource(getattr(solvers_module, function)) \
            for function in solver_functions
    }
    
    # Count how many tasks have corresponding solvers
    task_keys = data["train"].keys()
    solver_keys = [f.replace('solve_', '') for f in solver_functions]
    solvable_tasks = {k: True for k in task_keys if k in solver_keys}
    
    n_correct = 0
    n = len(solvable_tasks)
    
    # Track execution times
    total_execution_time = 0.0
    total_examples = 0
    slow_solvers = []
    
    if quiet:
        # Without progress bar in quiet mode
        solver_iterator = tqdm.tqdm(solvable_tasks.keys(), total=n)
    else:
        # With progress bar in normal mode
        print(f"Testing {n} tasks for correctness using {os.path.basename(solvers_module.__file__)}...")
        solver_iterator = solvable_tasks.keys()
    
    for key in solver_iterator:
        task = data['train'][key] + data['test'][key]
        num_train = len(data['train'][key])
        
        S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in task)
        try:
            if hasattr(solvers_module, f'solve_{key}'):
                solver = getattr(solvers_module, f'solve_{key}')
            else:
                continue
            
            solver_execution_time = 0.0
            success = True
            
            for i, ex in enumerate(task):
                start_time = time.time()
                result = solver(S, ex['input'])

                # Verify result
                if result != ex['output']:
                    success = False
                    if not quiet:
                        # print(f'{definitions.get(f"solve_{key}")}')
                        print(f"\nError: solve_{key} example {i+1} produced incorrect output")
                        print(f"Expected: {ex['output']}")
                        print(f"Got:      {result}")
                    break
            
                execution_time = time.time() - start_time
                
                # Accumulate statistics
                total_execution_time += execution_time
                total_examples += 1
                solver_execution_time += execution_time
                
                # Check if execution took too long
                if execution_time > timeout_warning:
                    print(f"\nWARNING: solve_{key} example {i+1} took {execution_time:.2f}s")
                    slow_solvers.append((key, i+1, execution_time))
                    
                    # If wait is enabled, pause for user inspection
                    if wait:
                        input("Press Enter to continue...")
                
            if success:
                n_correct += 1
                
        except Exception as e:
            definition = definitions.get(f"solve_{key}", "Solver not found")
            if quiet:
                lines = len(definition.split('\n')) if isinstance(definition, str) else 0
                
                # Add source location information to error message
                import sys, traceback
                exc_type, exc_obj, exc_tb = sys.exc_info()
                frame = traceback.extract_tb(exc_tb)[-1]
                line_info = f" at line {frame.lineno}" if frame else ""
                
                print_l(f"Error in {key}{line_info}: {lines} lines")
            else:
                # Include source location in exception message
                import sys, traceback
                exc_type, exc_obj, exc_tb = sys.exc_info()
                frame = traceback.extract_tb(exc_tb)[-1]
                filename = frame.filename.split('/')[-1] if frame else "unknown"
                lineno = frame.lineno if frame else "unknown"
                
                print_l(f'Exception in {filename}:{lineno}: {e}')
                print_l(f'Error in {key}:\n{definition}')
                if wait:
                    input("Press Enter to continue...")
    
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
            for key, example, time_taken in sorted(slow_solvers, key=lambda x: x[2], reverse=True)[:5]:
                print(f"  - solve_{key} example {example}: {time_taken:.2f}s")
                
    return n_correct, avg_time, n


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test ARC solvers")
    parser.add_argument("-q", "--quiet", help="Suppress verbose output and progress bars",
                        action="store_true")
    parser.add_argument("-k", "--key", help="Test only a specific task key",
                        type=str)
    parser.add_argument("-t", "--timeout", help="Warning threshold in seconds (default: 0.2)",
                        type=float, default=0.2)
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
    parser.add_argument("--solvers", help="Path to alternative solvers module (default: solvers.py)",
                        type=str, default=None)
    args = parser.parse_args()

    # Load the specified solver module or use default
    if args.solvers:
        if not os.path.exists(args.solvers):
            print(f"Error: Solvers module file {args.solvers} not found.")
            return
        try:
            solvers_module = load_module_from_file(args.solvers)
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

    # Filter data if a specific key was provided
    if args.key:
        if args.key in total_data['train']:
            data = {
                'train': {args.key: total_data['train'][args.key]},
                'test': {args.key: total_data['test'][args.key]}
            }
        else:
            print(f"Key '{args.key}' not found in training data.")
            return

    # Run tests with quiet option if specified
    run_dsl_tests(dsl, tests, args.quiet)
    test_solvers_formatting(solvers_module, dsl, args.quiet)
    n_correct, avg_time, n_tasks = test_solvers_correctness(total_data, solvers_module, args.quiet, args.timeout, args.wait)

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
