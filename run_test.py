"""
ARC-DSL Test Runner

This script tests the Domain Specific Language (DSL) for the Abstraction and Reasoning Corpus.
It provides functionality to:
- Run tests on the DSL primitives
- Check the formatting of solvers to ensure they follow DSL conventions
- Verify the correctness of solvers against training and test examples

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
import re
import sys
import traceback
import logging

import arc_types
import constants
import dsl
import tests
import solvers_pre

from grid import *
from utils import *


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


def check_solver_speed(data, solver, task_id, timeout=1):
    """ checks the speed of the solver """
    task = data['train'][task_id] + data['test'][task_id]
    S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in task)

    try:
        for i, ex in enumerate(task):
            # assert solver(S, ex['input']) == ex['output']
            timed_out, result = run_with_timeout(solver, [S, ex['input']], timeout)
            if timed_out:
                print_l(f'Solver for {task_id} failed sample {i} (or timed out)')
                return True
            # if result != ex['output']:
            #     print_l(f'Solver for {task_id} failed sample {i} (or timed out)')
    except Exception as e:
        pass

    return False


def check_solvers_correctness(data, solvers_module, specific_id=None, quiet=False, patch=False, update=False):
    """ tests the implemented solvers for correctness """
    # functions = get_functions(solvers_module.__file__)
    # solver_functions = [f for f in functions if f.startswith('solve_')]

    definitions = {
        function: inspect.getsource(getattr(solvers_module, function)) \
            for function in get_functions(solvers_module.__file__)
    }

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

        if task_id in data['train']:
            task_ids = [task_id]
            solve_func[task_id] = f'solve_{task_id}'
        else:
            print(f"Task_id '{task_id}' not found in training data.")
            return

        solver_source = get_solver_source(task_id, imports=[solvers_dir], best_only=True)
        if not solver_source:
            print(f"No solver found for task_id '{task_id}'.")
            return

        solver_module = importlib.import_module(solver_source.'path')
        solver = solver_module.solver if hasattr(solver_module, 'solver') else None
    else:
        task_ids = data['train'].keys()
        for task_id in task_ids:
            solve_func[task_id] = f'solve_{task_id}'

    n_correct = 0
    n = len(task_ids)

    if not quiet and specific_id is None:
        print(f"Testing {n} solver(s) for correctness...")
        iter_keys = tqdm.tqdm(task_ids, total=n)
    else:
        iter_keys = task_ids

    correct_train = 0
    correct_test = 0
    for task_id in iter_keys:
        task = data['train'][task_id] + data['test'][task_id]
        num_train = len(data['train'][task_id])
        num_test = len(data['test'][task_id])

        S = tuple((tuple(sample['input']), tuple(sample['output'])) for sample in task)
        try:
            if solver is not None:
                pass
            elif task_id in solve_func and hasattr(solvers_module, solve_func[task_id]):
                solver = getattr(solvers_module, solve_func[task_id])
            else:
                continue

            correct = 1
            for i, ex in enumerate(task):
                k_type = 'Train' if i < num_train else 'Test'

                ok = 'OK'
                if quiet:
                    assert solver(S, ex['input']) == ex['output']
                elif solver(S, ex['input']) != ex['output']:
                    correct = 0
                    ok = 'KO'

                if specific_id:
                    side_by_side( 
                        [ex['input'], ex['output'], solver(S, ex['input'])], 
                        titles=[f'{k_type} Input', f'{k_type} Output', f'{ok} Output'])

            n_correct += correct

        except NameError as e:
            if patch and specific_id:
                # Try to patch the undefined function with specialized variants
                error_msg = str(e)
                # Extract the undefined name from the error message
                import re
                match = re.search(r"name '([^']+)' is not defined", error_msg)
                if match:
                    missing_func = match[1]
                    # Try to patch with specialized variants (suffix _t, _f, etc.)
                    patched = patch_missing_function(solvers_module, missing_func, task_id, ex['input'], quiet, update)
                    if patched:
                        n_correct += 1
                        continue

            # If we reach here, either patching wasn't requested, or it failed
            definition = definitions.get(solve_func[task_id], "Solver not found")
            lines = len(definition.split('\n')) if isinstance(definition, str) else 0
            if quiet:
                print_l(f"Error in {task_id}: {lines} lines")
            else:
                print_l(f'Error in {task_id}:\n{definition}')
            if specific_id:  # Show detailed error for specific task_id
                print_l(f"NameError: {str(e)}")
                try:
                    # Try to show output anyway for debugging
                    output = solver(ex['input'])
                    side_by_side(
                        [ex['input'], ex['output'], output],
                        titles=['Input', 'Expected Output', 'Solver Output'])
                except Exception as e:
                    side_by_side(
                        [ex['input'], ex['output']],
                        titles=['Input', 'Expected Output'])
        except Exception as e:
            definition = definitions.get(solve_func[task_id], "Solver not found")
            lines = len(definition.split('\n')) if isinstance(definition, str) else 0
            if quiet:
                print_l(f"Error in {task_id}: {lines} lines")
            else:
                # Include source location in exception message
                exc_type, exc_obj, exc_tb = sys.exc_info()
                frame = traceback.extract_tb(exc_tb)[-1]
                filename = frame.filename.split('/')[-1] if frame else "unknown"
                lineno = frame.lineno if frame else "unknown"

                print_l(f'Exception in {filename}:{lineno}: {e}')
                print_l(f'Error in {task_id}:\n{definition}')

                show_exception(f'{task_id = }', e)
                print("traceback: ", traceback.format_exc())

            if specific_id:  # Show detailed error for specific task_id
                print_l(f"Error: {type(e).__name__}: {str(e)}")
                try:
                    # Try to show output anyway for debugging
                    side_by_side( 
                        [ex['input'], ex['output'], solver(ex['input'])], 
                        titles=['Input', 'Expected Output', 'Solver Output'])
                except Exception as e:
                    side_by_side(
                        [ex['input'], ex['output']],
                        titles=['Input', 'Expected Output'])

    print(f'{n_correct} out of {n} tasks solved correctly.')
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
    for name in dir(dsl):
        # Check if this is a variant of the missing function
        if name.startswith(f"{missing_func}_") and callable(getattr(dsl, name)):
            variants.append(name)
    
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
            # Create a namespace for the function
            namespace = {}
            
            # Add all dsl functions to the namespace
            for attr_name in dir(dsl):
                if not attr_name.startswith('_'):  # Skip internal attributes
                    namespace[attr_name] = getattr(dsl, attr_name)
            
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
                    print(f"Updated solvers.py with patched implementation")
            
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


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Test ARC solvers")
    parser.add_argument("--solvers", help="Use this instead of solvers_pre", type=str, default='solvers_pre')
    parser.add_argument("-i", "--task_id", help="Specific task_id to test", type=str)
    parser.add_argument("--check-dsl", help="Do DSL checks", action="store_true")
    parser.add_argument("--check-format", help="Do format checks", action="store_true")
    parser.add_argument("--do-tests", help="Do DSL tests", action="store_true")
    parser.add_argument("-q", "--quiet", help="Show only task_id errors and line counts", action="store_true")
    parser.add_argument("--patch", help="Attempt to patch functions with NameErrors using specialized variants", action="store_true")
    parser.add_argument("--update", help="Update solvers.py with successful patches", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(filename='run_test.log', level=logging.INFO,
                        format='%(levelname)s:%(name)s:%(message)s')

    # data = get_data(train=True)
    train_data = get_data(train=True)
    eval_data = get_data(train=False)
    # total_data = {k: {**train_data[k], **eval_data[k]} for k in train_data.keys()}
    total_data = train_data
    
    task_id = args.task_id

    print_l(f'{args.solvers = }')

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

    if args.check_dsl:
        run_dsl_tests(dsl, tests, args.quiet)
    if args.check_format:
        check_solvers_formatting(solvers_module, dsl, args.task_id, args.quiet)
    return check_solvers_correctness(total_data, solvers_module, args.task_id, args.quiet, args.patch, args.update)

if __name__ == "__main__":
    if success := main():
        sys.exit(0)

    sys.exit(1)