#!/usr/bin/env python3
"""
add_signatures.py - Add DSL function signatures as comments to split solver functions

This script parses dsl.py to extract function signatures and adds them as
comments to solver_evo/solve_b775ac94_split.py functions.

Usage:
    python add_signatures.py [--input <input_file>] [--output <output_file>] [--dsl <dsl_path>]
    
Arguments:
    --input        Path to the split solver Python file (default: solver_evo/solve_b775ac94_split.py)
    --output       Path to output file (default: adds "_comment" suffix to input file)
    --dsl          Path to dsl.py file (default: tries common locations)
"""

import re
import os
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Optional

def extract_function_signatures(dsl_path: str) -> Dict[str, str]:
    """
    Extract function signatures from dsl.py
    
    Args:
        dsl_path: Path to dsl.py file
        
    Returns:
        Dictionary mapping function names to their signature lines
    """
    signatures = {}
    
    with open(dsl_path, 'r') as f:
        content = f.read()
    
    # Pattern to match function definitions with their signatures
    function_pattern = r'(def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\([^)]*\)\s*->\s*[^:]*:)'
    
    for match in re.finditer(function_pattern, content):
        signature_line = match.group(1)
        function_name = match.group(2)
        
        # Clean up the signature by removing newlines and extra whitespace
        signature_line = re.sub(r'\s+', ' ', signature_line)
        signatures[function_name] = signature_line
    
    return signatures

def add_comments_to_solver(input_path: str, output_path: str, signatures: Dict[str, str]) -> None:
    """
    Add function signature comments to solver functions and parameter type hints
    
    Args:
        input_path: Path to input solver file
        output_path: Path to output file
        signatures: Dictionary of DSL function signatures
        
    Returns:
        None (writes to output file)
    """
    with open(input_path, 'r') as f:
        lines = f.readlines()
    
    output_lines = []
    in_function = False
    current_function = ""
    function_body = []
    
    # Track variable types for all x variables
    x_types = {}
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for function definition
        func_match = re.match(r'def\s+(solve_b775ac94(?:_x\d+|_O)?)\s*\((.*?)\):', line)
        if func_match:
            # Start of a new function
            in_function = True
            current_function = func_match.group(1)
            
            # Extract parameter list
            params = func_match.group(2).strip()
            param_list = [p.strip() for p in params.split(',')]
            
            # Add hints about x parameters
            x_param_comments = []
            for param in param_list:
                if param.startswith('x') and param[1:].isdigit() and param in x_types:
                    x_param_comments.append(f"# {param}: {x_types[param]}")
            
            if x_param_comments:
                output_lines.append("# Parameter types:\n")
                for comment in x_param_comments:
                    output_lines.append(f"{comment}\n")
            
            # Look ahead to find the single assignment line
            if i + 1 < len(lines):
                assign_line = lines[i + 1]
                assign_match = re.match(r'\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([a-zA-Z_][a-zA-Z0-9_]*)\(', assign_line)
                
                if assign_match:
                    var_name = assign_match.group(1)
                    dsl_func = assign_match.group(2)
                    
                    # Add function signature as comment
                    if dsl_func in signatures:
                        output_lines.append(f"# {signatures[dsl_func]}\n")
                        
                        # Try to determine the return type for this x variable
                        sig = signatures[dsl_func]
                        ret_type_match = re.search(r'->\s*([a-zA-Z_][a-zA-Z0-9_]*)', sig)
                        if ret_type_match:
                            ret_type = ret_type_match.group(1)
                            x_types[var_name] = ret_type
                    elif dsl_func.startswith('x') and dsl_func[1:].isdigit():
                        # It's a variable reference
                        if dsl_func in x_types:
                            output_lines.append(f"# Using {dsl_func}: {x_types[dsl_func]}\n")
                    else:
                        # Unknown function
                        output_lines.append(f"# Function: {dsl_func}\n")
            
            output_lines.append(line)
            i += 1
            continue
        
        # If we're looking at a return statement, we're exiting the function
        if in_function and line.strip().startswith('return '):
            in_function = False
        
        output_lines.append(line)
        i += 1
    
    # Write the modified lines to the output file
    with open(output_path, 'w') as f:
        f.writelines(output_lines)
    
    print(f"Added function signature comments and parameter types to {output_path}")

