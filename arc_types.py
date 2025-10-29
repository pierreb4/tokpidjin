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
IntegerSet = FrozenSet[Integer]
Grid = Tuple[Tuple[Integer]]
Samples = Tuple[Grid, Grid]

TTT_iii = Tuple[Tuple[Tuple[int, int, int], ...], ...]

# Cell = Tuple[Integer, IntegerTuple]
# Cell = Tuple[C_, IJ]
Cell = Tuple[I_, J_, C_]

Colors = Tuple[C_, ...]

Object = FrozenSet[Cell]
Objects = FrozenSet[Object]
Indices = FrozenSet[IJ]
IndicesSet = FrozenSet[Indices]
Patch = Union[Object, Indices]
# Element = Union[Object, Grid]
# Piece = Union[Grid, Patch]
TupleTuple = Tuple[Tuple]
ContainerContainer = Container[Container]
