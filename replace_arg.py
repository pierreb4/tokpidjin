import ast
import sys
import argparse
import os
import random

from utils import *

from inline_solver import inline_variables, parse_split_solver

def load_solver(identifier, input_file="solvers.py"):
    """
    Load a solver function from specified solver file by function name or key.
    
    Args:
        identifier (str): Either a function name like 'solve_f15e1fac' or a key like 'f15e1fac'
        input_file (str): Path to the solver file (default: solvers.py)
    
    Returns:
        str: The source code of the requested solver function
    """
    # If the identifier doesn't start with 'solve_', assume it's a key and prepend 'solve_'
    if not identifier.startswith('solve_'):
        identifier = f'solve_{identifier}('

    # Check if the input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' not found")

    # Read the solvers file
    with open(input_file, 'r') as file:
        content = file.read()

    # Split by function definitions
    function_chunks = content.split('\ndef ')

    # Handle the first function separately since it won't have the same prefix
    first_chunk = function_chunks[0]
    if first_chunk.startswith('def ') and identifier in first_chunk:
        # Extract the function body
        lines = first_chunk.split('\n')
        function_start = next(
            (i for i, line in enumerate(lines) if f'def {identifier}' in line),
            0,
        )
        function_lines = lines[function_start:]

        # Find the end of the function
        for i, line in enumerate(function_lines[1:], 1):
            if line.startswith('    if ') or line.startswith('        return'):
                continue
            if line and not line.startswith(' ') and not line.startswith('\t'):
                function_lines = function_lines[:i]
                break

        return '\n'.join(function_lines)

    # Check the rest of the functions
    for chunk in function_chunks[1:]:
        if chunk.startswith(identifier):
            # Extract function body
            function_text = f'def {chunk}'

            # Get only this function (stop at the next function definition)
            lines = function_text.split('\n')
            function_lines = []
            for line in lines:
                if line.startswith('    if ') or line.startswith('        return'):
                    continue
                if line and not line.startswith(' ') and not line.startswith('\t') and line != lines[0]:
                    break
                function_lines.append(line)

            return '\n'.join(function_lines)

    # If we reach here, the function was not found
    raise ValueError(f"Solver function '{identifier}' not found in {input_file}")


# Define transformations as (original, replacement) tuples
transformations = (
    # first and last transformations
    ('first', 'rbind(get_nth_f, F0)'),
    ('last', 'rbind(get_nth_f, L1)'),

    # mir_rot_t transformations
    ('hmirror_t', 'rbind(mir_rot_t, R0)'),
    ('dmirror_t', 'rbind(mir_rot_t, R1)'),
    ('vmirror_t', 'rbind(mir_rot_t, R2)'),
    ('cmirror_t', 'rbind(mir_rot_t, R3)'),
    ('rot90',     'rbind(mir_rot_t, R4)'),
    ('rot180',    'rbind(mir_rot_t, R5)'),
    ('rot270',    'rbind(mir_rot_t, R6)'),
        
    # mir_rot_f transformations
    ('hmirror_f', 'rbind(mir_rot_f, R0)'),
    ('dmirror_f', 'rbind(mir_rot_f, R1)'),
    ('vmirror_f', 'rbind(mir_rot_f, R2)'),
    ('cmirror_f', 'rbind(mir_rot_f, R3)'),
        
    # get_color_rank transformations
    ('mostcolor_t',  'rbind(get_color_rank_t, F0)'),
    ('leastcolor_t', 'rbind(get_color_rank_t, L1)'),
    ('mostcolor_f',  'rbind(get_color_rank_f, F0)'),
    ('leastcolor_f', 'rbind(get_color_rank_f, L1)'),

    # get_rank transformations
    ('maximum', 'rbind(get_rank, F0)'),
    ('minimum', 'rbind(get_rank, L1)'),

    # get_arg_rank transformations
    ('argmax_t', 'rbind(get_arg_rank_t, F0)'),
    ('argmax_f', 'rbind(get_arg_rank_f, F0)'),
    ('argmax',   'rbind(get_arg_rank,   F0)'),
    ('argmin_t', 'rbind(get_arg_rank_t, L1)'),
    ('argmin_f', 'rbind(get_arg_rank_f, L1)'),
    ('argmin',   'rbind(get_arg_rank,   L1)'),

    # get_val_rank transformations
    ('valmax_t', 'rbind(get_val_rank_t, F0)'),
    ('valmax_f', 'rbind(get_val_rank_f, F0)'),
    ('valmax',   'rbind(get_val_rank,   F0)'),
    ('valmin_t', 'rbind(get_val_rank_t, L1)'),
    ('valmin_f', 'rbind(get_val_rank_f, L1)'),
    ('valmin',   'rbind(get_val_rank,   L1)'),

    # get_common_rank transformations
    ('mostcommon_t',  'rbind(get_common_rank_t, F0)'),
    ('mostcommon_f',  'rbind(get_common_rank_f, F0)'),
    ('mostcommon',    'rbind(get_common_rank,   F0)'),
    ('leastcommon_t', 'rbind(get_common_rank_t, L1)'),
    ('leastcommon_f', 'rbind(get_common_rank_f, L1)'),
    ('leastcommon',   'rbind(get_common_rank,   L1)'),

    # corner transformations
    ('ulcorner', 'rbind(corner, R0)'),
    ('urcorner', 'rbind(corner, R1)'),
    ('llcorner', 'rbind(corner, R2)'),
    ('lrcorner', 'rbind(corner, R3)'),

    # row_col transformations
    ('lowermost', 'rbind(col_row, R0)'),
    ('uppermost', 'rbind(col_row, R1)'),
    ('leftmost',  'rbind(col_row, R2)'),
    ('rightmost', 'rbind(col_row, R3)'),
)


