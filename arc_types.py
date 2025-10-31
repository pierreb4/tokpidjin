from typing import (
    List,
    Union,
    Tuple,
    Any,
    Container,
    Callable,
    FrozenSet,
    Iterable
)

# Types supporting substitution
F_ = int #  0  to  9, from first
L_ = int # -10 to -1, from last
FL = int # -10 to  9, from both ends
R_ = int # Randomized symbols, such as colors
C_ = int # Colors
A_ = int # Angles
I_ = int # Row indices
J_ = int # Column indices
IJ = Tuple[I_, J_] # Grid locations
F_ = Callable # Function type

# Generic types
Boolean = bool # T/F, True / False
Integer = int # Integers

# IntegerTuple = Tuple[Integer, Integer]
Numerical = Union[Integer, IJ]

# Collection types (tuple-based, replacing frozenset-based types)
Grid = Tuple[Tuple[Integer], ...]  # 2D grid of integers
Samples = Tuple[Tuple[Grid, Grid], ...]  # Training samples: (input grid, output grid) pairs
Colors = Tuple[C_, ...]  # Sequence of color values
Cell = Tuple[I_, J_, C_]  # Single cell: (row, col, color)

# Composite collection types (all tuple-based)
Indices = Tuple[IJ, ...]  # Collection of grid coordinates (was FrozenSet[IJ])
IndicesSet = Tuple[Indices, ...]  # Collection of index collections (was FrozenSet[Indices])
Object = Tuple[Cell, ...]  # Collection of cells (was FrozenSet[Cell])
Objects = Tuple[Object, ...]  # Collection of objects (was FrozenSet[Object])
Patch = Union[Object, Indices]  # Either a collection of cells or coordinates

# Tuple collection types
TupleTuple = Tuple[Tuple, ...]  # Generic tuple of tuples
TTT_iii = Tuple[Tuple[Tuple[int, int, int], ...], ...]  # Triple tuple structure

# Container types (alias for backwards compatibility)
ContainerContainer = Container[Container]
