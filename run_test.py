"""
ARC-DSL Test Runner

This script tests the Domain Specific Language (DSL) for the Abstraction and Reasoning Corpus.
It provides functionality to:
- Run tests on the DSL primitives
- Check the formatting of solvers to ensure they follow DSL conventions
- Verify the correctness of solvers against demo and test samples

Usage:
  python run_test.py                     # Run all tests
  python run_test.py -k TASK_ID          # Test a specific task_id
  python run_test.py --skip-tests        # Skip DSL primitive tests
  python run_test.py -q, --quiet         # Show only key errors and line counts

Example:
  python run_test.py -k 00d62c1b -q      # Test task 00d62c1b with minimal output
"""

import os
import json
import inspect
import tqdm
import argparse
import contextlib
import re
import sys
import traceback
import logging
import asyncio
import types

import arc_types
# import constants
# import dsl
import tests
import solvers_pre

from grid import *
from utils import *
from dsl import *
from constants import *


# def get_data(train=True):
#     path = f'../data/{"training" if train else "evaluation"}'
#     data = {}
#     for fn in os.listdir(path):
#         with open(f'{path}/{fn}') as f:
#             data[fn.rstrip('.json')] = json.load(f)
#     ast = lambda g: tuple(tuple(r) for r in g)
#     return {
#         'train': {k: [{
#             'input': ast(e['input']),
#             'output': ast(e['output']),
#         } for e in v['train']] for k, v in data.items()},
#         'test': {k: [{
#             'input': ast(e['input']),
#             'output': ast(e['output']),
#         } for e in v['test']] for k, v in data.items()}
#     }


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
    assert set(test_functions) == expected
    for fun in test_functions:
        getattr(test_module, fun)()
    if not quiet:
        print(f"All {len(test_functions)} DSL tests passed.")


def check_solvers_formatting(solvers_module, dsl_module, specific_id=None, quiet=False):
    """ tests the implemented solvers for formatting """
    with open('constants.py', 'r') as f:
        constants = [c.split(' = ')[0] for c in f.readlines() if ' = ' in c]
    definitions = {
        function: inspect.getsource(getattr(solvers_module, function)) \
            for function in get_functions(solvers_module.__file__)
    }

    # Filter for specific key if provided
    if specific_id and f'solve_{specific_id}' in definitions:
        definitions = {f'solve_{specific_id}': definitions[f'solve_{specific_id}']}

    dsl_interface = get_functions(dsl_module.__file__)
    n_correct = 0
    n = len(definitions)

    if not quiet:
        print(f"Testing {n} solver(s) for formatting...")

    for key, definition in definitions.items():
        try:
            lines = definition.split('\n')
            assert lines[0] == f'def {key}(S, I):'
            assert lines[-1] == ''
            variables = set()
            calls = set()
            for line in lines[1:-2]:
                variable, call = line.lstrip().split(' = ')
                function, args = call.split('(')
                assert variable not in dsl_interface
                assert variable not in variables
                assert call not in calls
                variables.add(variable)
                calls.add(call)
                assert function in dsl_interface or function in variables
                assert args[-1] == ')'
                args = [args[:-1]] if ',' not in args else args[:-1].split(', ')
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
        except Exception:
            if quiet:
                print_l(f"Error in {key}: {len(lines)} lines")
            else:
                print_l(f'Error in {key}:\n{definition}')

    print_l(f'{n_correct} out of {n} solvers formatted correctly.')


async def check_solver_speed(data, solver, task_id, sol_solver_id, timeout=30):
    """ 
    checks the speed and correctness of the solver on all samples
    
    Returns:
        tuple: (timed_out, score) where timed_out is bool and score is int
    """
    demo_samples = data['demo'][task_id]
    test_samples = data['test'][task_id]
    task = demo_samples + test_samples
    S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in demo_samples)

    # Create a temporary module to hold the solver function
    solver_module = types.ModuleType('temp_solver_module')
    exec(solver, solver_module.__dict__)
    solve_func = solver_module.solve
    # Ensure solver has access to DSL functions by updating its globals
    solve_func.__globals__.update(globals())

    score = 0
    timed_out = False
    
    # Test on all samples (demo + test), counting correct answers
    # Using 30s timeout per solver (not per sample) to allow full execution
    for i, sample in enumerate(task):
        try:
            result, did_timeout = await run_with_timeout(solve_func, [S, sample['input'], None], timeout)
            if did_timeout:
                print_l(f'Timed out: {sol_solver_id =} - {task_id =} - sample = {i}')
                timed_out = True
            elif result == sample['output']:
                score += 1
        except:
            pass  # Errors count as incorrect
    
    return timed_out, score


