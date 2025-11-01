#!/usr/bin/env python3
"""
Comprehensive DSL Consolidation Tool
Replaces 34 _t/_f variant pairs with single tuple-based implementations
"""

import re
from pathlib import Path

# Functions to consolidate (base_name, keep_as_f_or_t or None for auto)
CONSOLIDATIONS = {
    'get_nth': 't',  # Keep _t logic (direct indexing)
    'get_nth_by_key': 't',
    'get_arg_rank': 't',
    'get_val_rank': 't',
    'get_common_rank': 't',
    'apply': 't',
    'rapply': 't',
    'mapply': 't',
    'first': 't',  # For frozenset, use tuple logic (iteration)
    'last': 't',
    'remove': 't',
    'other': 't',
    'sfilter': 't',
    'mfilter': 't',  # Note: mfilter_t returns frozenset, need special handling
    'merge': 't',
    'combine': 't',
    'size': 't',
    'valmax': 't',
    'valmin': 't',
    'argmax': 't',
    'argmin': 't',
    'mostcommon': 't',
    'leastcommon': 't',
    'mostcolor': 't',
    'leastcolor': 't',
    'shape': 't',
    'palette': 't',
    'square': 't',
    'hmirror': 't',
    'vmirror': 't',
    'dmirror': 't',
    'cmirror': 't',
    'portrait': 't',
    'colorcount': 't',
}

def extract_function_block(content, func_name, variant):
    """Extract a function definition block including its docstring"""
    # Pattern to match function definition through end of function
    pattern = rf'^(def {func_name}_{variant}\([^)]*\).*?->.*?:\n.*?)(?=\ndef |\Z)'
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    if match:
        return match.group(1)
    return None

def print_consolidation_plan():
    """Print detailed plan before making changes"""
    print("\n" + "="*70)
    print("DSL TYPE CONSOLIDATION PLAN")
    print("="*70)
    print(f"\nConsolidating {len(CONSOLIDATIONS)} function pairs:")
    print("-" * 70)
    
    for i, (base_name, keep_variant) in enumerate(CONSOLIDATIONS.items(), 1):
        print(f"{i:2d}. {base_name:30s} → keep _{keep_variant} variant")
    
    print("\n" + "-" * 70)
    print(f"Total function pairs to consolidate: {len(CONSOLIDATIONS)}")
    print(f"Expected lines removed: ~2000")
    print(f"Functions eliminated: {len(CONSOLIDATIONS)}")
    print("-" * 70)
    print("\nNOTE: This script analyzes the plan but does NOT modify dsl.py yet.")
    print("Next steps: Review plan, then execute manual consolidation or provide approval.")
    print("="*70 + "\n")

if __name__ == '__main__':
    dsl_path = Path('/Users/pierre/dsl/tokpidjin/dsl.py')
    if dsl_path.exists():
        content = dsl_path.read_text()
        print_consolidation_plan()
        
        # Verify all functions exist
        print("\n✓ Verification:")
        for base_name, keep_variant in CONSOLIDATIONS.items():
            t_exists = f'def {base_name}_t(' in content
            f_exists = f'def {base_name}_f(' in content
            
            status = "✓" if (t_exists and f_exists) else "✗"
            print(f"  {status} {base_name:30s} _t:{t_exists:5} _f:{f_exists:5}")
    else:
        print("Error: dsl.py not found")
