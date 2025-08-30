#!/usr/bin/env python3
"""
expand_solver.py - Expands condensed solver functions into readable versions with intermediate steps

This script takes a solver definition file (.def) containing a one-line return expression 
and generates an expanded version with intermediate variables for better readability
and debugging. It parses the nested function calls in the return statement and creates
a step-by-step implementation.

Usage:
    # Process a single .def file
    python expand_solver.py <def_file> <py_file>
    
    # Process a single file and update solvers_evo.py with the expanded function
    python expand_solver.py <def_file> <py_file> --solvers-file solvers_evo.py
    
    # Process all .def files in solver_evo/ directory (default)
    python expand_solver.py
    
    # Process all .def files in a specific directory
    python expand_solver.py --source solver_pre/
    
    # Process all .def files in a directory and update solvers_evo.py
    python expand_solver.py --source solver_evo/ --solvers-file solvers_evo.py

Arguments:
    def_file          Path to the .def file containing the condensed solver implementation
    py_file           Path to the output .py file where the expanded version will be written
    --source          Path to directory containing .def files to process (default: solver_evo/)
    --solvers-file    Path to solvers file to update with expanded functions

Examples:
    # Expand a specific solver and update solvers_evo.py
    python expand_solver.py solver_evo/solve_5117e062.def solver_evo/solve_5117e062.py --solvers-file solvers_evo.py
    
    # Process all solvers in solver_evo/ and add them to solvers_evo.py
    python expand_solver.py --source solver_evo/ --solvers-file solvers_evo.py

The script will:
1. Parse the function signature and return statement from the .def file
2. Break down the nested function calls using AST (Abstract Syntax Tree)
3. Generate an expanded version with intermediate variables
4. Write both the original and expanded versions to the output file
5. Optionally update the specified solvers file with the expanded function
"""

import argparse
import re
import os
import sys
import ast
import utils
import inspect
import traceback

from pathlib import Path
from timeit import default_timer as timer

from utils import *

# Lightweight module-level profiler wiring
_prof = None
def set_profiler(prof):
    global _prof
    _prof = prof


def parse_function_body(content):
    """
    Parse a function definition and its return statement from the content.
    This handles function definitions across multiple lines.
    
    Args:
        content: The entire file content as a string
    
    Returns:
        tuple: (func_name, func_params, expanded_steps) if found, None otherwise
    """
    # Find the function definition line
    # func_match = re.search(r'def\s+(solve_[a-f0-9]+)\s*\(([^)]*)\)\s*:', content)
    # func_match = re.search(r'def\s+(solve_[a-f0-9]+(?:_[a-f0-9]+)?)\s*\(([^)]*)\)\s*:', content)

    func_match = re.search(r'def\s+(solve|differ)\s*\(([^)]*)\)\s*:', content)

    if not func_match:
        func_match = re.search(r'def\s+(solve_[a-f0-9]+)\s*\(([^)]*)\)\s*:', content)

    if not func_match:
        print_l("Failed to match function definition in content")
        return None

    func_name = func_match[1]

    # print_l(f"Function name: {func_name}")
    print('.', end='')

    func_params = func_match[2]

    # Find the return statement, which might be on a different line
    return_match = re.search(r'return\s+(.*?)$', content, re.MULTILINE)
    if not return_match:
        print_l("Failed to find return statement in content")
        return None

    return_expr = return_match[1]

    # Parse the expression using AST
    try:
        t0 = timer()
        tree = ast.parse(return_expr)
        parse_dt = timer() - t0

        t1 = timer()
        steps, _ = expand_expression(tree.body[0].value)
        expand_dt = timer() - t1

        if _prof is not None:
            _prof['expand_solver.parse_function_body.parse'] += parse_dt
            _prof['expand_solver.parse_function_body.expand'] += expand_dt
        return func_name, func_params, steps
    except SyntaxError as e:
        print_l(f"Error parsing expression: {return_expr}")
        print_l(f"Syntax error: {e}")
        return None
    except Exception as e:
        print_l(f"Unexpected error: {e}")
        print_l(f"- traceback: {traceback.format_exc()}")
        return None

