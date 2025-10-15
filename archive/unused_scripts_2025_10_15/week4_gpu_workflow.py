#!/usr/bin/env python3
"""
Week 4 GPU Conversion Workflow - Complete automation

This script automates the entire Week 4 workflow:
1. Analyze all solvers for GPU potential
2. Convert top N candidates
3. Test each conversion
4. Generate report

Usage:
    # Analyze only
    python week4_gpu_workflow.py --analyze-only
    
    # Convert top 10
    python week4_gpu_workflow.py --convert 10
    
    # Convert top 20 with testing
    python week4_gpu_workflow.py --convert 20 --test
    
    # Convert specific solvers
    python week4_gpu_workflow.py --solvers solve_36d67576 solve_36fdfd69
"""

import argparse
import subprocess
import time
from utils import print_l


def run_analysis() -> list:
    """Run solver analysis and return top candidates."""
    print_l("=" * 100)
    print_l("STEP 1: ANALYZING SOLVERS")
    print_l("=" * 100)
    print_l("")
    
    result = subprocess.run(
        ['python', 'analyze_solvers_for_gpu.py', '--top', '50'],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print_l("❌ Analysis failed!")
        print_l(result.stderr)
        return []
    
    print_l(result.stdout)
    
    # Parse output to extract top candidates
    # This is a simple extraction - could be enhanced
    candidates = []
    in_priority_section = False
    
    for line in result.stdout.split('\n'):
        if 'HIGH PRIORITY' in line and 'mean ≥100 cells' in line:
            in_priority_section = True
            continue
        if 'GOOD CANDIDATES' in line:
            break
        if in_priority_section and line.strip().startswith('solve_'):
            solver_name = line.strip().split()[0]
            candidates.append(solver_name)
    
    return candidates


def convert_solvers(solver_names: list, dry_run: bool = False) -> tuple:
    """Convert multiple solvers."""
    print_l("")
    print_l("=" * 100)
    print_l(f"STEP 2: CONVERTING {len(solver_names)} SOLVERS")
    print_l("=" * 100)
    print_l("")
    
    cmd = ['python', 'convert_solver_to_gpu.py'] + solver_names
    if dry_run:
        cmd.append('--dry-run')
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    print_l(result.stdout)
    
    if result.returncode != 0:
        print_l("❌ Conversion failed!")
        print_l(result.stderr)
        return 0, 0
    
    # Parse summary
    for line in result.stdout.split('\n'):
        if 'SUMMARY:' in line:
            # Extract numbers from "SUMMARY: 10/10 solvers processed, 25 replacements"
            parts = line.split(',')
            if len(parts) >= 2:
                replacements = int(parts[1].split()[0])
                success = int(line.split('/')[0].split()[-1])
                return success, replacements
    
    return 0, 0


def test_solvers(solver_names: list) -> tuple:
    """Test converted solvers."""
    print_l("")
    print_l("=" * 100)
    print_l(f"STEP 3: TESTING {len(solver_names)} SOLVERS")
    print_l("=" * 100)
    print_l("")
    
    passed = []
    failed = []
    
    for solver_name in solver_names:
        task_id = solver_name.replace('solve_', '')
        print_l(f"\n🧪 Testing {solver_name} (task {task_id})...")
        
        result = subprocess.run(
            ['python', 'run_test.py', '-q', '-i', task_id],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0 and 'solved correctly' in result.stdout:
            print_l(f"  ✅ PASSED")
            passed.append(solver_name)
        else:
            print_l(f"  ❌ FAILED")
            print_l(f"     {result.stdout}")
            failed.append(solver_name)
        
        time.sleep(0.1)  # Brief pause between tests
    
    return passed, failed


def generate_report(
    total_analyzed: int,
    converted_count: int,
    replacements: int,
    passed: list,
    failed: list
):
    """Generate final report."""
    print_l("")
    print_l("=" * 100)
    print_l("WEEK 4 GPU CONVERSION REPORT")
    print_l("=" * 100)
    print_l("")
    
    print_l(f"📊 Solvers analyzed: {total_analyzed}")
    print_l(f"🔄 Solvers converted: {converted_count}")
    print_l(f"📝 Total replacements (o_g → o_g_t): {replacements}")
    print_l("")
    
    if passed or failed:
        print_l("🧪 Test Results:")
        print_l(f"   ✅ Passed: {len(passed)}")
        print_l(f"   ❌ Failed: {len(failed)}")
        print_l(f"   📈 Success rate: {len(passed)/(len(passed)+len(failed))*100:.1f}%")
        print_l("")
    
    if passed:
        print_l("✅ Successfully converted and tested:")
        for solver in passed:
            print_l(f"   • {solver}")
        print_l("")
    
    if failed:
        print_l("❌ Conversion succeeded but tests failed:")
        for solver in failed:
            print_l(f"   • {solver}")
        print_l("")
        print_l("⚠️  Review failed solvers manually")
        print_l("")
    
    print_l("=" * 100)
    print_l("EXPECTED IMPACT (based on Week 3 validation):")
    print_l("=" * 100)
    print_l("• Individual solvers: 2-6x speedup on large grids")
    print_l("• Average across tasks: 2.0-2.5x speedup")
    print_l("• Production run_batt.py: 40-50% reduction in execution time")
    print_l("")
    print_l("Next: Deploy to Kaggle and measure actual performance!")
    print_l("  bash run_card.sh -i -b -c -32")
    print_l("")


def main():
    parser = argparse.ArgumentParser(
        description='Week 4 GPU conversion workflow automation',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--analyze-only', action='store_true',
                       help='Only analyze solvers, don\'t convert')
    parser.add_argument('--convert', type=int, metavar='N',
                       help='Convert top N candidates')
    parser.add_argument('--solvers', nargs='+', metavar='SOLVER',
                       help='Convert specific solvers (e.g., solve_36d67576)')
    parser.add_argument('--test', action='store_true',
                       help='Test converted solvers')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be converted without applying')
    
    args = parser.parse_args()
    
    print_l("=" * 100)
    print_l("WEEK 4: GPU CONVERSION WORKFLOW")
    print_l("Scaling hybrid GPU strategy to 20-50 solvers")
    print_l("=" * 100)
    print_l("")
    
    # Step 1: Analysis
    if args.solvers:
        candidates = args.solvers
        total_analyzed = len(candidates)
    else:
        candidates = run_analysis()
        total_analyzed = len(candidates)
        
        if args.analyze_only:
            print_l("\n✅ Analysis complete!")
            print_l(f"Found {len(candidates)} high-priority candidates")
            print_l("\nRun with --convert N to convert top N solvers")
            return
    
    # Step 2: Conversion
    if args.convert:
        solvers_to_convert = candidates[:args.convert]
    elif args.solvers:
        solvers_to_convert = args.solvers
    else:
        print_l("\n⚠️  Specify --convert N or --solvers to proceed with conversion")
        return
    
    if len(solvers_to_convert) == 0:
        print_l("\n⚠️  No solvers to convert")
        return
    
    converted_count, replacements = convert_solvers(solvers_to_convert, dry_run=args.dry_run)
    
    if args.dry_run:
        print_l("\n✅ Dry run complete - no changes were made")
        return
    
    # Step 3: Testing
    passed = []
    failed = []
    
    if args.test and converted_count > 0 and replacements > 0:
        passed, failed = test_solvers(solvers_to_convert)
    
    # Step 4: Report
    generate_report(total_analyzed, converted_count, replacements, passed, failed)


if __name__ == '__main__':
    main()
