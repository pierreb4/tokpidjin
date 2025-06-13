"""
Grid Display Utility

This module provides functions for visualizing grid data from the ARC dataset
in a more human-readable format.
"""

# Shared default color map for all grid display functions
DEFAULT_COLOR_MAP = {
    0: '\033[40m\033[37m',  # Black bg, white text for zero
    1: '\033[44m\033[37m',  # Blue
    2: '\033[41m\033[37m',  # Red
    3: '\033[42m\033[37m',  # Green
    4: '\033[43m\033[30m',  # Yellow (with black text)
    5: '\033[100m\033[37m', # Bright Black/Gray
    6: '\033[45m\033[37m',  # Magenta
    7: '\033[48;5;208m\033[30m',  # Orange (with black text)
    8: '\033[46m\033[30m',  # Cyan (with black text)
    9: '\033[48;5;88m\033[37m',   # Burgundy (with white text)
    10: '\033[47m\033[30m',  # White (with black text)
}


def table(grid):
    """
    Display a grid as a formatted table.
    
    Args:
        grid: A tuple of tuples representing a grid where each inner tuple is a row
             and each element is a cell value
    
    Returns:
        None, prints the formatted grid to the console
    """
    # Find the maximum number width for proper alignment
    max_width = max(len(str(cell)) for row in grid for cell in row)
    
    # Print top border
    border = '+' + '-' * (len(grid[0]) * (max_width + 3) - 1) + '+'
    print(border)
    
    # Print rows
    for row in grid:
        formatted_row = '| ' + ' | '.join(str(cell).center(max_width) for cell in row) + ' |'
        print(formatted_row)
        print(border)
    
    print()  # Extra newline for spacing


def print_grid(grid, color_map=None):
    """
    Display a grid with color coding based on cell values.
    
    Args:
        grid: A tuple of tuples representing a grid
        color_map: Optional dictionary mapping values to ANSI color codes
                  Default uses a standard color palette for ARC grids
    
    Returns:
        None, prints the colored grid to the console
    """
    if color_map is None:
        color_map = DEFAULT_COLOR_MAP
    
    reset = '\033[0m'
    
    for row in grid:
        line = ''
        for cell in row:
            color_code = color_map.get(cell, '\033[0m')
            line += f"{color_code} {cell} {reset}"
        print(line)
    
    print()  # Extra newline for spacing


def empty_mask(grid, patch):
    """
    Display a grid with positions in the patch shown as empty spaces.
    
    Args:
        grid: A tuple of tuples representing a grid
        patch: A frozenset of (row, col) coordinates that should be masked
    
    Returns:
        None, prints the grid with masked positions
    """
    for r, row in enumerate(grid):
        line = ''
        for c, cell in enumerate(row):
            if (r, c) in patch:
                # Print empty space for positions in patch
                line += '   '
            else:
                # Print normal cell value with padding
                line += f' {cell} '
        print(line)
    
    print()  # Extra newline for spacing


def get_mask(grid, patch, color_map=None, display=True):
    """
    Create a grid with positions in the patch highlighted.
    
    Args:
        grid: A tuple of tuples representing a grid
        patch: A frozenset of (row, col) coordinates that should be highlighted
        color_map: Optional dictionary mapping values to ANSI color codes
        display: If True, print the colored grid with highlights
    
    Returns:
        A colored grid representation with highlighted cells at patch positions
        that can be passed to other visualization functions
    """
    if color_map is None:
        color_map = DEFAULT_COLOR_MAP
    
    # Highlight color for masked positions (bright white background with black text)
    highlight = color_map.get(10, '\033[107m\033[30m')  # White background, black text
    reset = '\033[0m'
    
    # Create highlighted grid representation
    highlighted_grid = []
    
    for r, row in enumerate(grid):
        line = ''
        highlighted_row = []
        
        for c, cell in enumerate(row):
            if (r, c) in patch:
                # Highlight cells in patch
                colored_cell = f"{highlight} {cell} {reset}"
                # Store the cell with highlight info for potential return
                highlighted_row.append((cell, True))
            else:
                # Normal colored display
                color_code = color_map.get(cell, '\033[0m')
                colored_cell = f"{color_code} {cell} {reset}"
                highlighted_row.append((cell, False))
            
            line += colored_cell
            
        if display:
            print(line)
        
        highlighted_grid.append(tuple(highlighted_row))
    
    if display:
        print()  # Extra newline for spacing
    
    return tuple(highlighted_grid)


