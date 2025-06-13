"""
DSL Function Call Pattern Analyzer

This script analyzes function call patterns across solvers to identify:
- Common function sequences (functions that are often called together)
- Function call chains (where output of one function becomes input for another)
- Type conversion patterns (when data changes types between function calls)
- Specialized optimization opportunities

Usage:
    python analyze_call_patterns.py [directory_with_stats_files]
"""

import os
import sys
import json
from collections import defaultdict, Counter

def load_all_stats(directory='.'):
    """Load all solver stats files from the given directory."""
    stats_files = [f for f in os.listdir(directory) if f.endswith('_dsl_stats.json')]
    
    # Store all signature data
    all_data = {}
    
    # Track function sequences per solver
    function_sequences = defaultdict(list)
    
    for stats_file in stats_files:
        solver_key = stats_file.split('_dsl_stats.json')[0]
        
        with open(os.path.join(directory, stats_file), 'r') as f:
            stats = json.load(f)
        
        # Store stats data
        all_data[solver_key] = stats
        
        # Extract sequence of function calls for this solver
        func_sequence = []
        
        # This assumes the JSON structure has call_sites that include line numbers
        for func_name, func_data in stats.items():
            # Get all call sites and their counts
            call_sites = func_data.get('call_sites', {})
            
            for call_site, count in call_sites.items():
                # Extract line number from call site
                if 'solvers.py:' in call_site:
                    line_num = int(call_site.split(':')[1])
                    func_sequence.append((line_num, func_name, count))
        
        # Sort by line number to get the sequence of calls
        func_sequence.sort()
        function_sequences[solver_key] = func_sequence
    
    return {
        'all_data': all_data,
        'function_sequences': function_sequences
    }

def find_common_sequences(function_sequences, min_length=2, min_occurrences=2):
    """Find common sequences of function calls across solvers."""
    # Extract just the function names from each sequence
    name_sequences = {}
    for solver, sequence in function_sequences.items():
        name_sequences[solver] = [func_name for _, func_name, _ in sequence]
    
    # Find all subsequences of length min_length or greater
    subsequences = defaultdict(list)
    
    for solver, sequence in name_sequences.items():
        # Skip sequences that are too short
        if len(sequence) < min_length:
            continue
            
        # Find all subsequences of sufficient length
        for i in range(len(sequence) - min_length + 1):
            for j in range(i + min_length, len(sequence) + 1):
                subseq = tuple(sequence[i:j])
                subsequences[subseq].append(solver)
    
    # Filter for sequences that occur in multiple solvers
    common_sequences = {
        seq: solvers 
        for seq, solvers in subsequences.items() 
        if len(solvers) >= min_occurrences
    }
    
    return common_sequences

def find_type_conversion_patterns(all_data):
    """Identify patterns where data changes types between function calls."""
    conversion_patterns = []
    
    # Look for functions with mixed input/output types
    for solver_key, stats in all_data.items():
        for func_name, func_data in stats.items():
            # Check if we have both type signatures and return types
            if 'type_signatures' in func_data:
                for type_sig in func_data.get('type_signatures', []):
                    # Extract input types
                    input_types = []
                    if '(' in type_sig and ')' in type_sig:
                        input_part = type_sig[type_sig.find('(')+1:type_sig.rfind(')')]
                        if input_part:
                            input_types = [t.strip() for t in input_part.split(',')]
                    
                    # Look for tuple->frozenset or frozenset->tuple conversions
                    if ('tuple' in input_types and 'frozenset' in func_name) or \
                       ('frozenset' in input_types and 'tuple' in func_name):
                        conversion_patterns.append({
                            'function': func_name,
                            'input_types': input_types,
                            'solver': solver_key,
                            'signature': type_sig
                        })
    
    return conversion_patterns

def analyze_most_used_functions(all_data):
    """Identify the most commonly used DSL functions across all solvers."""
    function_usage = Counter()
    
    for solver_key, stats in all_data.items():
        for func_name, func_data in stats.items():
            # Add up the call counts
            calls = func_data.get('calls', 0)
            if isinstance(calls, int):
                function_usage[func_name] += calls
    
    return function_usage

def find_specialization_candidates(all_data):
    """Find functions that would benefit from specialized implementations."""
    candidates = {}
    
    for solver_key, stats in all_data.items():
        for func_name, func_data in stats.items():
            # Check if function has multiple type signatures
            type_signatures = func_data.get('type_signatures', [])
            
            if len(type_signatures) > 1:
                # This function is called with multiple signatures in this solver
                if func_name not in candidates:
                    candidates[func_name] = {
                        'type_signatures': set(),
                        'solvers': set(),
                        'call_count': 0
                    }
                
                # Add the signatures and solver
                candidates[func_name]['type_signatures'].update(type_signatures)
                candidates[func_name]['solvers'].add(solver_key)
                candidates[func_name]['call_count'] += func_data.get('calls', 0)
    
    # Convert to regular dict for JSON serialization
    result = {}
    for func_name, data in candidates.items():
        result[func_name] = {
            'type_signatures': list(data['type_signatures']),
            'solvers': list(data['solvers']),
            'call_count': data['call_count'],
            'num_signatures': len(data['type_signatures']),
            'num_solvers': len(data['solvers'])
        }
    
    return result

def print_analysis_results(data):
    """Print analysis results in a readable format."""
    # Print common function sequences
    common_sequences = find_common_sequences(data['function_sequences'])
    print("\n=== Common Function Sequences ===")
    for i, (sequence, solvers) in enumerate(
        sorted(common_sequences.items(), key=lambda x: len(x[1]), reverse=True)[:10]
    ):
        print(f"\nSequence #{i+1} (used in {len(solvers)} solvers):")
        print(f"  {' → '.join(sequence)}")
        print(f"  Used in: {', '.join(solvers[:5])}{' and more' if len(solvers) > 5 else ''}")
    
    # Print type conversion patterns
    conversion_patterns = find_type_conversion_patterns(data['all_data'])
    print("\n=== Type Conversion Patterns ===")
    for pattern in conversion_patterns[:10]:
        print(f"\n{pattern['function']} in {pattern['solver']}:")
        print(f"  {pattern['signature']}")
    
    # Print most used functions
    function_usage = analyze_most_used_functions(data['all_data'])
    print("\n=== Most Used DSL Functions ===")
    for func, count in function_usage.most_common(20):
        print(f"  {func}: {count} total calls")
    
    # Print specialization candidates
    candidates = find_specialization_candidates(data['all_data'])
    print("\n=== Functions That Would Benefit From Specialization ===")
    for func, info in sorted(candidates.items(), 
                            key=lambda x: (x[1]['num_signatures'], x[1]['call_count']), 
                            reverse=True)[:10]:
        print(f"\n{func} ({info['call_count']} calls, {info['num_signatures']} signatures):")
        for sig in info['type_signatures'][:3]:
            print(f"  {sig}")
        if len(info['type_signatures']) > 3:
            print(f"  ... and {len(info['type_signatures']) - 3} more")
        print(f"  Used in {len(info['solvers'])} solvers")

def main():
    """Main function to process command line arguments and run analysis."""
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    print(f"Loading solver stats from {directory}...")
    data = load_all_stats(directory)
    
    print(f"Analyzing call patterns across {len(data['all_data'])} solvers...")
    print_analysis_results(data)

if __name__ == "__main__":
    main()