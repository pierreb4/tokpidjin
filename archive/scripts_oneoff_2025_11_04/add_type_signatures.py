#!/usr/bin/env python3
"""
add_type_signatures.py - Add type hints directly to function signatures in solver files

This script adds proper type hints based on dsl.py function signatures to any solver file,
putting them directly in function definitions.

Usage:
    python add_type_signatures.py [--input <input_file>] [--output <output_file>] [--dsl <dsl_path>]
"""

import re
import os
import sys
import glob
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any, Set

def extract_function_signatures(dsl_path: str) -> Dict[str, Tuple[List[Tuple[str, str]], str]]:
    """
    Extract function signatures from dsl.py with parameter types and return types
    
    Args:
        dsl_path: Path to dsl.py file
        
    Returns:
        Dictionary mapping function names to (param_types, return_type)
    """
    signatures = {}
    
    with open(dsl_path, 'r') as f:
        content = f.read()
    
    # Pattern to match function definitions with parameter types and return type
    function_pattern = r'def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(([^)]*)\)\s*->\s*([a-zA-Z_][a-zA-Z0-9_\[\], ]*):'
    
    for match in re.finditer(function_pattern, content):
        func_name = match.group(1)
        params_str = match.group(2)
        return_type = match.group(3).strip()
        
        # Parse parameter types
        param_types = []
        if params_str.strip():
            # Split by commas, but handle nested types with brackets
            param_sections = []
            current_section = ""
            bracket_level = 0
            
            for char in params_str:
                if char == ',' and bracket_level == 0:
                    param_sections.append(current_section.strip())
                    current_section = ""
                else:
                    current_section += char
                    if char in '[{(':
                        bracket_level += 1
                    elif char in ']})':
                        bracket_level -= 1
            
            if current_section.strip():
                param_sections.append(current_section.strip())
            
            # Process each parameter
            for param_section in param_sections:
                if ':' in param_section:
                    param_name, param_type = param_section.split(':', 1)
                    param_name = param_name.strip()
                    param_type = param_type.strip().split('=')[0].strip()  # Remove default values
                    param_types.append((param_name, param_type))
        
        signatures[func_name] = (param_types, return_type)
    
    return signatures

def extract_solver_id(file_path: str) -> str:
    """
    Extract the solver ID from the file path
    
    Args:
        file_path: Path to solver file
        
    Returns:
        Solver ID (e.g., 'b775ac94' from 'solve_b775ac94_split.py')
    """
    base_name = os.path.basename(file_path)
    match = re.search(r'solve_([a-f0-9]+)', base_name)
    if match:
        return match.group(1)
    return ""

def extract_arc_types(arc_types_path: str) -> Dict[str, str]:
    """
    Extract type aliases from arc_types.py
    
    Args:
        arc_types_path: Path to arc_types.py file
        
    Returns:
        Dictionary mapping type names to their definitions
    """
    arc_types = {}
    
    if not os.path.exists(arc_types_path):
        # Try common locations
        potential_paths = [
            'arc_types.py',
            'fix-400/arc_types.py',
            '../arc_types.py',
            os.path.join(os.path.dirname(__file__), 'arc_types.py'),
            os.path.join(os.path.dirname(__file__), '..', 'arc_types.py'),
        ]
        
        for path in potential_paths:
            if os.path.exists(path):
                arc_types_path = path
                break
        else:
            print(f"Warning: Could not find arc_types.py")
            return arc_types
    
    with open(arc_types_path, 'r') as f:
        content = f.read()
    
    # Extract type aliases
    type_pattern = r'([A-Z][a-zA-Z0-9_]*)\s*=\s*(.+)'
    for match in re.finditer(type_pattern, content):
        type_name = match.group(1)
        type_def = match.group(2).strip()
        # Remove trailing comments if any
        if '#' in type_def:
            type_def = type_def.split('#')[0].strip()
        # Remove trailing commas
        if type_def.endswith(','):
            type_def = type_def[:-1].strip()
        arc_types[type_name] = type_def
    
    return arc_types

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