def print_highlighted_grid(highlighted_grid, color_map=None):
    """
    Print a grid that was previously processed by the mask function.
    
    Args:
        highlighted_grid: A tuple of tuples where each cell is (value, is_highlighted)
        color_map: Optional dictionary mapping values to ANSI color codes
    """
    if color_map is None:
        color_map = DEFAULT_COLOR_MAP
        
    highlight = color_map.get(10, '\033[107m\033[30m')  # White background, black text
    reset = '\033[0m'
    
    for row in highlighted_grid:
        line = ''
        for cell, is_highlighted in row:
            if is_highlighted:
                line += f"{highlight} {cell} {reset}"
            else:
                color_code = color_map.get(cell, '\033[0m')
                line += f"{color_code} {cell} {reset}"
        print(line)
    
    print()  # Extra newline for spacing


def side_by_side(grids, titles=None, color_maps=None):
    """
    Display multiple grids side by side, even if they have different dimensions.
    
    Args:
        grids: A list of grids (tuple of tuples), each representing a grid
        titles: Optional list of titles for each grid
        color_maps: Optional list of color maps for each grid
        
    Returns:
        None, prints the grids side by side
    """
    if not grids:
        print("No grids to display")
        return
    
    # Get dimensions for each grid
    dimensions = [(len(g), len(g[0]) if g else 0) for g in grids]
    max_rows = max(dim[0] for dim in dimensions)
    
    # Setup color maps for each grid
    if color_maps is None:
        color_maps = [DEFAULT_COLOR_MAP] * len(grids)
    elif len(color_maps) < len(grids):
        color_maps.extend([DEFAULT_COLOR_MAP] * (len(grids) - len(color_maps)))
    
    # Setup titles
    if titles is None:
        titles = [f"Grid {i+1} ({dim[0]}×{dim[1]})" for i, dim in enumerate(dimensions)]
    elif len(titles) < len(grids):
        titles.extend([f"Grid {i+1} ({dimensions[i][0]}×{dimensions[i][1]})" 
                      for i in range(len(titles), len(grids))])
    
    # Calculate width for each grid display based on its own dimensions
    cell_width = 3  # Space for each cell (digit + padding)
    grid_widths = [dim[1] * cell_width for dim in dimensions]
    
    # Print titles
    for i, title in enumerate(titles):
        print(f"{title.center(grid_widths[i])}", end="   ")
    print("\n")
    
    # Print the grids side by side
    reset = '\033[0m'
    for r in range(max_rows):
        for i, grid in enumerate(grids):
            if r < dimensions[i][0]:  # Only print if this grid has this row
                # Print cells for this grid row
                for c in range(dimensions[i][1]):
                    color_code = color_maps[i].get(grid[r][c], '\033[0m')
                    print(f"{color_code} {grid[r][c]} {reset}", end="")
            else:
                # Print empty space for missing rows
                print(" " * grid_widths[i], end="")
            # Separator between grids
            print("   ", end="")
        print()  # New line after each row
    
    print()  # Extra newline for spacing


def get_grid(points, default_value=0, from_origin=False):
    """
    Create a grid from a frozenset of value-coordinate pairs.
    
    Args:
        points: A frozenset of tuples where each tuple is (value, (row, col))
               representing a value to place at the given coordinates
        default_value: The value to use for cells not specified in points
        from_origin: If True, force grid to start from (0,0) regardless of input coordinates
    
    Returns:
        A tuple of tuples representing the smallest possible grid containing
        all the specified points
    """
    if not points:
        return ((default_value,),)
    
    # Extract all coordinates
    coords = [p[1] for p in points]
    
    # Find the dimensions of the smallest grid containing all points
    min_row = 0 if from_origin else min(c[0] for c in coords)
    max_row = max(c[0] for c in coords)
    min_col = 0 if from_origin else min(c[1] for c in coords)
    max_col = max(c[1] for c in coords)
    
    # Create a grid of the appropriate size filled with default_value
    height = max_row - min_row + 1
    width = max_col - min_col + 1
    
    # Initialize grid with default values
    result_grid = [[default_value for _ in range(width)] for _ in range(height)]
    
    # Place values from the frozenset into the grid
    for value, (row, col) in points:
        # Adjust coordinates to be zero-based within our grid
        adj_row = row - min_row
        adj_col = col - min_col
        result_grid[adj_row][adj_col] = value
    
    # Convert to tuple of tuples for immutability
    return tuple(tuple(row) for row in result_grid)


