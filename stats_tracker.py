import json
import os
from datetime import datetime
from typing import Any, Dict, List, Tuple, Union, Callable
import inspect
import functools

# Global variable to control whether statistics are tracked
STATS_ENABLED = True

# Path to save statistics
STATS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'function_stats.json')

def is_color_argument(arg: Any) -> bool:
    """Determine if an argument is likely a color value (integer in range 0-9)"""
    return isinstance(arg, int) and 0 <= arg <= 9

def is_width_argument(arg_name: str, func_name: str) -> bool:
    """Determine if an argument is related to width based on name or function"""
    width_related = ['width', 'w', 'cols', 'columns', 'j']
    return (arg_name.lower() in width_related or 
            'width' in func_name.lower() or 
            'horizontal' in func_name.lower())

def is_height_argument(arg_name: str, func_name: str) -> bool:
    """Determine if an argument is related to height based on name or function"""
    height_related = ['height', 'h', 'rows', 'i']
    return (arg_name.lower() in height_related or 
            'height' in func_name.lower() or 
            'vertical' in func_name.lower())

def get_grid_dimensions(grid):
    """Get dimensions from a grid-like structure"""
    if not grid or not hasattr(grid, '__len__'):
        return None
    
    try:
        if isinstance(grid, tuple) and len(grid) > 0 and hasattr(grid[0], '__len__'):
            return (len(grid), len(grid[0]))  # height, width
    except (IndexError, TypeError):
        pass
    return None

def load_stats() -> Dict:
    """Load existing statistics from file"""
    if os.path.exists(STATS_FILE):
        try:
            with open(STATS_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_stats(stats: Dict) -> None:
    """Save statistics to file"""
    with open(STATS_FILE, 'w') as f:
        json.dump(stats, f, indent=2)

def track_stats(func: Callable) -> Callable:
    """Decorator to track function call statistics"""
    # Skip built-in functions and methods
    if func.__module__ == 'builtins' or func.__name__ in ('__init__', '__new__', '__call__'):
        return func
        
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not STATS_ENABLED:
            return func(*args, **kwargs)
        
        # Get today's date as string
        today = datetime.now().strftime('%Y-%m-%d')
        
        # Get function signature
        sig = inspect.signature(func)
        param_names = list(sig.parameters.keys())
        
        # Load existing stats
        stats = load_stats()
        
        # Initialize stats structure if needed
        if today not in stats:
            stats[today] = {}
        
        func_name = func.__name__
        if func_name not in stats[today]:
            stats[today][func_name] = {
                "calls": 0,
                "arg_types": {
                    "colors": 0,
                    "width": 0,
                    "height": 0,
                    "other": 0
                }
            }
        
        # Increment call count
        stats[today][func_name]["calls"] += 1
        
        # Analyze arguments
        for i, arg in enumerate(args):
            if i < len(param_names):
                arg_name = param_names[i]
                
                # Check for grid-like structures and extract dimensions
                dimensions = get_grid_dimensions(arg)
                if dimensions:
                    stats[today][func_name]["arg_types"]["height"] += 1
                    stats[today][func_name]["arg_types"]["width"] += 1
                    continue
                
                # Check for color arguments
                if is_color_argument(arg):
                    stats[today][func_name]["arg_types"]["colors"] += 1
                # Check for width/height arguments
                elif is_width_argument(arg_name, func_name):
                    stats[today][func_name]["arg_types"]["width"] += 1
                elif is_height_argument(arg_name, func_name):
                    stats[today][func_name]["arg_types"]["height"] += 1
                else:
                    stats[today][func_name]["arg_types"]["other"] += 1
        
        # Save updated stats
        save_stats(stats)
        
        # Call the original function
        return func(*args, **kwargs)
    
    return wrapper

def enable_stats():
    """Enable statistics tracking"""
    global STATS_ENABLED
    STATS_ENABLED = True

def disable_stats():
    """Disable statistics tracking"""
    global STATS_ENABLED
    STATS_ENABLED = False
