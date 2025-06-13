#!/usr/bin/env python3
"""
Function Call Replacement Tool

This module provides functionality to replace function calls in Python solver files 
according to predefined transformation patterns. It's designed to convert legacy 
function calls to their canonical forms in DSL-based solver implementations.

The tool supports two types of transformations:
1. Single-argument transformations: Maps old function names to new ones with additional parameters
2. Multi-argument transformations: Maps function calls with specific argument patterns to new forms

Example transformations:
- first(x) -> get_nth_f(x, F0)
- objects(grid, F, T, T) -> o_g(grid, R3)

Usage:
    python replace_func.py --input solvers_ref.py --output solvers.py
    python replace_func.py --quiet  # Suppress output messages

Features:
- Configurable input/output files
- Quiet mode for batch processing
- Support for wildcard argument matching
- Argument substitution with placeholders ($1, $2, etc.)
- Backward compatibility with existing single-argument patterns

Author: DSL Transformation Team
Date: 2025
"""

import re
import argparse
import random

def replace_functions(input_file='solvers_ref.py', output_file='solvers.py', quiet=False):
    """
    Replace function calls according to the transformation dictionary.
    
    Args:
        input_file: Source file to process
        output_file: Destination file for processed code
        quiet: If True, suppress informational output
    """
    # Dictionary mapping function calls to their canonical forms
    # Format: (function_name, arg1, arg2, arg3, ...) -> (target_function, new_args...)
    transformations = {
        # Single argument transformations (existing)
        'first_t': ('get_nth_t', 'F0'),
        'first_f': ('get_nth_f', 'F0'),
        'first':   ('get_nth_f', 'F0'),
        'last_t':  ('get_nth_t', 'L1'),
        'last_f':  ('get_nth_f', 'L1'),
        'last':    ('get_nth_f', 'L1'),

        # mir_rot_t transformations
        'hmirror_t': ('mir_rot_t', 'R0'),
        'dmirror_t': ('mir_rot_t', 'R1'),
        'vmirror_t': ('mir_rot_t', 'R2'),
        'cmirror_t': ('mir_rot_t', 'R3'),
        'rot90':     ('mir_rot_t', 'R4'),
        'rot180':    ('mir_rot_t', 'R5'),
        'rot270':    ('mir_rot_t', 'R6'),

        # mir_rot_f transformations
        'hmirror_f': ('mir_rot_f', 'R0'),
        'dmirror_f': ('mir_rot_f', 'R1'),
        'vmirror_f': ('mir_rot_f', 'R2'),
        'cmirror_f': ('mir_rot_f', 'R3'),

        # get_color_rank transformations
        'mostcolor_t':  ('get_color_rank_t', 'F0'),
        'leastcolor_t': ('get_color_rank_t', 'L1'),
        'mostcolor_f':  ('get_color_rank_f', 'F0'),
        'leastcolor_f': ('get_color_rank_f', 'L1'),

        # get_rank transformations
        'maximum': ('get_rank', 'F0'),
        'minimum': ('get_rank', 'L1'),

        # get_arg_rank transformations
        'argmax_t': ('get_arg_rank_t', 'F0'),
        'argmax_f': ('get_arg_rank_f', 'F0'),
        'argmax':   ('get_arg_rank',   'F0'),
        'argmin_t': ('get_arg_rank_t', 'L1'),
        'argmin_f': ('get_arg_rank_f', 'L1'),
        'argmin':   ('get_arg_rank',   'L1'),

        # get_val_rank transformations
        'valmax_t': ('get_val_rank_t', 'F0'),
        'valmax_f': ('get_val_rank_f', 'F0'),
        'valmax':   ('get_val_rank',   'F0'),
        'valmin_t': ('get_val_rank_t', 'L1'),
        'valmin_f': ('get_val_rank_f', 'L1'),
        'valmin':   ('get_val_rank',   'L1'),

        # get_common_rank transformations
        'mostcommon_t':  ('get_common_rank_t', 'F0'),
        'mostcommon_f':  ('get_common_rank_f', 'F0'),
        'mostcommon':    ('get_common_rank',   'F0'),
        'leastcommon_t': ('get_common_rank_t', 'L1'),
        'leastcommon_f': ('get_common_rank_f', 'L1'),
        'leastcommon':   ('get_common_rank',   'L1'),

        # corner transformations
        'ulcorner': ('corner', 'R0'),
        'urcorner': ('corner', 'R1'),
        'llcorner': ('corner', 'R2'),
        'lrcorner': ('corner', 'R3'),

        # row_col transformations
        'lowermost': ('col_row', 'R0'),
        'uppermost': ('col_row', 'R1'),
        'leftmost':  ('col_row', 'R2'),
        'rightmost': ('col_row', 'R3'), 


        # Multi-argument transformations (new pattern)
        ('objects', '*', 'F', 'F', 'F'): ('o_g', '$1', 'R0'),
        ('objects', '*', 'F', 'F', 'T'): ('o_g', '$1', 'R1'),
        ('objects', '*', 'F', 'T', 'F'): ('o_g', '$1', 'R2'),
        ('objects', '*', 'F', 'T', 'T'): ('o_g', '$1', 'R3'),
        ('objects', '*', 'T', 'F', 'F'): ('o_g', '$1', 'R4'),
        ('objects', '*', 'T', 'F', 'T'): ('o_g', '$1', 'R5'),
        ('objects', '*', 'T', 'T', 'F'): ('o_g', '$1', 'R6'),
        ('objects', '*', 'T', 'T', 'T'): ('o_g', '$1', 'R7'),

        # Add more multi-argument patterns as needed
        # ('function_name', 'pattern_arg1', 'pattern_arg2'): ('target_func', 'new_arg1', 'new_arg2'),
    }

    def replacer_single_arg(match):
        """Handle single-argument function replacements"""
        var_assign = match.group(1)
        func = match.group(2)
        arg = match.group(3)

        if func in transformations:
            target_func, target_param = transformations[func]
            return f"{var_assign}{target_func}({arg}, {target_param})"
        else:
            return match.group(0)  # fallback, should not occur

    def replacer_multi_arg(match):
        """Handle multi-argument function replacements"""
        var_assign = match.group(1)
        func = match.group(2)
        args_str = match.group(3)

        # Parse arguments
        args = [arg.strip() for arg in args_str.split(',')]

        # Try to find a matching pattern in transformations
        for pattern, replacement in transformations.items():
            if isinstance(pattern, tuple) and len(pattern) >= 2:
                pattern_func = pattern[0]
                pattern_args = pattern[1:]

                if func == pattern_func and len(args) == len(pattern_args):
                    # Check if arguments match the pattern
                    match_found = True
                    substituted_args = []

                    for i, (actual_arg, pattern_arg) in enumerate(zip(args, pattern_args)):
                        if pattern_arg in [actual_arg, '*']:  # '*' matches any argument
                            substituted_args.append(actual_arg)
                        else:
                            match_found = False
                            break

                    if match_found:
                        target_func = replacement[0]
                        new_args = replacement[1:]

                        # Substitute placeholders in new_args if needed
                        final_args = []
                        for new_arg in new_args:
                            if new_arg.startswith('$'):  # $1, $2, etc. refer to original arguments
                                arg_index = int(new_arg[1:]) - 1
                                if 0 <= arg_index < len(substituted_args):
                                    final_args.append(substituted_args[arg_index])
                                else:
                                    final_args.append(new_arg)
                            else:
                                final_args.append(new_arg)

                        return f"{var_assign}{target_func}({', '.join(final_args)})"

        return match.group(0)  # No replacement found

    with open(input_file, 'r') as file:
        code = file.read()

    # First, handle single-argument transformations (existing pattern)
    single_arg_functions = [k for k in transformations if isinstance(k, str)]
    if single_arg_functions:
        function_pattern = '|'.join(single_arg_functions)
        single_arg_pattern = f'(\\s*\\w+\\s*=\\s*)({function_pattern})\\(([^)]+)\\)'
        code = re.sub(single_arg_pattern, replacer_single_arg, code)

    # Then, handle multi-argument transformations (new pattern)
    multi_arg_functions = [k[0] for k in transformations if isinstance(k, tuple)]
    if multi_arg_functions:
        # Remove duplicates while preserving order
        unique_functions = list(dict.fromkeys(multi_arg_functions))
        function_pattern = '|'.join(unique_functions)
        multi_arg_pattern = f'(\\s*\\w+\\s*=\\s*)({function_pattern})\\(([^)]+)\\)'
        code = re.sub(multi_arg_pattern, replacer_multi_arg, code)

    # Count total replacements (approximate)
    total_patterns = len(
        [k for k in transformations if isinstance(k, str)]
    ) + len({k[0] for k in transformations if isinstance(k, tuple)})

    with open(output_file, 'w') as file:
        file.write("# Generated by replace_func.py\n")
        file.write(code)

    if not quiet:
        print(f"Processed {input_file} and saved results to {output_file}")
        print(f"Processed {total_patterns} transformation patterns")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert function calls to canonical form")
    parser.add_argument("--input", "-i", default="solvers_ref.py", 
                        help="Source file to process (default: solvers_ref.py)")
    parser.add_argument("--output", "-o", default="solvers.py", 
                        help="Destination file for processed code (default: solvers.py)")
    parser.add_argument("--quiet", "-q", action="store_true",
                        help="Suppress informational output")
    
    args = parser.parse_args()
    replace_functions(args.input, args.output, args.quiet)