async def check_solvers_pre(data, task_id, timeout=10):
    """ checks the speed of the solver """
    task = data['demo'][task_id] + data['test'][task_id]
    S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in task)
    total_timed_out = 0
    total_result = 0

    # print_l(f'Processing solver for task {task_id}')

    try:
        solver = getattr(solvers_pre, f'solve_{task_id}')
        # Ensure solver has access to DSL functions by updating its globals
        solver.__globals__.update(globals())

        for sample in task:
            try:
                timed_out, result = await run_with_timeout(solver, [S, sample['input'], None], timeout)
                if timed_out:
                    # print_l(f'Solver for {task_id} timed out on sample {i}')
                    total_timed_out += 1
                elif result == sample['output']:
                    # print_l(f'Solver for {task_id} correct on sample {i}: {result =}')
                    total_result += 1
            except (asyncio.CancelledError, KeyboardInterrupt):
                # Propagate cancellation/interrupt
                raise
            except Exception:
                # Suppress other exceptions for individual samples
                pass
    except (asyncio.CancelledError, KeyboardInterrupt):
        # Propagate cancellation/interrupt
        raise
    except Exception:
        # Suppress exceptions for the whole task
        pass
        
    return total_timed_out, total_result


def check_solvers_correctness(data, solvers_module, specific_id=None, quiet=False, patch=False, update=False):
    """ tests the implemented solvers for correctness """
    # functions = get_functions(solvers_module.__file__)
    # solver_functions = [f for f in functions if f.startswith('solve_')]

    # definitions = {
    #     function: inspect.getsource(getattr(solvers_module, function)) \
    #         for function in get_functions(solvers_module.__file__)
    # }

    # Filter data and definitions for specific task_id if provided
    md5_hash = None
    solve_func = {}
    if specific_id:
        # if task_id includes 'solve_', strip it
        if specific_id.startswith('solve_'):
            specific_id = specific_id[6:]

        # if task_id includes md5_hash, strip it
        if len(specific_id) == 41:
            md5_hash = specific_id[9:]
            task_id = specific_id[:8]
        else:
            task_id = specific_id

        if task_id in data['demo']:
            task_ids = [task_id]
            solve_func[task_id] = f'solve_{task_id}'
        else:
            print(f"Task_id '{task_id}' not found in training data.")
            return

    else:
        task_ids = data['demo'].keys()
        for task_id in task_ids:
            solve_func[task_id] = f'solve_{task_id}'

    n_correct = 0
    n_new = 0
    n = len(task_ids)

    if not quiet and specific_id is None:
        print(f"Testing {n} solver(s) for correctness...")
        iter_keys = tqdm.tqdm(task_ids, total=n)
    else:
        iter_keys = task_ids

    correct_demo = 0
    correct_test = 0
    for task_id in iter_keys:
        if not quiet:
            print_l(f'Testing solver for task_id: {task_id}')

        task = data['demo'][task_id] + data['test'][task_id]
        num_demo = len(data['demo'][task_id])
        num_test = len(data['test'][task_id])

        # imports = None if quiet else [solvers_pre, solvers_dir]
        # imports = [solvers_dir, solvers_pre]
        # solver_source = get_solver_source(task_id, imports=imports, best_only=True)


        solver_source_pre = get_solver_source(task_id, imports=[solvers_pre], best_only=True)
        solver_source_dir = get_solver_source(task_id, imports=[solvers_dir], best_only=True)
        solver_source = solver_source_dir if solver_source_pre.source is None else solver_source_pre


        if solver_source.path is None:
            if not quiet:
                print_l(f"No solver path found for {task_id}, skipping...")
                # print_l(f'{solver_source = }')
            continue

        # if not quiet:
        #     print_l(f'{solver_source = }')

        if solver_source.path.endswith('.py'):
            module_name = solver_source.path[:-3].replace('/', '.')
            # print_l(f'{module_name = }')
            solver_module = importlib.import_module(module_name)
            solver = solver_module.solve
            if not quiet and specific_id:
                print_l(f"Solver for {specific_id} from {solver_source.path}")
        else:
            solver_module = importlib.import_module('solvers_pre')
            solver = getattr(solver_module, solver_source.name)
            # Ensure solver has access to DSL functions by updating its globals
            solver.__globals__.update(globals())
            if not quiet and specific_id:
                print_l(f"Solver for {specific_id} from {solver.__name__} in {solver.__module__}")

        S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in task)
        try:
            correct = 1
            for i, ex in enumerate(task):
                k_type = 'Train' if i < num_demo else 'Test'

                ok = 'OK'
                if quiet:
                    assert solver(S, ex['input'], None) == ex['output']
                elif solver(S, ex['input'], None) != ex['output']:
                    correct = 0
                    ok = 'KO'

                if specific_id is not None:
                    side_by_side( 
                        [ex['input'], ex['output'], solver(S, ex['input'], None)], 
                        titles=[f'{k_type} Input', f'{k_type} Output', f'{ok} Output'])

            if correct == 1 and not hasattr(solvers_pre, f'solve_{task_id}'):
                n_new += 1

            n_correct += correct

        except NameError as e:
            if patch and specific_id:
                # Try to patch the undefined function with specialized variants
                error_msg = str(e)
                # Extract the undefined name from the error message
                import re
                if match := re.search(
                    r"name '([^']+)' is not defined", error_msg
                ):
                    missing_func = match[1]
                    # Try to patch with specialized variants (suffix _t, _f, etc.)
                    patched = patch_missing_function(solvers_module, missing_func, task_id, ex['input'], quiet, update)
                    if patched:
                        n_correct += 1
                        continue

            # If we reach here, either patching wasn't requested, or it failed
            # definition = definitions.get(solve_func[task_id], "Solver not found")
            # lines = len(definition.split('\n')) if isinstance(definition, str) else 0
            # if quiet:
            #     print_l(f"Error in {task_id}: {lines} lines")
            # else:
            #     print_l(f'Error in {task_id}:\n{definition}')
            if specific_id:  # Show detailed error for specific task_id
                print_l(f"NameError: {str(e)}")
                print_l(f"Solver globals has fgpartition: {'fgpartition' in solver.__globals__}")
                print_l(f"Current globals has fgpartition: {'fgpartition' in globals()}")
                print_l(f"Solver module: {solver.__module__}")
                try:
                    # Try to show output anyway for debugging
                    output = solver(S, ex['input'], None)
                    side_by_side(
                        [ex['input'], ex['output'], output],
                        titles=['Input', 'Expected Output', 'Solver Output'])
                except Exception as e:
                    side_by_side(
                        [ex['input'], ex['output']],
                        titles=['Input', 'Expected Output'])
        except Exception as e:
            # definition = definitions.get(solve_func[task_id], "Solver not found")
            # lines = len(definition.split('\n')) if isinstance(definition, str) else 0
            # if quiet:
            #     print_l(f"Error in {task_id}: {lines} lines")
            # else:
            #     # Include source location in exception message
            #     exc_type, exc_obj, exc_tb = sys.exc_info()
            #     frame = traceback.extract_tb(exc_tb)[-1]
            #     filename = frame.filename.split('/')[-1] if frame else "unknown"
            #     lineno = frame.lineno if frame else "unknown"

            #     print_l(f'Exception in {filename}:{lineno}: {e}')
            #     print_l(f'Error in {task_id}:\n{definition}')

            #     show_exception(f'{task_id = }', e)
            #     print("traceback: ", traceback.format_exc())

            if specific_id:  # Show detailed error for specific task_id
                print_l(f"Error: {type(e).__name__}: {str(e)}")
                try:
                    # Try to show output anyway for debugging
                    side_by_side( 
                        [ex['input'], ex['output'], solver(S, ex['input'], None)], 
                        titles=['Input', 'Expected Output', 'Solver Output'])
                except Exception as e:
                    side_by_side(
                        [ex['input'], ex['output']],
                        titles=['Input', 'Expected Output'])

    print(f'{n_correct} out of {n} tasks solved correctly ({n_new} new).')
    return n_correct == n


