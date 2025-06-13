#!/usr/bin/env python3
"""
inline_solver.py - Transform split solvers into more compact versions

This script processes split solver files, replacing variable references with
their function calls to create a more compact version of the solver.

Usage:
    python inline_solver.py [--input <file_or_dir>] [--output-suffix <suffix>]

Example:
    python inline_solver.py --input solver_evo/solve_d4a91cb9_split.py
"""

import re
import os
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple

def parse_split_solver(file_content: str) -> Dict[str, str]:
    """
    Parse a split or regular solver file to extract variable assignments
    
    Args:
        file_content: Content of the solver file
        
    Returns:
        Dictionary mapping variable names to their function calls
    """
    var_defs = {}

    # First, try to handle the split solver format
    func_pattern = re.compile(r'def\s+solve_[a-f0-9]+_(?:x\d+|O)\s*\(.*?\):(.*?)return', re.DOTALL)
    var_pattern = re.compile(r'\s+((?:x\d+)|O)\s*=\s*(.+?)$', re.MULTILINE)

    for func_match in func_pattern.finditer(file_content):
        func_body = func_match.group(1)
        if var_match := var_pattern.search(func_body):
            var_name = var_match[1]
            var_expr = var_match[2].strip()
            var_defs[var_name] = var_expr

    # If no variables were found using the split format, try the regular format
    if not var_defs:
        # Match a single solver function
        single_func_pattern = re.compile(r'def\s+solve_[a-f0-9]+\s*\(.*?\):(.*?)return', re.DOTALL)
        if single_func_match := single_func_pattern.search(file_content):
            func_body = single_func_match[1]

            # Extract all variable assignments
            assignments = var_pattern.finditer(func_body)
            for assign_match in assignments:
                var_name = assign_match.group(1)
                var_expr = assign_match.group(2).strip()
                var_defs[var_name] = var_expr

    return var_defs

def inline_variables(solver_id: str, var_defs: Dict[str, str]) -> str:
    """
    Create a new solver with inlined variables
    
    Args:
        solver_id: ID of the solver (e.g., 'd4a91cb9')
        var_defs: Dictionary of variable definitions
        
    Returns:
        New solver function with inlined variables
    """
    # Get the O expression which will be the return value
    if 'O' not in var_defs:
        # Check if the last variable might be intended as the output
        if var_defs:
            # Try to use the last assigned variable as 'O'
            var_names = list(var_defs.keys())
            last_var = var_names[-1]
            print(f"Warning: No 'O' variable found in solver. Using '{last_var}' as the output variable.")
            var_defs['O'] = var_defs[last_var]
        else:
            raise ValueError("No 'O' variable found in solver and no alternative output variable available")

    # Build dependency graph
    dependencies = {}
    for var_name, expr in var_defs.items():
        deps = set()
        for other_var in var_defs:
            if other_var != var_name and re.search(r'\b' + other_var + r'\b', expr):
                deps.add(other_var)
        dependencies[var_name] = deps

    # Topologically sort variables for inlining
    processed = set()
    inlined_vars = {}

    def process_var(var_name: str) -> str:
        if var_name in processed:
            return inlined_vars[var_name]

        processed.add(var_name)
        expr = var_defs[var_name]

        # Replace all dependencies with their inlined expressions
        for dep in dependencies[var_name]:
            inlined_dep = process_var(dep) if dep not in processed else inlined_vars[dep]

            # Replace the dependency with its inlined definition
            expr = re.sub(r'\b' + dep + r'\b', inlined_dep, expr)

        inlined_vars[var_name] = expr
        return expr

    # Process 'O' which will pull in all dependencies
    final_expr = process_var('O')

    # Create the new solver function
    return f"def solve_{solver_id}(S, I):\n    return {final_expr}"

def process_file(input_file: str, output_suffix: str = "_two", output_dir: str = None) -> Optional[str]:
    """
    Process a single solver file
    
    Args:
        input_file: Path to input solver file
        output_suffix: Suffix for output file (default: "_two")
        output_dir: Directory for output file (default: "solver_evo" or input file directory)
        
    Returns:
        Path to the output file, or None if processing failed
    """
    # Parse the solver ID from the filename
    file_path = Path(input_file)
    match = re.match(r'solve_([a-f0-9]+)', file_path.stem)
    if not match:
        print(f"Error: File {input_file} does not appear to be a solver file")
        return None

    solver_id = match[1]

    # Use the specified output directory, or solver_evo, or the input file directory
    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(os.path.abspath(input_file)), "solver_evo")
        py_or_def = "py"
    else:
        output_suffix = ''
        py_or_def = "def"

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Create output file path
    output_file = os.path.join(output_dir, f"solve_{solver_id}{output_suffix}.{py_or_def}")

    try:
        return generate_file(input_file, solver_id, output_file)
    except Exception as e:
        print(f"Error processing {input_file}: {e}")
        import traceback
        traceback.print_exc()
        return None


def generate_file(input_file, solver_id, output_file):
    # Read the input file
    with open(input_file, 'r') as f:
        content = f.read()

    # Extract comments at the top of the file
    comment_lines = []
    for line in content.split('\n'):
        if line.strip().startswith('#'):
            comment_lines.append(line)
        elif not line.strip():
            continue
        else:
            break

    # Parse variable definitions
    var_defs = parse_split_solver(content)

    # Generate new solver with inlined variables
    inlined_solver = inline_variables(solver_id, var_defs)

    # Combine comments and new solver
    output_content = '\n'.join(comment_lines) + '\n\n' + inlined_solver + '\n'

    # Write the output
    with open(output_file, 'w') as f:
        f.write(output_content)

    print(f"Created inlined solver: {output_file}")
    return output_file


def process_directory(directory: str, output_suffix: str = "_two", output_dir: str = None) -> int:
    """
    Process all split solver files in a directory
    
    Args:
        directory: Path to directory containing split solver files
        output_suffix: Suffix for output files (default: "_two")
        output_dir: Directory for output files (default: "solver_evo")
        
    Returns:
        Number of successfully processed files
    """
    # Set default output directory to solver_evo if not specified
    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(directory), "solver_evo")

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Find all *_split.py files
    solver_files = []
    solver_files.extend(
        os.path.join(directory, file)
        for file in os.listdir(directory)
        if file.endswith('_split.py') and file.startswith('solve_')
    )
    
    if not solver_files:
        print(f"No split solver files found in {directory}")
        return 0

    print(f"Found {len(solver_files)} split solver files")
    print(f"Output files will be saved to: {output_dir}")

    success_count = sum(bool(process_file(file_path, output_suffix, output_dir))
                    for file_path in sorted(solver_files))

    print(f"Successfully created {success_count} inlined solvers")
    return success_count

def main() -> int:
    parser = argparse.ArgumentParser(description='Transform split solvers into more compact versions')
    parser.add_argument('--input', required=True, 
                        help='Path to split solver file or directory')
    parser.add_argument('--output-suffix', default='_two',
                        help='Suffix for output files (default: _two)')
    parser.add_argument('--output-dir', default=None,
                        help='Directory for output files (default: solver_evo)')
    
    args = parser.parse_args()
    
    # Default to solver_evo if no output directory is specified
    output_dir = args.output_dir or "solver_evo"
    
    if os.path.isdir(args.input):
        return 0 if process_directory(args.input, args.output_suffix, output_dir) > 0 else 1
    elif os.path.isfile(args.input):
        return 0 if process_file(args.input, args.output_suffix, output_dir) else 1
    else:
        print(f"Error: Input path does not exist: {args.input}")
        return 1

if __name__ == "__main__":
    sys.exit(main())