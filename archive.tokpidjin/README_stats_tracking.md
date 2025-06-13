# Implementation Summary: Statistics Tracking for dsl.py

I've implemented a statistics tracking system for the tokpidjin DSL that tracks argument types with a focus on colors, width, and height. The implementation includes:

1. A statistics tracker module that records function calls by day
2. A toggle mechanism to enable/disable statistics gathering
3. A loader that allows switching between versions with and without statistics

## Files Created/Modified

- `stats_tracker.py`: Core statistics tracking functionality
- `dsl_with_stats.py`: DSL with statistics tracking enabled
- `dsl_loader.py`: Loader to toggle between versions
- `test_stats_tracking.py`: Test script to validate functionality
- `function_stats.json`: Output statistics file (generated during runtime)

## How It Works

### Statistics Tracking

The system tracks:
- Function call counts by day
- Argument types, categorized as:
  - Colors (integers 0-9)
  - Width (arguments related to horizontal dimensions)
  - Height (arguments related to vertical dimensions)
  - Other (all other argument types)

### Toggle Mechanism

Two methods are provided to toggle statistics gathering:

1. **Runtime toggle**: Use `enable_stats()` and `disable_stats()` functions from `stats_tracker.py`
2. **Import toggle**: Use `get_dsl(stats_enabled=True/False)` from `dsl_loader.py`

### Statistics Output

Statistics are saved to a JSON file with the following structure:
```json
{
  "YYYY-MM-DD": {
    "function_name": {
      "calls": count,
      "arg_types": {
        "colors": count,
        "width": count,
        "height": count,
        "other": count
      }
    }
  }
}
```

## Usage Instructions

### Basic Usage

```python
# Import the DSL with statistics tracking
import dsl_with_stats as dsl

# Use DSL functions normally
result = dsl.add(3, 4)
grid = ((0, 1, 2), (1, 2, 3), (2, 3, 0))
width = dsl.width(grid)
```

### Using the Toggle

```python
# Method 1: Runtime toggle
from stats_tracker import enable_stats, disable_stats

enable_stats()  # Start tracking
# ... use DSL functions ...
disable_stats()  # Stop tracking

# Method 2: Import toggle
from dsl_loader import get_dsl

dsl = get_dsl(stats_enabled=True)  # Get DSL with tracking
# ... use DSL functions ...
dsl = get_dsl(stats_enabled=False)  # Get DSL without tracking
```

### Accessing Statistics

The statistics are saved to `function_stats.json` in the same directory as the DSL files. You can load and process this file using standard JSON tools:

```python
import json

with open('function_stats.json', 'r') as f:
    stats = json.load(f)
    
# Process statistics as needed
```

## Implementation Notes

1. The statistics tracking is implemented as a decorator that wraps each function in the DSL.
2. The decorator analyzes function arguments to categorize them as colors, width, or height.
3. Grid-like structures are detected and counted as both width and height.
4. The toggle mechanism uses a global variable to enable/disable tracking at runtime.
5. The loader provides a clean way to switch between versions without changing imports throughout your code.

## Known Limitations

1. Some functions that use built-in Python functions internally may have issues with the decorator. These have been handled in the current implementation, but if you encounter any errors, please report them.
2. The statistics file grows over time as more days are added. You may want to periodically archive or clear old statistics.
