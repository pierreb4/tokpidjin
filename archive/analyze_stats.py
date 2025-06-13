"""
Module Statistics Analysis Tool

This script analyzes function call statistics collected from modules
to identify optimization opportunities and type usage patterns.

It provides insights about:
- Functions that accept both tuple and frozenset arguments
- Functions with high execution times that could benefit from optimization
- Functions with inconsistent argument types
- Call sites with mixed argument types

Usage:
    python analyze_stats.py path/to/module_stats.json
"""

import json
import sys
from collections import defaultdict
from typing import Dict, List, Set, Tuple, Any

def load_stats(filename: str) -> Dict:
    """
    Load the statistics from a JSON file.
    
    Args:
        filename: Path to the JSON statistics file
        
    Returns:
        Dict containing the parsed statistics data
    """
    with open(filename, 'r') as f:
        return json.load(f)

def find_mixed_type_functions(stats: Dict) -> Dict:
    """
    Find functions that are called with both tuple and frozenset arguments.
    
    Args:
        stats: Dictionary containing the function statistics
        
    Returns:
        Dictionary of function names mapped to their call site argument type data,
        containing only functions that use both tuple and frozenset types
    """
    mixed_type_functions = {}
    
    for func_name, func_data in stats.items():
        # Check if call_site_arg_types exists
        if "call_site_arg_types" not in func_data:
            continue
        
        # Track if this function has both tuple and frozenset types
        has_tuple = False
        has_frozenset = False
        
        # Check each call site
        for call_site, type_counts in func_data["call_site_arg_types"].items():
            # Check each arg type signature at this call site
            for arg_type_str, count in type_counts.items():
                if "'tuple'" in arg_type_str:
                    has_tuple = True
                if "'frozenset'" in arg_type_str:
                    has_frozenset = True
                
                # If we've found both types, we can break early
                if has_tuple and has_frozenset:
                    break
            
            # If we've found both types, we can break early
            if has_tuple and has_frozenset:
                break
        
        # If this function has both types, add it to our results
        if has_tuple and has_frozenset:
            mixed_type_functions[func_name] = func_data["call_site_arg_types"]
    
    return mixed_type_functions

def find_optimization_opportunities(stats: Dict) -> List[Dict]:
    """
    Find functions that might benefit from optimization.
    
    Args:
        stats: Dictionary containing the function statistics
        
    Returns:
        List of dictionaries describing optimization opportunities:
        - high_execution_time: Functions that take a long time to execute
        - inconsistent_arg_types: Functions that receive different types for the same parameter
    """
    opportunities = []
    
    for func_name, func_data in stats.items():
        if func_data['calls'] < 100:  # Skip rarely called functions
            continue
            
        # Check for high execution time
        avg_time = func_data['execution_time'] / func_data['calls'] if func_data['calls'] > 0 else 0
        if avg_time > 0.0001:  # Arbitrary threshold
            opportunities.append({
                'function': func_name,
                'reason': 'high_execution_time',
                'calls': func_data['calls'],
                'avg_time': avg_time
            })
            
        # Check for inconsistent argument types
        if "arg_types" in func_data:
            # Look for parameters that receive multiple types
            param_types = defaultdict(set)
            for key, count in func_data["arg_types"].items():
                if isinstance(key, tuple) and len(key) >= 2:
                    param, type_name = key[0], key[1]
                    param_types[param].add(type_name)
                else:
                    print(f"Unexpected key format in arg_types: {key}")
                
            for param, types in param_types.items():
                if len(types) > 1:
                    opportunities.append({
                        'function': func_name,
                        'reason': 'inconsistent_arg_types',
                        'parameter': param,
                        'types': list(types)
                    })
    
    return opportunities

def analyze_call_sites(stats: Dict) -> Dict:
    """
    Analyze call sites to find common patterns.
    
    Args:
        stats: Dictionary containing the function statistics
        
    Returns:
        Dictionary mapping function names to analysis results:
        - top_call_sites: Most frequent call sites
        - call_sites_with_mixed_types: Call sites with multiple argument types for the same parameter
    """
    results = {}
    
    for func_name, func_data in stats.items():
        if 'call_sites' not in func_data:
            continue
            
        # Find the most common call sites
        call_sites = sorted(
            func_data['call_sites'].items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]  # Top 10 call sites
        
        # Check if any call site has multiple arg types
        call_sites_with_mixed_types = []
        if 'call_site_arg_types' in func_data:
            for call_site, type_counts in func_data['call_site_arg_types'].items():
                params_with_multiple_types = defaultdict(set)
                for arg_type_str, count in type_counts.items():
                    # Extract the parameter name from the arg_type_str
                    try:
                        param = arg_type_str.split("'")[1]
                        type_name = arg_type_str.split("'")[3]
                        params_with_multiple_types[param].add(type_name)
                    except:
                        continue
                
                # Find parameters with multiple types
                mixed_types = {
                    param: list(types)
                    for param, types in params_with_multiple_types.items()
                    if len(types) > 1
                }
                
                if mixed_types:
                    call_sites_with_mixed_types.append({
                        'call_site': call_site,
                        'mixed_types': mixed_types
                    })
        
        results[func_name] = {
            'top_call_sites': call_sites,
            'call_sites_with_mixed_types': call_sites_with_mixed_types
        }
    
    return results

def main():
    """
    Main function to parse command line arguments and run analysis.
    Prints the analysis results in a readable format.
    """
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} path/to/module_stats.json")
        return
    
    stats_file = sys.argv[1]
    stats = load_stats(stats_file)
    
    # Find functions with mixed tuple and frozenset arguments
    mixed_functions = find_mixed_type_functions(stats)
    if mixed_functions:
        print(f"\n=== Functions with mixed tuple and frozenset types ({len(mixed_functions)}) ===")
        for func_name, call_sites in mixed_functions.items():
            print(f"\n{func_name}:")
            for call_site, type_counts in list(call_sites.items())[:3]:  # Show up to 3 call sites
                print(f"  {call_site}:")
                for arg_type, count in type_counts.items():
                    print(f"    {arg_type}: {count}")
    
    # Find optimization opportunities
    opportunities = find_optimization_opportunities(stats)
    if opportunities:
        print(f"\n=== Optimization Opportunities ({len(opportunities)}) ===")
        for opp in opportunities:
            if opp['reason'] == 'high_execution_time':
                print(f"\n{opp['function']}: High execution time")
                print(f"  {opp['calls']} calls, avg time: {opp['avg_time']:.6f}s")
            elif opp['reason'] == 'inconsistent_arg_types':
                print(f"\n{opp['function']}: Inconsistent argument types")
                print(f"  Parameter '{opp['parameter']}' receives types: {', '.join(opp['types'])}")
    
    # Analyze call sites
    call_site_analysis = analyze_call_sites(stats)
    
    # Show functions that might benefit from specialized variants
    print("\n=== Functions that might benefit from specialized variants ===")
    for func_name, analysis in call_site_analysis.items():
        if analysis['call_sites_with_mixed_types']:
            print(f"\n{func_name}:")
            for site_info in analysis['call_sites_with_mixed_types'][:3]:  # Top 3
                print(f"  {site_info['call_site']}:")
                for param, types in site_info['mixed_types'].items():
                    print(f"    {param}: {', '.join(types)}")

if __name__ == "__main__":
    main()