def add_typed_signatures_to_solver(input_path: str, output_path: str, signatures: Dict[str, str]) -> None:
    """
    Add type hints directly to function signatures in solver functions
    
    Args:
        input_path: Path to input solver file
        output_path: Path to output file
        signatures: Dictionary of DSL function signatures
        
    Returns:
        None (writes to output file)
    """
    with open(input_path, 'r') as f:
        lines = f.readlines()
    
    output_lines = []
    x_types = {}  # Track inferred types for all x variables
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for function definition
        func_match = re.match(r'def\s+(solve_b775ac94(?:_x\d+|_O)?)\s*\((.*?)\):', line)
        if func_match:
            func_name = func_match.group(1)
            params_str = func_match.group(2).strip()
            
            # Parse parameters
            params = []
            if params_str:
                param_parts = params_str.split(',')
                for part in param_parts:
                    part = part.strip()
                    if ':' in part:  # Already has type annotation
                        params.append(part)
                    else:
                        param_name = part.strip()
                        if param_name == 'S':
                            params.append('S: Samples')
                        elif param_name == 'I':
                            params.append('I: Grid')
                        elif param_name.startswith('x') and param_name in x_types:
                            params.append(f'{param_name}: {x_types[param_name]}')
                        else:
                            params.append(param_name)
            
            # Extract return type based on function name
            return_type = 'Any'
            if func_name == 'solve_b775ac94':
                return_type = 'Grid'
            elif func_name == 'solve_b775ac94_O':
                return_type = 'Grid'
            elif func_name.startswith('solve_b775ac94_x'):
                # Look ahead to find variable assignment
                var_match = re.match(r'\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=', lines[i+1])
                if var_match:
                    var_name = var_match.group(1)
                    # Look for function call to determine return type
                    func_call_match = re.search(r'=\s*([a-zA-Z_][a-zA-Z0-9_]*)\(', lines[i+1])
                    if func_call_match:
                        dsl_func = func_call_match.group(1)
                        if dsl_func in signatures:
                            # Parse the return type from the signature
                            ret_type_match = re.search(r'->\s*([a-zA-Z_][a-zA-Z0-9_]*)', signatures[dsl_func])
                            if ret_type_match:
                                return_type = ret_type_match.group(1)
                                x_types[var_name] = return_type
                
            # Generate new function signature with type annotations
            new_signature = f"def {func_name}({', '.join(params)}) -> {return_type}:"
            output_lines.append(new_signature + "\n")
            
            # Add the original DSL function signature as a comment above
            if i + 1 < len(lines):
                assign_line = lines[i+1]
                func_call_match = re.search(r'=\s*([a-zA-Z_][a-zA-Z0-9_]*)\(', assign_line)
                if func_call_match:
                    dsl_func = func_call_match.group(1)
                    if dsl_func in signatures:
                        output_lines.insert(-1, f"# {signatures[dsl_func]}\n")
            
            i += 1
            continue
        
        output_lines.append(line)
        i += 1
    
    # Write the modified lines to the output file
    with open(output_path, 'w') as f:
        f.writelines(output_lines)
    
    print(f"Added type hints to function signatures in {output_path}")

def find_dsl_path() -> Optional[str]:
    """Find the dsl.py file in common locations"""
    potential_paths = [
        'dsl.py',
        'fix-400/dsl.py',
        '../dsl.py',
        os.path.join(os.path.dirname(__file__), 'dsl.py'),
        os.path.join(os.path.dirname(__file__), '..', 'dsl.py'),
    ]
    
    for path in potential_paths:
        if os.path.exists(path):
            return path
    
    return None

def main():
    parser = argparse.ArgumentParser(description='Add DSL function signatures to split solver functions')
    parser.add_argument('--input', default='solver_evo/solve_b775ac94_split.py', 
                        help='Path to input solver file')
    parser.add_argument('--output', help='Path to output file (default: adds "_comment" suffix)')
    parser.add_argument('--dsl', help='Path to dsl.py file')
    
    args = parser.parse_args()
    
    # Find dsl.py if not specified
    dsl_path = args.dsl or find_dsl_path()
    if not dsl_path:
        print("Error: Could not find dsl.py. Please specify with --dsl")
        return 1
    
    # Determine output file path
    input_path = args.input
    if not args.output:
        input_path_obj = Path(input_path)
        output_path = str(input_path_obj.with_stem(input_path_obj.stem + "_comment"))
    else:
        output_path = args.output
    
    # Extract DSL function signatures
    print(f"Extracting DSL function signatures from {dsl_path}")
    signatures = extract_function_signatures(dsl_path)
    print(f"Extracted {len(signatures)} function signatures")
    
    # Add comments to solver functions
    print(f"Processing {input_path}")
    add_comments_to_solver(input_path, output_path, signatures)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())