"""
DSL Function Signature Validation Tool

This tool checks if a solver's function call chain is valid by analyzing each
function's expected signature and verifying that arguments are passed correctly.
Helps detect type errors, missing arguments, or incorrect function composition.

Usage:
    python check_solver.py <solver_key>
"""

import os
import sys
import inspect
import importlib
from collections import defaultdict

import dsl
import solvers
from grid import print_grid

def get_data(solver_key):
    """Load sample input data for the solver."""
    path = f'../data/training'
    for fn in os.listdir(path):
        if solver_key in fn:
            with open(f'{path}/{fn}') as f:
                data = json.load(f)
                # Convert to tuples
                ast = lambda g: tuple(tuple(r) for r in g)
                examples = [{
                    'input': ast(e['input']),
                    'output': ast(e['output']),
                } for e in data['train']]
                
                return examples[0]['input'] if examples else None
    return None

def analyze_function_chain(solver_key):
    """Analyze the function chain in a solver to identify parameter mismatch issues."""
    # Get the solver function
    solver_name = f'solve_{solver_key}'
    if not hasattr(solvers, solver_name):
        print(f"Error: No solver function found for '{solver_key}'")
        return
    
    solver_func = getattr(solvers, solver_name)
    solver_source = inspect.getsource(solver_func)
    
    print(f"Analyzing solver: {solver_name}")
    print("\nDefinition:")
    print(solver_source)
    
    # Extract the sequence of variable assignments
    lines = solver_source.strip().split('\n')
    assignments = []
    
    for line in lines[1:-2]:  # Skip function def and return line
        if '=' in line:
            line = line.strip()
            var, expr = line.split(' = ', 1)
            assignments.append((var, expr))
    
    # Track variables and their types/sources
    var_info = {}
    
    # Load a sample input if available
    sample_input = get_data(solver_key)
    if sample_input:
        var_info['I'] = {
            'value': sample_input,
            'type': type(sample_input).__name__,
            'source': 'input'
        }
    else:
        var_info['I'] = {
            'type': 'tuple',
            'source': 'input'
        }
    
    # Extract function call info
    function_issues = []
    
    for var, expr in assignments:
        # Extract function name and arguments
        if '(' in expr and ')' in expr:
            func_name = expr.split('(')[0]
            args_str = expr[len(func_name)+1:-1]
            args = [arg.strip() for arg in args_str.split(',')] if args_str else []
            
            # Check if this is a DSL function
            if hasattr(dsl, func_name):
                dsl_func = getattr(dsl, func_name)
                signature = inspect.signature(dsl_func)
                param_names = list(signature.parameters.keys())
                
                # Check parameter count
                if len(args) != len(param_names):
                    function_issues.append({
                        'variable': var,
                        'function': func_name,
                        'issue': f"Expected {len(param_names)} arguments ({', '.join(param_names)}), got {len(args)} ({', '.join(args)})",
                        'severity': 'high' if abs(len(args) - len(param_names)) > 0 else 'warning'
                    })
                
                # Track variable information
                var_info[var] = {
                    'type': 'unknown',  # We don't know the return type yet
                    'source': f"call to {func_name}({', '.join(args)})"
                }
                
                # Check if all arguments are defined variables
                for arg in args:
                    if arg not in var_info and not arg.isdigit() and arg not in dir(dsl):
                        function_issues.append({
                            'variable': var,
                            'function': func_name,
                            'issue': f"Argument '{arg}' is not defined before use",
                            'severity': 'high'
                        })
            
            # Check if this is a variable that was defined earlier
            elif func_name in var_info:
                var_info[var] = {
                    'type': 'unknown',
                    'source': f"call to variable {func_name}({', '.join(args)})"
                }
            
            # Otherwise it might be a constant or something else
            else:
                var_info[var] = {
                    'type': 'unknown',
                    'source': f"call to {func_name}({', '.join(args)})"
                }
    
    # Now check the track functions that require special attention
    for var, expr in assignments:
        # Special cases for functions that create or compose functions
        if 'fork(' in expr:
            # Extract outer and inner function names
            args_str = expr[5:-1]  # Remove 'fork(' and ')'
            args = [arg.strip() for arg in args_str.split(',')]
            
            # Check if we have the right number of args for fork
            if len(args) != 3:
                function_issues.append({
                    'variable': var,
                    'function': 'fork',
                    'issue': f"fork expects 3 arguments (outer, a, b), got {len(args)}",
                    'severity': 'high'
                })
            else:
                # Check if each argument is a valid function
                for i, arg in enumerate(['outer', 'a', 'b']):
                    if i < len(args) and not (hasattr(dsl, args[i]) or args[i] in var_info):
                        function_issues.append({
                            'variable': var,
                            'function': 'fork',
                            'issue': f"{arg} argument '{args[i]}' is not a recognized function",
                            'severity': 'medium'
                        })
        
        elif 'compose(' in expr:
            # Extract outer and inner function names
            args_str = expr[8:-1]  # Remove 'compose(' and ')'
            args = [arg.strip() for arg in args_str.split(',')]
            
            # Check if we have the right number of args for compose
            if len(args) != 2:
                function_issues.append({
                    'variable': var,
                    'function': 'compose',
                    'issue': f"compose expects 2 arguments (outer, inner), got {len(args)}",
                    'severity': 'high'
                })
            else:
                # Check if each argument is a valid function
                for i, arg in enumerate(['outer', 'inner']):
                    if i < len(args) and not (hasattr(dsl, args[i]) or args[i] in var_info):
                        function_issues.append({
                            'variable': var,
                            'function': 'compose',
                            'issue': f"{arg} argument '{args[i]}' is not a recognized function",
                            'severity': 'medium'
                        })
        
        # Check special case when a function expect a function but gets data
        if 'mapply(' in expr:
            args_str = expr[7:-1]  # Remove 'mapply(' and ')'
            args = [arg.strip() for arg in args_str.split(',')]
            
            if len(args) == 2:
                # First argument to mapply should be a function
                if args[0] in var_info:
                    # Check if the argument comes from fork, compose, etc.
                    source = var_info[args[0]].get('source', '')
                    if not any(fn in source for fn in ['fork', 'compose', 'rbind', 'lbind', 'power']):
                        function_issues.append({
                            'variable': var,
                            'function': 'mapply',
                            'issue': f"First argument to mapply '{args[0]}' may not be a function: {source}",
                            'severity': 'medium'
                        })
    
    # Print the analysis results
    if function_issues:
        print("\n⚠️ Potential issues found:")
        for issue in function_issues:
            severity_marker = "❌" if issue['severity'] == 'high' else "⚠️"
            print(f"{severity_marker} {issue['variable']} = {issue['function']}(...): {issue['issue']}")
    else:
        print("\n✅ No obvious function signature issues found")
    
    # Print the variable chain for debugging
    print("\nVariable chain:")
    for var, info in var_info.items():
        print(f"  {var}: {info.get('source', 'unknown')}")
    
    return function_issues

def main():
    if len(sys.argv) != 2:
        print("Usage: python check_solver.py <solver_key>")
        print("Example: python check_solver.py d037b0a7")
        return
    
    solver_key = sys.argv[1]
    analyze_function_chain(solver_key)

if __name__ == "__main__":
    import json  # needed for get_data
    main()