class ReplaceConstantTransformer(ast.NodeTransformer):
    """AST transformer to replace specific constants with function calls"""
    
    def __init__(self, transformations):
        self.transformations = transformations
    
    def visit_Name(self, node):
        # Check if this node's id matches any transformation target
        for orig, repl in self.transformations:
            if isinstance(node, ast.Name) and node.id == orig:
                # Parse the replacement expression and use it instead
                new_node = ast.parse(repl, mode="eval").body
                return ast.copy_location(new_node, node)
        return node


def transform_code(code_str):
    """Transform code by replacing constants with function calls"""
    tree = ast.parse(code_str)
    transformer = ReplaceConstantTransformer(transformations)
    transformed_tree = transformer.visit(tree)
    ast.fix_missing_locations(transformed_tree)
    return ast.unparse(transformed_tree)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transform solver functions by replacing constants with function calls")
    parser.add_argument("key", nargs="?", default="1f876c06",
                        help="Solver key or function name (default: 1f876c06)")
    parser.add_argument("--input", "-i", default="solvers.py",
                        help="Input solvers file to process (default: solvers.py)")
    parser.add_argument("--output-dir", "-o", default="solver_pre",
                        help="Output directory for transformed solvers (default: solver_pre)")
    parser.add_argument("--quiet", "-q", action="store_true",
                        help="Suppress informational output")
    
    args = parser.parse_args()
    
    try:
        # Create output directory if it doesn't exist
        os.makedirs(args.output_dir, exist_ok=True)
        
        # Load the solver code
        solver_code = load_solver(args.key, args.input)
        if not args.quiet:
            print(f"Loaded solver '{args.key}' from {args.input}")
        
        # Transform the code
        transformed_code = transform_code(solver_code)
        
        # print_l(f'{transformed_code = }')

        # Parse and inline the variables
        var_defs = parse_split_solver(transformed_code)
        inline_solver = inline_variables(args.key, var_defs)
        
        # Save the transformed code to a new file
        output_path = args.key.replace('_', '/')
        output_file = os.path.join(args.output_dir, f'{output_path}.def')
        with open(output_file, 'w') as f:
            f.write(inline_solver + '\n')
        
        if not args.quiet:
            print(f"Transformed code saved to '{output_file}'")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)