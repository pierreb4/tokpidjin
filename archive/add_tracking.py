"""
Add tracking to all solver and DSL functions to record calls between modules.

This script directly patches functions in both solvers.py and dsl.py to track
inter-module function calls. Run this before running main.py.
"""
import inspect
import importlib
import sys
import functools
import os
from collections import defaultdict
import json

# Stats storage for direct function calls
call_stats = defaultdict(lambda: defaultdict(int))

def log_call(func_name, caller_file, caller_line):
    """Log a function call with caller information."""
    caller_location = f"{caller_file}:{caller_line}"
    call_stats[func_name][caller_location] += 1

def track_call(func):
    """Decorator to track function calls with caller information."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Get caller frame
        frame = inspect.currentframe().f_back
        try:
            caller_file = os.path.basename(frame.f_code.co_filename)
            caller_line = frame.f_lineno
            # Log this call
            log_call(func.__name__, caller_file, caller_line)
        except:
            pass
        finally:
            # Clean up frame reference
            del frame
        
        # Call the original function
        return func(*args, **kwargs)
    
    return wrapper

def patch_all_modules():
    """Patch both solvers.py and dsl.py to track function calls."""
    # Import modules to patch
    import dsl
    import solvers
    
    # Patch all functions in dsl
    dsl_functions = inspect.getmembers(dsl, inspect.isfunction)
    for name, func in dsl_functions:
        if func.__module__ == dsl.__name__:
            setattr(dsl, name, track_call(func))
    
    # Patch all functions in solvers
    solver_functions = inspect.getmembers(solvers, inspect.isfunction)
    for name, func in solver_functions:
        if func.__module__ == solvers.__name__:
            setattr(solvers, name, track_call(func))
    
    print(f"Patched {len(dsl_functions)} DSL functions and {len(solver_functions)} solver functions")

def export_stats(filename="direct_calls.json"):
    """Export the call statistics to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(call_stats, f, indent=2)
    print(f"Call statistics exported to {filename}")

def analyze_calls():
    """Analyze and print solver-to-dsl call statistics."""
    solver_to_dsl = defaultdict(list)
    
    # Find DSL functions called from solvers
    for func_name, call_sites in call_stats.items():
        # Skip if this is a solver function
        if func_name.startswith('solve_'):
            continue
        
        # Check each call site
        for call_site, count in call_sites.items():
            if 'solvers.py:' in call_site:
                # Extract the line number
                line_num = int(call_site.split(':')[1])
                
                # Find which solver this call came from
                solver_found = False
                for solver_name in call_stats:
                    if solver_name.startswith('solve_'):
                        solver_call_sites = call_stats[solver_name]
                        # Check if any solver call sites are near this line
                        for solver_site in solver_call_sites:
                            if 'solvers.py:' in solver_site:
                                solver_line = int(solver_site.split(':')[1])
                                # If within a few lines, likely the same solver
                                if abs(solver_line - line_num) < 20:
                                    solver_to_dsl[solver_name].append({
                                        'dsl_function': func_name,
                                        'call_site': call_site,
                                        'count': count
                                    })
                                    solver_found = True
                                    break
                        if solver_found:
                            break
                
                # If we couldn't find a matching solver, record as unknown
                if not solver_found:
                    solver_to_dsl[f"unknown_solver_at_line_{line_num}"].append({
                        'dsl_function': func_name,
                        'call_site': call_site,
                        'count': count
                    })
    
    # Print results
    print("\n=== DSL Functions Called By Solvers ===")
    for solver_name, calls in sorted(solver_to_dsl.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"\n{solver_name}: uses {len(calls)} DSL functions")
        # Group by DSL function
        by_func = defaultdict(int)
        for call in calls:
            by_func[call['dsl_function']] += call['count']
        
        # Print used functions
        for func, count in sorted(by_func.items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"  {func}: {count} calls")
    
    return solver_to_dsl

if __name__ == "__main__":
    # Patch modules
    patch_all_modules()
    
    # Run a solver to test
    import solvers
    from grid import print_grid
    
    # Create a simple test grid
    test_grid = (
        (0, 0, 0),
        (0, 1, 0),
        (0, 0, 0)
    )
    
    # Run a simple solver function
    print("Running test solver...")
    result = solvers.solve_67a3c6ac(test_grid)
    print_grid(result)
    
    # Export and analyze stats
    export_stats()
    analyze_calls()