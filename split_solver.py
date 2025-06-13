#!/usr/bin/env python3
"""
split_solver.py - Split a solver function into multiple sub-functions

This script takes a solver function with multiple steps and splits it into:
1. A main solver function that stays the same
2. Individual functions for each step of the solver (x1, x2, etc.)

Usage:
    python split_solver.py <solver_file> [--output <output_file>] [--verbose]
    
Arguments:
    solver_file     Path to the solver file to split
    --output        Optional output file (default: adds "_split" suffix to input file)
    --verbose       Print more detailed information during processing
    
Example:
    python split_solver.py solver_evo/solve_b775ac94.py
"""

import re
import os
import sys
import argparse
import ast
from pathlib import Path

def parse_solver_function(file_content):
    """
    Extract solver function details from file content
    
    Args:
        file_content: String content of the solver file
        
    Returns:
        Dictionary with solver info, including all variables
    """
    solver_info = {
        'name': '',
        'code': '',
        'params': '',
        'vars': [],
        'original_code': '',
        'comments': [],
        'timing_comment': None
    }
    
    # Extract comments at the beginning of the file
    comment_lines = []
    for line in file_content.split('\n'):
        if line.strip().startswith('#'):
            comment_lines.append(line)
        elif not line.strip():
            continue
        else:
            break
            
    solver_info['comments'] = comment_lines
    
    # Find the condensed solver function (ending with _one)
    one_pattern = re.compile(r'def\s+(solve_[a-f0-9]+)_one\s*\(([^)]*)\):(.*?)(?=\n\s*\n|\n\s*def|\Z)', 
                          re.MULTILINE | re.DOTALL)
    one_match = one_pattern.search(file_content)
    
    if one_match:
        solver_info['name'] = one_match.group(1)
        solver_info['params'] = one_match.group(2)
        solver_info['original_code'] = one_match.group(0)
        
        # Extract timing comment if it exists
        timing_pattern = re.compile(r'# t - step.*', re.MULTILINE)
        timing_search = file_content[one_match.end():]
        timing_match = timing_pattern.search(timing_search)
        if timing_match:
            solver_info['timing_comment'] = timing_match.group(0)
    
    # Find the expanded solver function
    solver_pattern = re.compile(r'def\s+(solve_[a-f0-9]+)\s*\(([^)]*)\):(?:\s*(?:#[^\n]*)?\n)*(?:\s+[^\n]+\n)+', 
                            re.MULTILINE | re.DOTALL)
    solver_match = solver_pattern.search(file_content)
    
    if solver_match:
        # If we didn't find a _one version, use the regular function name
        if not solver_info['name']:
            solver_info['name'] = solver_match.group(1)
            solver_info['params'] = solver_match.group(2)
            
        solver_info['code'] = solver_match.group(0)
        
        # Extract all variable assignments capturing the exact line (preserving whitespace)
        var_pattern = re.compile(r'^(\s+)(x\d+|O)\s*=\s*(.*?)$', re.MULTILINE)
        variables = []
        
        for var_match in var_pattern.finditer(solver_info['code']):
            var_indent = var_match.group(1)
            var_name = var_match.group(2)
            var_expr = var_match.group(3)
            variables.append((var_name, var_expr, var_indent))
            
        solver_info['vars'] = variables
    
    return solver_info

def create_split_functions(solver_info):
    """
    Create individual functions for each step in the solver
    
    Args:
        solver_info: Dictionary with solver information
        
    Returns:
        List of strings, each containing a generated function
    """
    var_funcs = []
    solver_name = solver_info['name']
    params = solver_info['params']
    
    # Create individual functions for each variable
    for i, (var_name, var_expr, var_indent) in enumerate(solver_info['vars']):            
        # For each step, check what previous variables it uses
        var_deps = []
        for j in range(1, i + 1):
            prev_var = f"x{j}"
            # Check if this variable explicitly appears in the expression
            if re.search(r'\b' + prev_var + r'\b', var_expr):
                var_deps.append(prev_var)
        
        # Create function signature with dependencies
        func_name = f"{solver_name}_{var_name}"
        if var_deps:
            # Add the dependencies as parameters
            dep_params = ", ".join(var_deps)
            func_def = f"def {func_name}({params}, {dep_params}):"
        else:
            func_def = f"def {func_name}({params}):"
            
        # Replace references to other x variables not in dependencies
        modified_expr = var_expr
        for j in range(1, i + 1):
            prev_var = f"x{j}"
            if prev_var not in var_deps and re.search(r'\b' + prev_var + r'\b', modified_expr):
                # Find the expression for this dependency
                dep_expr = None
                for dep_name, dep_expr_val, _ in solver_info['vars']:
                    if dep_name == prev_var:
                        dep_expr = dep_expr_val
                        break
                
                if dep_expr:
                    # Replace the variable with its expression
                    modified_expr = re.sub(r'\b' + prev_var + r'\b', f"({dep_expr})", modified_expr)
            
        # Create the function body - preserving whitespace/indentation
        func_body = [
            func_def,
            f"{var_indent}{var_name} = {modified_expr}",
            f"{var_indent}return {var_name}"
        ]
        var_funcs.append("\n".join(func_body))
    
    return var_funcs