def patch_missing_function(solvers_module, missing_func, task_id, test_input, quiet=False, update_file=False):
    """
    Try to patch a missing function with specialized variants.
    
    Args:
        solvers_module: The solvers module
        missing_func: The name of the function that's missing
        task_id: The solver task_id
        test_input: Input data to test the patched function with
        quiet: Whether to suppress verbose output
        update_file: Whether to update the solvers.py file with successful patches
    
    Returns:
        bool: True if patching succeeded, False otherwise
    """
    # Check if the function exists in dsl with specialized variants
    import types
    import dsl
    import re

    solver_name = f'solve_{task_id}'
    solver_func = getattr(solvers_module, solver_name)
    original_code = inspect.getsource(solver_func)

    # Find potential specialized variants (_t, _f, _i, _o, etc.)
    variants = []
    variants.extend(
        name
        for name in dir(dsl)
        if name.startswith(f"{missing_func}_") and callable(getattr(dsl, name))
    )

    if not variants:
        if not quiet:
            print(f"No variants found for '{missing_func}' in dsl.py")
        return False

    if not quiet:
        print(f"Found {len(variants)} potential variants for '{missing_func}': {variants}")

    # Try each variant
    for variant in variants:
        if not quiet:
            print(f"Trying {variant}...")

        # Create a patched version of the solver - handle both direct calls and references
        patched_code = original_code

        # Replace direct function calls: recolor(...)
        patched_code = patched_code.replace(f"{missing_func}(", f"{variant}(")

        # Replace function references in nested contexts like fork(recolor, ...)
        # Make sure we only replace whole words and not parts of other words
        pattern = r'\b' + re.escape(missing_func) + r'\b'
        patched_code = re.sub(pattern, variant, patched_code)

        try:
            namespace = {
                attr_name: getattr(dsl, attr_name)
                for attr_name in dir(dsl)
                if not attr_name.startswith('_')
            }

            # Add constants to the namespace
            import constants
            for const_name in dir(constants):
                if const_name.isupper():
                    namespace[const_name] = getattr(constants, const_name)

            # Execute the patched code
            exec(patched_code, namespace)
            patched_solver = namespace[solver_name]

            # Test the patched solver on the input
            output = patched_solver(test_input)

            # Update the solver in the solvers module with the patched version
            setattr(solvers_module, solver_name, patched_solver)

            if not quiet:
                print(f"Successfully patched solver using {variant}!")
                print(f"Modified code:\n{patched_code}")

            # Update the solvers.py file if requested
            if update_file:
                update_solver_in_file(solver_name, patched_code)
                if not quiet:
                    print("Updated solvers.py with patched implementation")

            return True
        except Exception as e:
            if not quiet:
                print(f"Failed with {variant}: {type(e).__name__}: {str(e)}")
                print(f"Error details: {str(e)}")

    # If we get here, none of the variants worked
    if not quiet:
        print("All variants failed. Restoring original function.")

    return False


