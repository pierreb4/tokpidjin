"""
DSL Function Signature Analysis

This script analyzes the call signatures of DSL functions across all solvers
to identify patterns and potential optimization opportunities based on argument types.

Usage:
    python analyze_signatures.py [directory_with_stats_files]
"""

import os
import json
import sys
from collections import defaultdict

def load_all_solver_stats(directory='.'):
    """Load all solver stats files with enhanced signature support."""
    stats_files = [f for f in os.listdir(directory) if f.endswith('_dsl_stats.json')]
    
    all_signatures = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    
    for stats_file in stats_files:
        solver_key = stats_file.split('_dsl_stats.json')[0]
        
        with open(os.path.join(directory, stats_file), 'r') as f:
            stats = json.load(f)
            
        for func_name, func_data in stats.items():
            type_signatures = func_data.get('type_signatures', [])
            value_signatures = func_data.get('value_signatures', [])
            
            # Store both signature types
            for type_sig in type_signatures:
                if type_sig not in all_signatures[func_name][solver_key]["type_signatures"]:
                    all_signatures[func_name][solver_key]["type_signatures"].append(type_sig)
                    
            for value_sig in value_signatures:
                if value_sig not in all_signatures[func_name][solver_key]["value_signatures"]:
                    all_signatures[func_name][solver_key]["value_signatures"].append(value_sig)
    
    return all_signatures

def analyze_signature_patterns(all_signatures):
    """Analyze signature patterns with enhanced signature data."""
    # Functions with multiple distinct type signatures
    multi_sig_funcs = {}
    
    # Functions with consistent type signatures
    consistent_sig_funcs = {}
    
    # Functions with mixed argument types
    mixed_type_funcs = {}
    
    # Functions with unusual value patterns
    value_pattern_funcs = {}
    
    for func_name, solver_signatures in all_signatures.items():
        # Get all type signatures across solvers
        all_type_sigs = []
        for solver_key, sig_types in solver_signatures.items():
            all_type_sigs.extend(sig_types["type_signatures"])
        
        # Get unique signatures
        unique_sigs = list(set(all_type_sigs))
        
        # Multiple distinct signatures
        if len(unique_sigs) > 1:
            multi_sig_funcs[func_name] = unique_sigs
        
        # Consistent signatures
        if len(unique_sigs) == 1:
            consistent_sig_funcs[func_name] = unique_sigs[0]
        
        # Check for mixed arg types
        for sig in unique_sigs:
            if ('tuple' in sig and 'frozenset' in sig) or \
               any(sig.count(type_name) > 1 for type_name in ['tuple', 'frozenset', 'int', 'list']):
                if func_name not in mixed_type_funcs:
                    mixed_type_funcs[func_name] = []
                mixed_type_funcs[func_name].append(sig)
        
        # Analyze value patterns
        value_patterns = []
        for solver_key, sig_types in solver_signatures.items():
            for value_sig in sig_types["value_signatures"]:
                # Look for interesting patterns like nested collections
                if ('frozenset(' in value_sig and 'frozenset(' in value_sig[value_sig.find('frozenset(')+9:]) or \
                   ('tuple(' in value_sig and 'tuple(' in value_sig[value_sig.find('tuple(')+6:]):
                    value_patterns.append(value_sig)
        
        if value_patterns:
            value_pattern_funcs[func_name] = value_patterns
    
    return {
        'multi_sig_funcs': multi_sig_funcs,
        'consistent_sig_funcs': consistent_sig_funcs,
        'mixed_type_funcs': mixed_type_funcs,
        'value_pattern_funcs': value_pattern_funcs
    }

def print_analysis(analysis):
    """Print the enhanced signature analysis."""
    # Print functions with multiple signatures
    print("\n=== Functions with Multiple Type Signatures ===")
    for func, sigs in sorted(analysis['multi_sig_funcs'].items(), key=lambda x: len(x[1]), reverse=True):
        print(f"\n{func} ({len(sigs)} signatures):")
        for sig in sigs[:5]:
            print(f"  {sig}")
        if len(sigs) > 5:
            print(f"  ... and {len(sigs) - 5} more")
    
    # Print functions with mixed argument types
    print("\n=== Functions with Mixed Argument Types ===")
    for func, sigs in sorted(analysis['mixed_type_funcs'].items()):
        print(f"\n{func}:")
        for sig in sigs[:5]:
            print(f"  {sig}")
    
    # Print functions with interesting value patterns
    print("\n=== Functions with Complex Value Patterns ===")
    for func, values in sorted(analysis['value_pattern_funcs'].items()):
        print(f"\n{func}:")
        for val in values[:3]:
            print(f"  {val}")
        if len(values) > 3:
            print(f"  ... and {len(values) - 3} more")
    
    # Print most consistent functions
    print("\n=== Functions with Consistent Signatures ===")
    for func, sig in sorted(analysis['consistent_sig_funcs'].items()):
        print(f"  {func}: {sig}")

def main():
    """Main function to process command line arguments and display results."""
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    print(f"Loading solver stats from {directory}...")
    all_signatures = load_all_solver_stats(directory)
    
    print(f"Analyzing signature patterns across {len(all_signatures)} DSL functions...")
    analysis = analyze_signature_patterns(all_signatures)
    
    print_analysis(analysis)

if __name__ == "__main__":
    main()