def process_file(input_file, output_file=None, verbose=False, include_condensed=True, include_expanded=True):
    """
    Process a solver file to split it into multiple functions
    
    Args:
        input_file: Path to input solver file
        output_file: Path to output file (default: replace "_xxx" with "_split")
        verbose: Whether to print verbose output
        include_condensed: Whether to include the condensed solver in the output
        include_expanded: Whether to include the expanded solver in the output
        
    Returns:
        Path to the generated output file
    """
    # Default output file replaces "_xxx" with "_split" if present, otherwise adds "_split" suffix
    if not output_file:
        input_path = Path(input_file)
        stem = input_path.stem
        if "_xxx" in stem:
            new_stem = stem.replace("_xxx", "_split")
            output_file = str(input_path.with_stem(new_stem))
        else:
            output_file = str(input_path.with_stem(stem + "_split"))
    
    # Read the file
    with open(input_file, 'r') as f:
        content = f.read()
    
    # Extract solver function
    solver_info = parse_solver_function(content)
    
    if verbose:
        print(f"Found solver: {solver_info['name']}")
        print(f"Number of variables: {len(solver_info['vars'])}")
        if solver_info['original_code']:
            print("Original condensed function found")
            
    if not solver_info['vars']:
        print("Error: Could not find any variable assignments in the solver")
        return None
    
    # Generate functions based on user options
    functions = []
    
    # Add the original condensed function if available and requested
    if include_condensed and solver_info['original_code']:
        functions.append(solver_info['original_code'])
        
        # Add timing comment if found
        if solver_info['timing_comment']:
            functions.append(solver_info['timing_comment'])
    
    # Add the full expanded function if requested
    if include_expanded:
        full_func = solver_info['code']
        # Check if the function is missing a return statement
        if not re.search(r'\s+return\s+O', full_func):
            # Find the last line of the function by looking for the O = assignment
            o_match = re.search(r'(\s+)O\s*=\s*.*$', full_func, re.MULTILINE)
            if o_match:
                indent = o_match.group(1)
                # Add return statement after the last line
                full_func = full_func.rstrip() + f"\n{indent}return O"
        
        functions.append(full_func)
    
    # Create individual functions for each variable
    var_funcs = create_split_functions(solver_info)
    
    # Create output with split functions
    output_content = ""
    if solver_info['comments']:
        output_content += "\n".join(solver_info['comments']) + "\n\n"
    
    # Combine all functions
    all_functions = functions + var_funcs
    output_content += "\n\n".join(all_functions)
    
    # Write the output
    with open(output_file, 'w') as f:
        f.write(output_content)
    
    print(f"Split solver into {len(solver_info['vars'])} functions")
    if not include_condensed:
        print("Condensed solver function excluded from output")
    if not include_expanded:
        print("Expanded solver function excluded from output")
    print(f"Output saved to: {output_file}")
    return output_file

def process_directory(directory, verbose=False, include_condensed=True, include_expanded=True):
    """
    Process all solver files in a directory
    
    Args:
        directory: Path to directory containing solver files
        verbose: Whether to print verbose output
        include_condensed: Whether to include condensed solvers
        include_expanded: Whether to include expanded solvers
        
    Returns:
        Number of successfully processed files
    """
    # Find all Python files in the directory that match the solver pattern with _xxx suffix
    solver_files = []
    for file in os.listdir(directory):
        if file.endswith('.py') and re.match(r'solve_[a-f0-9]+_xxx\.py$', file):
            solver_files.append(os.path.join(directory, file))
    
    if not solver_files:
        print(f"No solver files with _xxx suffix found in {directory}")
        return 0
    
    print(f"Found {len(solver_files)} solver files in {directory}")
    
    # Process each file
    success_count = 0
    for file_path in sorted(solver_files):
        try:
            if verbose:
                print(f"\nProcessing: {file_path}")
            output_file = process_file(file_path, None, verbose, include_condensed, include_expanded)
            if output_file:
                success_count += 1
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            if verbose:
                import traceback
                traceback.print_exc()
    
    print(f"\nSuccessfully processed {success_count} out of {len(solver_files)} files")
    return success_count

def main():
    parser = argparse.ArgumentParser(description='Split a solver function into multiple sub-functions')
    parser.add_argument('solver_file', nargs='?', help='Path to the solver file (optional if --source is used)')
    parser.add_argument('--output', help='Output file path (default: replace "_xxx" with "_split")')
    parser.add_argument('--verbose', '-v', action='store_true', help='Print verbose output')
    parser.add_argument('--no-condensed', action='store_true', 
                        help='Exclude the condensed (one-line) solver function from output')
    parser.add_argument('--no-expanded', action='store_true',
                        help='Exclude the expanded solver function from output')
    parser.add_argument('--source', help='Process all solver files with _xxx suffix in the specified directory')
    
    args = parser.parse_args()
    
    # Check if directory processing is requested
    if args.source:
        if not os.path.isdir(args.source):
            print(f"Error: Directory not found: {args.source}")
            return 1
            
        return 0 if process_directory(
            args.source, 
            args.verbose, 
            include_condensed=not args.no_condensed,
            include_expanded=not args.no_expanded
        ) > 0 else 1
    
    # Otherwise, we need a single file
    if not args.solver_file:
        print("Error: Please specify a solver file or use --dir to process a directory")
        parser.print_help()
        return 1
        
    if not os.path.exists(args.solver_file):
        print(f"Error: File not found: {args.solver_file}")
        return 1
    
    try:
        output_file = process_file(
            args.solver_file, 
            args.output, 
            args.verbose,
            include_condensed=not args.no_condensed,
            include_expanded=not args.no_expanded
        )
        if output_file:
            print(f"Success! Created split solver file: {output_file}")
            return 0
        return 1
    except Exception as e:
        print(f"Error processing file: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())