#!/usr/bin/env python3
"""
Generate Specialized Functions Analysis JSON
============================================

This script analyzes DSL function usage statistics and creates a JSON summary
of specialization opportunities for tuple (_t) and frozenset (_f) variants.

The script identifies instances where a DSL function is always or predominantly called
with a specific data type (tuple or frozenset) and could benefit from using the 
specialized variant of that function. Specialized variants are typically more efficient
as they avoid type checking and can use optimized implementations.

Features:
- Analyzes call statistics to identify specialization opportunities
- Detects what percentage of calls use tuple or frozenset arguments
- Identifies "perfect matches" where 100% of calls use a specific type
- Highlights high-impact functions that are called frequently
- Generates a structured JSON report with the analysis results

Usage:
    python gen_special_dsl.py [stats_file] [--output OUTPUT_FILE]
    python gen_special_dsl.py stats/module_stats.json --threshold 5.0
    
Arguments:
    stats_file:   JSON file containing function call statistics (default: stats/module_stats.json)
    --output:     Output file for the analysis results (default: stats/special_dsl_[input_name].json)
    --threshold:  Minimum percentage of specialized calls to consider for reporting (default: 100%)
    
Output JSON structure:
    - summary: Overview statistics of functions analyzed
    - specialized_functions: List of functions with specialized variants
    - high_impact_opportunities: Functions with high call counts that could benefit
      from specialization
    - perfect_matches: Functions where 100% of calls use a specific type
    - analyzed_functions: Complete list of functions analyzed
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
    """Analyze function call statistics to find specialization opportunities, grouped by call site."""
    results = {}
    all_functions = []
    
    # Iterate through each function in the stats
    for function_name, function_stats in stats_data.items():
        # Record all function names for output
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
        
        # Initialize counters
        tuple_calls = 0
        frozenset_calls = 0
        other_calls = 0
        total_calls = function_stats.get('calls', 0)
        
        # Initialize call site tracking
        call_sites = {}
        
        # Check if there's call_sites information in the new format
        if 'call_sites' in function_stats:
            for site, site_data in function_stats['call_sites'].items():
                call_count = site_data.get('count', 0)
                site_signatures = []
                
                # Extract signatures for this call site
                for sig in site_data.get('signatures', []):
                    if 'type_signature' in sig:
                        signature = sig['type_signature']
                        site_signatures.append(signature)
                        
                        # Parse signature format to determine type
                        if '(' in signature and ')' in signature:
                            arg_str = signature.split('(')[1].split(')')[0]
                            if arg_str:
                                arg_types = [arg.strip() for arg in arg_str.split(',')]
                                if arg_types:
                                    first_arg_type = arg_types[0]
                                    # Count by type
                                    if first_arg_type == 'tuple':
                                        tuple_calls += call_count
                                    elif first_arg_type == 'frozenset':
                                        frozenset_calls += call_count
                                    else:
                                        other_calls += call_count
                
                # Store call site data
                call_sites[site] = {
                    'count': call_count,
                    'code_context': site_data.get('code_context'),
                    'signatures': site_signatures,
                    'tuple_calls': sum(1 for sig in site_signatures if sig.startswith(f"{function_name}(tuple")),
                    'frozenset_calls': sum(1 for sig in site_signatures if sig.startswith(f"{function_name}(frozenset"))
                }
        else:
            # Fall back to old format without call site grouping
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
        
        # If we didn't get any call counts from call sites, use the total
        if tuple_calls + frozenset_calls + other_calls == 0:
            other_calls = total_calls
        
        # The sum of specific calls might not match total_calls if the same function
        # is called with different signatures, so adjust totals
        if tuple_calls + frozenset_calls > total_calls:
            # Normalize to match total calls
            ratio = total_calls / (tuple_calls + frozenset_calls)
            tuple_calls = int(tuple_calls * ratio)
            frozenset_calls = int(frozenset_calls * ratio)
        
        # Calculate match scores for specialized variants
        tuple_match = variants['tuple'] is not None
        frozenset_match = variants['frozenset'] is not None
        
        # Add to results
        results[function_name] = {
            'total_calls': total_calls,
            'tuple_calls': tuple_calls,
            'tuple_percent': (tuple_calls / total_calls * 100) if total_calls > 0 else 0,
            'has_tuple_variant': tuple_match,
            'tuple_variant': variants['tuple'],
            'frozenset_calls': frozenset_calls,
            'frozenset_percent': (frozenset_calls / total_calls * 100) if total_calls > 0 else 0,
            'has_frozenset_variant': frozenset_match,
            'frozenset_variant': variants['frozenset'],
            'other_calls': other_calls,
            'other_percent': (other_calls / total_calls * 100) if total_calls > 0 else 0,
            'call_sites': call_sites
        }
    
    return results, all_functions

def generate_analysis_json(stats_data, threshold=1.0):
    """Generate JSON analysis output data with call site grouping."""
    results, all_functions = analyze_function_signatures(stats_data)
    
    # Build summary data
    dsl_functions = sum(1 for f in all_functions if f['in_dsl'])
    t_variants = sum(1 for f in all_functions if f['in_dsl'] and hasattr(dsl, f"{f['name']}_t"))
    f_variants = sum(1 for f in all_functions if f['in_dsl'] and hasattr(dsl, f"{f['name']}_f"))
    
    # Get functions with specialized variants
    functions_with_variants = []
    for function_name, stats in results.items():
        if stats['has_tuple_variant'] or stats['has_frozenset_variant']:
            result = {
                "name": function_name,
                "total_calls": stats["total_calls"],
                "tuple_percent": stats["tuple_percent"],
                "has_tuple_variant": stats["has_tuple_variant"],
                "frozenset_percent": stats["frozenset_percent"],
                "has_frozenset_variant": stats["has_frozenset_variant"],
                "meets_threshold": (stats["has_tuple_variant"] and stats["tuple_percent"] >= threshold) or 
                                  (stats["has_frozenset_variant"] and stats["frozenset_percent"] >= threshold)
            }
            
            # Add call site information if available
            if stats.get('call_sites'):
                call_sites_info = {}
                for site, site_data in stats['call_sites'].items():
                    site_info = {
                        "count": site_data['count'],
                        "code_context": site_data.get('code_context', ""),
                        "tuple_calls": site_data.get('tuple_calls', 0),
                        "frozenset_calls": site_data.get('frozenset_calls', 0)
                    }
                    call_sites_info[site] = site_info
                result["call_sites"] = call_sites_info
            
            functions_with_variants.append(result)
    
    # Find high-impact opportunities
    high_impact_functions = []
    for function_name, stats in results.items():
        if stats['total_calls'] >= 50:
            if stats['tuple_percent'] >= 30 and stats['has_tuple_variant']:
                result = {
                    "name": function_name,
                    "variant": stats['tuple_variant'],
                    "type": "tuple",
                    "percent": stats['tuple_percent'],
                    "calls": stats['total_calls']
                }
                
                # Add call sites for high-impact functions
                if stats.get('call_sites'):
                    call_sites = {site: {"count": site_data['count'], "code_context": site_data.get('code_context')} 
                                 for site, site_data in stats['call_sites'].items() 
                                 if site_data.get('tuple_calls', 0) > 0}
                    result["call_sites"] = call_sites
                    
                high_impact_functions.append(result)
                
            if stats['frozenset_percent'] >= 30 and stats['has_frozenset_variant']:
                result = {
                    "name": function_name,
                    "variant": stats['frozenset_variant'],
                    "type": "frozenset",
                    "percent": stats['frozenset_percent'],
                    "calls": stats['total_calls']
                }
                
                # Add call sites for high-impact functions
                if stats.get('call_sites'):
                    call_sites = {site: {"count": site_data['count'], "code_context": site_data.get('code_context')} 
                                 for site, site_data in stats['call_sites'].items() 
                                 if site_data.get('frozenset_calls', 0) > 0}
                    result["call_sites"] = call_sites
                    
                high_impact_functions.append(result)
    
    # Find perfect matches (100% specialized variant usage)
    perfect_matches = []
    for function_name, stats in results.items():
        if stats['total_calls'] >= 1:
            if stats['tuple_percent'] == 100 and stats['has_tuple_variant']:
                result = {
                    "name": function_name,
                    "variant": stats['tuple_variant'],
                    "type": "tuple",
                    "calls": stats['total_calls']
                }
                
                # Add call sites for perfect matches
                if stats.get('call_sites'):
                    call_sites = {site: {"count": site_data['count'], "code_context": site_data.get('code_context')} 
                                 for site, site_data in stats['call_sites'].items() 
                                 if site_data.get('tuple_calls', 0) > 0}
                    result["call_sites"] = call_sites
                    
                perfect_matches.append(result)
                
            elif stats['frozenset_percent'] == 100 and stats['has_frozenset_variant']:
                result = {
                    "name": function_name,
                    "variant": stats['frozenset_variant'],
                    "type": "frozenset",
                    "calls": stats['total_calls']
                }
                
                # Add call sites for perfect matches
                if stats.get('call_sites'):
                    call_sites = {site: {"count": site_data['count'], "code_context": site_data.get('code_context')} 
                                 for site, site_data in stats['call_sites'].items() 
                                 if site_data.get('frozenset_calls', 0) > 0}
                    result["call_sites"] = call_sites
                    
                perfect_matches.append(result)
    
    # Build output JSON structure
    analysis_data = {
        "summary": {
            "total_functions": len(all_functions),
            "dsl_functions": dsl_functions,
            "non_dsl_functions": len(all_functions) - dsl_functions,
            "functions_with_t_variants": t_variants,
            "functions_with_f_variants": f_variants,
            "threshold_percent": threshold
        },
        "specialized_functions": functions_with_variants,
        "high_impact_opportunities": high_impact_functions,
        "perfect_matches": perfect_matches,
        "analyzed_functions": [f['name'] for f in all_functions]
    }
    
    return analysis_data

def main():
    parser = argparse.ArgumentParser(description="Generate specialized functions analysis JSON.")
    parser.add_argument("stats_file", nargs="?", default="stats/module_stats.json", 
                        help="JSON file containing the function statistics")
    parser.add_argument("--threshold", type=float, default=100.0,
                        help="Minimum percentage of calls to consider for reporting (default: 100%%)")
    parser.add_argument("--output", type=str, default=None, 
                        help="Output JSON file path (default: stats/special_dsl_analysis.json)")
    args = parser.parse_args()
    
    # Create stats directory if it doesn't exist
    os.makedirs(os.path.dirname(os.path.abspath(args.stats_file)), exist_ok=True)
    
    # Determine output file
    if args.output:
        output_file = args.output
    else:
        # Generate output filename based on input
        base_name = os.path.basename(args.stats_file)
        name_i_without_ext = os.path.splitext(base_name)[0]
        name_o_without_ext = name_i_without_ext.replace("generic_", "special_")
        output_file = f"stats/{name_o_without_ext}.json"
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    print(f"Processing file: {args.stats_file}")
    
    stats = load_stats_file(args.stats_file)
    if not stats:
        print(f"Error: Failed to load statistics from {args.stats_file} or file is empty.")
        return
    
    analysis_data = generate_analysis_json(stats, args.threshold)
    
    # Write results to JSON file
    with open(output_file, 'w') as f:
        json.dump(analysis_data, f, indent=2)
    
    print(f"Analysis complete. Results saved to {output_file}")
    
    # Print summary 
    print(f"\nSummary:")
    print(f"- Total functions analyzed: {analysis_data['summary']['total_functions']}")
    print(f"- DSL functions: {analysis_data['summary']['dsl_functions']}")
    print(f"- Functions with specialized variants: {len(analysis_data['specialized_functions'])}")
    print(f"- High impact opportunities: {len(analysis_data['high_impact_opportunities'])}")
    print(f"- Perfect matches (100% specialized usage): {len(analysis_data['perfect_matches'])}")

if __name__ == "__main__":
    main()