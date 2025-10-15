#!/usr/bin/env python3
"""
Automatically convert solver o_g calls to o_g_t for GPU acceleration.

This script performs safe, automated conversion of o_g() calls to o_g_t()
in solver functions, enabling GPU acceleration for large grids.

Usage:
    # Convert a single solver
    python convert_solver_to_gpu.py solve_36d67576
    
    # Convert and test
    python convert_solver_to_gpu.py solve_36d67576 --test
    
    # Dry run (show changes without applying)
    python convert_solver_to_gpu.py solve_36d67576 --dry-run
    
    # Convert multiple solvers
    python convert_solver_to_gpu.py solve_36d67576 solve_36fdfd69 solve_1a07d186
"""

import argparse
import re
import os
from typing import List, Tuple
from utils import print_l


class SolverConverter:
    """Convert solver o_g calls to o_g_t."""
    
    def __init__(self, solvers_file: str = 'solvers_pre.py'):
        self.solvers_file = solvers_file
        self.content = None
        
    def load_file(self):
        """Load solvers file."""
        with open(self.solvers_file, 'r') as f:
            self.content = f.read()
    
    def save_file(self, backup: bool = True):
        """Save modified content."""
        if backup:
            backup_file = f'{self.solvers_file}.bak'
            with open(backup_file, 'w') as f:
                f.write(self.content)
            print_l(f"  ✅ Backup saved to {backup_file}")
        
        with open(self.solvers_file, 'w') as f:
            f.write(self.content)
        print_l(f"  ✅ Changes saved to {self.solvers_file}")
    
    def find_solver_function(self, solver_name: str) -> Tuple[int, int, str]:
        """
        Find a solver function in the content.
        
        Returns:
            (start_pos, end_pos, function_text) or (None, None, None) if not found
        """
        # Pattern to match function definition
        pattern = rf'^def {solver_name}\(.*?\):'
        
        lines = self.content.split('\n')
        
        # Find function start
        start_line = None
        for i, line in enumerate(lines):
            if re.match(pattern, line):
                start_line = i
                break
        
        if start_line is None:
            return None, None, None
        
        # Find function end (next def or end of file)
        end_line = len(lines)
        for i in range(start_line + 1, len(lines)):
            if re.match(r'^def ', lines[i]):
                end_line = i
                break
        
        # Get function text
        func_lines = lines[start_line:end_line]
        func_text = '\n'.join(func_lines)
        
        # Calculate positions in original content
        start_pos = sum(len(line) + 1 for line in lines[:start_line])
        end_pos = start_pos + len(func_text)
        
        return start_pos, end_pos, func_text
    
    def convert_o_g_to_o_g_t(self, func_text: str) -> Tuple[str, int]:
        """
        Convert o_g( calls to o_g_t( in function text.
        
        Returns:
            (converted_text, num_replacements)
        """
        # Pattern: o_g( but not o_g_t( or o_g_tuple(
        # Use negative lookahead to avoid matching o_g_t or o_g_tuple
        pattern = r'\bo_g\('
        
        # Count matches
        matches = re.findall(pattern, func_text)
        num_replacements = len(matches)
        
        # Replace o_g( with o_g_t(
        converted = re.sub(pattern, 'o_g_t(', func_text)
        
        return converted, num_replacements
    
    def convert_solver(self, solver_name: str, dry_run: bool = False) -> Tuple[bool, int]:
        """
        Convert a solver function.
        
        Returns:
            (success, num_replacements)
        """
        print_l(f"\n{'[DRY RUN] ' if dry_run else ''}Converting {solver_name}...")
        
        # Find solver function
        start_pos, end_pos, func_text = self.find_solver_function(solver_name)
        
        if func_text is None:
            print_l(f"  ❌ Function {solver_name} not found")
            return False, 0
        
        # Check if already uses o_g_t
        if 'o_g_t(' in func_text:
            print_l(f"  ℹ️  Already uses o_g_t - no conversion needed")
            return True, 0
        
        # Check if uses o_g
        if 'o_g(' not in func_text:
            print_l(f"  ℹ️  No o_g calls found - no conversion needed")
            return True, 0
        
        # Convert
        converted, num_replacements = self.convert_o_g_to_o_g_t(func_text)
        
        print_l(f"  📝 Found {num_replacements} o_g call(s) to convert")
        
        if dry_run:
            print_l("\n  === BEFORE ===")
            print_l(func_text)
            print_l("\n  === AFTER ===")
            print_l(converted)
            print_l("")
            return True, num_replacements
        
        # Apply changes
        self.content = self.content[:start_pos] + converted + self.content[end_pos:]
        print_l(f"  ✅ Converted {num_replacements} call(s): o_g → o_g_t")
        
        return True, num_replacements
    
    def convert_multiple(self, solver_names: List[str], dry_run: bool = False) -> Tuple[int, int]:
        """
        Convert multiple solvers.
        
        Returns:
            (num_success, total_replacements)
        """
        self.load_file()
        
        num_success = 0
        total_replacements = 0
        
        for solver_name in solver_names:
            success, replacements = self.convert_solver(solver_name, dry_run)
            if success:
                num_success += 1
                total_replacements += replacements
        
        if not dry_run and total_replacements > 0:
            self.save_file(backup=True)
        
        return num_success, total_replacements


