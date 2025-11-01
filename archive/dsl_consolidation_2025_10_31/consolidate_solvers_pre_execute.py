#!/usr/bin/env python3
"""
Phase 4: Migrate solvers_pre.py
Replace all _f variant calls with base names (e.g., size_f -> size)

Functions to update (210 occurrences of 15 unique _f variants):
- Tier 1: combine_f, mfilter_f, other_f, rapply_f, sfilter_f
- Tier 3: palette_f, portrait_f, shape_f, size_f
- Tier 2: get_val_rank_f
- Custom: mir_rot_f, upscale_f, height_f, width_f, get_color_rank_f (not in original 34)
"""

import re
from pathlib import Path

def migrate_solvers_pre():
    """Migrate solvers_pre.py to use base names instead of _f variants."""
    
    solvers_pre_file = Path("/Users/pierre/dsl/tokpidjin/solvers_pre.py")
    
    print("=" * 70)
    print("PHASE 4: MIGRATE solvers_pre.py")
    print("=" * 70)
    print()
    
    # Read file
    content = solvers_pre_file.read_text()
    original_content = content
    
    # Create backup
    backup_file = solvers_pre_file.with_suffix('.py.pre_consolidation_backup')
    if not backup_file.exists():
        solvers_pre_file.write_text(original_content)
        solvers_pre_file.write_text(original_content)
        print(f"Backup created: {backup_file}")
    
    # Functions to replace (from Tier 1, 2, 3 consolidations)
    tier_functions = {
        # Tier 1 - Collection operations
        'combine_f': 'combine',
        'mfilter_f': 'mfilter',
        'other_f': 'other',
        'rapply_f': 'rapply',
        'sfilter_f': 'sfilter',
        
        # Tier 3 - Statistics operations
        'palette_f': 'palette',
        'portrait_f': 'portrait',
        'shape_f': 'shape',
        'size_f': 'size',
        
        # Tier 2 - Selection operations
        'get_val_rank_f': 'get_val_rank',
        
        # Custom functions (not in original 34, but also need updating)
        'mir_rot_f': 'mir_rot',
        'upscale_f': 'upscale',
        'height_f': 'height',
        'width_f': 'width',
        'get_color_rank_f': 'get_color_rank',
    }
    
    print(f"Replacing {len(tier_functions)} _f variants:")
    for old_name, new_name in sorted(tier_functions.items()):
        print(f"  {old_name:25} → {new_name}")
    print()
    
    # Count occurrences before
    replacement_count = 0
    
    for old_name, new_name in tier_functions.items():
        # Match function calls: func_f(
        pattern = f'{re.escape(old_name)}\\('
        matches = len(re.findall(pattern, content))
        
        if matches > 0:
            # Replace: old_f( → new(
            content = re.sub(f'{re.escape(old_name)}\\(', f'{new_name}(', content)
            replacement_count += matches
            print(f"  {old_name:25} {matches:3} replacements")
    
    print()
    print(f"Total replacements: {replacement_count}")
    
    # Verify the changes
    lines_changed = sum(1 for c1, c2 in zip(original_content, content) if c1 != c2)
    
    print(f"Characters modified: {len(original_content) != len(content)}")
    print()
    
    # Check for any remaining _f calls
    remaining_f_calls = re.findall(r'\b\w+_f\(', content)
    if remaining_f_calls:
        print(f"⚠️  Remaining _f variants: {set(remaining_f_calls)}")
    else:
        print("✅ No remaining _f variant calls")
    
    print()
    
    # Write back
    solvers_pre_file.write_text(content)
    print(f"✓ Updated: {solvers_pre_file}")
    print()
    print("Next steps:")
    print("  1. Run: python run_test.py --solvers solvers_pre (verify correctness)")
    print("  2. If tests pass, proceed to Phase 5 (update constants.py)")
    print("  3. If tests fail, check: git diff solvers_pre.py")
    print()
    
    return True


def main():
    try:
        success = migrate_solvers_pre()
        return 0 if success else 1
    except Exception as e:
        print(f"❌ Error during migration: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