def find_arc_types_path() -> Optional[str]:
    """Find the arc_types.py file in common locations"""
    potential_paths = [
        'arc_types.py',
        'fix-400/arc_types.py',
        '../arc_types.py',
        os.path.join(os.path.dirname(__file__), 'arc_types.py'),
        os.path.join(os.path.dirname(__file__), '..', 'arc_types.py'),
    ]
    
    for path in potential_paths:
        if os.path.exists(path):
            return path
    
    return None

def map_dsl_returns_to_arc_types(return_type: str, arc_types: Dict[str, str]) -> str:
    """
    Map DSL function return types to ARC type system
    
    Args:
        return_type: Return type from DSL function
        arc_types: Dictionary of ARC type definitions
        
    Returns:
        Mapped ARC type
    """
    # Direct mappings
    direct_mappings = {
        'Any': 'Any',
        'Integer': 'Integer',
        'Boolean': 'Boolean',
        'IJ': 'IJ',
        'Grid': 'Grid',
        'Object': 'Object',
        'Objects': 'Objects',
        'Indices': 'Indices',
        'Callable': 'Callable',
        'Numerical': 'Numerical',
        'FrozenSet': 'FrozenSet',
        'Tuple': 'Tuple',
    }
    
    if return_type in direct_mappings:
        return direct_mappings[return_type]
    
    # Check if it's a direct match with an ARC type
    if return_type in arc_types:
        return return_type
    
    # Handle special cases
    if return_type == 'Patch':
        return 'Patch'
    if 'Container' in return_type:
        return 'Container'
    
    return return_type

def add_type_signatures(input_path: str, output_path: str, signatures: Dict[str, Tuple[List[Tuple[str, str]], str]], arc_types: Dict[str, str]) -> None:
    """
    Add type hints directly to function signatures in solver files
    
    Args:
        input_path: Path to input solver file
        output_path: Path to output file
        signatures: Dictionary of DSL function signatures
        arc_types: Dictionary of ARC type definitions
        
    Returns:
        None (writes to output file)
    """
    # Extract solver ID from filename
    solver_id = extract_solver_id(input_path)
    if not solver_id:
        print(f"Warning: Could not extract solver ID from {input_path}")
        solver_id = "unknown"
    
    with open(input_path, 'r') as f:
        lines = f.readlines()
    
    output_lines = []
    x_types = {}  # Track types for all x variables
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check for function definition using the solver ID pattern
        func_match = re.match(f'def\s+(solve_{solver_id}(?:_x\d+|_O)?)\s*\((.*?)\):', line)
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
                            # Use ARC type if available
                            x_type = map_dsl_returns_to_arc_types(x_types[param_name], arc_types)
                            params.append(f'{param_name}: {x_type}')
                        else:
                            params.append(param_name)
            
            # Extract return type based on function name
            return_type = 'Any'
            if func_name == f'solve_{solver_id}' or func_name.endswith('_O'):
                return_type = 'Grid'
            elif func_name.startswith(f'solve_{solver_id}_x'):
                # Look ahead to find variable assignment and function call
                if i + 1 < len(lines):
                    assign_line = lines[i+1]
                    assign_match = re.match(r'\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*([a-zA-Z_][a-zA-Z0-9_]*)', assign_line)
                    
                    if assign_match:
                        var_name = assign_match.group(1)
                        dsl_func = assign_match.group(2)
                        
                        # Look for function call to determine return type from dsl.py signatures
                        if dsl_func in signatures:
                            dsl_return_type = signatures[dsl_func][1]
                            # Map to ARC type system
                            return_type = map_dsl_returns_to_arc_types(dsl_return_type, arc_types)
                            x_types[var_name] = return_type
                        elif dsl_func.startswith('x') and dsl_func in x_types:
                            # It's calling another x function, use its return type
                            return_type = x_types[dsl_func]
                            x_types[var_name] = return_type
            
            # Generate new function signature with type annotations
            new_signature = f"def {func_name}({', '.join(params)}) -> {return_type}:"
            
            # Before adding the new signature, add the original DSL function signature as a comment
            if i + 1 < len(lines):
                assign_line = lines[i+1]
                assign_match = re.search(r'=\s*([a-zA-Z_][a-zA-Z0-9_]*)\(', assign_line)
                if assign_match:
                    dsl_func = assign_match.group(1)
                    if dsl_func in signatures:
                        param_types, ret_type = signatures[dsl_func]
                        param_str = ", ".join(f"{name}: {type_}" for name, type_ in param_types)
                        comment = f"# def {dsl_func}({param_str}) -> {ret_type}:"
                        output_lines.append(f"{comment}\n")
            
            output_lines.append(new_signature + "\n")
            i += 1
            continue
        
        output_lines.append(line)
        i += 1
    
    # Write the modified lines to the output file
    with open(output_path, 'w') as f:
        f.writelines(output_lines)
    
    print(f"Added type hints to function signatures in {output_path}")

