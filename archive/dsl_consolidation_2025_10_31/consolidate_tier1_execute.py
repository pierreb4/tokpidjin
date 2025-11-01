#!/usr/bin/env python3
"""
Tier 1 Consolidation - EXECUTION
Consolidates: apply, rapply, mapply, first, last, remove, other, sfilter, mfilter, merge, combine
"""

import re
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, List

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


def consolidate_tier1(dsl_file: Path) -> bool:
    """Consolidate Tier 1 functions in-place."""
    
    tier1_functions = [
        "apply", "rapply", "mapply", "first", "last", "remove", "other",
        "sfilter", "mfilter", "merge", "combine"
    ]
    
    print("=" * 70)
    print("TIER 1 CONSOLIDATION - EXECUTION")
    print("=" * 70)
    print()
    
    # Read file
    content = dsl_file.read_text()
    lines = content.split('\n')
    
    print(f"Original file: {len(lines)} lines")
    print()
    
    # Build consolidation map: (function_name) -> (t_func, f_func)
    consolidations = {}
    
    for func_name in tier1_functions:
        t_func = find_function_bounds(lines, func_name, "_t")
        f_func = find_function_bounds(lines, func_name, "_f")
        
        if not t_func or not f_func:
            print(f"❌ {func_name}: missing _t or _f variant, SKIPPING")
            return False
        
        consolidations[func_name] = (t_func, f_func)
    
    # Sort by start_line in REVERSE order (bottom-up deletion prevents index shifts)
    sorted_consolidations = sorted(
        consolidations.items(),
        key=lambda x: max(x[1][0].start_line, x[1][1].start_line),
        reverse=True
    )
    
    print("Consolidating functions (bottom-up to avoid index shifts):")
    print()
    
    deleted_lines = 0
    
    for func_name, (t_func, f_func) in sorted_consolidations:
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
        
        print(f"  ✓ {func_name:20} consolidated (removed {lines_removed:3} lines)")
    
    print()
    print(f"Total lines removed: {deleted_lines}")
    print(f"New file size: {len(lines)} lines")
    print()
    
    # Write back
    new_content = '\n'.join(lines)
    dsl_file.write_text(new_content)
    
    print("✅ Successfully consolidated all Tier 1 functions!")
    print(f"✓ Updated: {dsl_file}")
    print()
    print("Next steps:")
    print("  1. Run: python run_test.py (verify correctness)")
    print("  2. If tests pass, proceed to Tier 2 consolidation")
    print("  3. If tests fail, check: git diff dsl.py")
    print()
    
    return True


def main():
    dsl_file = Path("/Users/pierre/dsl/tokpidjin/dsl.py")
    
    if not dsl_file.exists():
        print(f"❌ File not found: {dsl_file}")
        return 1
    
    # Create backup
    backup_file = dsl_file.with_suffix('.py.pre_tier1_backup')
    if not backup_file.exists():
        import shutil
        shutil.copy(dsl_file, backup_file)
        print(f"Backup created: {backup_file}")
        print()
    
    try:
        success = consolidate_tier1(dsl_file)
        return 0 if success else 1
    except Exception as e:
        print(f"❌ Error during consolidation: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
