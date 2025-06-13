"""
Mixed Type Function Extractor

This script analyzes function call statistics from a JSON file to identify
functions that are called with both tuple and frozenset argument types.
These mixed-type functions are good candidates for specialized implementations.

Usage:
    python extract_mixed_type.py path/to/module_stats.json
"""

import json
import sys

def extract_mixed_type_functions(stats_file):
    """
    Extract functions that are called with both tuple and frozenset arguments.
    
    Args:
        stats_file (str): Path to the JSON statistics file
        
    Returns:
        dict: Dictionary mapping function names to their call site argument type data,
              containing only functions that use both tuple and frozenset types
    """
    # Load the JSON data
    with open(stats_file, 'r') as f:
        stats = json.load(f)
    
    # Store functions with mixed types
    mixed_type_functions = {}
    
    # Iterate through all functions in the stats
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
            for arg_type_str in type_counts.keys():
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

def main():
    """
    Parse command line arguments and print mixed type functions in a readable format.
    """
    if len(sys.argv) != 2:
        print("Usage: python script.py path/to/module_stats.json")
        return
    
    stats_file = sys.argv[1]
    mixed_functions = extract_mixed_type_functions(stats_file)
    
    # Print the results in a readable format
    if mixed_functions:
        print(f"Found {len(mixed_functions)} functions with mixed tuple and frozenset types:")
        for func_name, call_sites in mixed_functions.items():
            print(f"\n{func_name}:")
            for call_site, type_counts in call_sites.items():
                print(f"  {call_site}:")
                for arg_type, count in type_counts.items():
                    print(f"    {arg_type}: {count}")
    else:
        print("No functions with mixed tuple and frozenset types found.")

if __name__ == "__main__":
    main()