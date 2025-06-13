# stats.py - A new module for collecting function statistics

import functools
import inspect
import os
import random
import time
from collections import defaultdict
from typing import Any, Dict, List, Tuple, Set, Optional

# Global statistics storage
_stats = defaultdict(lambda: {
    'calls': 0,
    'execution_time': 0.0,
    'arg_types': defaultdict(int),
    'return_types': defaultdict(int),
    'arg_samples': defaultdict(list),
    'return_samples': []
})

# Configuration
_config = {
    'enabled': False,
    'sampling_rate': 0.01,  # Sample 1% of calls
    'max_samples': 100,     # Store up to 100 samples per arg/return
    'sample_size_limit': 100,  # Don't sample values larger than this
    'exclude_functions': set(),  # Functions to exclude from tracking
}

def enable(enabled=True):
    """Enable or disable statistics collection."""
    _config['enabled'] = enabled

def configure(sampling_rate=None, max_samples=None, sample_size_limit=None):
    """Configure statistics collection parameters."""
    if sampling_rate is not None:
        _config['sampling_rate'] = sampling_rate
    if max_samples is not None:
        _config['max_samples'] = max_samples
    if sample_size_limit is not None:
        _config['sample_size_limit'] = sample_size_limit

def exclude_functions(*funcs):
    """Exclude specific functions from tracking."""
    for func in funcs:
        _config['exclude_functions'].add(func.__name__)

def _should_sample():
    """Determine if this call should be sampled based on sampling rate."""
    return random.random() < _config['sampling_rate']

def _safe_repr(value):
    """Get a safe string representation of a value, limited by size."""
    try:
        if isinstance(value, (list, tuple, set, dict, frozenset)) and len(value) > _config['sample_size_limit']:
            return f"{type(value).__name__}(length={len(value)})"
        return repr(value)
    except:
        return f"<{type(value).__name__} object>"

