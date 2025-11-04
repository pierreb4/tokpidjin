#!/usr/bin/env python3
"""
List Solver Keys
===============

This script extracts all solver keys from the solvers.py file.
Solver keys are the hexadecimal identifiers in function names like solve_88a62173.
The script can output keys in various formats and provides options for sampling and sorting.

Features:
- Extract keys from solvers.py and output in plain text or JSON format
- View detailed information about solvers including line numbers and code length
- Sort by key or by code complexity (line count)
- Generate random samples of solvers for testing
- Output control with quiet mode for scripting

Usage Examples:
--------------
# List all solver keys
python list_solvers.py

# Output detailed information about solvers, sorted by code length
python list_solvers.py --details --sort length

# Get a random sample of 10 solvers
python list_solvers.py --sample 10

# Get reproducible samples with a fixed seed
python list_solvers.py --sample 5 --seed 42

# Output keys only (for piping to other commands)
python list_solvers.py --quiet

# Save results to JSON file
python list_solvers.py --output solvers.json

Arguments:
---------
  --output, -o FILE       Save output to JSON file
  --verbose, -v           Show verbose processing information
  --quiet, -q             Suppress summary information, show only essential output
  --details, -d           Show detailed information about each solver
  --sort, -s {key,length} Sort results by key (default) or code length
  --sample N              Return a random sample of N solver keys
  --seed N                Set random seed for reproducible sampling
"""

import os
import re
import argparse
import json
import random
from typing import List, Dict, Any


def extract_solver_keys(solvers_path: str = "solvers.py", verbose: bool = False) -> List[str]:
    """
    Extract all solver keys from the solvers.py file.
    
    Args:
        solvers_path: Path to the solvers.py file
        verbose: If True, print additional information
    
    Returns:
        List of solver keys
    """
    if verbose:
        print(f"Reading solvers from: {solvers_path}")
    
    try:
        with open(solvers_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Solvers file '{solvers_path}' not found.")
        return []
    
    # Find all function definitions with the pattern def solve_XXXXX(I):
    pattern = r'def\s+solve_([a-f0-9]+(?:_[a-f0-9]+)*)\s*\('
    matches = re.findall(pattern, content)
    
    if verbose:
        print(f"Found {len(matches)} solver keys")
    
    return matches


def get_solver_details(solvers_path: str = "solvers.py", verbose: bool = False) -> List[Dict[str, Any]]:
    """
    Extract detailed information about each solver.
    
    Returns:
        List of dictionaries with solver details
    """
    try:
        with open(solvers_path, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: Solvers file '{solvers_path}' not found.")
        return []

    solvers = []
    current_solver = None
    docstring_lines = []
    in_docstring = False

    for i, line in enumerate(lines):
        if match := re.match(
            r'def\s+solve_([a-f0-9]+(?:_[a-f0-9]+)*)\s*\(', line
        ):
            key = match[1]
            current_solver = {
                "key": key,
                "line_number": i + 1,
                "function_name": f"solve_{key}",
                "docstring": None,
                "code_length": 0,
            }
            solvers.append(current_solver)
            docstring_lines = []
            in_docstring = False

            # Check for docstring start on the next line
            if i + 1 < len(lines) and '"""' in lines[i + 1]:
                in_docstring = True

        elif current_solver and in_docstring:
            docstring_lines.append(line.strip())
            if '"""' in line and len(docstring_lines) > 1:  # End of docstring
                current_solver["docstring"] = "\n".join(docstring_lines[:-1]) if len(docstring_lines) > 1 else ""
                in_docstring = False

        elif current_solver:
            if re.match(r'def\s+', line):  # Next function definition
                current_solver = None
            elif line.strip() and not line.strip().startswith('#'):
                current_solver["code_length"] += 1

    return solvers


def main():
    parser = argparse.ArgumentParser(description="List all solver keys from solvers.py")
    parser.add_argument("--input", "-i", type=str, default="solvers.py",
                        help="Input solvers file to process (default: solvers.py)")
    parser.add_argument("--output", "-o", type=str, help="Output file to save the keys (JSON format)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Print verbose information")
    parser.add_argument("--quiet", "-q", action="store_true", help="Suppress summary information")
    parser.add_argument("--details", "-d", action="store_true", help="Include detailed information about each solver")
    parser.add_argument("--sort", "-s", choices=["key", "length"], default="key", 
                       help="Sort results by key (default) or code length")
    parser.add_argument("--sample", type=int, help="Return a random sample of N solver keys")
    parser.add_argument("--seed", type=int, help="Random seed for reproducible sampling")
    
    args = parser.parse_args()
    
    # Set random seed if specified
    if args.seed is not None:
        random.seed(args.seed)
    
    if args.details:
        results = get_solver_details(args.input, args.verbose)
        
        # Sort the results
        if args.sort == "length":
            results.sort(key=lambda x: x["code_length"], reverse=True)
        else:  # Default: sort by key
            results.sort(key=lambda x: x["key"])
        
        # Apply sampling if requested
        if args.sample and args.sample > 0:
            if args.sample < len(results):
                results = random.sample(results, args.sample)
                if not args.quiet:
                    print(f"Showing random sample of {args.sample} solvers from {len(results)} total\n")
            elif not args.quiet:
                print(f"Sample size {args.sample} exceeds available solvers ({len(results)}), showing all\n")
        
        # Print the results
        if not args.quiet:
            print(f"Found {len(results)} solvers in {args.input}\n")
        
        print(f"{'Solver Key':<12} {'Line':<6} {'Code Lines':<10}")
        print("-" * 30)
        
        for solver in results:
            print(f"{solver['key']:<12} {solver['line_number']:<6} {solver['code_length']:<10}")
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2)
            if not args.quiet:
                print(f"\nSaved detailed solver information to {args.output}")
    
    else:
        # Just extract the keys
        keys = extract_solver_keys(args.input, args.verbose)
        
        # Sort the keys if requested
        keys.sort()
        
        # Apply sampling if requested
        if args.sample and args.sample > 0:
            if args.sample < len(keys):
                keys = random.sample(keys, args.sample)
                if not args.quiet:
                    print(f"Showing random sample of {args.sample} solvers from {len(keys)} total\n")
            elif not args.quiet:
                print(f"Sample size {args.sample} exceeds available solvers ({len(keys)}), showing all\n")
        
        # Print the results
        if not args.quiet:
            print(f"Found {len(keys)} solver keys in {args.input}:\n")
        
        for key in keys:
            print(key)
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(keys, f, indent=2)
            if not args.quiet:
                print(f"\nSaved solver keys to {args.output}")


if __name__ == "__main__":
    main()