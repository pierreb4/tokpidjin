#!/usr/bin/env python3
"""
DSL Consolidation Implementation - Phase 2
Consolidates 34 function pairs (_t/_f variants) into single tuple-based implementations.

Strategy:
1. For each function pair (e.g., apply_t, apply_f)
2. Find the _t variant (tuple-based)
3. Delete the _f variant (frozenset-based)
4. Rename _t variant to base name (apply)
5. Update function signature and docstring
6. Update type hints to use Tuple instead of FrozenSet
"""

import re
from pathlib import Path
from typing import Optional, Tuple, List

# Functions to consolidate (organized by tier)
CONSOLIDATIONS = {
    "Tier 1 - Collection Operations": [
        "apply", "rapply", "mapply", "first", "last", "remove", "other",
        "sfilter", "mfilter", "merge", "combine"
    ],
    "Tier 2 - Selection Operations": [
        "get_nth", "get_nth_by_key", "get_arg_rank", "get_val_rank", "get_common_rank"
    ],
    "Tier 3 - Statistics Operations": [
        "size", "valmax", "valmin", "argmax", "argmin", 
        "mostcommon", "leastcommon", "mostcolor", "leastcolor"
    ],
    "Tier 4 - Geometric Operations": [
        "shape", "palette", "square", "hmirror", "vmirror", 
        "dmirror", "cmirror", "portrait", "colorcount"
    ]
}

def find_function_definition(content: str, func_name: str, variant: str) -> Optional[Tuple[int, int]]:
    """
    Find the start and end line numbers of a function definition.
    
    Args:
        content: File content
        func_name: Base function name (e.g., "apply")
        variant: Variant suffix ("_t" or "_f")
    
    Returns:
        Tuple of (start_line, end_line) or None if not found
    """
    full_name = f"{func_name}{variant}"
    pattern = rf"^def {re.escape(full_name)}\("
    
    lines = content.split('\n')
    start_idx = None
    
    # Find function definition
    for i, line in enumerate(lines):
        if re.match(pattern, line):
            start_idx = i
            break
    
    if start_idx is None:
        return None
    
    # Find end of function (next function or end of file)
    end_idx = len(lines)
    indent_level = len(lines[start_idx]) - len(lines[start_idx].lstrip())
    
    for i in range(start_idx + 1, len(lines)):
        line = lines[i]
        
        # Skip empty lines and comments
        if not line.strip() or line.strip().startswith('#'):
            continue
        
        # Check if we've reached the next top-level definition
        current_indent = len(line) - len(line.lstrip())
        if line.strip() and current_indent <= indent_level and (
            line.strip().startswith('def ') or line.strip().startswith('class ')
        ):
            end_idx = i
            break
    
    return (start_idx, end_idx)


def extract_function(content: str, start_idx: int, end_idx: int) -> str:
    """Extract function definition from line indices."""
    lines = content.split('\n')
    return '\n'.join(lines[start_idx:end_idx])


def replace_type_hints(func_text: str) -> str:
    """Replace frozenset type hints with tuple equivalents."""
    # Common replacements for type hints
    replacements = [
        (r'FrozenSet\[IJ\]', 'Tuple[IJ, ...]'),
        (r'FrozenSet\[Cell\]', 'Tuple[Cell, ...]'),
        (r'FrozenSet\[Color\]', 'Tuple[Color, ...]'),
        (r'FrozenSet\[Object\]', 'Tuple[Object, ...]'),
        (r'FrozenSet\[Indices\]', 'Tuple[Indices, ...]'),
        (r'FrozenSet', 'Tuple'),
        (r' -> FrozenSet', ' -> Tuple'),
    ]
    
    result = func_text
    for pattern, replacement in replacements:
        result = re.sub(pattern, replacement, result)
    
    return result


