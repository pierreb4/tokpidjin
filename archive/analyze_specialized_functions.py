#!/usr/bin/env python3
"""
Specialized Function Analysis Tool

This script analyzes DSL function usage statistics and identifies opportunities
where generic functions could be replaced with more specialized type-specific
variants (ending with _t for tuple or _f for frozenset).

It helps optimize the DSL by showing which specialized function implementations
would have the greatest impact on performance.

Usage:
    python analyze_specialized_functions.py [stats_file] [--threshold PERCENT] [--verbose]

Arguments:
    stats_file: Path to the JSON file containing DSL function usage statistics
               (default: stats/module_stats.json)
    --threshold: Minimum percentage of calls to consider for reporting (default: 1%)
    --verbose: Show detailed information about all functions found in the stats file
"""

import os
import sys
import json
import argparse
from collections import defaultdict
import inspect

# Import DSL module to check for function existence
import dsl


def load_stats_file(filename):
    """Load statistics from a JSON file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Statistics file '{filename}' not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: '{filename}' is not a valid JSON file.")
        return {}


def get_specialized_variants(function_name):
    """Get tuple and frozenset specialized variants of a function name."""
    t_variant = f"{function_name}_t"
    f_variant = f"{function_name}_f"
    
    has_t_variant = hasattr(dsl, t_variant)
    has_f_variant = hasattr(dsl, f_variant)
    
    return {
        'tuple': t_variant if has_t_variant else None,
        'frozenset': f_variant if has_f_variant else None
    }


def analyze_function_signatures(stats_data):
    """Analyze function call statistics to find specialization opportunities."""
    results = {}
    all_functions = []
    
    # Iterate through each function in the stats
    for function_name, function_stats in stats_data.items():
        # Record all function names for verbose output
        all_functions.append({
            'name': function_name,
            'calls': function_stats.get('calls', 0),
            'in_dsl': hasattr(dsl, function_name)
        })
        
        # Skip if function name already has a suffix _t or _f
        if function_name.endswith('_t') or function_name.endswith('_f'):
            continue
            
        # Skip if function is not in the DSL module
        if not hasattr(dsl, function_name):
            continue
        
        # Get specialized variants
        variants = get_specialized_variants(function_name)
        
        # Skip if no specialized variants exist
        if not variants['tuple'] and not variants['frozenset']:
            continue
        
        # Analyze argument types
        tuple_calls = 0
        frozenset_calls = 0
        other_calls = 0
        total_calls = function_stats.get('calls', 0)
        
        # Extract from type_signatures
        for signature in function_stats.get('type_signatures', []):
            # Parse signature format like "function_name(type1, type2)"
            if '(' in signature and ')' in signature:
                arg_str = signature.split('(')[1].split(')')[0]
                if arg_str:
                    arg_types = [arg.strip() for arg in arg_str.split(',')]
                    if arg_types:
                        first_arg_type = arg_types[0]
                        # Detect tuple vs frozenset
                        if first_arg_type == 'tuple':
                            tuple_calls += function_stats.get('calls', 0)
                        elif first_arg_type == 'frozenset':
                            frozenset_calls += function_stats.get('calls', 0)
                        else:
                            other_calls += function_stats.get('calls', 0)
                    else:
                        other_calls += function_stats.get('calls', 0)
                else:
                    other_calls += function_stats.get('calls', 0)
            else:
                other_calls += function_stats.get('calls', 0)
        
        # If no signatures found, count all as "other"
        if not function_stats.get('type_signatures'):
            other_calls = total_calls
        
        # The sum of specific calls might not match total_calls if the same function
        # is called with different signatures, so adjust totals
        if tuple_calls + frozenset_calls > total_calls:
            # Normalize to match total calls
            ratio = total_calls / (tuple_calls + frozenset_calls)
            tuple_calls = int(tuple_calls * ratio)
            frozenset_calls = int(frozenset_calls * ratio)
        
        # Calculate match scores for specialized variants
        tuple_match = "Yes" if variants['tuple'] else "No"
        frozenset_match = "Yes" if variants['frozenset'] else "No"
        
        # Add to results
        results[function_name] = {
            'total_calls': total_calls,
            'tuple_calls': tuple_calls,
            'tuple_percent': (tuple_calls / total_calls * 100) if total_calls > 0 else 0,
            'has_tuple_variant': variants['tuple'] is not None,
            'tuple_variant': variants['tuple'],
            'tuple_match': tuple_match,
            'frozenset_calls': frozenset_calls,
            'frozenset_percent': (frozenset_calls / total_calls * 100) if total_calls > 0 else 0,
            'has_frozenset_variant': variants['frozenset'] is not None,
            'frozenset_variant': variants['frozenset'],
            'frozenset_match': frozenset_match,
            'other_calls': other_calls,
            'other_percent': (other_calls / total_calls * 100) if total_calls > 0 else 0
        }
    
    return results, all_functions


def print_all_functions(functions):
    """Print all functions found in the stats file."""
    print("\n=== All Functions Found in Stats File ===\n")
    
    # Sort by call count in descending order
    sorted_functions = sorted(functions, key=lambda x: x['calls'], reverse=True)
    
    # Format as a table
    header = f"{'Function':<25} {'Calls':<10} {'In DSL Module':<15} {'Has _t':<10} {'Has _f':<10}"
    print(header)
    print("-" * len(header))
    
    for func in sorted_functions:
        fname = func['name']
        has_t = hasattr(dsl, f"{fname}_t") if func['in_dsl'] else False
        has_f = hasattr(dsl, f"{fname}_f") if func['in_dsl'] else False
        
        row = f"{fname:<25} {func['calls']:<10} {'Yes' if func['in_dsl'] else 'No':<15} {'Yes' if has_t else 'No':<10} {'Yes' if has_f else 'No':<10}"
        print(row)
    
    # Print summary
    print(f"\nTotal functions: {len(functions)}")
    dsl_functions = sum(1 for f in functions if f['in_dsl'])
    print(f"DSL functions: {dsl_functions}")
    print(f"Non-DSL functions: {len(functions) - dsl_functions}")
    
    # Count functions with specialized variants
    t_variants = sum(1 for f in functions if f['in_dsl'] and hasattr(dsl, f"{f['name']}_t"))
    f_variants = sum(1 for f in functions if f['in_dsl'] and hasattr(dsl, f"{f['name']}_f"))
    print(f"Functions with _t variants: {t_variants}")
    print(f"Functions with _f variants: {f_variants}")


def print_findings(results, threshold=1.0):
    """Print the findings from analysis in a readable format."""
    if not results:
        print("No suitable functions for specialization analysis.")
        return
    
    # Sort by total calls in descending order
    sorted_results = sorted(results.items(), key=lambda x: x[1]['total_calls'], reverse=True)
    
    # Check if any function has specialized variants
    has_specialized_variants = any(
        stats['has_tuple_variant'] or stats['has_frozenset_variant'] 
        for _, stats in sorted_results
    )
    
    if not has_specialized_variants:
        print("\n=== Function Specialization Analysis ===\n")
        print("None of the functions in this stats file have specialized variants in the DSL.")
        print("\nMost frequently called functions:\n")
        
        # Show top 10 most called functions
        header = f"{'Function':<20} {'Total Calls':<12} {'In DSL':<10}"
        print(header)
        print("-" * len(header))
        
        top_functions = sorted(sorted_results, key=lambda x: x[1]['total_calls'], reverse=True)[:10]
        for function_name, stats in top_functions:
            row = f"{function_name:<20} {stats['total_calls']:<12} {'Yes':<10}"
            print(row)
            
        print("\nTo improve performance, consider adding specialized variants for these functions:")
        for function_name, stats in top_functions[:3]:
            if stats['tuple_percent'] > 0:
                print(f"- Add {function_name}_t for tuple arguments ({stats['tuple_percent']:.1f}% of calls)")
            if stats['frozenset_percent'] > 0:
                print(f"- Add {function_name}_f for frozenset arguments ({stats['frozenset_percent']:.1f}% of calls)")
        return
    
    # Print header for function specialization analysis
    print("\n=== Function Specialization Analysis ===\n")
    
    # Get all functions with specialized variants - LOWER the minimum call threshold to 1
    functions_with_variants = []
    for function_name, stats in sorted_results:
        # Consider ALL functions with specialized variants (previously required at least 5 calls)
        if stats['has_tuple_variant'] or stats['has_frozenset_variant']:
            functions_with_variants.append((function_name, stats))
    
    if not functions_with_variants:
        print("No functions found with specialized variants.")
        return
    
    print(f"Showing all functions with specialized variants (threshold: {threshold:.1f}%):\n")
    
    # Format as a table
    header = f"{'Function':<20} {'Total Calls':<12} {'Tuple %':<10} {'Tuple Match':<12} {'Frznset %':<10} {'Frznset Match':<12} {'Meets Threshold':<15}"
    print(header)
    print("-" * len(header))
    
    # Track counts for summary
    total_specialization_opportunities = 0
    high_impact_functions = 0
    functions_meeting_threshold = 0
    
    for function_name, stats in functions_with_variants:
        # Check if function meets threshold
        tuple_meets = stats['has_tuple_variant'] and stats['tuple_percent'] >= threshold
        frozenset_meets = stats['has_frozenset_variant'] and stats['frozenset_percent'] >= threshold
        meets_threshold = "Yes" if (tuple_meets or frozenset_meets) else "No"
        
        # Format the row
        row = (
            f"{function_name:<20} "
            f"{stats['total_calls']:<12} "
            f"{stats['tuple_percent']:>8.1f}% "
            f"{'Yes' if stats['has_tuple_variant'] else 'No':<12} "
            f"{stats['frozenset_percent']:>8.1f}% "
            f"{'Yes' if stats['has_frozenset_variant'] else 'No':<12} "
            f"{meets_threshold:<15}"
        )
        
        print(row)
        
        # Track statistics
        if tuple_meets:
            total_specialization_opportunities += 1
        if frozenset_meets:
            total_specialization_opportunities += 1
            
        if tuple_meets or frozenset_meets:
            functions_meeting_threshold += 1
            
        # Consider a function high impact if it has many calls and high specialization percentage
        if stats['total_calls'] >= 50 and (stats['tuple_percent'] >= 30 or stats['frozenset_percent'] >= 30):
            high_impact_functions += 1
    
    # Print summary
    print(f"\nFound {len(functions_with_variants)} functions with specialized variants")
    print(f"Functions meeting {threshold:.1f}% threshold: {functions_meeting_threshold}")
    print(f"Total specialization opportunities: {total_specialization_opportunities}")
    print(f"High-impact functions with specialization potential: {high_impact_functions}")
    
    # Print recommendations for any high impact functions
    if high_impact_functions > 0:
        print("\n=== Recommendations ===")
        print("Consider prioritizing these high-impact functions for optimization:")
        
        for function_name, stats in sorted_results:
            if stats['total_calls'] >= 100:
                if stats['tuple_percent'] >= 30 and stats['has_tuple_variant']:
                    t_name = stats['tuple_variant']
                    print(f"- Replace {function_name} with {t_name} for tuple arguments (affects {stats['tuple_percent']:.1f}% of calls)")
                
                if stats['frozenset_percent'] >= 30 and stats['has_frozenset_variant']:
                    f_name = stats['frozenset_variant']
                    print(f"- Replace {function_name} with {f_name} for frozenset arguments (affects {stats['frozenset_percent']:.1f}% of calls)")
    
    # Always print a detailed signature analysis
    print("\n=== Detailed Function Signature Analysis ===\n")
    found_perfect_matches = False
    
    for function_name, stats in sorted(results.items(), key=lambda x: x[1]['total_calls'], reverse=True):
        # Lower threshold to 1 call for showing perfect matches
        if stats['total_calls'] >= 1:  # Was 10
            if stats['tuple_percent'] == 100 and stats['has_tuple_variant']:
                print(f"- {function_name}: All {stats['total_calls']} calls use tuple arguments → Use {stats['tuple_variant']}")
                found_perfect_matches = True
            elif stats['frozenset_percent'] == 100 and stats['has_frozenset_variant']:
                print(f"- {function_name}: All {stats['total_calls']} calls use frozenset arguments → Use {stats['frozenset_variant']}")
                found_perfect_matches = True
    
    if not found_perfect_matches:
        print("No functions with 100% specialized variant usage were found.")


def main():
    parser = argparse.ArgumentParser(description="Analyze DSL function specialization opportunities.")
    parser.add_argument("stats_file", nargs="?", default="stats/module_stats.json", 
                        help="JSON file containing the function statistics")
    parser.add_argument("--threshold", type=float, default=1.0,
                        help="Minimum percentage of calls to consider for reporting (default: 1%%)")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Show detailed information about all functions in stats file")
    parser.add_argument("--debug", action="store_true",
                        help="Show debug information")
    args = parser.parse_args()
    
    # Create stats directory if it doesn't exist
    os.makedirs(os.path.dirname(os.path.abspath(args.stats_file)), exist_ok=True)
    
    # Print basic info about the analysis
    print(f"Processing file: {args.stats_file}")
    
    stats = load_stats_file(args.stats_file)
    if not stats:
        print(f"Error: Failed to load statistics from {args.stats_file} or file is empty.")
        return
    
    # Always print basic info about what was loaded
    print(f"Loaded {len(stats)} functions from statistics file.")
    
    if args.debug:
        print("\nFunction names in stats file:")
        for i, func_name in enumerate(stats.keys()):
            if i < 10:  # Just show first 10
                print(f"  - {func_name}")
            else:
                print(f"  - ... and {len(stats) - 10} more")
                break
    
    # Basic analysis of function calls
    print("\n=== Basic Usage Statistics ===")
    print(f"Top functions by call count:")
    for i, (func_name, func_stats) in enumerate(sorted(stats.items(), 
                                                     key=lambda x: x[1].get('calls', 0), 
                                                     reverse=True)[:5]):
        print(f"  {i+1}. {func_name}: {func_stats.get('calls', 0)} calls")
    
    # Specialized variant analysis
    results, all_functions = analyze_function_signatures(stats)
    
    # If verbose mode is enabled, print all functions found in stats file
    if args.verbose:
        print_all_functions(all_functions)
    
    # Always show some information about function variants
    dsl_functions = sum(1 for f in all_functions if f['in_dsl'])
    t_variants = sum(1 for f in all_functions if f['in_dsl'] and hasattr(dsl, f"{f['name']}_t"))
    f_variants = sum(1 for f in all_functions if f['in_dsl'] and hasattr(dsl, f"{f['name']}_f"))
    
    print("\n=== Function Specialization Summary ===")
    print(f"DSL functions in stats: {dsl_functions} out of {len(all_functions)}")
    print(f"Functions with tuple (_t) variants: {t_variants}")
    print(f"Functions with frozenset (_f) variants: {f_variants}")
    
    # Print the typical findings if there are any results
    if results:
        print_findings(results, args.threshold)
        
        # Always print a specialized signature analysis even if empty
        print("\n=== Detailed Function Signature Analysis ===\n")
        found_perfect_matches = False
        
        for function_name, stats in sorted(results.items(), key=lambda x: x[1]['total_calls'], reverse=True):
            if stats['total_calls'] >= 10:  # Only show frequently used functions
                if stats['tuple_percent'] == 100 and stats['has_tuple_variant']:
                    print(f"- {function_name}: All {stats['total_calls']} calls use tuple arguments → Use {stats['tuple_variant']}")
                    found_perfect_matches = True
                elif stats['frozenset_percent'] == 100 and stats['has_frozenset_variant']:
                    print(f"- {function_name}: All {stats['total_calls']} calls use frozenset arguments → Use {stats['frozenset_variant']}")
                    found_perfect_matches = True
        
        if not found_perfect_matches:
            print("No functions with 100% specialized variant usage were found.")
    else:
        print("\n=== Function Specialization Analysis ===")
        print("No specialized function variants could be analyzed from this stats file.")
        print("This could be because:")
        print("1. None of the functions in the stats file have specialized variants (_t or _f)")
        print("2. The functions don't contain sufficient type signature information")
        print("3. The stats file uses a different format than expected")
    
    print("\nAnalysis complete.")

if __name__ == "__main__":
    main()