def expand_expression(node, depth=1, parent_expr=None, var_map=None, next_var_id=None):
    """
    Recursively expand an AST expression into a series of assignments
    using intermediate variables
    
    Args:
        node: The AST node to expand
        depth: Current depth in the expression tree
        parent_expr: Parent expression node
        var_map: Dictionary mapping expressions to variable names for deduplication
        next_var_id: Counter for generating unique variable names
        
    Returns:
        tuple: (steps, next_var_id) where steps is a list of (variable_name, code_line) tuples
    """
    if var_map is None:
        var_map = {}

    if next_var_id is None:
        next_var_id = 1

    # Check if this exact expression has been seen before
    node_str = ast.unparse(node)
    if node_str in var_map:
        # Return the existing variable without generating a new step
        return [(var_map[node_str], "")], next_var_id

    # Special case for function applications: f(args)(more_args)
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Call):
        # First expand the inner function call
        inner_steps, current_var_id = expand_expression(node.func, depth, None, var_map, next_var_id)
        inner_var = inner_steps[-1][0]

        # Then handle the outer call with the inner result as the function
        steps = inner_steps
        args = []

        for arg in node.args:
            arg_result, current_var_id = expand_expression(arg, current_var_id, node, var_map, current_var_id)

            if isinstance(arg_result, list):  # Nested function calls
                if arg_result := [s for s in arg_result if s[1]]:
                    steps.extend(arg_result)
                    var_name = arg_result[-1][0]
                else:
                    node_arg_str = ast.unparse(arg)
                    if node_arg_str in var_map:
                        var_name = var_map[node_arg_str]
                    else:
                        var_name = f"x{current_var_id}"
                        var_map[node_arg_str] = var_name
                        current_var_id += 1

                args.append(var_name)
            else:  # Simple argument
                args.append(arg_result)

        # Create the function application step
        args_str = ", ".join(str(arg) for arg in args)

        # Never use "O" for intermediate variables, only for the final result
        variable = f"x{current_var_id}"
        current_var_id += 1

        # Add this function application step
        var_map[node_str] = variable
        step = (variable, f"{variable} = {inner_var}({args_str})")
        steps.append(step)

        return steps, current_var_id

    elif isinstance(node, ast.Call):
        # Check if the exact same function call is already in var_map
        if node_str in var_map:
            return [(var_map[node_str], "")], next_var_id

        # Process function arguments first
        steps = []
        args = []
        current_var_id = next_var_id

        for arg in node.args:
            arg_result, current_var_id = expand_expression(arg, current_var_id, node, var_map, current_var_id)

            if isinstance(arg_result, list):  # Nested function calls
                if arg_result := [s for s in arg_result if s[1]]:
                    steps.extend(arg_result)
                    var_name = arg_result[-1][0]
                else:
                    node_arg_str = ast.unparse(arg)
                    if node_arg_str in var_map:
                        var_name = var_map[node_arg_str]
                    else:
                        var_name = f"x{current_var_id}"
                        var_map[node_arg_str] = var_name
                        current_var_id += 1

                args.append(var_name)
            else:  # Simple argument
                args.append(arg_result)

        # Create this function call
        func_name = ast.unparse(node.func).strip()
        args_str = ", ".join(str(arg) for arg in args)

        # Assign a new variable name, never use "O" for intermediate variables
        variable = f"x{current_var_id}"
        current_var_id += 1

        # Store this expression in the variable map
        var_map[node_str] = variable

        # Add this function call as a step
        step = (variable, f"{variable} = {func_name}({args_str})")
        steps.append(step)

        return steps, current_var_id

    elif isinstance(node, ast.Attribute):
        # Handle attribute access
        return ast.unparse(node), next_var_id

    elif isinstance(node, ast.Name):
        # Handle variable names
        return node.id, next_var_id

    elif isinstance(node, ast.Constant):
        # Handle constants
        return node.value, next_var_id

    else:
        # Handle other types by converting back to source
        return ast.unparse(node), next_var_id