def test_solver(solver_name: str) -> bool:
    """Test a converted solver."""
    task_id = solver_name.replace('solve_', '')
    
    print_l(f"\n🧪 Testing {solver_name} (task {task_id})...")
    
    import subprocess
    result = subprocess.run(
        ['python', 'run_test.py', '-q', '-i', task_id],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        # Check for success message
        if 'solved correctly' in result.stdout:
            print_l(f"  ✅ Test passed!")
            return True
        else:
            print_l(f"  ⚠️  Test completed but check output:")
            print_l(result.stdout)
            return False
    else:
        print_l(f"  ❌ Test failed!")
        print_l(result.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Convert solver o_g calls to o_g_t for GPU acceleration',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert single solver
  python convert_solver_to_gpu.py solve_36d67576
  
  # Convert and test
  python convert_solver_to_gpu.py solve_36d67576 --test
  
  # Dry run (preview changes)
  python convert_solver_to_gpu.py solve_36d67576 --dry-run
  
  # Convert multiple solvers
  python convert_solver_to_gpu.py solve_36d67576 solve_36fdfd69 solve_1a07d186
        """
    )
    
    parser.add_argument('solvers', nargs='+', help='Solver function name(s) to convert')
    parser.add_argument('--dry-run', action='store_true', help='Show changes without applying')
    parser.add_argument('--test', action='store_true', help='Run tests after conversion')
    parser.add_argument('--file', default='solvers_pre.py', help='Solvers file (default: solvers_pre.py)')
    
    args = parser.parse_args()
    
    print_l("=" * 100)
    print_l("SOLVER GPU CONVERTER")
    print_l("Converting o_g → o_g_t for GPU acceleration")
    print_l("=" * 100)
    
    converter = SolverConverter(solvers_file=args.file)
    num_success, total_replacements = converter.convert_multiple(args.solvers, dry_run=args.dry_run)
    
    print_l("")
    print_l("=" * 100)
    print_l(f"SUMMARY: {num_success}/{len(args.solvers)} solvers processed, {total_replacements} replacements")
    print_l("=" * 100)
    
    if args.dry_run:
        print_l("\n⚠️  This was a dry run - no changes were made")
        print_l("Remove --dry-run flag to apply changes")
    elif total_replacements > 0:
        print_l(f"\n✅ Successfully converted {total_replacements} o_g call(s)")
        print_l(f"   Backup saved to {args.file}.bak")
        
        if args.test:
            print_l("\n" + "=" * 100)
            print_l("RUNNING TESTS")
            print_l("=" * 100)
            
            all_passed = True
            for solver_name in args.solvers:
                if not test_solver(solver_name):
                    all_passed = False
            
            if all_passed:
                print_l("\n✅ All tests passed!")
            else:
                print_l("\n⚠️  Some tests failed - review output above")
        else:
            print_l("\nRun with --test flag to validate changes")
            print_l("Or manually test with: python run_test.py -q -i TASKID")
    else:
        print_l("\nℹ️  No conversions needed (solvers already optimized or don't use o_g)")
    
    print_l("")


if __name__ == '__main__':
    main()