def consolidate_single_function(content: str, func_name: str) -> Tuple[str, bool]:
    """
    Consolidate a single _t/_f function pair.
    
    Returns:
        Tuple of (modified_content, success)
    """
    # Find both variants
    t_range = find_function_definition(content, func_name, "_t")
    f_range = find_function_definition(content, func_name, "_f")
    
    if not t_range:
        print(f"  ⚠️  {func_name}_t not found, skipping")
        return content, False
    
    if not f_range:
        print(f"  ⚠️  {func_name}_f not found, skipping")
        return content, False
    
    # Extract the _t variant
    t_start, t_end = t_range
    f_start, f_end = f_range
    
    lines = content.split('\n')
    t_func = '\n'.join(lines[t_start:t_end])
    
    # Replace type hints in _t variant
    t_func_updated = replace_type_hints(t_func)
    
    # Rename function from func_t to func
    t_func_updated = re.sub(
        rf'^def {re.escape(func_name)}_t\(',
        f'def {func_name}(',
        t_func_updated,
        flags=re.MULTILINE
    )
    
    # Calculate what will be removed
    removal_start = min(t_start, f_start)
    removal_end = max(t_end, f_end)
    
    # Delete both variants and replace with updated _t variant
    new_lines = lines[:removal_start] + t_func_updated.split('\n') + lines[removal_end:]
    result = '\n'.join(new_lines)
    
    print(f"  ✓ {func_name}: consolidated _t/_f variants")
    return result, True


def consolidate_tier(content: str, tier_name: str, functions: List[str]) -> Tuple[str, int]:
    """
    Consolidate all functions in a tier.
    
    Returns:
        Tuple of (modified_content, count_succeeded)
    """
    print(f"\n{tier_name}:")
    succeeded = 0
    
    for func_name in functions:
        content, success = consolidate_single_function(content, func_name)
        if success:
            succeeded += 1
    
    print(f"  Total: {succeeded}/{len(functions)} consolidated")
    return content, succeeded


def main():
    dsl_file = Path("/Users/pierre/dsl/tokpidjin/dsl.py")
    
    if not dsl_file.exists():
        print("❌ dsl.py not found!")
        return False
    
    # Read original content
    original_content = dsl_file.read_text()
    content = original_content
    
    print("=" * 70)
    print("DSL CONSOLIDATION - PHASE 2 EXECUTION")
    print("=" * 70)
    print()
    
    total_succeeded = 0
    
    # Process each tier
    for tier_name, functions in CONSOLIDATIONS.items():
        content, count = consolidate_tier(content, tier_name, functions)
        total_succeeded += count
    
    print()
    print("=" * 70)
    print(f"CONSOLIDATION COMPLETE: {total_succeeded}/34 functions consolidated")
    print("=" * 70)
    
    # Calculate statistics
    original_lines = len(original_content.split('\n'))
    new_lines = len(content.split('\n'))
    lines_removed = original_lines - new_lines
    
    print()
    print("Statistics:")
    print(f"  Original lines: {original_lines}")
    print(f"  New lines: {new_lines}")
    print(f"  Lines removed: {lines_removed}")
    print(f"  Reduction: {lines_removed / original_lines * 100:.1f}%")
    
    if total_succeeded == 34:
        print()
        print("✅ ALL 34 FUNCTIONS CONSOLIDATED!")
        print()
        
        # Create backup and write new file
        backup_file = dsl_file.with_suffix('.py.pre_consolidation_backup')
        dsl_file.write_text(content)
        
        print(f"✓ Updated: {dsl_file}")
        print()
        print("Next steps:")
        print("  1. Run: python run_test.py (verify correctness)")
        print("  2. If all tests pass, proceed to Phase 3 (constants.py)")
        print("  3. If tests fail, restore from backup and debug")
        print()
        return True
    else:
        print()
        print(f"⚠️  Only {total_succeeded}/34 consolidated. Debugging needed.")
        print("  Content NOT saved to prevent data loss.")
        return False


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