def generate_expanded_function(func_name, func_params, steps):
    """
    Generate the expanded version of the function with intermediate steps
    
    Args:
        func_name: Name of the function (will be used as is, not appending _expanded)
        func_params: Function parameters
        steps: List of steps, each step is a tuple (variable_name, code_line)
        
    Returns:
        String containing the expanded function code
    """
    # Start with function definition
    # lines = [f"def {func_name}({func_params}):"]
    # Adding arg x for introspection
    # lines = [f"def {func_name}(S, I, x=0):"]
    t0 = timer()
    lines = [f"def {func_name}(S, I):"]
    
    # Filter out empty steps and ensure unique lines
    unique_steps = []
    seen_lines = set()
    
    # Process all steps except the last one
    for step in steps[:-1]:
        if isinstance(step, tuple) and len(step) == 2:
            var_name, code_line = step
            if code_line and code_line not in seen_lines:
                unique_steps.append((var_name, code_line))
                seen_lines.add(code_line)
    
    # Add the last step if it exists
    last_step = None
    if steps and isinstance(steps[-1], tuple) and len(steps[-1]) == 2:
        var_name, code_line = steps[-1]
        if code_line and code_line not in seen_lines:
            last_step = (var_name, code_line)
    
    # Renumber all variables to ensure sequential numbering
    var_mapping = {}
    next_var_num = 1
    
    processed_lines = []
    for i, (var_name, code_line) in enumerate(unique_steps):
        # Map old variable name to new sequentially numbered variable
        if var_name not in var_mapping:
            var_mapping[var_name] = f"x{next_var_num}"
            next_var_num += 1
        
        # Replace all variable occurrences in the line
        new_line = code_line
        new_test = ''
        new_retx = ''
        for old_var, new_var in var_mapping.items():
            # Replace only whole variable names (not substrings)
            new_line = re.sub(r'\b' + re.escape(old_var) + r'\b', new_var, new_line)
            # new_line = re.sub(rf'(?<![\w.])' + re.escape(old_var) + rf'(?<![\w.])', new_var, new_line)
            # Return the variable if arg matches
            new_test = f"if x == {next_var_num - 1}:"
            new_retx = f"    return {new_var}" 
        
        processed_lines.append(f"    {new_line}")
        # processed_lines.append(f"    {new_test}")
        # processed_lines.append(f"    {new_retx}")

    # Add all processed lines
    lines.extend(processed_lines)
    
    # Process the last step separately and rename its variable to 'O'
    if last_step:
        var_name, code_line = last_step
        
        # Apply variable mappings to the code
        new_line = code_line
        for old_var, new_var in var_mapping.items():
            new_line = re.sub(r'\b' + re.escape(old_var) + r'\b', new_var, new_line)
            # new_line = re.sub(rf'(?<![\w.])' + re.escape(old_var) + rf'(?<![\w.])', new_var, new_line)
        
        # Replace the final variable name with 'O'
        if var_name in var_mapping:
            new_line = new_line.replace(f"{var_mapping[var_name]} =", "O =")
        else:
            new_line = new_line.replace(f"{var_name} =", "O =")
        
        lines.append(f"    {new_line}")
    
    # Add the return statement with 'O'
    lines.append("    return O")
    
    code = "\n".join(lines)
    if _prof is not None:
        _prof['expand_solver.generate_expanded_function'] += timer() - t0
    return code

def expand_file(def_file, py_file, update_solvers_file=None, quiet=False):
    """
    Process the .def file and generate the .py file with expanded version.
    Renames the original function with _one suffix and gives the original name to the expanded version.
    
    Args:
        def_file: Path to .def file containing condensed implementation
        py_file: Path to output .py file for expanded version
        update_solvers_file: Optional path to solvers_evo.py file to update with the expanded function
        quiet: If True, suppress informational output
        
    Returns:
        bool: True if processing was successful, False otherwise
    """
    try:
        t_io0 = timer()
        with open(def_file, 'r') as f:
            content = f.read()
        io_read_dt = timer() - t_io0

        if func_parsed := parse_function_body(content):
            # _, func_params, steps = func_parsed
            func_name, func_params, steps = func_parsed
            
            # Get function name from def_file
            # def_stem_split = Path(def_file).stem.split('_')
            # func_name = f'solve_{def_stem_split[0]}'

            # func_name = 'solve'

            # Create the original function with _one suffix
            # original_renamed = content.replace(f"def {func_name}", f"def {func_name}_one")
            
            # Generate expanded function with the original function name
            t_gen0 = timer()
            expanded_func = generate_expanded_function(func_name, func_params, steps)
            gen_dt = timer() - t_gen0
            
            header = "from dsl import *\nfrom constants import *\n\n"
            output = header + expanded_func + "\n"


            t_io1 = timer()
            with open(py_file, 'w') as out_f:
                out_f.write(output)
            io_write_dt = timer() - t_io1
            
            if not quiet:
                print_l(f"Successfully generated {py_file} with expanded version")
                # print_l(f"Original function renamed to {func_name}_one")
                print_l(f"Expanded function uses name {func_name}")
            
            # Update solvers_*.py if specified
            if update_solvers_file:
                t_upd0 = timer()
                update_solvers(update_solvers_file, def_file, func_name, expanded_func, quiet)
                upd_dt = timer() - t_upd0
            else:
                upd_dt = 0.0
            if _prof is not None:
                _prof['expand_solver.expand_file.read'] += io_read_dt
                _prof['expand_solver.expand_file.generate'] += gen_dt
                _prof['expand_solver.expand_file.write'] += io_write_dt
                _prof['expand_solver.expand_file.update_solvers'] += upd_dt
                
            return True
        else:
            # Print the first few lines to help debug
            if not quiet:
                print_l(f"No valid function definition found in {def_file}. File content starts with:")
                with open(def_file, 'r') as f:
                    head = [next(f) for _ in range(5)]
                    for line in head:
                        print_l(f"  > {line.strip()}")
            else:
                print_l(f"Error: No valid function definition in {def_file}")
        
        return False
        
    except Exception as e:
        print_l(f"Error processing file: {e}")
        return False


