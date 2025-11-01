#!/usr/bin/env python3
"""
Consolidate ALL remaining tiers (2-4) in one execution
Tiers: Selection (5), Statistics (9), Geometric (9)
Total: 23 functions, ~250+ lines to remove
"""

import re
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, List, Dict, Tuple

@dataclass
class FunctionDef:
    name: str
    variant: str
    start_line: int
    end_line: int
    
    @property
    def full_name(self) -> str:
        return f"{self.name}{self.variant}"
    
    def lines_count(self) -> int:
        return self.end_line - self.start_line


def find_function_bounds(lines: List[str], func_name: str, variant: str) -> Optional[FunctionDef]:
    """Find the start and end line of a function definition."""
    pattern = rf"^def {re.escape(func_name)}{re.escape(variant)}\("
    
    start_idx = None
    for i, line in enumerate(lines):
        if re.match(pattern, line):
            start_idx = i
            break
    
    if start_idx is None:
        return None
    
    base_indent = len(lines[start_idx]) - len(lines[start_idx].lstrip())
    end_idx = len(lines)
    
    for i in range(start_idx + 1, len(lines)):
        line = lines[i]
        
        if not line.strip():
            continue
        
        current_indent = len(line) - len(line.lstrip())
        if line.strip().startswith('def ') and current_indent <= base_indent:
            end_idx = i
            break
    
    return FunctionDef(func_name, variant, start_idx, end_idx)


def consolidate_multi_tier(dsl_file: Path, tiers: Dict[str, List[str]]) -> bool:
    """Consolidate multiple tiers."""
    
    print("=" * 70)
    print("MULTI-TIER CONSOLIDATION - TIERS 2-4")
    print("=" * 70)
    print()
    
    # Read file
    content = dsl_file.read_text()
    lines = content.split('\n')
    
    print(f"Original file: {len(lines)} lines")
    print()
    
    # Flatten all functions
    all_functions = {}
    for tier_name, func_list in tiers.items():
        for func_name in func_list:
            all_functions[func_name] = tier_name
    
    # Build consolidation map
    consolidations = {}
    
    for func_name, tier_name in all_functions.items():
        t_func = find_function_bounds(lines, func_name, "_t")
        f_func = find_function_bounds(lines, func_name, "_f")
        
        if not t_func or not f_func:
            print(f"❌ {func_name}: missing _t or _f variant, SKIPPING")
            return False
        
        consolidations[func_name] = (t_func, f_func, tier_name)
    
    # Sort by start_line in REVERSE order (bottom-up deletion)
    sorted_consolidations = sorted(
        consolidations.items(),
        key=lambda x: max(x[1][0].start_line, x[1][1].start_line),
        reverse=True
    )
    
    # Track consolidated functions by tier
    tier_results = {tier_name: [] for tier_name in tiers.keys()}
    
    print("Consolidating functions (bottom-up):")
    print()
    
    deleted_lines = 0
    
    for func_name, (t_func, f_func, tier_name) in sorted_consolidations:
        # Determine which comes first
        if t_func.start_line < f_func.start_line:
            kept_func = t_func
            removed_func = f_func
        else:
            kept_func = t_func  # Always keep _t variant
            removed_func = f_func
        
        # Extract the _t variant
        t_lines = lines[kept_func.start_line:kept_func.end_line]
        
        # Fix type hints: FrozenSet -> Tuple
        t_lines_updated = []
        for line in t_lines:
            # Replace function signature
            line = re.sub(
                rf'^def {re.escape(func_name)}_t\(',
                f'def {func_name}(',
                line
            )
            # Replace type hints
            line = re.sub(r'FrozenSet\[IJ\]', 'Tuple[IJ, ...]', line)
            line = re.sub(r'FrozenSet\[Cell\]', 'Tuple[Cell, ...]', line)
            line = re.sub(r'FrozenSet\[Color\]', 'Tuple[Color, ...]', line)
            line = re.sub(r'FrozenSet\[Object\]', 'Tuple[Object, ...]', line)
            line = re.sub(r'FrozenSet\[Indices\]', 'Tuple[Indices, ...]', line)
            line = re.sub(r'FrozenSet', 'Tuple', line)
            line = re.sub(r' -> FrozenSet', ' -> Tuple', line)
            
            t_lines_updated.append(line)
        
        # Calculate removal range
        remove_start = min(kept_func.start_line, removed_func.start_line)
        remove_end = max(kept_func.end_line, removed_func.end_line)
        
        # Build new lines array: [before] + [updated_t] + [after]
        before = lines[:remove_start]
        after = lines[remove_end:]
        lines = before + t_lines_updated + after
        
        lines_removed = remove_end - remove_start - (kept_func.end_line - kept_func.start_line)
        deleted_lines += lines_removed
        
        tier_results[tier_name].append((func_name, lines_removed))
    
    # Print results by tier
    print()
    for tier_name, tiers_dict in tiers.items():
        results = tier_results[tier_name]
        if results:
            print(f"{tier_name}:")
            tier_lines = 0
            for func_name, lines_removed in sorted(results):
                print(f"  ✓ {func_name:20} ({lines_removed:3} lines)")
                tier_lines += lines_removed
            print(f"  Subtotal: {tier_lines} lines")
            print()
    
    print(f"Total lines removed: {deleted_lines}")
    print(f"New file size: {len(lines)} lines")
    print()
    
    # Write back
    new_content = '\n'.join(lines)
    dsl_file.write_text(new_content)
    
    print(f"✅ Successfully consolidated {len(consolidations)} functions!")
    print(f"✓ Updated: {dsl_file}")
    print()
    print("Next steps:")
    print("  1. Run: python run_test.py (verify correctness)")
    print("  2. If tests pass, proceed to Phase 3 (constants.py)")
    print("  3. If tests fail, check: git diff dsl.py")
    print()
    
    return True


def main():
    dsl_file = Path("/Users/pierre/dsl/tokpidjin/dsl.py")
    
    if not dsl_file.exists():
        print(f"❌ File not found: {dsl_file}")
        return 1
    
    # Create backup
    backup_file = dsl_file.with_suffix('.py.pre_tiers234_backup')
    if not backup_file.exists():
        import shutil
        shutil.copy(dsl_file, backup_file)
        print(f"Backup created: {backup_file}")
        print()
    
    tiers = {
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
    
    try:
        success = consolidate_multi_tier(dsl_file, tiers)
        return 0 if success else 1
    except Exception as e:
        print(f"❌ Error during consolidation: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