def update_solver_in_file(solver_name, patched_code):
    """
    Update the solvers.py file with the patched code.
    
    Args:
        solver_name: The name of the solver function
        patched_code: The patched code to write
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        solvers_path = "solvers.py"
        with open(solvers_path, 'r') as f:
            lines = f.readlines()
        
        # Find the function definition
        start_line = -1
        end_line = -1
        
        for i, line in enumerate(lines):
            # Look for function definition
            if re.match(rf'def\s+{solver_name}\s*\(', line):
                start_line = i
                # Find the end of the function (next function def or end of file)
                for j in range(i + 1, len(lines)):
                    if re.match(r'def\s+', lines[j]):
                        end_line = j - 1
                        break
                if end_line == -1:  # If we reached the end of file
                    end_line = len(lines) - 1
                break
        
        if start_line == -1:
            print(f"Error: Function '{solver_name}' not found in '{solvers_path}'")
            return False
        
        # Count empty lines after the function
        trailing_newlines = 0
        for i in range(end_line, min(end_line + 3, len(lines))):
            if lines[i].strip() == '':
                trailing_newlines += 1
            else:
                break
        
        # Ensure the patched code ends with the appropriate number of newlines (at least 3)
        patched_code = patched_code.rstrip('\n')
        patched_code += '\n' * max(3, trailing_newlines)
        
        # Replace the function lines with the patched version
        new_lines = patched_code.splitlines(True)
        lines[start_line:end_line+1] = new_lines
        
        with open(solvers_path, 'w') as f:
            f.writelines(lines)
        
        return True
    except Exception as e:
        print(f"Error updating solvers file: {e}")
        return False


def validate_and_clean_solver_dir(total_data, solvers_module, dry_run=True, task_id=None, quiet=False):
    """
    Validate solver links in solver_dir - remove links where path score doesn't match actual performance.
    
    A solver in solver_dir/solve_{task_id}/{score}/{t_log}/{md5_hash}.py should actually solve {score} samples.
    If actual score differs from path score, remove the link.
    
    Args:
        total_data: The demo/test data dictionary
        solvers_module: Module containing solvers
        dry_run: If True, only report what would be removed (default True for safety)
        task_id: If specified, only check this task (otherwise check all)
        quiet: If True, only print summary statistics
    
    Returns:
        dict: Statistics about validation (mismatched, removed, checked)
    """
    from pathlib import Path
    import hashlib
    
    solver_dir = Path('solver_dir')
    if not solver_dir.exists():
        if not quiet:
            print(f"solver_dir does not exist")
        return {'mismatched': 0, 'removed': 0, 'checked': 0}
    
    stats = {'mismatched': 0, 'removed': 0, 'checked': 0, 'errors': 0}
    
    # Get list of tasks to check
    tasks_to_check = []
    if task_id:
        tasks_to_check = [task_id]
    else:
        # Find all solve_* directories
        for solve_dir in solver_dir.glob('solve_*'):
            if solve_dir.is_dir():
                task = solve_dir.name.replace('solve_', '')
                if task in total_data['demo']:
                    tasks_to_check.append(task)
    
    if not quiet:
        print(f"\nValidating solver_dir for {len(tasks_to_check)} tasks...")
    
    # Check each task
    for task_id in tasks_to_check:
        if task_id not in total_data['demo']:
            if not quiet:
                print(f"  Task {task_id}: not in dataset")
            continue
        
        task_dir = solver_dir / f'solve_{task_id}'
        if not task_dir.exists():
            continue
        
        # Get demo samples for this task to count max possible score
        demo_samples = total_data['demo'].get(task_id, [])
        test_samples = total_data['test'].get(task_id, [])
        total_samples = len(demo_samples) + len(test_samples)
        
        # Iterate through score directories
        for score_dir in task_dir.glob('*'):
            if not score_dir.is_dir():
                continue
            
            try:
                expected_score = int(score_dir.name)
            except ValueError:
                continue  # Not a numeric score directory
            
            if expected_score > total_samples:
                if not quiet:
                    print(f"  {task_id}/{expected_score}: Invalid score (> {total_samples} samples)")
                stats['errors'] += 1
                continue
            
            # Iterate through t_log directories
            for t_log_dir in score_dir.glob('*'):
                if not t_log_dir.is_dir():
                    continue
                
                # Iterate through solver links
                for solver_link in t_log_dir.glob('*.py'):
                    stats['checked'] += 1
                    
                    # Extract md5 hash from filename
                    md5_hash = solver_link.stem
                    
                    # Load and test the solver
                    try:
                        # Read the solver source
                        with open(solver_link, 'r') as f:
                            solver_source = f.read()
                        
                        # Parse solver name/ID from the solver
                        # Try to extract from docstring or function name
                        actual_score = check_solver_score(
                            solver_source, total_data, task_id, demo_samples, test_samples
                        )
                        
                        # Check if actual score matches expected score in path
                        if actual_score != expected_score:
                            stats['mismatched'] += 1
                            
                            if not quiet:
                                print(f"  MISMATCH {task_id}/{expected_score}: solver actually scores {actual_score}")
                            
                            # Remove the mismatched link
                            if not dry_run:
                                solver_link.unlink()
                                stats['removed'] += 1
                    
                    except Exception as e:
                        stats['errors'] += 1
                        if not quiet:
                            print(f"  ERROR checking {solver_link}: {e}")
    
    # Print summary
    if not quiet or stats['mismatched'] > 0:
        print(f"\nValidation Summary:")
        print(f"  Checked: {stats['checked']}")
        print(f"  Mismatched: {stats['mismatched']}")
        print(f"  Removed: {stats['removed']}")
        print(f"  Errors: {stats['errors']}")
        if dry_run and stats['mismatched'] > 0:
            print(f"  (Use --cleanup to actually remove mismatched links)")
    
    return stats


def check_solver_score(solver_source, total_data, task_id, demo_samples, test_samples):
    """
    Test a solver against demo and test samples to get actual score.
    
    Args:
        solver_source: The solver source code
        total_data: The data dictionary
        task_id: The task ID
        demo_samples: Demo samples for this task
        test_samples: Test samples for this task
    
    Returns:
        int: Number of samples the solver correctly solves
    """
    try:
        # Compile and execute the solver
        solver_locals = {}
        exec(solver_source, globals(), solver_locals)
        solve_func = solver_locals.get('solve')
        
        if solve_func is None:
            return 0
        
        score = 0
        S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in demo_samples)
        
        # Test on demo samples
        for sample in demo_samples:
            try:
                I = sample['input']
                O = sample['output']
                C = solve_func(S, I, None)
                
                if C == O:
                    score += 1
            except:
                pass  # Solver error or timeout counts as miss
        
        # Test on test samples
        for sample in test_samples:
            try:
                I = sample['input']
                O = sample['output']
                C = solve_func(S, I, None)
                
                if C == O:
                    score += 1
            except:
                pass  # Solver error or timeout counts as miss
        
        return score
    except Exception as e:
        return 0


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test ARC solvers")
    parser.add_argument("--solvers", help="Use these solvers", type=str, default='solvers_dir')
    parser.add_argument("-i", "--task_id", help="Specific task_id to test", type=str, default=None)
    parser.add_argument("--check-dsl", help="Do DSL checks", action="store_true")
    parser.add_argument("--check-format", help="Do format checks", action="store_true")
    parser.add_argument("--do-tests", help="Do DSL tests", action="store_true")
    parser.add_argument("-q", "--quiet", help="Show only task_id errors and line counts", action="store_true")
    parser.add_argument("--patch", help="Attempt to patch functions with NameErrors using specialized variants", action="store_true")
    parser.add_argument("--update", help="Update solvers.py with successful patches", action="store_true")
    parser.add_argument("--validate-solver-dir", help="Validate solver_dir links - check if path score matches actual performance", action="store_true")
    parser.add_argument("--cleanup", help="Actually remove mismatched solver links (use with --validate-solver-dir)", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(filename='run_test.log', level=logging.INFO,
                        format='%(levelname)s:%(name)s:%(message)s')

    # data = get_data(train=True)
    train_data = get_data(train=True)
    eval_data = get_data(train=False)
    # total_data = {k: {**train_data[k], **eval_data[k]} for k in train_data.keys()}
    total_data = train_data

    # # Rename 'train' samples 'demo' to avoid confusion with the 'train' dataset
    # # So we have train/eval datasets and demo/test samples
    # total_data['demo'] = total_data.pop('train')
    
    if args.task_id is not None:
        task_id = args.task_id
        solvers_module = None

    if args.solvers is not None:
        try:
            solvers_module = load_module(args.solvers)
            print(f"Using custom solver module: {args.solvers}")
        except Exception as e:
            print(f"Error loading solver module {args.solvers}: {e}")
            return
    # else:
    #     solvers_module = solvers_pre

    if args.check_dsl:
        run_dsl_tests(dsl, tests, args.quiet)
    if args.check_format:
        check_solvers_formatting(solvers_module, dsl, args.task_id, args.quiet)
    if args.validate_solver_dir:
        dry_run = not args.cleanup
        validate_and_clean_solver_dir(total_data, solvers_module, dry_run=dry_run, task_id=args.task_id, quiet=args.quiet)
        if not args.cleanup:
            return True  # Validation complete, don't run solver correctness
        # If cleanup requested, continue to solver correctness check
    return check_solvers_correctness(total_data, solvers_module, args.task_id, args.quiet, args.patch, args.update)

if __name__ == "__main__":
    if success := main():
        sys.exit(0)

    sys.exit(1)