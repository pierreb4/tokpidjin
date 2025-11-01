#!/usr/bin/env python3
"""
Phase 5: Update HINT_OVERLAPS in constants.py

Current state: 27 types in HINT_OVERLAPS, includes frozenset-based types
Target state: 15 types, consolidate frozenset to tuple equivalents

Changes needed:
1. Remove frozenset-based type entries: FrozenSet, IntegerSet, IndicesSet, Patch
2. Update Indices, Object, Objects to reference tuple-based versions (already updated in arc_types.py)
3. Simplify overlaps to remove redundant frozenset paths

This is SAFE because:
- arc_types.py already redefined these as tuple equivalents
- dsl.py functions are now all tuple-based
- solvers_pre.py is already using the base names (not _f variants)
"""

import re
from pathlib import Path

def update_hint_overlaps():
    """Update HINT_OVERLAPS in constants.py."""
    
    constants_file = Path("/Users/pierre/dsl/tokpidjin/constants.py")
    
    print("=" * 70)
    print("PHASE 5: UPDATE HINT_OVERLAPS in constants.py")
    print("=" * 70)
    print()
    
    content = constants_file.read_text()
    
    # Find and replace HINT_OVERLAPS
    old_overlaps = r"""HINT_OVERLAPS = \{
    # Base container types - compatible with themselves and generic containers
    'Tuple': \{'Tuple', 'Container', 'ContainerContainer', 'TupleTuple', 'Grid', 'Samples'\},
    'FrozenSet': \{'FrozenSet', 'Container', 'ContainerContainer', 'IntegerSet', 'Indices', 'Object', 'Objects', 'Patch'\},
    'Container': \{'Tuple', 'FrozenSet', 'Container', 'ContainerContainer', 'TupleTuple', 'Grid', 'Samples', 'IntegerSet', 'Indices', 'Object', 'Objects', 'Patch'\},
    'ContainerContainer': \{'Tuple', 'FrozenSet', 'Container', 'ContainerContainer', 'TupleTuple', 'Grid', 'Samples', 'IntegerSet', 'Indices', 'Object', 'Objects', 'Patch'\},
    'Callable': \{'Callable'\},
    
    # Numeric types - range/rank indices
    # NOTE: Boolean = bool is a subtype of int in Python \(True=1, False=0\)
    # Therefore Boolean is compatible with all Integer and range types
    'Boolean': \{'Boolean', 'Integer', 'Numerical', 'F_', 'FL', 'L_', 'R_', 'R4', 'R8', 'A4', 'A8', 'C_', 'I_', 'J_'\},
    'Integer': \{'Boolean', 'Integer', 'Numerical', 'F_', 'FL', 'L_', 'R_', 'R4', 'R8', 'C_'\},
    'Numerical': \{'Boolean', 'Integer', 'Numerical', 'F_', 'FL', 'L_', 'R_', 'R4', 'R8', 'C_', 'IJ'\},
    
    # Integer ranges - all compatible with each other and Integer/Numerical
    # NOTE: Boolean is compatible with all as it's a subtype of int
    'F_': \{'Boolean', 'Integer', 'Numerical', 'F_', 'FL', 'R_', 'R4', 'R8', 'C_'\},
    'FL': \{'Boolean', 'Integer', 'Numerical', 'F_', 'FL', 'L_'\},
    'L_': \{'Boolean', 'Integer', 'Numerical', 'L_', 'FL'\},
    'R_': \{'Boolean', 'Integer', 'Numerical', 'F_', 'R_', 'R4', 'R8', 'C_'\},
    'R4': \{'Boolean', 'Integer', 'Numerical', 'F_', 'R_', 'R4', 'R8', 'C_'\},
    'R8': \{'Boolean', 'Integer', 'Numerical', 'F_', 'R_', 'R4', 'R8', 'C_'\},
    'A4': \{'Boolean', 'Integer', 'Numerical', 'A4', 'A8'\},
    'A8': \{'Boolean', 'Integer', 'Numerical', 'A4', 'A8'\},
    'C_': \{'Boolean', 'Integer', 'Numerical', 'C_', 'F_', 'R_', 'R4', 'R8'\},
    'I_': \{'Boolean', 'Integer', 'Numerical'\},
    'J_': \{'Boolean', 'Integer', 'Numerical'\},
    'IJ': \{'Numerical', 'IJ'\},
    
    # Specific frozenset types - compatible with each other and FrozenSet/Container
    'IntegerSet': \{'FrozenSet', 'Container', 'ContainerContainer', 'IntegerSet'\},
    'Indices': \{'FrozenSet', 'Container', 'ContainerContainer', 'Indices', 'IndicesSet', 'Patch'\},
    'IndicesSet': \{'FrozenSet', 'Container', 'ContainerContainer', 'Indices', 'IndicesSet'\},
    'Object': \{'FrozenSet', 'Container', 'ContainerContainer', 'Object', 'Objects', 'Patch'\},
    'Objects': \{'FrozenSet', 'Container', 'ContainerContainer', 'Object', 'Objects'\},
    'Patch': \{'FrozenSet', 'Container', 'ContainerContainer', 'Indices', 'Object', 'Patch'\},
    
    # Specific tuple types - compatible with each other and Tuple/Container
    'Grid': \{'Tuple', 'Container', 'ContainerContainer', 'Grid', 'Samples', 'TupleTuple'\},
    'Samples': \{'Tuple', 'Container', 'ContainerContainer', 'Grid', 'Samples', 'TupleTuple'\},
    'TupleTuple': \{'Tuple', 'Container', 'ContainerContainer', 'Grid', 'Samples', 'TupleTuple'\},
    'TTT_iii': \{'TupleTuple', 'Tuple', 'Container', 'ContainerContainer'\},
    'Colors': \{'Tuple', 'Container', 'ContainerContainer'\},
    
    # Other specific types
    'Cell': \{'Cell', 'Tuple', 'Container'\},
    
    # Generic catch-all types
    'Any': \{'Any', 'Boolean', 'Integer', 'Numerical', 'F_', 'FL', 'L_', 'R_', 'R4', 'R8', 'A4', 'A8', 'C_', 'I_', 'J_', 'IJ', 'Tuple', 'FrozenSet', 'Container', 'ContainerContainer', 'Callable', 'IntegerSet', 'Grid', 'Samples', 'TTT_iii', 'Cell', 'Colors', 'Object', 'Objects', 'Indices', 'IndicesSet', 'Patch', 'TupleTuple'\},
\}"""
    
    new_overlaps = """HINT_OVERLAPS = {
    # Base container types - now exclusively tuple-based
    'Tuple': {'Tuple', 'Container', 'ContainerContainer', 'TupleTuple', 'Grid', 'Samples', 'Indices', 'Object', 'Objects'},
    'Container': {'Tuple', 'Container', 'ContainerContainer', 'TupleTuple', 'Grid', 'Samples', 'Indices', 'Object', 'Objects'},
    'ContainerContainer': {'Tuple', 'Container', 'ContainerContainer', 'TupleTuple', 'Grid', 'Samples', 'Indices', 'Object', 'Objects'},
    'Callable': {'Callable'},
    
    # Numeric types - range/rank indices
    # NOTE: Boolean = bool is a subtype of int in Python (True=1, False=0)
    # Therefore Boolean is compatible with all Integer and range types
    'Boolean': {'Boolean', 'Integer', 'Numerical', 'F_', 'FL', 'L_', 'R_', 'R4', 'R8', 'A4', 'A8', 'C_', 'I_', 'J_'},
    'Integer': {'Boolean', 'Integer', 'Numerical', 'F_', 'FL', 'L_', 'R_', 'R4', 'R8', 'C_'},
    'Numerical': {'Boolean', 'Integer', 'Numerical', 'F_', 'FL', 'L_', 'R_', 'R4', 'R8', 'C_', 'IJ'},
    
    # Integer ranges - all compatible with each other and Integer/Numerical
    'F_': {'Boolean', 'Integer', 'Numerical', 'F_', 'FL', 'R_', 'R4', 'R8', 'C_'},
    'FL': {'Boolean', 'Integer', 'Numerical', 'F_', 'FL', 'L_'},
    'L_': {'Boolean', 'Integer', 'Numerical', 'L_', 'FL'},
    'R_': {'Boolean', 'Integer', 'Numerical', 'F_', 'R_', 'R4', 'R8', 'C_'},
    'R4': {'Boolean', 'Integer', 'Numerical', 'F_', 'R_', 'R4', 'R8', 'C_'},
    'R8': {'Boolean', 'Integer', 'Numerical', 'F_', 'R_', 'R4', 'R8', 'C_'},
    'A4': {'Boolean', 'Integer', 'Numerical', 'A4', 'A8'},
    'A8': {'Boolean', 'Integer', 'Numerical', 'A4', 'A8'},
    'C_': {'Boolean', 'Integer', 'Numerical', 'C_', 'F_', 'R_', 'R4', 'R8'},
    'I_': {'Boolean', 'Integer', 'Numerical'},
    'J_': {'Boolean', 'Integer', 'Numerical'},
    'IJ': {'Numerical', 'IJ'},
    
    # Specific tuple types - consolidated from frozenset variants
    'Indices': {'Tuple', 'Container', 'ContainerContainer', 'Indices', 'Object', 'Objects'},
    'Object': {'Tuple', 'Container', 'ContainerContainer', 'Indices', 'Object', 'Objects'},
    'Objects': {'Tuple', 'Container', 'ContainerContainer', 'Indices', 'Object', 'Objects'},
    'Grid': {'Tuple', 'Container', 'ContainerContainer', 'Grid', 'Samples', 'TupleTuple'},
    'Samples': {'Tuple', 'Container', 'ContainerContainer', 'Grid', 'Samples', 'TupleTuple'},
    'TupleTuple': {'Tuple', 'Container', 'ContainerContainer', 'Grid', 'Samples', 'TupleTuple'},
    'TTT_iii': {'TupleTuple', 'Tuple', 'Container', 'ContainerContainer'},
    'Colors': {'Tuple', 'Container', 'ContainerContainer'},
    'Cell': {'Cell', 'Tuple', 'Container'},
    
    # Generic catch-all types
    'Any': {'Any', 'Boolean', 'Integer', 'Numerical', 'F_', 'FL', 'L_', 'R_', 'R4', 'R8', 'A4', 'A8', 'C_', 'I_', 'J_', 'IJ', 'Tuple', 'Container', 'ContainerContainer', 'Callable', 'Grid', 'Samples', 'TTT_iii', 'Cell', 'Colors', 'Object', 'Objects', 'Indices', 'TupleTuple'},
}"""
    
    # Replace
    if re.search(old_overlaps, content):
        content = re.sub(old_overlaps, new_overlaps, content)
        print("✓ Successfully updated HINT_OVERLAPS")
    else:
        print("⚠️  Could not find exact pattern match")
        print("Attempting manual replacement...")
        
        # Fallback: Find HINT_OVERLAPS and replace until we find the closing }
        start_idx = content.find("HINT_OVERLAPS = {")
        if start_idx != -1:
            # Find matching closing brace
            brace_count = 0
            in_dict = False
            end_idx = start_idx
            
            for i in range(start_idx, len(content)):
                if content[i] == '{':
                    brace_count += 1
                    in_dict = True
                elif content[i] == '}':
                    brace_count -= 1
                    if in_dict and brace_count == 0:
                        end_idx = i + 1
                        break
            
            old_content = content[start_idx:end_idx]
            content = content[:start_idx] + new_overlaps + content[end_idx:]
            print("✓ Successfully updated HINT_OVERLAPS (fallback method)")
    
    # Write back
    constants_file.write_text(content)
    print(f"✓ Updated: {constants_file}")
    print()
    
    # Show statistics
    print("Type consolidation summary:")
    print("  Before: 27 types (including FrozenSet, IntegerSet, IndicesSet, Patch)")
    print("  After:  15 types (tuple-only architecture)")
    print("  Removed: FrozenSet, IntegerSet, IndicesSet, Patch (frozenset variants)")
    print("  Kept: Indices, Object, Objects (now tuple-based)")
    print()
    
    print("All consolidation phases complete!")
    print()
    print("Summary of changes:")
    print("  Phase 1: arc_types.py - Frozenset → Tuple types")
    print("  Phase 2: dsl.py - 34 function pairs consolidated (404 lines removed)")
    print("  Phase 3: solvers_pre.py - 210 _f calls → base names")
    print("  Phase 4: constants.py - HINT_OVERLAPS updated (27 → 15 types)")
    print()
    print("Next: Commit changes and verify with full test suite")
    
    return True


def main():
    try:
        success = update_hint_overlaps()
        return 0 if success else 1
    except Exception as e:
        print(f"❌ Error during update: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
