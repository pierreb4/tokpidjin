"""
Test script to validate the statistics tracking functionality in dsl_with_stats.py
"""

import os
import json
from stats_tracker import enable_stats, disable_stats, STATS_FILE
import dsl_with_stats as dsl
from dsl_loader import get_dsl

def clear_stats_file():
    """Remove the statistics file if it exists"""
    if os.path.exists(STATS_FILE):
        os.remove(STATS_FILE)
        print(f"Removed existing stats file: {STATS_FILE}")

def print_stats():
    """Print the current statistics from the file"""
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, 'r') as f:
            stats = json.load(f)
            print(json.dumps(stats, indent=2))
    else:
        print("No statistics file found.")

def test_basic_functions():
    """Test basic arithmetic functions with different argument types"""
    print("\n=== Testing Basic Functions ===")
    
    # Test with integers
    result = dsl.add(3, 4)
    print(f"add(3, 4) = {result}")
    
    # Test with tuples (coordinates)
    result = dsl.add((1, 2), (3, 4))
    print(f"add((1, 2), (3, 4)) = {result}")
    
    # Test multiplication
    result = dsl.multiply(2, 3)
    print(f"multiply(2, 3) = {result}")
    
    # Test with mixed types
    result = dsl.multiply(2, (3, 4))
    print(f"multiply(2, (3, 4)) = {result}")

def test_color_functions():
    """Test functions that work with colors"""
    print("\n=== Testing Color Functions ===")
    
    # Create a simple grid with colors
    grid = ((0, 1, 2), (1, 2, 3), (2, 3, 0))
    
    # Test color-related functions
    result = dsl.colorcount(grid, 2)
    print(f"colorcount(grid, 2) = {result}")
    
    # Test color filtering
    indices = dsl.ofcolor(grid, 1)
    print(f"ofcolor(grid, 1) = {indices}")

def test_dimension_functions():
    """Test functions that work with width and height"""
    print("\n=== Testing Dimension Functions ===")
    
    # Create a grid
    grid = ((0, 1, 2, 3), (1, 2, 3, 0), (2, 3, 0, 1))
    
    # Test dimension-related functions
    result = dsl.width(grid)
    print(f"width(grid) = {result}")
    
    result = dsl.height(grid)
    print(f"height(grid) = {result}")
    
    result = dsl.shape(grid)
    print(f"shape(grid) = {result}")
    
    # Test resizing
    result = dsl.resize(grid, 5, 6)
    print(f"resize(grid, 5, 6) has shape {dsl.shape(result)}")
    
    # Test cropping
    result = dsl.crop(grid, (0, 0), (2, 2))
    print(f"crop(grid, (0, 0), (2, 2)) has shape {dsl.shape(result)}")

def test_toggle_mechanism():
    """Test the toggle mechanism for statistics gathering"""
    print("\n=== Testing Toggle Mechanism ===")
    
    # First enable stats and make some calls
    print("Stats enabled:")
    enable_stats()
    dsl.add(5, 6)
    dsl.multiply(2, 3)
    print_stats()
    
    # Clear stats file
    clear_stats_file()
    
    # Now disable stats and make some calls
    print("\nStats disabled:")
    disable_stats()
    dsl.add(7, 8)
    dsl.multiply(3, 4)
    print_stats()
    
    # Re-enable stats
    print("\nStats re-enabled:")
    enable_stats()
    dsl.add(9, 10)
    dsl.multiply(4, 5)
    print_stats()

def test_dsl_loader():
    """Test the DSL loader functionality"""
    print("\n=== Testing DSL Loader ===")
    
    # Clear stats file
    clear_stats_file()
    
    # Get DSL without stats
    print("Using DSL without stats:")
    dsl_no_stats = get_dsl(stats_enabled=False)
    dsl_no_stats.add(1, 2)
    dsl_no_stats.multiply(3, 4)
    print_stats()
    
    # Get DSL with stats
    print("\nUsing DSL with stats:")
    dsl_with_stats = get_dsl(stats_enabled=True)
    dsl_with_stats.add(5, 6)
    dsl_with_stats.multiply(7, 8)
    print_stats()

def main():
    """Main test function"""
    print("Starting statistics tracking tests...")
    
    # Clear any existing stats file
    clear_stats_file()
    
    # Make sure stats are enabled
    enable_stats()
    
    # Run tests
    test_basic_functions()
    test_color_functions()
    test_dimension_functions()
    
    # Print final statistics
    print("\n=== Final Statistics ===")
    print_stats()
    
    # Test toggle mechanism
    test_toggle_mechanism()
    
    # Test DSL loader
    test_dsl_loader()
    
    print("\nTests completed.")

if __name__ == "__main__":
    main()
