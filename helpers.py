from arc_types import *
from collections import Counter


def difference(
    a: FrozenSet,
    b: FrozenSet
) -> FrozenSet:
    """ set difference """
    return type(a)(e for e in a if e not in b)


def and_tuple(a: Tuple, b: Tuple) -> Tuple:
    """Return intersection (common elements) of two tuples"""
    return tuple((Counter(a) & Counter(b)).elements())