def process_directory(source_dir, update_solvers_file=None, quiet=False):
    """
    Process all .def files in the given directory and generate .py files.
    
    Args:
        source_dir: Path to the directory containing .def files
        update_solvers_file: Optional path to solvers_evo.py file to update with expanded functions
        quiet: If True, suppress informational output
    
    Returns:
        tuple: (processed_count, success_count)
    """
    if not os.path.exists(source_dir):
        print_l(f"Error: Source directory {source_dir} not found")
        return 0, 0
    
    # Find all .def files in the directory
    def_files = [str(f) for f in Path(source_dir).rglob('*.def')]
    
    if not def_files:
        if not quiet:
            print_l(f"No .def files found in {source_dir}")
        return 0, 0
    
    if not quiet:
        print_l(f"Found {len(def_files)} .def files in {source_dir}")

    processed = 0
    succeeded = 0
    
    # If we're updating a solvers file and overwriting it completely,
    # initialize it with just the imports
    if update_solvers_file:
        with open(update_solvers_file, 'w') as f:
            f.write("from dsl import *\nfrom constants import *\n\n\n")

        if not quiet:
            print_l(f"Initialized {update_solvers_file} with imports (overwriting all contents)")
    
    for def_file in def_files:
        py_file = def_file.replace('.def', '.py')
        
        if not quiet:
            print_l(f"Processing {def_file} -> {py_file}...")

        processed += 1
        
        # Pass the quiet parameter to expand_file
        if expand_file(def_file, py_file, update_solvers_file, quiet):
            succeeded += 1
    
    return processed, succeeded


def update_solvers(solvers_file, def_file, func_name, expanded_func, quiet=False):
    """
    Update the solvers file with the expanded function
    
    Args:
        solvers_file: Path to solvers file
        func_name: Name of the function to add/update
        expanded_func: Expanded function code to add/update
        quiet: If True, suppress informational output
    """
    try:
        # Create file if it doesn't exist
        if not os.path.exists(solvers_file):
            with open(solvers_file, 'w') as f:
                f.write("from dsl import *\nfrom constants import *\n\n\n")
            if not quiet:
                print_l(f"Created new solvers file: {solvers_file}")

        with open(solvers_file, 'r') as f:
            content = f.read()

        # Get function name from .def file name
        # XXX This here might involve some cleanup
        func_name = Path(def_file).stem

        # Check if function already exists
        pattern = re.compile(f'^def {func_name}\s*\(.*?\).*?(?=^def|\Z)', re.MULTILINE | re.DOTALL)

        if match := pattern.search(content):
            # Replace existing function
            # XXX No, we skip
            # new_content = pattern.sub(expanded_func, content)
            if not quiet:
                print_l(f"Skip existing {func_name} in {solvers_file}")
        else:
            # Add new function at the end
            if content.endswith('\n\n'):
                new_content = content + expanded_func
            elif content.endswith('\n'):
                new_content = content + '\n' + expanded_func
            else:
                new_content = content + '\n\n' + expanded_func

            if not expanded_func.endswith('\n\n'):
                new_content += '\n' if expanded_func.endswith('\n') else '\n\n'
            if not quiet:
                print_l(f"Added new {func_name} to {solvers_file}")

        # Write the updated content back
        with open(solvers_file, 'w') as f:
            f.write(new_content)

    except Exception as e:
        print_l(f"Error updating {solvers_file}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Expand condensed solver functions into readable versions with intermediate steps"
    )
    parser.add_argument("def_file", nargs="?", help="Path to the .def file", default=None)
    parser.add_argument("py_file", nargs="?", help="Path to the output .py file", default=None)
    parser.add_argument("--source", help="Process all .def files in directory", default="solver_pre/")
    parser.add_argument("--solvers-file", help="Update solver functions in specified file", default=None)
    parser.add_argument("--quiet", "-q", action="store_true", help="Suppress informational output")
    
    args = parser.parse_args()
    
    if args.def_file and args.py_file:
        # Single file mode
        if not os.path.exists(args.def_file):
            print_l(f"Error: Definition file {args.def_file} not found")
            sys.exit(1)
        
        if expand_file(args.def_file, args.py_file, args.solvers_file, args.quiet):
            if not args.quiet:
                print_l("Success!")
        else:
            print_l("Failed to process file")
            sys.exit(1)
    else:
        # Directory mode
        processed, succeeded = process_directory(args.source, args.solvers_file, args.quiet)
        if not args.quiet:
            print_l(f"Processed {processed} files, {succeeded} succeeded")
            
            if processed > 0 and succeeded == processed:
                print_l("All files processed successfully!")
            elif succeeded > 0:
                print_l(f"Partially successful: {succeeded}/{processed} files processed")
        
        if processed == 0 or succeeded == 0:
            print_l("Failed to process any files")
            sys.exit(1)