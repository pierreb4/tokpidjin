#!/usr/bin/env python3
"""
Automated DSL Type Consolidation Script
Consolidates _t and _f variants into single tuple-based functions
"""

import re
import sys
from pathlib import Path

def consolidate_dsl():
    """Main consolidation function"""
    dsl_path = Path('/Users/pierre/dsl/tokpidjin/dsl.py')
    content = dsl_path.read_text()
    
    # Functions to consolidate: (base_name, has_both_variants)
    consolidate_functions = [
        'get_nth', 'get_nth_by_key', 'get_arg_rank', 'get_val_rank', 'get_common_rank',
        'apply', 'rapply', 'mapply', 'first', 'last', 'remove', 'other',
        'sfilter', 'mfilter', 'merge', 'combine', 'size',
        'valmax', 'valmin', 'argmax', 'argmin', 'mostcommon', 'leastcommon',
        'mostcolor', 'leastcolor', 'shape', 'palette', 'square',
        'hmirror', 'vmirror', 'dmirror', 'cmirror', 'portrait',
        'colorcount'
    ]
    
    modifications = []
    
    for func_name in consolidate_functions:
        # Find _t variant
        t_variant_pattern = rf'^def {func_name}_t\('
        f_variant_pattern = rf'^def {func_name}_f\('
        
        t_match = re.search(t_variant_pattern, content, re.MULTILINE)
        f_match = re.search(f_variant_pattern, content, re.MULTILINE)
        
        if t_match and f_match:
            print(f"✓ Found both {func_name}_t and {func_name}_f - will consolidate")
            modifications.append((func_name, 'both'))
        elif t_match:
            print(f"✓ Found {func_name}_t (no _f) - will rename")
            modifications.append((func_name, 't_only'))
        elif f_match:
            print(f"⚠ Found {func_name}_f (no _t) - will rename")
            modifications.append((func_name, 'f_only'))
        else:
            print(f"✗ No variants found for {func_name}")
    
    print(f"\nTotal functions to consolidate: {len([m for m in modifications if m[1] == 'both'])}")
    print(f"Total functions to rename: {len([m for m in modifications if m[1] != 'both'])}")
    
    return modifications

if __name__ == '__main__':
    mods = consolidate_dsl()
    print(f"\nPhase 2 consolidation will handle {len(mods)} functions")
