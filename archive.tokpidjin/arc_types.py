from collections import Counter
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

Boolean = bool
Integer = int
IntegerTuple = Tuple[Integer, Integer]
Numerical = Union[Integer, IntegerTuple]
# IntegerSet = FrozenSet[Integer]
IntegerSet = Tuple[Integer]
Grid = Tuple[Tuple[Integer]]
SampleTuple = Tuple[Grid, Grid]
Cell = Tuple[Integer, IntegerTuple]
Object = FrozenSet[Cell]
# Object -> ObjectTuple
ObjectTuple = Tuple[Cell]
Objects = FrozenSet[Object]
# Objects -> ObjectsTuple
ObjectsTuple = Tuple[Object]
Indices = FrozenSet[IntegerTuple]
# Indices -> IndiceTuple
IndiceTuple = Tuple[IntegerTuple]
IndicesSet = FrozenSet[Indices]
# IndicesSet -> IndicesSetTuple
IndicesTuple = Tuple[IndiceTuple]
Patch = Union[Object, Indices]
# Patch -> PatchTuple
PatchTuple = Union[ObjectTuple, IndiceTuple]
Element = Union[Object, Grid]
# Element -> ElementTuple
ElementTuple = Union[ObjectTuple, Grid]
Piece = Union[Grid, Patch]
# Piece -> PieceTuple
PieceTuple = Union[Grid, PatchTuple]
TupleTuple = Tuple[Tuple]
ContainerContainer = Container[Container]
