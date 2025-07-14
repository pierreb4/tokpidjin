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

# Regular types, no sub (yet)
I_ = int
J_ = int
IJ = Tuple[I_, J_]
F_ = Callable

# Generic types
Boolean = bool
Integer = int
# IntegerTuple = Tuple[Integer, Integer]
Numerical = Union[Integer, IJ]
IntegerSet = FrozenSet[Integer]
Grid = Tuple[Tuple[Integer]]
Samples = Tuple[Grid, Grid]

# Cell = Tuple[Integer, IntegerTuple]
# Cell = Tuple[C_, IJ]
Cell = Tuple(I_, J_, C_)

Object = FrozenSet[Cell]
Objects = FrozenSet[Object]
Indices = FrozenSet[IJ]
IndicesSet = FrozenSet[Indices]
Patch = Union[Object, Indices]
# Element = Union[Object, Grid]
# Piece = Union[Grid, Patch]
TupleTuple = Tuple[Tuple]
ContainerContainer = Container[Container]
