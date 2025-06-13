"""
Module Patching Utility for Statistics Tracking

This script provides functionality to decorate functions in specified modules
with the stats.track_stats decorator to collect statistics about function calls,
argument types, and execution times.

The collected statistics can be used to identify optimization opportunities
and understand usage patterns in the code.
"""

import inspect
import importlib
import sys
from types import ModuleType
from stats import track_stats

def patch_module(module_name):
    """
    Patch all functions in a module with the track_stats decorator.
    
    Args:
        module_name (str): The name of the module to patch
        
    Returns:
        ModuleType: The patched module with all functions decorated
    """
    # Import the module
    module = importlib.import_module(module_name)
    
    # Find all functions in the module
    functions = inspect.getmembers(module, inspect.isfunction)
    
    # Apply decorator to each function
    for name, func in functions:
        if func.__module__ == module.__name__:
            # Create a decorated version of the function
            decorated_func = track_stats(func)
            
            # Update the module's attribute with the decorated function
            setattr(module, name, decorated_func)
    
    # Return the modified module
    return module

def enable_tracking(modules=None):
    """
    Enable statistics tracking for specified modules.
    
    Args:
        modules (list): List of module names to patch. If None, defaults to ['dsl', 'solvers']
        
    Returns:
        dict: Dictionary mapping module names to patched module objects
    """
    from stats import enable, configure
    enable(True)
    
    # Configure with suitable defaults for tracking
    configure(
        sampling_rate=0.1,  # Sample 10% of function calls
        max_samples=100,    # Store up to 100 samples per function
        sample_size_limit=50  # Limit size of complex data structures in samples
    )
    
    if modules is None:
        modules = ['dsl', 'solvers']
    
    patched_modules = {}
    
    for module_name in modules:
        # Patch the module
        patched_module = patch_module(module_name)
        
        # Replace the original module in sys.modules
        sys.modules[module_name] = patched_module
        patched_modules[module_name] = patched_module
        
        print(f"{module_name} statistics tracking enabled")
    
    return patched_modules

def disable_tracking(modules=None):
    """
    Disable tracking and restore the original modules.
    
    Args:
        modules (list): List of module names to restore. If None, defaults to ['dsl', 'solvers']
    """
    from stats import enable
    enable(False)
    
    if modules is None:
        modules = ['dsl', 'solvers']
    
    for module_name in modules:
        # Reload the original module
        importlib.reload(sys.modules[module_name])
        print(f"{module_name} statistics tracking disabled")

def export_stats_to_file(filename="module_stats.json"):
    """
    Export the collected statistics to a JSON file.
    
    Args:
        filename (str): Name of the JSON file to write statistics to
    """
    from stats import export_stats
    export_stats(filename)
    print(f"Statistics exported to {filename}")

# Convenience functions for specific modules
def enable_dsl_tracking():
    """
    Enable tracking for the DSL module only.
    
    Returns:
        dict: Dictionary with the patched dsl module
    """
    return enable_tracking(['dsl'])

def enable_solvers_tracking():
    """
    Enable tracking for the solvers module only.
    
    Returns:
        dict: Dictionary with the patched solvers module
    """
    return enable_tracking(['solvers'])

def enable_all_tracking():
    """
    Enable tracking for both DSL and solvers modules.
    
    Returns:
        dict: Dictionary with both patched modules
    """
    return enable_tracking(['dsl', 'solvers'])