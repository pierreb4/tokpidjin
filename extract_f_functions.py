#!/usr/bin/env python3
"""
Extract all _f suffixed functions from old dsl.py and output them
"""

def extract_function(lines, start_idx, func_name):
    """Extract a function starting at start_idx until next top-level definition"""
    func_lines = [lines[start_idx]]
    j = start_idx + 1
    
    # Continue collecting lines while indented or empty
    while j < len(lines):
        line = lines[j]
        if line.strip() == '':
            func_lines.append(line)
        elif line[0].isspace():
            func_lines.append(line)
        else:
            # Hit next top-level statement
            break
        j += 1
    
    return ''.join(func_lines).rstrip() + '\n\n'

# Read old dsl.py
with open('/tmp/old_dsl.py', 'r') as f:
    lines = f.readlines()

# Key functions we need
needed_funcs = {
    'p_f': None,
    'get_nth_f': None, 
    'get_nth_by_key_f': None,
    'mir_rot_f': None,
    'palette_f': None,
    'get_color_rank_f': None,
    'get_arg_rank_f': None,
    'get_val_rank_f': None,
    'get_common_rank_f': None,
    'merge_f': None,
    'combine_f': None,
    'size_f': None,
    'valmax_f': None,
    'valmin_f': None,
    'argmax_f': None,
    'argmin_f': None,
    'mostcommon_f': None,
    'leastcommon_f': None,
    'sfilter_f': None,
    'mfilter_f': None,
    'apply_f': None,
    'rapply_f': None,
    'mapply_f': None,
    'first_f': None,
    'last_f': None,
    'colorcount_f': None,
    'numcolors_f': None,
    'mostcolor_f': None,
    'leastcolor_f': None,
    'other_f': None,
    'height_f': None,
    'width_f': None,
    'square_f': None,
    'shape_f': None,
    'portrait_f': None,
    'hmirror_f': None,
    'vmirror_f': None,
    'dmirror_f': None,
    'cmirror_f': None,
    'upscale_f': None,
}

# Find each function
for i, line in enumerate(lines):
    for func_name in needed_funcs:
        if needed_funcs[func_name] is None and f'def {func_name}(' in line:
            needed_funcs[func_name] = extract_function(lines, i, func_name)
            print(f"Found {func_name}")

# Report missing
missing = [name for name, body in needed_funcs.items() if body is None]
if missing:
    print(f"\nMissing: {missing}")

# Write output
with open('/Users/pierre/dsl/tokpidjin/_f_functions.txt', 'w') as out:
    for func_name in sorted(needed_funcs.keys()):
        if needed_funcs[func_name]:
            out.write(needed_funcs[func_name])

print(f"\nWrote {len([b for b in needed_funcs.values() if b])} functions to _f_functions.txt")
