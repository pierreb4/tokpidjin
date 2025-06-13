"""
Track Solver-to-DSL Function Call Analyzer

This script directly executes selected solver functions with input examples and
traces which DSL functions they call. It provides a direct approach to understand
the relationship between solver implementations and their DSL function usage.

Key features:
- Executes solvers with real input data from the ARC dataset
- Records all DSL function calls and their signatures
- Captures both parameter types and actual values
- Continues tracking even if a solver crashes
- Exports statistics in a format compatible with other analysis tools

Usage:
    python track_solver.py <solver_key> [--quiet]
    
Examples:
    python track_solver.py 67a3c6ac           # Full analysis with grid display
    python track_solver.py a65b410d --quiet   # Suppresses grid printing
"""

import importlib
import inspect
import sys
import os
import json
import time
import functools
from collections import defaultdict
import argparse

# Import necessary modules
import dsl
import solvers_pre
import solvers_evo
from grid import print_grid

# Global trackers
call_stack = []
function_calls = defaultdict(int)
solver_to_dsl_calls = defaultdict(lambda: defaultdict(int))
call_signatures = defaultdict(lambda: defaultdict(list))

def get_data(train=True, key=None):
    """Load ARC task data, optionally filtering by key."""
    path = f'../data/{"training" if train else "evaluation"}'
    data = {}
    for fn in os.listdir(path):
        task_key = fn.rstrip('.json')
        if key is None or task_key == key:
            with open(f'{path}/{fn}') as f:
                data[task_key] = json.load(f)
    
    # Convert to tuples
    ast = lambda g: tuple(tuple(r) for r in g)
    return {
        'train': {k: [{
            'input': ast(e['input']),
            'output': ast(e['output']),
        } for e in v['train']] for k, v in data.items()},
        'test': {k: [{
            'input': ast(e['input']),
            'output': ast(e['output']),
        } for e in v['test']] for k, v in data.items()}
    }