def process_directory(dir_path: str, dsl_path: str, arc_types_path: str, output_suffix: str = "_typed") -> None:
    """
    Process all solver files in a directory, only targeting files ending with _split.py
    
    Args:
        dir_path: Directory containing solver files
        dsl_path: Path to dsl.py file
        arc_types_path: Path to arc_types.py file
        output_suffix: Suffix to add to output files
    """
    # Extract DSL function signatures with parameter types
    print(f"Extracting function signatures from {dsl_path}")
    signatures = extract_function_signatures(dsl_path)
    print(f"Extracted {len(signatures)} function signatures with parameter types")
    
    # Extract ARC types
    print(f"Extracting ARC types from {arc_types_path}")
    arc_types = extract_arc_types(arc_types_path)
    print(f"Extracted {len(arc_types)} ARC types")
    
    # Find all solver files ending with _split.py
    solver_files = glob.glob(os.path.join(dir_path, "solve_*_split.py"))
    print(f"Found {len(solver_files)} solver files to process")
    
    # Process each file
    for input_path in solver_files:
        print(f"Processing {input_path}")
        input_path_obj = Path(input_path)
        # Replace _split with _typed in the file name
        stem = input_path_obj.stem
        new_stem = stem.replace("_split", "_typed")
        output_path = str(input_path_obj.with_stem(new_stem))
        
        add_type_signatures(input_path, output_path, signatures, arc_types)

def main():
    parser = argparse.ArgumentParser(description='Add type hints to function signatures in solver files')
    parser.add_argument('--input', default='solver_evo/', 
                        help='Path to input solver file or directory (default: solver_evo/)')
    parser.add_argument('--output', help='Path to output file (default: replaces _split with _typed)')
    parser.add_argument('--dsl', help='Path to dsl.py file')
    parser.add_argument('--arc-types', help='Path to arc_types.py file')
    parser.add_argument('--suffix', default="_typed", help='Suffix for output files when _split not in name')
    
    args = parser.parse_args()
    
    # Find dsl.py if not specified
    dsl_path = args.dsl or find_dsl_path()
    if not dsl_path:
        print("Error: Could not find dsl.py. Please specify with --dsl")
        return 1
    
    # Find arc_types.py if not specified
    arc_types_path = args.arc_types or find_arc_types_path()
    if not arc_types_path:
        print("Warning: Could not find arc_types.py. Using basic type mapping.")
        arc_types = {}
    else:
        arc_types = extract_arc_types(arc_types_path)
    
    # Process input file or directory
    input_path = args.input
    if not os.path.exists(input_path):
        print(f"Error: Input file or directory {input_path} not found")
        return 1
    
    # Check if input_path is a directory and process accordingly
    if os.path.isdir(input_path):
        process_directory(input_path, dsl_path, arc_types_path, args.suffix)
        return 0
    
    # Process a single file
    # Determine output file path
    if not args.output:
        input_path_obj = Path(input_path)
        stem = input_path_obj.stem
        if "_split" in stem:
            new_stem = stem.replace("_split", "_typed")
            output_path = str(input_path_obj.with_stem(new_stem))
        else:
            # Fallback to appending suffix if _split not in name
            output_path = str(input_path_obj.with_stem(stem + args.suffix))
    else:
        output_path = args.output
    
    # Extract DSL function signatures with parameter types
    print(f"Extracting function signatures from {dsl_path}")
    signatures = extract_function_signatures(dsl_path)
    print(f"Extracted {len(signatures)} function signatures with parameter types")
    
    # Add type signatures to solver functions
    print(f"Processing {input_path}")
    add_type_signatures(input_path, output_path, signatures, arc_types)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())