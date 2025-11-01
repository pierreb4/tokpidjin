#!/usr/bin/env python3
"""
Phase 3: Update HINT_OVERLAPS in constants.py

Current state: 27 types, includes frozenset-based types
Target state: 15 types, consolidate frozenset to tuple equivalents

Changes:
- Removed: IntegerSet, Indices, IndicesSet, Object, Objects (frozenset variants)
- Kept: Indices, Object, Objects (now tuple-based, redefined in arc_types.py)
- Result: Tuple and FrozenSet both removed from HINT_OVERLAPS (using tuple equivalents)

This analysis shows what needs to be updated.
"""

import re
from pathlib import Path

def analyze_hint_overlaps():
    """Analyze current HINT_OVERLAPS."""
    constants_file = Path("/Users/pierre/dsl/tokpidjin/constants.py")
    content = constants_file.read_text()
    
    # Extract HINT_OVERLAPS
    pattern = r"HINT_OVERLAPS = \{(.*?)\n\}"
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        print("❌ Could not find HINT_OVERLAPS in constants.py")
        return
    
    overlaps_text = match.group(1)
    
    # Count types
    type_lines = [line.strip() for line in overlaps_text.split('\n') if line.strip() and not line.strip().startswith('#')]
    print("=" * 70)
    print("HINT_OVERLAPS ANALYSIS")
    print("=" * 70)
    print()
    print(f"Total entries: {len(type_lines)}")
    print()
    
    # Extract type names
    types = set()
    for line in type_lines:
        if "': {" in line:
            type_name = line.split("'")[1]
            types.add(type_name)
    
    print(f"Unique types ({len(types)}):")
    for t in sorted(types):
        print(f"  - {t}")
    
    print()
    print("Consolidation Plan:")
    print("=" * 70)
    print()
    
    frozenset_types = {'FrozenSet', 'IntegerSet', 'Indices', 'IndicesSet', 'Object', 'Objects'}
    tuple_types = {'Tuple', 'Indices', 'Object', 'Objects'}
    
    print("FrozenSet-based types being removed:")
    print("  - IntegerSet (merged into Indices)")
    print("  - IndicesSet (now Tuple[Indices, ...])")
    print()
    
    print("Tuple-based types being kept:")
    print("  - Indices (redefined as Tuple[IJ, ...] in arc_types.py)")
    print("  - Object (redefined as Tuple[Cell, ...] in arc_types.py)")
    print("  - Objects (redefined as Tuple[Object, ...] in arc_types.py)")
    print()
    
    print("Types after consolidation (15 total):")
    remaining_types = types - {'FrozenSet', 'IntegerSet', 'IndicesSet', 'Patch'} | {'Indices', 'Object', 'Objects'}
    for t in sorted(remaining_types):
        print(f"  - {t}")
    
    print()
    print("NEXT: Run consolidate_constants_execute.py to update constants.py")


if __name__ == "__main__":
    analyze_hint_overlaps()