def trace_function(func):
    """Decorator to trace function calls with detailed signature information."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Get the caller and function name
        func_name = func.__name__
        func_module = func.__module__.split('.')[-1]
        
        # Store original function's argument count for rbind
        wrapper._original_argcount = func.__code__.co_argcount
        
        # Check if we're in a solver context and get the call site
        current_solver = None
        call_site = None
        for frame_info in inspect.stack():
            if frame_info.function.startswith('solve_') and 'solvers.py' in frame_info.filename:
                current_solver = frame_info.function
                # Store the direct caller location
                if call_site is None:
                    call_site = f"{os.path.basename(frame_info.filename)}:{frame_info.lineno}"
                    # Get a snippet of the calling code for context
                    code_context = frame_info.code_context[0].strip() if frame_info.code_context else "unknown"
                break
        
        # Record the call
        function_calls[f"{func_module}.{func_name}"] += 1
        
        # If this is a DSL function called by a solver, record that relationship
        if func_module == 'dsl' and current_solver:
            solver_to_dsl_calls[current_solver][func_name] += 1
            
            # Record type signature
            arg_types = [f"{type(arg).__name__}" for arg in args]
            type_signature = f"{func_name}({', '.join(arg_types)})"
            
            # Record value signature with safe string representations
            arg_values = []
            for arg in args:
                if isinstance(arg, (tuple, frozenset)) and len(arg) > 5:
                    # Truncate large collections
                    value_str = f"{type(arg).__name__}(len={len(arg)})"
                else:
                    # For small collections or primitives, use full repr
                    try:
                        value_str = repr(arg)[:50]  # Limit length
                    except:
                        value_str = f"{type(arg).__name__}(...)"
                arg_values.append(value_str)
            
            value_signature = f"{func_name}({', '.join(arg_values)})"
            
            # Store both signatures with call site information
            signatures = {
                "type_signature": type_signature,
                "value_signature": value_signature,
                "call_site": call_site or f"solvers.py:{current_solver}",
                "code_context": code_context if 'code_context' in locals() else None
            }
            
            # Add to signatures if not already present
            if signatures not in call_signatures[current_solver][func_name]:
                call_signatures[current_solver][func_name].append(signatures)
        
        # Call function
        result = func(*args, **kwargs)
        
        return result
    
    # Store original function's argument count as an attribute
    wrapper._original_argcount = func.__code__.co_argcount
    
    return wrapper

def patch_module(module):
    """Patch all functions in a module with the tracing decorator."""
    # Find all functions
    functions = inspect.getmembers(module, inspect.isfunction)

    # Apply decorator to each function
    for name, func in functions:
        if func.__module__ == module.__name__:
            # Create a decorated version of the function
            decorated_func = trace_function(func)
            
            # Update the module's attribute with the decorated function
            setattr(module, name, decorated_func)
    
    return module

# Add this function to export data in the trace_solver_calls compatible format
def export_solver_stats(solver_name, filename="stats/solver_dsl_stats.json", error_info=None):
    """
    Export the tracked DSL function calls with detailed signatures, grouped by call site.
    
    Args:
        solver_name: Name of the solver function
        filename: Path to save the statistics JSON file
        error_info: Optional error information to include in the output
    """
    stats_data = {}
    
    # Add error information if provided
    if error_info:
        stats_data["error"] = error_info
    
    # For each DSL function we've tracked
    for dsl_func, count in solver_to_dsl_calls[solver_name].items():
        # Get call signatures for this function
        signatures = call_signatures[solver_name].get(dsl_func, [])
        
        # Organize signatures by call site
        call_sites = defaultdict(lambda: {"count": 0, "signatures": [], "code_context": None})
        
        for sig in signatures:
            call_site = sig.get("call_site", f"solvers.py:{solver_name}")
            call_sites[call_site]["count"] += 1
            call_sites[call_site]["signatures"].append({
                "type_signature": sig["type_signature"],
                "value_signature": sig["value_signature"]
            })
            # Save code context if available
            if sig.get("code_context") and not call_sites[call_site]["code_context"]:
                call_sites[call_site]["code_context"] = sig["code_context"]
        
        # Deduplicate signatures within each call site
        for site, site_data in call_sites.items():
            unique_signatures = []
            seen = set()
            
            for sig in site_data["signatures"]:
                sig_tuple = (sig["type_signature"], sig["value_signature"])
                if sig_tuple not in seen:
                    seen.add(sig_tuple)
                    unique_signatures.append(sig)
            
            site_data["signatures"] = unique_signatures
        
        # Create the function entry in stats_data
        stats_data[dsl_func] = {
            "calls": count,
            "execution_time": 0.0,
            "call_sites": dict(call_sites),
            "type_signatures": list({sig["type_signature"] for site_data in call_sites.values() for sig in site_data["signatures"]}),
            "value_signatures": list({sig["value_signature"] for site_data in call_sites.values() for sig in site_data["signatures"]})
        }
    
    # Create stats directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Save to file
    with open(filename, 'w') as f:
        json.dump(stats_data, f, indent=2)
    
    print(f"Solver-to-DSL call statistics exported to {filename}")
    return stats_data


def track_solver(solver_key, quiet=False):
    """Track the execution of a specific solver."""
    # Load the task data for this solver
    data = get_data(train=True, key=solver_key)
    
    # Skip if key not found
    if solver_key not in data['train']:
        print(f"Error: No data found for task key '{solver_key}'")
        return
    
    # Get the solver function
    solver_name = f'solve_{solver_key}'
    if not hasattr(solvers, solver_name):
        print(f"Error: No solver function found for '{solver_key}'")
        return
    
    solver_func = getattr(solvers, solver_name)
    
    # Load the examples
    examples = data['train'][solver_key] + data['test'][solver_key]
    
    # Print solver information
    print(f"Analyzing solver: {solver_name}")
    if not quiet:
        print(f"Solver definition:")
        print(inspect.getsource(solver_func))
    
    # Patch both the DSL module and the solvers module
    patched_dsl = patch_module(dsl)
    
    # Important: We need to patch the DSL functions that were already imported into solvers
    for name in dir(dsl):
        if not name.startswith('_'):  # Skip private attributes
            dsl_attr = getattr(dsl, name)
            if callable(dsl_attr) and hasattr(solvers, name):
                # Replace the imported function in solvers with the tracked version from DSL
                setattr(solvers, name, getattr(dsl, name))
    
    # Make sure constants are properly accessible in solvers
    import constants as const_module
    for name in dir(const_module):
        if name.isupper():  # Constants are typically uppercase
            setattr(solvers, name, getattr(const_module, name))
    
    # Track if any examples executed successfully
    any_success = False
    
    # Keep track of DSL calls even if solver crashes
    solver_name = f'solve_{solver_key}'
    
    # Track errors for reporting
    error_occurred = False
    error_info = None
    
    # Execute the solver on each example
    for i, example in enumerate(examples):
        print(f"\nExecuting example {i+1}:")
        if not quiet:
            print("Input:")
            print_grid(example['input'])
        
        # Reset call tracking for this example
        example_dsl_calls = defaultdict(int)
        example_call_signatures = defaultdict(list)
        
        # Execute and time the solver, catching exceptions
        start_time = time.time()
        try:
            # Execute the solver function
            result = solver_func(example['input'])
            execution_time = time.time() - start_time
            
            any_success = True
            
            if not quiet:
                print("Output:")
                print_grid(result)
            print(f"Execution time: {execution_time:.6f}s")
            
            # Check correctness
            is_correct = result == example['output']
            print(f"Correct: {is_correct}")
            
            if not is_correct and not quiet:
                print("Expected:")
                print_grid(example['output'])
                
        except Exception as e:
            execution_time = time.time() - start_time
            print(f"Error: {type(e).__name__}: {e}")
            print(f"Execution time before error: {execution_time:.6f}s")
            
            # Record error information
            error_occurred = True
            
            # Detailed error information for the JSON file
            import traceback
            tb_frames = []
            for frame in traceback.extract_tb(e.__traceback__):
                tb_frames.append({
                    "filename": frame.filename,
                    "lineno": frame.lineno,
                    "name": frame.name,
                    "line": frame.line
                })
            
            # Find DSL function that caused the error
            dsl_error_func = None
            dsl_error_line = None
            for frame in traceback.extract_tb(e.__traceback__):
                if frame.filename.endswith('dsl.py'):
                    dsl_error_func = frame.name
                    dsl_error_line = frame.lineno
                    break
            
            error_info = {
                "type": type(e).__name__,
                "message": str(e),
                "example_index": i,
                "traceback": tb_frames,
                "dsl_function": dsl_error_func,
                "dsl_line": dsl_error_line
            }
            
            # Show detailed error info
            if not quiet:
                print("\nDetailed error:")
                traceback.print_exc()
                
                # Try to identify which DSL function caused the error
                if dsl_error_func:
                    print(f"\nError occurred in DSL function: {dsl_error_func} at line {dsl_error_line}")
    
    # Report DSL usage statistics even if the solver crashed
    print("\nDSL Function Usage:")
    dsl_calls = solver_to_dsl_calls.get(solver_name, {})
    if dsl_calls:
        # Sort by call count
        for dsl_func, call_count in sorted(dsl_calls.items(), key=lambda x: x[1], reverse=True):
            # Get signatures for this function
            signatures = call_signatures[solver_name].get(dsl_func, [])
            
            # Extract unique type signatures for display
            type_sigs = [sig.get("type_signature", "") for sig in signatures]
            unique_type_sigs = list(set(type_sigs))  # Remove duplicates
            
            # Format display string with unique type signatures
            sig_display = f" [{', '.join(unique_type_sigs[:3])}]" if unique_type_sigs else ""
            if len(unique_type_sigs) > 3:
                sig_display = sig_display[:-1] + f" and {len(unique_type_sigs)-3} more]"  # Add count of additional signatures
            
            print(f"  {dsl_func}: {call_count} calls{sig_display}")
            
            # Optionally show some sample values
            if not quiet and signatures and len(signatures) > 0:
                value_sigs = [sig.get("value_signature", "") for sig in signatures]
                unique_value_sigs = list(set(value_sigs))[:2]  # Take up to 2 unique values
                if unique_value_sigs:
                    print(f"    Example calls: {', '.join(unique_value_sigs)}")
        
        # Save statistics to correct file based on error state
        if error_occurred:
            # Use special filename for error case
            filename = f"error/generic_dsl_{solver_key}.json"
            export_solver_stats(solver_name, filename, error_info)
            print(f"Statistics with error details saved to {filename}")
        else:
            # Normal file for successful case
            filename = f"stats/generic_dsl_{solver_key}.json"
            export_solver_stats(solver_name, filename)
            print(f"Statistics saved to {filename}")
    else:
        print("  No DSL function calls were recorded")
        
        # Create minimal error report if we had an error but no DSL calls
        if error_occurred:
            filename = f"error/generic_dsl_{solver_key}.json"
            with open(filename, 'w') as f:
                json.dump({"error": error_info}, f, indent=2)
            print(f"Error details saved to {filename}")
        
    # If no examples succeeded but we have DSL calls, don't return early
    if not any_success and not dsl_calls:
        print("\nNo successful executions to gather DSL usage statistics")

def main():
    parser = argparse.ArgumentParser(description="Track DSL function usage in ARC solvers")
    parser.add_argument("solver_key", help="Solver key to analyze (e.g. 67a3c6ac)")
    parser.add_argument("-q", "--quiet", action="store_true", help="Suppress grid printing")
    args = parser.parse_args()
    
    track_solver(args.solver_key, quiet=args.quiet)

if __name__ == "__main__":
    main()