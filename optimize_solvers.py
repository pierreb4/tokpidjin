#!/usr/bin/env python3
"""
Optimize Solvers with Specialized Functions

This script reads specialized analysis JSON files and updates the corresponding
solver functions in solvers.py to use specialized variants of DSL functions
where appropriate.

Usage:
    python optimize_solvers.py [analysis_file] [--apply]
    python optimize_solvers.py --all [--apply]

Arguments:
    analysis_file: Path to the specialized analysis JSON file
    --all: Process all specialized analysis JSON files in the stats directory
    --apply: Actually modify the solvers.py file (without this, changes are only shown)
"""

import os
import sys
import json
import re
import argparse
import glob
import datetime
from typing import Dict, List, Tuple


def load_analysis_file(filename: str) -> dict:
    """Load specialized function analysis from a JSON file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading analysis file '{filename}': {e}")
        return {}


def extract_solver_key(filename: str) -> str:
    """Extract solver key from analysis filename."""
    base = os.path.basename(filename)
    # Extract from special_dsl_XXXXX.json
    match = re.search(r'special_dsl_([a-f0-9]+)\.json', base)
    
    if match:
        return match.group(1)
    return None


def find_solver_function(solver_key: str, solvers_path: str = "solvers.py") -> Tuple[str, int, int]:
    """
    Find the solver function in the solvers.py file.
    
    Returns:
        Tuple containing (function_text, start_line, end_line)
    """
    function_name = f"solve_{solver_key}"
    
    try:
        with open(solvers_path, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: Solvers file '{solvers_path}' not found.")
        return None, -1, -1
    
    # Find the function definition
    start_line = -1
    end_line = -1
    
    for i, line in enumerate(lines):
        # Look for function definition
        if re.match(rf'def\s+{function_name}\s*\(', line):
            start_line = i
            # Find the end of the function (next function def or end of file)
            for j in range(i + 1, len(lines)):
                if re.match(r'def\s+', lines[j]):
                    end_line = j - 1
                    break
            if end_line == -1:  # If we reached the end of file
                end_line = len(lines) - 1
            break
    
    if start_line == -1:
        print(f"Error: Solver function '{function_name}' not found in '{solvers_path}'")
        return None, -1, -1
    
    function_text = ''.join(lines[start_line:end_line+1])
    return function_text, start_line, end_line


def optimize_solver_function(function_text: str, perfect_matches: List[dict]) -> str:
    """
    Replace generic function calls with specialized variants based on perfect matches.
    
    Args:
        function_text: The complete text of the solver function
        perfect_matches: List of perfect matches from the analysis
    
    Returns:
        Modified function text with specialized function calls
    """
    modified_text = function_text
    replacements_made = []
    
    # For each function to replace
    for match in perfect_matches:
        func_name = match["name"]
        specialized_variant = match["variant"]
        func_type = match["type"]  # tuple or frozenset
        
        # Create regex pattern to match the function call
        # This handles function calls with arguments but avoids partial matches
        pattern = r'(?<![a-zA-Z0-9_])' + re.escape(func_name) + r'\s*\('
        
        # Replace the function name with its specialized variant
        new_text = re.sub(pattern, specialized_variant + '(', modified_text)
        
        # Check if any replacements were made
        if new_text != modified_text:
            replacements_made.append(f"{func_name} → {specialized_variant}")
            modified_text = new_text
    
    return modified_text, replacements_made


def update_solvers_file(solvers_path: str, start_line: int, end_line: int, new_function_text: str) -> bool:
    """
    Update the solvers.py file with the optimized function.
    
    Args:
        solvers_path: Path to the solvers.py file
        start_line: Start line of the function to replace
        end_line: End line of the function to replace
        new_function_text: New function text to insert
    
    Returns:
        True if successful, False otherwise
    """
    try:
        with open(solvers_path, 'r') as f:
            lines = f.readlines()
        
        # Replace the function lines with the new optimized version
        new_lines = new_function_text.splitlines(True)
        lines[start_line:end_line+1] = new_lines
        
        with open(solvers_path, 'w') as f:
            f.writelines(lines)
        
        return True
    except Exception as e:
        print(f"Error updating solvers file: {e}")
        return False


def check_call_sites(solver_function: str, perfect_matches: List[dict]) -> dict:
    """
    Verify that all perfect matches appear in the expected call sites.
    
    Args:
        solver_function: The text of the solver function
        perfect_matches: List of perfect matches from the analysis
    
    Returns:
        Dictionary of errors for matches that don't appear in expected call sites
    """
    errors = {}
    
    # For each function that should be specialized
    for match in perfect_matches:
        func_name = match["name"]
        expected_sites = []
        
        # Get all expected call sites for this function
        if "call_sites" in match:
            for site, site_data in match["call_sites"].items():
                line_num = site.split(":")[-1] if ":" in site else "unknown"
                context = site_data.get("code_context", "")
                if context:
                    expected_sites.append({"line": line_num, "context": context})
        
        # If we have expected call sites, verify they appear in the function
        if expected_sites:
            # Create pattern to match function calls
            pattern = r'(?<![a-zA-Z0-9_])' + re.escape(func_name) + r'\s*\('
            actual_calls = re.findall(pattern, solver_function)
            
            # Count actual calls vs expected
            if len(actual_calls) != len(expected_sites):
                errors[func_name] = {
                    "expected_sites": expected_sites,
                    "actual_calls": len(actual_calls),
                    "expected_calls": len(expected_sites),
                    "message": f"Found {len(actual_calls)} calls but expected {len(expected_sites)}"
                }
                
            # Also check if each context appears in the function
            for site in expected_sites:
                context = site["context"].strip()
                if context and context not in solver_function:
                    if func_name not in errors:
                        errors[func_name] = {
                            "expected_sites": expected_sites,
                            "actual_calls": len(actual_calls),
                            "expected_calls": len(expected_sites),
                            "message": "Call site context not found in function"
                        }
                    # Add detail about the specific missing context
                    errors[func_name].setdefault("missing_contexts", []).append(context)
    
    return errors


def generate_error_report(solver_key: str, errors: dict) -> str:
    """
    Generate an error report for mismatched call sites.
    
    Args:
        solver_key: Key of the solver function
        errors: Dictionary of errors from check_call_sites
    
    Returns:
        Path to the generated error report
    """
    if not errors:
        return None
    
    # Create error directory if it doesn't exist
    os.makedirs("error", exist_ok=True)
    
    # Generate error report filename
    report_file = f"error/call_site_mismatch_{solver_key}.json"
    
    # Create error report
    report = {
        "solver_key": solver_key,
        "timestamp": datetime.datetime.now().isoformat(),
        "errors": errors
    }
    
    # Write report to file
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    return report_file


def process_analysis_file(analysis_file: str, apply_changes: bool = False, force: bool = False) -> None:
    """Process a single analysis file and update the solver function."""
    print(f"\nProcessing analysis file: {analysis_file}")
    
    # Load the analysis
    analysis = load_analysis_file(analysis_file)
    if not analysis:
        return
    
    # Extract solver key from filename
    solver_key = extract_solver_key(analysis_file)
    if not solver_key:
        print(f"Error: Could not determine solver key from filename '{analysis_file}'")
        return
    
    print(f"Identified solver key: {solver_key}")
    
    # Get perfect matches
    perfect_matches = analysis.get("perfect_matches", [])
    if not perfect_matches:
        print("No perfect matches found for specialization")
        return
    
    print(f"Found {len(perfect_matches)} perfect matches for specialization:")
    for match in perfect_matches:
        func_name = match['name']
        specialized_variant = match['variant']
        calls = match['calls']
        
        # Extract call sites directly from the match data
        print(f"  - {func_name} → {specialized_variant} ({calls} calls)")
        
        # Check if call_sites exists in this match
        if "call_sites" in match:
            print("    Call sites:")
            for site, site_data in match["call_sites"].items():
                line_num = site.split(":")[-1] if ":" in site else "unknown"
                context = site_data.get("code_context", "")
                count = site_data.get("count", 1)
                print(f"      Line {line_num}: {context} ({count} calls)")
        else:
            print("    Call sites: information not available")
    
    # Find solver function
    solver_function, start_line, end_line = find_solver_function(solver_key)
    if not solver_function:
        return
    
    # Check for call site mismatches
    call_site_errors = check_call_sites(solver_function, perfect_matches)
    if call_site_errors:
        error_report = generate_error_report(solver_key, call_site_errors)
        print(f"\nWARNING: Call site inconsistencies detected!")
        print(f"See error report: {error_report}")
        print("These inconsistencies may indicate changes to the solver since analysis was generated.")
        
        # Print summary of errors
        for func_name, error in call_site_errors.items():
            print(f"  - {func_name}: {error['message']}")
            if "missing_contexts" in error:
                for ctx in error["missing_contexts"]:
                    print(f"      Missing: {ctx}")
        
        if not force:
            print("\nUse --force to apply changes despite inconsistencies")
            return
        else:
            print("\nForcing changes despite inconsistencies (--force flag)")
    
    # Optimize the function
    optimized_function, replacements = optimize_solver_function(solver_function, perfect_matches)
    
    if not replacements:
        print("No replacements to do. Function may already be optimized.")
        return
    
    print("\nOptimized solver function:")
    print("-------------------------")
    print(optimized_function)
    print("-------------------------")
    
    print(f"\nReplacement to do: {', '.join(replacements)}")
    
    # Update the solvers file if requested
    if apply_changes:
        success = update_solvers_file("solvers.py", start_line, end_line, optimized_function)
        if success:
            print(f"Successfully updated solve_{solver_key} in solvers.py")
        else:
            print(f"Failed to update solve_{solver_key} in solvers.py")
    else:
        print("\nChanges not applied. Use --apply to modify solvers.py")


def main():
    parser = argparse.ArgumentParser(
        description="Optimize solvers with specialized function variants."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("analysis_file", nargs="?", help="Specialized analysis JSON file to process")
    group.add_argument("--all", action="store_true", help="Process all analysis files in stats directory")
    parser.add_argument("--apply", action="store_true", help="Apply changes to solvers.py")
    parser.add_argument("--force", action="store_true", help="Force changes even with call site inconsistencies")
    
    args = parser.parse_args()
    
    if args.all:
        # Process all analysis files
        analysis_files = glob.glob("stats/special_dsl_*.json")
        if not analysis_files:
            analysis_files = glob.glob("stats/*_dsl_stats.json")
        
        if not analysis_files:
            print("No analysis files found in stats directory")
            return
        
        print(f"Found {len(analysis_files)} analysis files to process")
        for file in analysis_files:
            process_analysis_file(file, args.apply, args.force)
    else:
        # Process a single analysis file
        process_analysis_file(args.analysis_file, args.apply, args.force)
    
    print("\nDone!")


if __name__ == "__main__":
    main()