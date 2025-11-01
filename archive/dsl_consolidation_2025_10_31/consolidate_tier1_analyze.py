#!/usr/bin/env python3
"""
Tier 1 Consolidation - Collection Operations
Consolidates: apply, rapply, mapply, first, last, remove, other, sfilter, mfilter, merge, combine
"""

import re
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, Tuple, List

@dataclass
class FunctionDef:
    """Represents a function definition in the source code."""
    name: str
    variant: str  # "_t" or "_f"
    start_line: int  # 0-indexed
    end_line: int  # 0-indexed (exclusive)
    
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
    
    # Find end: next def at same or lower indentation
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
    
    return FunctionDef(
        name=func_name,
        variant=variant,
        start_line=start_idx,
        end_line=end_idx
    )


def consolidate_function_tier1(dsl_file: Path, func_names: List[str]) -> Tuple[bool, List[str]]:
    """
    Consolidate a set of functions (Tier 1).
    Returns: (success, messages)
    """
    messages = []
    content = dsl_file.read_text()
    lines = content.split('\n')
    
    messages.append("=" * 70)
    messages.append("TIER 1 CONSOLIDATION - COLLECTION OPERATIONS")
    messages.append("=" * 70)
    messages.append("")
    
    # Find all functions first
    functions_to_consolidate = {}
    
    for func_name in func_names:
        t_func = find_function_bounds(lines, func_name, "_t")
        f_func = find_function_bounds(lines, func_name, "_f")
        
        if not t_func:
            messages.append(f"⚠️  {func_name}_t NOT FOUND")
            continue
        
        if not f_func:
            messages.append(f"⚠️  {func_name}_f NOT FOUND")
            continue
        
        functions_to_consolidate[func_name] = (t_func, f_func)
        messages.append(f"✓ Found {func_name}: _t at {t_func.start_line+1}, _f at {f_func.start_line+1}")
    
    found_count = len(functions_to_consolidate)
    messages.append(f"\nReady to consolidate {found_count}/{len(func_names)} functions")
    
    if found_count == 0:
        messages.append("\n❌ No functions found for consolidation!")
        return False, messages
    
    # Show consolidation plan
    messages.append("\nConsolidation Plan:")
    messages.append("-" * 70)
    
    total_lines_to_remove = 0
    for func_name in sorted(functions_to_consolidate.keys()):
        t_func, f_func = functions_to_consolidate[func_name]
        
        # Calculate what will be removed (both functions minus the kept _t)
        lines_in_t = t_func.lines_count()
        lines_in_f = f_func.lines_count()
        lines_removed = lines_in_f  # We keep _t renamed, remove _f
        
        total_lines_to_remove += lines_removed
        
        messages.append(f"  {func_name:20} _t({lines_in_t:3} lines) _f({lines_in_f:3} lines) → remove {lines_removed:3} lines")
    
    messages.append("-" * 70)
    messages.append(f"Total lines to remove: {total_lines_to_remove}")
    messages.append("")
    
    # Show what consolidation means
    messages.append("For each function:")
    messages.append("  1. Extract the _t variant (tuple-based)")
    messages.append("  2. Replace FrozenSet type hints with Tuple")
    messages.append("  3. Rename 'def func_t(' to 'def func('")
    messages.append("  4. Delete the _f variant (frozenset-based)")
    messages.append("")
    
    messages.append("Next: Run consolidate_tier1_execute.py to actually perform consolidation")
    
    return True, messages


def main():
    dsl_file = Path("/Users/pierre/dsl/tokpidjin/dsl.py")
    
    tier1_functions = [
        "apply", "rapply", "mapply", "first", "last", "remove", "other",
        "sfilter", "mfilter", "merge", "combine"
    ]
    
    success, messages = consolidate_function_tier1(dsl_file, tier1_functions)
    
    for msg in messages:
        print(msg)
    
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