def track_stats(func):
    """Decorator to track function statistics."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Skip if disabled or excluded
        if not _config['enabled'] or func.__name__ in _config['exclude_functions']:
            return func(*args, **kwargs)
        
        # Track call count and execution time
        stats = _stats[func.__name__]
        stats['calls'] += 1
        
        # Get caller information using inspect
        caller_info = None
        try:
            # Get the frame 1 level up (the caller of this function)
            frame = inspect.currentframe().f_back
            filename = frame.f_code.co_filename
            lineno = frame.f_lineno
            # Store only relative path if possible
            rel_filename = os.path.relpath(filename, os.path.dirname(__file__)) if filename else "unknown"
            caller_info = f"{rel_filename}:{lineno}"
            
            # Initialize call_sites if needed
            if 'call_sites' not in stats:
                stats['call_sites'] = defaultdict(int)
            
            # Initialize call_site_arg_types if needed
            if 'call_site_arg_types' not in stats:
                stats['call_site_arg_types'] = defaultdict(lambda: defaultdict(int))
            
            # Track this call site
            stats['call_sites'][caller_info] += 1
        except:
            pass  # Fail gracefully if stack inspection fails
        finally:
            # Clean up frame reference to avoid reference cycles
            if 'frame' in locals():
                del frame
        
        # Start timing
        start_time = time.time()
        
        # Call the function
        result = func(*args, **kwargs)
        
        # Record execution time
        execution_time = time.time() - start_time
        stats['execution_time'] += execution_time
        
        # Always track argument types per call site, not just when sampling
        if caller_info:
            # Get parameter names
            sig = inspect.signature(func)
            param_names = list(sig.parameters.keys())
            
            # Handle positional args
            for i, arg in enumerate(args):
                if i < len(param_names):
                    arg_name = param_names[i]
                    arg_type = type(arg).__name__
                    
                    # Track overall arg types as before
                    stats['arg_types'][(arg_name, arg_type)] += 1
                    
                    # Track arg types per call site
                    stats['call_site_arg_types'][caller_info][(arg_name, arg_type)] += 1
            
            # Handle keyword args
            for name, value in kwargs.items():
                arg_type = type(value).__name__
                
                # Track overall arg types as before
                stats['arg_types'][(name, arg_type)] += 1
                
                # Track arg types per call site
                stats['call_site_arg_types'][caller_info][(name, arg_type)] += 1
        
        # Sample this call?
        if _should_sample():
            # Record argument samples
            sig = inspect.signature(func)
            param_names = list(sig.parameters.keys())
            
            # Handle positional args
            for i, arg in enumerate(args):
                if i < len(param_names):
                    arg_name = param_names[i]
                    
                    # Save sample if we haven't reached the limit and it's not a duplicate
                    arg_repr = _safe_repr(arg)
                    if (len(stats['arg_samples'][arg_name]) < _config['max_samples'] and 
                            arg_repr not in stats['arg_samples'][arg_name]):
                        stats['arg_samples'][arg_name].append(arg_repr)
            
            # Handle keyword args
            for name, value in kwargs.items():
                # Save sample if we haven't reached the limit and it's not a duplicate
                value_repr = _safe_repr(value)
                if (len(stats['arg_samples'][name]) < _config['max_samples'] and 
                        value_repr not in stats['arg_samples'][name]):
                    stats['arg_samples'][name].append(value_repr)
            
            # Record return type and sample
            return_type = type(result).__name__
            stats['return_types'][return_type] += 1
            
            # Save sample if we haven't reached the limit and it's not a duplicate
            result_repr = _safe_repr(result)
            if (len(stats['return_samples']) < _config['max_samples'] and 
                    result_repr not in stats['return_samples']):
                stats['return_samples'].append(result_repr)
            
            # Save call site with this sample if we have it and it's not a duplicate
            if caller_info and len(stats.get('call_site_samples', [])) < _config['max_samples']:
                if 'call_site_samples' not in stats:
                    stats['call_site_samples'] = []
                if caller_info not in stats['call_site_samples']:
                    stats['call_site_samples'].append(caller_info)
        
        return result
    
    return wrapper

def get_stats():
    """Get the collected statistics."""
    return dict(_stats)

def get_function_stats(function_name):
    """Get statistics for a specific function."""
    return dict(_stats[function_name])

def print_stats(function_name=None):
    """Print statistics for a function or all functions."""
    if function_name:
        stats = get_function_stats(function_name)
        print(f"Statistics for {function_name}:")
        _print_function_stats(function_name, stats)
    else:
        stats = get_stats()
        for func_name, func_stats in stats.items():
            print(f"\nStatistics for {func_name}:")
            _print_function_stats(func_name, func_stats)

def _print_function_stats(func_name, stats):
    """Helper to print stats for a single function."""
    print(f"  Calls: {stats['calls']}")
    avg_time = stats['execution_time'] / stats['calls'] if stats['calls'] > 0 else 0
    print(f"  Avg execution time: {avg_time:.6f}s")
    
    # Print top call sites
    if 'call_sites' in stats and stats['call_sites']:
        print("  Top call sites:")
        top_sites = sorted(stats['call_sites'].items(), key=lambda x: x[1], reverse=True)[:5]
        for site, count in top_sites:
            print(f"    {site}: {count} calls")
            
            # Print arg types for this call site
            if 'call_site_arg_types' in stats and site in stats['call_site_arg_types']:
                site_arg_types = sorted(stats['call_site_arg_types'][site].items(), 
                                    key=lambda x: x[1], reverse=True)
                if site_arg_types:
                    print(f"      Arg types at this location:")
                    for (arg_name, arg_type), count in site_arg_types:
                        print(f"        {arg_name}: {arg_type} ({count} occurrences)")
    
    # Sort argument types by frequency (overall)
    arg_types = sorted(stats['arg_types'].items(), key=lambda x: x[1], reverse=True)
    if arg_types:
        print("  All argument types (across all call sites):")
        for (arg_name, arg_type), count in arg_types:
            print(f"    {arg_name}: {arg_type} ({count} occurrences)")
    
    # Sort return types by frequency 
    return_types = sorted(stats['return_types'].items(), key=lambda x: x[1], reverse=True)
    if return_types:
        print("  Return types:")
        for return_type, count in return_types:
            print(f"    {return_type} ({count} occurrences)")
    
    # Print unique argument samples
    if any(samples for samples in stats['arg_samples'].values()):
        print("  Argument samples (unique):")
        for arg_name, samples in stats['arg_samples'].items():
            if samples:
                # We now know all samples are unique
                print(f"    {arg_name}: {', '.join(samples[:5])}{'...' if len(samples) > 5 else ''}")
    
    # Print unique return samples
    if stats['return_samples']:
        print("  Return samples (unique):")
        print(f"    {', '.join(stats['return_samples'][:5])}{'...' if len(stats['return_samples']) > 5 else ''}")
    
    # Print unique call sites
    if 'call_site_samples' in stats and stats['call_site_samples']:
        print("  Sample call sites:")
        for sample in stats['call_site_samples'][:5]:
            print(f"    {sample}")

def reset_stats():
    """Reset all collected statistics."""
    global _stats
    _stats = defaultdict(lambda: {
        'calls': 0,
        'execution_time': 0.0,
        'arg_types': defaultdict(int),
        'return_types': defaultdict(int),
        'arg_samples': defaultdict(list),
        'return_samples': [],
        'call_sites': defaultdict(int),
        'call_site_samples': [],
        'call_site_arg_types': defaultdict(lambda: defaultdict(int))
    })

def export_stats(filename):
    """Export statistics to a JSON file."""
    import json
    
    # Convert defaultdicts to regular dicts for serialization
    def convert_to_dict(obj):
        if isinstance(obj, defaultdict):
            return {str(k): convert_to_dict(v) for k, v in obj.items()}
        elif isinstance(obj, dict):
            return {str(k): convert_to_dict(v) for k, v in obj.items()}
        elif isinstance(obj, (list, tuple)):
            return [convert_to_dict(x) for x in obj]
        else:
            return obj
    
    export_data = convert_to_dict(_stats)
    
    with open(filename, 'w') as f:
        json.dump(export_data, f, indent=2)
    
    print(f"Statistics exported to {filename}")