def print_set(points, color_map=None, title=None, default_value=0, from_origin=False):
    """
    Visualize a frozenset of value-coordinate pairs as a colored grid.
    
    Args:
        points: A frozenset of tuples where each tuple is (value, (row, col))
        color_map: Optional dictionary mapping values to ANSI color codes
        title: Optional title for the grid
        default_value: The value to use for cells not specified in points
        from_origin: If True, force grid to start from (0,0) regardless of input coordinates
    
    Returns:
        The created grid
    """
    # Convert points to a grid
    result_grid = get_grid(points, default_value, from_origin)
    
    # Display the grid with title
    if title:
        print(f"{title}:")
    
    # Print the grid with colors
    print_grid(result_grid, color_map)
    
    return result_grid


if __name__ == "__main__":
    # Example grid
    example_grid = (
        (0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0), 
        (8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 8, 0, 0, 8, 0, 8, 0),
        (0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0),
        (0, 0, 8, 8, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 8, 0, 0, 0, 0, 8, 0, 0),
        (0, 0, 8, 0, 0, 0, 8, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 8),
        (0, 0, 0, 0, 0, 8, 8, 0, 0, 0, 0),
        (0, 8, 0, 0, 8, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 8, 0, 0, 8, 0),
        (0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0)
    )
    
    larger_grid = (
        (2, 2, 2, 2, 2),
        (2, 0, 0, 0, 2),
        (2, 0, 0, 0, 2),
        (2, 0, 0, 0, 2),
        (2, 2, 2, 2, 2),
    )

    smaller_grid = (
        (1, 1, 1),
        (1, 0, 1),
        (1, 1, 1),
    )

    # Example patch
    example_patch = frozenset({(12, 1), (14, 4), (15, 8), (5, 8), (2, 7), (10, 1), 
                              (8, 10), (2, 9), (13, 9), (13, 6), (6, 6)})
    
    # Example object
    point_set = frozenset({
        (4, (6, 6)), (4, (4, 4)), (4, (6, 4)), (4, (3, 3)), (7, (7, 5)), 
        (4, (4, 6)), (7, (5, 4)), (7, (4, 5)), (7, (5, 6)), (4, (5, 5)), (7, (6, 5))
    })

    print("Colored Grid Display:")
    print_grid(example_grid)
    
    print("Colored Masked Grid (highlighted patch):")
    get_mask(example_grid, example_patch)
    
    # Test masking a grid and then using it in side by side display
    print("Testing mask with return value:")
    highlighted_grid = get_mask(example_grid, example_patch, display=False)

    print("Using highlighted grid in other functions:")
    print_highlighted_grid(highlighted_grid)

    # Create a smaller version to demonstrate a grid with different dimensions
    smaller_grid = tuple(row[:5] for row in example_grid[:8])
    smaller_patch = frozenset(p for p in example_patch if p[0] < 8 and p[1] < 5)
    highlighted_smaller = get_mask(smaller_grid, smaller_patch, display=False)

    # Example usage of side_by_side
    modified_grid = tuple(
        tuple(cell if cell != 8 else 4 for cell in row)
        for row in example_grid
    )
    
    modified_grid2 = tuple(
        tuple(cell if cell != 8 else 2 for cell in row)
        for row in example_grid
    )
    
    print("Two grids side by side:")
    side_by_side(
        [example_grid, modified_grid], 
        titles=["Original", "Modified (8→4)"]
    )
    
    print("Three grids side by side:")
    side_by_side(
        [example_grid, modified_grid, modified_grid2], 
        titles=["Original", "Modified (8→4)", "Modified (8→2)"]
    )
    
    print("Grids with different dimensions:")
    side_by_side([smaller_grid, larger_grid], titles=["Small", "Large"])

    print("Using display_point_set function:")
    print_set(point_set, title="Yellow (4) and Orange (7) Pattern", from_origin=False)

    print("Using display_point_set function:")
    print_set(point_set, title="Yellow (4) and Orange (7) Pattern", from_origin=True)

    print("Points to Grid Demonstration:")
    result_from_origin = get_grid(point_set, from_origin=True)
    result_not_from_origin = get_grid(point_set, from_origin=False)
    side_by_side([result_from_origin, result_not_from_origin],
                 titles=["Yes From Origin", "Not From Origin"])

