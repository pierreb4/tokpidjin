import itertools
import random
import math

from collections import Counter

from arc_types import *
from utils import *


def identity(
    x: 'Any'
) -> 'Any':
    """ identity function """
    return x


def first(container: 'Container') -> 'Any':
    """First item of container"""
    iterator = iter(container)
    return next(iterator, None)


def second(container: 'Container') -> 'Any':
    """Second item of container"""
    iterator = iter(container)
    next(iterator)
    return next(iterator, None)


def difference_tuple(a: 'Tuple', b: 'Tuple') -> 'Tuple':
    """Set difference"""
    return type(a)(e for e in a if e not in b)


def p_f( element: 'FrozenSet' ) -> 'IntegerSet':
    """ colors occurring in object """
    return frozenset(v for v, _ in element)


def p_g( grid: 'Grid' ) -> 'IntegerSet':
    """ colors occurring in grid """
    return tuple({cell for row in grid for cell in row})


def p_o( obj: 'Object' ) -> 'IntegerSet':
    """ colors occurring in object """
    # return tuple({v for v, _ in obj})
    return tuple({c for _, _, c in obj})


def dedupe_pair_tuple(S: 'Samples') -> 'Samples':
    """Remove sample pairs where input equals output"""
    return tuple((a, b) for a, b in S if a != b)


def s_iz(S: 'Samples', solver: 'Callable', x_n: int, function: 'Callable') -> 'Any':
    # Filter out identical pairs first
    # For now, we don't use them
    x1 = dedupe_pair_tuple(S)
    # Check that we have something left
    if not x1:
        return False, None
    # Apply first to each sample left in x1 -> sample['input]
    x2 = apply(first, x1)
    # Build call and apply solver to inputs
    x3 = rbind(solver, S)
    x4 = lbind(x3, x_n)
    # Apply partial solver to get intermediate grid
    x5 = apply(x4, x2)
    # Apply function to each item of x5
    x6 = apply(function, x5)

    # Apply second to each sample left in x1 -> sample['output]
    x7 = apply(second, x1)
    # Apply function to each item of x3
    x8 = apply(function, x7)
    # Calculate difference after applying function
    x9 = papply(difference_tuple, x6, x8)
    x10 = dedupe(x9)

    if len(x10) == 1:
        # if x10[0] != ():
        #     print(f"Single result in s_iz: {solver.__name__} - {x} - {x10[0]}")
        return True, x10[0] if x10[0] != () else None
    return False, x10 if len(x10) > 0 else None


def s_iz_n(S: 'Samples', solver: 'Callable', x_n: int, function: 'Callable', index: 'R_') -> C_:
    """Returns a color value from the input-output difference at specified index"""
    (ret_bool, ret_tuple) = s_iz(S, solver, x_n, function)
    if ret_bool and ret_tuple is not None:
        return C_(ret_tuple[index]) if index < len(ret_tuple) else None
    return None


def s_zo(S: 'Samples', solver: 'Callable', x_n: int, function: 'Callable') -> 'Any':
    # Filter out identical pairs first
    # For now, we don't use them
    x1 = dedupe_pair_tuple(S)
    # Check that we have something left
    if not x1:
        return False, None
    # Apply first to each sample left in x1 -> sample['input]
    x2 = apply(first, x1)
    # Build call and apply solver to inputs
    x3 = rbind(solver, S)
    x4 = lbind(x3, x_n)
    # Apply partial solver to get intermediate grid
    x5 = apply(x4, x2)
    # Apply function to each item of x5
    x6 = apply(function, x5)

    # Apply second to each sample left in x1 -> sample['output]
    x7 = apply(second, x1)
    # Apply function to each item of x3
    x8 = apply(function, x7)
    # Calculate difference after applying function
    x9 = papply(difference_tuple, x8, x6)
    x10 = dedupe(x9)

    if len(x10) == 1:
        # if x10[0] != ():
        #     print(f"Single result in s_iz: {solver.__name__} - {x} - {x10[0]}")
        return True, x10[0] if x10[0] != () else None
    return False, x10 if len(x10) > 0 else None


def s_zo_n(S: 'Samples', solver: 'Callable', x_n: int, function: 'Callable', index: 'R_') -> C_:
    """Returns a color value from the input-output difference at specified index"""
    (ret_bool, ret_tuple) = s_zo(S, solver, x_n, function)
    if ret_bool and ret_tuple is not None:
        return C_(ret_tuple[index]) if index < len(ret_tuple) else None
    return None


def b_iz(S: 'Samples', function: 'Callable') -> 'Any':
    x1 = apply(first, S)
    x2 = apply(second, S)
    x3 = dedupe(mapply_t(function, x1))
    x4 = dedupe(mapply_t(function, x2))
    return difference_tuple(x3, x4)


def b_iz_n(S: 'Samples', function: 'Callable', index: 'F_') -> 'C_':
    """Returns a color value from the output-input difference at specified index"""
    ret_tuple = b_iz(S, function)
    return C_(ret_tuple[index]) if index < len(ret_tuple) else None


def b_zo(S: 'Samples', function: 'Callable') -> 'Any':
    x1 = apply(first, S)
    x2 = apply(second, S)
    x3 = dedupe(mapply_t(function, x1))
    x4 = dedupe(mapply_t(function, x2))
    return difference_tuple(x4, x3)


def b_zo_n(S: 'Samples', function: 'Callable', index: 'F_') -> 'C_':
    """Returns a color value from the output-input difference at specified index"""
    ret_tuple = b_zo(S, function)
    return C_(ret_tuple[index]) if index < len(ret_tuple) else None

# c_ for C_
def c_iz(S: 'Samples', function: 'Callable') -> 'Any':
    x1 = apply(first, S)
    x2 = apply(second, S)
    x3 = dedupe(mapply_t(function, x1))
    x4 = dedupe(mapply_t(function, x2))
    return difference_tuple(x3, x4)


def c_iz_n(S: 'Samples', function: 'Callable', pick: 'Callable') -> 'C_':
    """Returns pick of a color value from the input-output difference"""
    ret_tuple = c_iz(S, function)
    return pick(ret_tuple)


def c_zo(S: 'Samples', function: 'Callable') -> 'Any':
    x1 = apply(first, S)
    x2 = apply(second, S)
    x3 = dedupe(mapply_t(function, x1))
    x4 = dedupe(mapply_t(function, x2))
    return difference_tuple(x4, x3)


def c_zo_n(S: 'Samples', function: 'Callable', pick: 'Callable') -> 'C_':
    """Returns pick of a color value from the output-input difference"""
    ret_tuple = c_zo(S, function)
    return pick(ret_tuple)


# a_ for A_
def a_mr(S: 'Samples') -> 'A8':
    return next(
        (
            a
            for a in range(8)
            if all(ex_o == mir_rot_t(ex_i, a) for ex_i, ex_o in S)
        ),
        None,
    )


# i_ for integer
def i_iz(S: 'Samples', function: 'Callable') -> 'Any':
    x1 = apply(first, S)
    x2 = apply(second, S)
    # No need to dedupe a frozenset
    x3 = mapply(function, x1)
    x4 = mapply(function, x2)
    return difference(x3, x4)


def i_iz_n(S: 'Samples', function: 'Callable', pick: 'Callable') -> 'C_':
    ret_frozenset = i_iz(S, function)
    return pick(ret_frozenset)


def i_zo(S: 'Samples', function: 'Callable') -> 'Any':
    x1 = apply(first, S)
    x2 = apply(second, S)
    # No need to dedupe a frozenset
    x3 = mapply(function, x1)
    x4 = mapply(function, x2)
    return difference(x4, x3)


def i_zo_n(S: 'Samples', function: 'Callable', pick: 'Callable') -> 'C_':
    ret_frozenset = i_zo(S, function)
    return pick(ret_frozenset)


# NOTE Function needs to take a grid and return a frozenset, like ottt_g
# TODO Add option to order results in various ways in f_iz_n and f_zo_n
# Sample call: get_arg_rank_f(objects(I, T, T, T), size, F0)
# def f_iz(S: Samples, function: 'Callable', r_n: 'R8') -> 'Any':
#     x1 = apply(first, S)
#     x2 = apply(second, S)
#     x3 = lbind(function, r_n)
#     x4 = dedupe(mapply(x3, x1))
#     x5 = dedupe(mapply(x3, x2))
#     return difference(x4, x5)


# def f_iz_n(S: Samples, function: 'Callable', key: 'Callable', index: 'FL') -> 'Object':
#     ret_frozenset = f_iz(S, function, r_n)
#     return get_arg_rank_f(ret_frozenset, key, index)


# f_ fot frozenset
def f_iz(S: Samples, function: 'Callable') -> 'Any':
    x1 = apply(first, S)
    x2 = apply(second, S)
    x4 = dedupe(mapply(function, x1))
    x5 = dedupe(mapply(function, x2))
    return difference(x4, x5)


def f_iz_n(S: Samples, function: 'Callable', pick: 'Callable') -> 'Object':
    ret_frozenset = f_iz(S, function)
    return pick(ret_frozenset)


# def f_zo(S: Samples, function: 'Callable', r_n: 'R8') -> 'Any':
#     x1 = apply(first, S)
#     x2 = apply(second, S)
#     x3 = lbind(function, r_n)
#     x4 = dedupe(mapply(x3, x1))
#     x5 = dedupe(mapply(x3, x2))
#     return difference(x5, x4)


# def f_zo_n(S: Samples, function: 'Callable', key: 'Callable', index: 'FL') -> 'Object':
#     ret_frozenset = f_zo(S, function, r_n)
#     return get_arg_rank_f(ret_frozenset, key, index)


def f_zo(S: Samples, function: 'Callable') -> 'Any':
    x1 = apply(first, S)
    x2 = apply(second, S)
    x4 = dedupe(mapply(function, x1))
    x5 = dedupe(mapply(function, x2))
    return difference(x5, x4)


def f_zo_n(S: Samples, function: 'Callable', pick: 'Callable') -> 'Object':
    ret_frozenset = f_zo(S, function)
    return pick(ret_frozenset)


def get_nth_t(container: 'Tuple', rank: 'FL') -> 'Any':
    """Nth item of container, 0-based"""
    if not hasattr(container, '__len__'):
        return None
    if rank < -len(container):
        return None
    if rank >= len(container):
        return None 
    return container[rank] if container else None


def get_nth_f(container: 'FrozenSet', rank: 'FL') -> 'Any':
    """Nth item of container, 0-based"""
    if not hasattr(container, '__iter__'):
        return ()
    if rank < 0:
        # For negative rank, reverse the iterator
        iterator = iter(reversed(tuple(container)))
        for _ in range(-rank-1):
            next(iterator, ())
    else:
        iterator = iter(container)
        for _ in range(rank):
            next(iterator, ())
    return next(iterator, ())


# Original sorting with: key=identity
# Reverse sorting with: key=invert (only for numeric types)
def get_nth_by_key_t( container: 'Tuple', rank: 'FL', key = identity ) -> 'Any':
    """Nth item of container, 0-based, using key function"""
    sorted_tuple = sorted(container, key=key)
    return sorted_tuple[rank] if sorted_tuple else None


# Original sorting with: key=identity
# Reverse sorting with: key=invert (only for numeric types)
def get_nth_by_key_f( container: 'FrozenSet', rank: 'F_', key = identity ) -> 'Any':
    """Nth item of container, 0-based, using key function"""
    sorted_frozenset = sorted(container, key=key)
    iterator = iter(sorted_frozenset)
    for _ in range(rank):
        next(iterator, None)
    return next(iterator, None)


def o_g( grid: 'Grid', type: 'R8' ) -> 'Objects':
    if type == 0:
        return objects(grid, False, False, False)
    elif type == 1:
        return objects(grid, False, False, True)
    elif type == 2:
        return objects(grid, False, True, False)
    elif type == 3:
        return objects(grid, False, True, True)
    elif type == 4:
        return objects(grid, True, False, False)
    elif type == 5:
        return objects(grid, True, False, True)
    elif type == 6:
        return objects(grid, True, True, False)
    elif type == 7:
        return objects(grid, True, True, True)


def mir_rot_t( grid: 'Grid', type: 'A8' ) -> 'Grid':
    if type == 0:
        # Horizontal mirror
        return hmirror_t(grid)
    elif type == 1:
        # Diagonal mirror
        return dmirror_t(grid)
    elif type == 2:
        # Vertical mirror
        return vmirror_t(grid)
    elif type == 3:
        # Counter-diagonal mirror
        return cmirror_t(grid)
    elif type == 4:
        # Quarter rotation clockwise
        return rot90(grid)
    elif type == 5:
        # Half rotation
        return rot180(grid)
    elif type == 6:
        # Quarter rotation counter-clockwise
        return rot270(grid)
    return grid


def mir_rot_f( patch: 'Patch', type: 'A4' ) -> 'Patch':
    if type == 0:
        # Horizontal mirror
        return hmirror_f(patch)
    elif type == 1:
        # Diagonal mirror
        return dmirror_f(patch)
    elif type == 2:
        # Vertical mirror
        return vmirror_f(patch)
    elif type == 3:
        # Counter-diagonal mirror
        return cmirror_f(patch)
    return patch


# NOTE rank can go positive or negative
# rank=0: most common, rank=-1: least common
def get_color_rank_t( grid: 'Grid', rank: 'FL' ) -> 'C_':
    colors = [v for row in grid for v in row]
    ranked = Counter(colors).most_common()
    return ranked[rank][0] if -len(ranked) <= rank < len(ranked) else None


# NOTE rank can go positive or negative
# rank=0: most common, rank=-1: least common
def get_color_rank_f( obj: 'Object', rank: 'FL' ) -> 'C_':
    colors = [v for v, _ in obj]
    ranked = Counter(colors).most_common()
    return ranked[rank][0] if -len(ranked) <= rank < len(ranked) else None


def get_rank( container: 'IntegerSet', rank: 'FL') -> 'Integer':
    if not all(isinstance(e, int) for e in container):
        return None
    ranked = sorted(container, reverse=True)
    return ranked[rank] if -len(ranked) <= rank < len(ranked) else 0


def get_arg_rank( container: 'Container', compfunc: 'Callable', rank: 'FL') -> 'Any':
    ranked = sorted(container, key=compfunc, reverse=True)
    return ranked[rank] if -len(ranked) <= rank < len(ranked) else None


def get_arg_rank_t( container: 'Tuple', compfunc: 'Callable', rank: 'FL') -> 'Any':
    ranked = sorted(container, key=compfunc, reverse=True)
    return ranked[rank] if -len(ranked) <= rank < len(ranked) else None


def get_arg_rank_f( container: 'FrozenSet', compfunc: 'Callable', rank: 'FL') -> 'Any':
    ranked = sorted(container, key=compfunc, reverse=True)
    return ranked[rank] if -len(ranked) <= rank < len(ranked) else None


def get_val_rank( container: 'Container', compfunc: 'Callable', rank: 'FL') -> 'Any':
    ranked = sorted(container, key=compfunc)
    if -len(ranked) <= rank < len(ranked):
        return compfunc(ranked[rank])
    return compfunc(0)


def get_val_rank_t( container: 'Tuple', compfunc: 'Callable', rank: 'FL') -> 'Any':
    ranked = sorted(container, key=compfunc)
    if -len(ranked) <= rank < len(ranked):
        return compfunc(ranked[rank])
    return compfunc(0)


def get_val_rank_f( container: 'FrozenSet', compfunc: 'Callable', rank: 'FL') -> 'Any':
    ranked = sorted(container, key=compfunc)
    if -len(ranked) <= rank < len(ranked):
        return compfunc(ranked[rank])
    return compfunc(0)


def get_common_rank( container: 'Container', rank: 'FL') -> 'Any':
    ranked = sorted(set(container), key=container.count)
    return ranked[rank] if -len(ranked) <= rank < len(ranked) else None


def get_common_rank_t( container: 'Tuple', rank: 'FL') -> 'Any':
    ranked = sorted(set(container), key=container.count)
    return ranked[rank] if -len(ranked) <= rank < len(ranked) else None


def get_common_rank_f( container: 'FrozenSet', rank: 'FL') -> 'Any':
    # Since frozensets have unique elements, convert to list first
    container_list = list(container)
    ranked = sorted(set(container_list), key=container_list.count)
    return ranked[rank] if -len(ranked) <= rank < len(ranked) else None


def add(
    a: 'Numerical',
    b: 'Numerical'
) -> 'Numerical':
    """ addition """
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] + b[0], a[1] + b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a + b[0], a + b[1])
    return (a[0] + b, a[1] + b)


def subtract(
    a: 'Numerical',
    b: 'Numerical'
) -> 'Numerical':
    """ subtraction """
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] - b[0], a[1] - b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a - b[0], a - b[1])
    return (a[0] - b, a[1] - b)


def multiply(
    a: 'Numerical',
    b: 'Numerical'
) -> 'Numerical':
    """ multiplication """
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] * b[0], a[1] * b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a * b[0], a * b[1])
    return (a[0] * b, a[1] * b)
    

def divide(
    a: 'Numerical',
    b: 'Numerical'
) -> 'Numerical':
    """ floor division """
    if isinstance(a, int) and isinstance(b, int):
        return a // b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] // b[0], a[1] // b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a // b[0], a // b[1])
    return (a[0] // b, a[1] // b)


def invert(
    n: 'Numerical'
) -> 'Numerical':
    """ inversion with respect to addition """
    return -n if isinstance(n, int) else (-n[0], -n[1])


def even(
    n: 'Integer'
) -> 'Boolean':
    """ evenness """
    return n % 2 == 0


def double(
    n: 'Numerical'
) -> 'Numerical':
    """ scaling by two """
    return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)


def halve(
    n: 'Numerical'
) -> 'Numerical':
    """ scaling by one half """
    return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)


def flip(
    b: 'Boolean'
) -> 'Boolean':
    """ logical not """
    return not b


def equality(
    a: 'Any',
    b: 'Any'
) -> 'Boolean':
    """ equality """
    return a == b


def contained(
    value: 'Any',
    container: 'Container'
) -> 'Boolean':
    """ element of """
    return value in container


def combine(
    a: 'Container',
    b: 'Container'
) -> 'Container':
    """ union """
    return type(a)((*a, *b))


def intersection(
    a: 'FrozenSet',
    b: 'FrozenSet'
) -> 'FrozenSet':
    """ returns the intersection of two containers """
    return a & b


def difference(
    a: 'FrozenSet',
    b: 'FrozenSet'
) -> 'FrozenSet':
    """ set difference """
    return type(a)(e for e in a if e not in b)


def dedupe(
    tup: 'Tuple'
) -> 'Tuple':
    """ remove duplicates """
    return tuple(e for i, e in enumerate(tup) if tup.index(e) == i)


def order(
    container: 'Container',
    compfunc: 'Callable'
) -> 'Tuple':
    """ order container by custom key """
    return tuple(sorted(container, key=compfunc))


def repeat(
    item: 'Any',
    num: 'C_'
) -> 'Tuple':
    """ repetition of item within vector """
    return tuple(item for _ in range(num))


def greater(
    a: 'Integer',
    b: 'Integer'
) -> 'Boolean':
    """ greater """
    return a > b


def size(
    container: 'Container'
) -> 'Integer':
    """ cardinality """
    return len(container)


def merge(
    containers: 'ContainerContainer'
) -> 'Container':
    """ merging """
    return type(containers)(e for c in containers for e in c)


def merge_f(
    containers: 'ContainerContainer'
) -> 'Container':
    """ merging """
    return type(containers)(e for c in containers for e in c)


def merge_t(
    containers: 'ContainerContainer'
) -> 'Container':
    """ merging """
    return type(containers)(e for c in containers for e in c)


# See get_rank
def maximum(
    container: 'IntegerSet'
) -> 'Integer':
    """ maximum """
    return max(container, default=0)


# See get_rank
def minimum(
    container: 'IntegerSet'
) -> 'Integer':
    """ minimum """
    return min(container, default=0)


# See get_val_rank
def valmax(
    container: 'Container',
    compfunc: 'Callable'
) -> 'Integer':
    """ maximum by custom function """
    return compfunc(max(container, key=compfunc, default=0))


# See get_val_rank
def valmin(
    container: 'Container',
    compfunc: 'Callable'
) -> 'Integer':
    """ minimum by custom function """
    return compfunc(min(container, key=compfunc, default=0))


# See get_arg_rank
def argmax(
    container: 'Container',
    compfunc: 'Callable'
) -> 'Any':
    """ largest item by custom order """
    return max(container, key=compfunc)


# See get_arg_rank
def argmin(
    container: 'Container',
    compfunc: 'Callable'
) -> 'Any':
    """ smallest item by custom order """
    return min(container, key=compfunc)


def mostcommon(
    container: 'Container'
) -> 'Any':
    """ most common item """
    return max(set(container), key=container.count)


def leastcommon(
    container: 'Container'
) -> 'Any':
    """ least common item """
    return min(set(container), key=container.count)


def initset(
    value: 'Any'
) -> 'FrozenSet':
    """ initialize container """
    return frozenset({value})


def both(
    a: 'Boolean',
    b: 'Boolean'
) -> 'Boolean':
    """ logical and """
    return a and b


def either(
    a: 'Boolean',
    b: 'Boolean'
) -> 'Boolean':
    """ logical or """
    return a or b


def increment(
    x: 'Numerical'
) -> 'Numerical':
    """ incrementing """
    return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)


def decrement(
    x: 'Numerical'
) -> 'Numerical':
    """ decrementing """
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)


def crement(
    x: 'Numerical'
) -> 'Numerical':
    """ incrementing positive and decrementing negative """
    if isinstance(x, int):
        return 0 if x == 0 else (x + 1 if x > 0 else x - 1)
    return (
        0 if x[0] == 0 else (x[0] + 1 if x[0] > 0 else x[0] - 1),
        0 if x[1] == 0 else (x[1] + 1 if x[1] > 0 else x[1] - 1)
    )


def sign(
    x: 'Numerical'
) -> 'Numerical':
    """ sign """
    if isinstance(x, int):
        return 0 if x == 0 else (1 if x > 0 else -1)
    return (
        0 if x[0] == 0 else (1 if x[0] > 0 else -1),
        0 if x[1] == 0 else (1 if x[1] > 0 else -1)
    )


def positive(
    x: 'Integer'
) -> 'Boolean':
    """ positive """
    return x > 0


def toivec(
    i: 'Integer'
) -> 'IJ':
    """ vector pointing vertically """
    return (i, 0)


def tojvec(
    j: 'Integer'
) -> 'IJ':
    """ vector pointing horizontally """
    return (0, j)


def extract(
    container: 'Container',
    condition: 'Callable'
) -> 'Any':
    """ first element of container that satisfies condition """
    return next((e for e in container if condition(e)), None)


def totuple(
    container: 'FrozenSet'
) -> 'Tuple':
    """ conversion to tuple """
    return tuple(container)


def insert(
    value: 'Any',
    container: 'FrozenSet'
) -> 'FrozenSet':
    """ insert item into container """
    return container.union(frozenset({value}))


def other(
    container: 'Container',
    value: 'Any'
) -> 'Any':
    """ other value in the container """
    return first(remove(value, container))


def interval(
    start: 'Integer',
    stop: 'Integer',
    step: 'Integer'
) -> 'Tuple':
    """ range """
    return tuple(range(start, stop, step))


def astuple(
    a: 'Integer',
    b: 'Integer'
) -> 'Tuple':
    """ constructs a tuple """
    return (b[0], b[1], a) if isinstance(b, tuple) else (a, b)


def astriple(
    i: 'I_',
    j: 'J_',
    c: 'C_'
) -> 'Tuple':
    """ constructs a triple tuple """
    return (i, j, c)


def product(
    a: 'Container',
    b: 'Container'
) -> 'FrozenSet':
    """ cartesian product """
    return frozenset((i, j) for j in b for i in a)


def pair(
    a: 'Tuple',
    b: 'Tuple'
) -> 'TupleTuple':
    """ zipping of two tuples """
    return tuple(zip(a, b))


def branch(
    condition: 'Boolean',
    a: 'Any',
    b: 'Any'
) -> 'Any':
    """ if else branching """
    return a if condition else b


def c_branch(
    condition: 'Boolean',
    a: 'C_',
    b: 'C_'
) -> 'Any':
    """ if else branching """
    return a if condition else b


def compose(
    outer: 'Callable',
    inner: 'Callable'
) -> 'Callable':
    """ function composition """
    return lambda x: outer(inner(x))


def chain(
    h: 'Callable',
    g: 'Callable',
    f: 'Callable',
) -> 'Callable':
    """ function composition with three functions """
    return lambda x: h(g(f(x)))


def matcher(
    function: 'Callable',
    target: 'Any'
) -> 'Callable':
    """ construction of equality function """
    return lambda x: function(x) == target


def rbind(
    function: 'Callable',
    fixed: 'Any'
) -> 'Callable':
    """ fix the rightmost argument """
    # Use _original_argcount if available (for decorated functions)
    if hasattr(function, '_original_argcount'):
        n = function._original_argcount
    else:
        n = function.__code__.co_argcount

    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)


# def rbind_1(
#     function: 'Callable',
#     fixed: 'Any'
# ) -> 'Callable':
#     """ fix the rightmost argument """
#     return lambda x: function(x, fixed)


# def rbind_2(
#     function: 'Callable',
#     fixed: 'Any'
# ) -> 'Callable':
#     """ fix the rightmost argument """
#     return lambda x, y: function(x, y, fixed)


# def rbind_3(
#     function: 'Callable',
#     fixed: 'Any'
# ) -> 'Callable':
#     """ fix the rightmost argument """
#     return lambda x, y, z: function(x, y, z, fixed)


def lbind(
    function: 'Callable',
    fixed: 'Any'
) -> 'Callable':
    """ fix the leftmost argument """
    # Use _original_argcount if available (for decorated functions)
    if hasattr(function, '_original_argcount'):
        n = function._original_argcount
    else:
        n = function.__code__.co_argcount

    if n == 2:
        return lambda y: function(fixed, y)
    elif n == 3:
        return lambda y, z: function(fixed, y, z)
    else:
        return lambda y, z, a: function(fixed, y, z, a)


# def lbind_1(
#     function: 'Callable',
#     fixed: 'Any'
# ) -> 'Callable':
#     """ fix the leftmost argument """
#     return lambda y: function(fixed, y)


# def lbind_2(
#     function: 'Callable',
#     fixed: 'Any'
# ) -> 'Callable':
#     """ fix the leftmost argument """
#     return lambda y, z: function(fixed, y, z)


# def lbind_3(
#     function: 'Callable',
#     fixed: 'Any'
# ) -> 'Callable':
#     """ fix the leftmost argument """
#     return lambda y, z, a: function(fixed, y, z, a)


def power(
    function: 'Callable',
    n: 'Integer'
) -> 'Callable':
    """ power of function """
    return function if n == 1 else compose(function, power(function, n - 1))


def fork(
    outer: 'Callable',
    a: 'Callable',
    b: 'Callable'
) -> 'Callable':
    """ creates a wrapper function """
    return lambda x: outer(a(x), b(x))


def combine_t(
    a: 'Tuple',
    b: 'Tuple'
) -> 'Tuple':
    """ union for tuples """
    return a + b


def combine_f(
    a: 'FrozenSet',
    b: 'FrozenSet'
) -> 'FrozenSet':
    """ union for frozensets """
    return a | b


def size_t(
    container: 'Tuple'
) -> 'Integer':
    """ cardinality of tuple """
    return len(container)


def size_f(
    container: 'FrozenSet'
) -> 'Integer':
    """ cardinality of frozenset """
    return len(container)

# See get_val_rank_t
def valmax_t(
    container: 'Tuple',
    compfunc: 'Callable'
) -> 'Integer':
    """ maximum by custom function for tuples """
    return compfunc(max(container, key=compfunc, default=0))


# See get_val_rank_f
def valmax_f(
    container: 'FrozenSet',
    compfunc: 'Callable'
) -> 'Integer':
    """ maximum by custom function for frozensets """
    return compfunc(max(container, key=compfunc, default=0))

# See get_val_rank_t
def valmin_t(
    container: 'Tuple',
    compfunc: 'Callable'
) -> 'Integer':
    """ minimum by custom function for tuples """
    return compfunc(min(container, key=compfunc, default=0))


# See get_val_rank_f
def valmin_f(
    container: 'FrozenSet',
    compfunc: 'Callable'
) -> 'Integer':
    """ minimum by custom function for frozensets """
    return compfunc(min(container, key=compfunc, default=0))


# See get_arg_rank_t
def argmax_t(
    container: 'Tuple',
    compfunc: 'Callable'
) -> 'Any':
    """ largest item by custom order for tuples """
    return max(container, key=compfunc)


# See get_arg_rank_f
def argmax_f(
    container: 'FrozenSet',
    compfunc: 'Callable'
) -> 'Any':
    """ largest item by custom order for frozensets """
    return max(container, key=compfunc)


# See get_arg_rank_t
def argmin_t(
    container: 'Tuple',
    compfunc: 'Callable'
) -> 'Any':
    """ smallest item by custom order for tuples """
    return min(container, key=compfunc)


# See get_arg_rank_f
def argmin_f(
    container: 'FrozenSet',
    compfunc: 'Callable'
) -> 'Any':
    """ smallest item by custom order for frozensets """
    return min(container, key=compfunc)


# See get_common_rank_t
def mostcommon_t(
    container: 'Tuple'
) -> 'Any':
    """ most common item in tuple """
    return max(set(container), key=container.count)


# See get_common_rank_f
def mostcommon_f(
    container: 'FrozenSet'
) -> 'Any':
    """ most common item in frozenset - returns the item itself for frozensets """
    # Since frozensets have unique elements, convert to list first
    container_list = list(container)
    return max(set(container_list), key=container_list.count)


# See get_common_rank_t
def leastcommon_t(
    container: 'Tuple'
) -> 'Any':
    """ least common item in tuple """
    return min(set(container), key=container.count)


# See get_common_rank_f
def leastcommon_f(
    container: 'FrozenSet'
) -> 'Any':
    """ least common item in frozenset - returns the item itself for frozensets """
    # Since frozensets have unique elements, convert to list first
    container_list = list(container)
    return min(set(container_list), key=container_list.count)


def sfilter(
    container: 'Container',
    condition: 'Callable'
) -> 'Container':
    """ keep elements in container that satisfy condition """
    return type(container)(e for e in container if condition(e))


def sfilter_t(
    container: 'Tuple',
    condition: 'Callable'
) -> 'Tuple':
    """ keep elements in tuple that satisfy condition """
    return tuple(e for e in container if condition(e))


def sfilter_f(
    container: 'FrozenSet',
    condition: 'Callable'
) -> 'FrozenSet':
    """ keep elements in frozenset that satisfy condition """
    return frozenset(e for e in container if condition(e))


def mfilter(
    container: 'Container',
    function: 'Callable'
) -> 'FrozenSet':
    """ filter and merge """
    return merge_f(sfilter(container, function))


def mfilter_t(
    container: 'Tuple',
    function: 'Callable'
) -> 'FrozenSet':
    """ filter and merge for tuples """
    # Directly create a frozenset of filtered elements
    return frozenset(e for e in container if function(e))


def mfilter_f(
    container: 'FrozenSet',
    function: 'Callable'
) -> 'FrozenSet':
    """ filter and merge for frozensets """
    # Directly create a frozenset of filtered elements
    # return frozenset(e for e in container if function(e))
    return merge_f(sfilter(container, function))


# def first(
#     container: 'Container'
# ) -> 'Any':
#     """ first item of container """
#     return next(iter(container), None) if container else None


def first_t(
    container: 'Tuple'
) -> 'Any':
    """ first item of tuple """
    return container[0] if container else None


def first_f(
    container: 'FrozenSet'
) -> 'Any':
    """ first item of frozenset """
    return next(iter(container), None) if container else None


def last(
    container: 'Container'
) -> 'Any':
    """ last item of container """
    return max(enumerate(container))[1] if container else None


def last_t(
    container: 'Tuple'
) -> 'Any':
    """ last item of tuple """
    return container[-1] if container else None


def last_f(
    container: 'FrozenSet'
) -> 'Any':
    """ last item of frozenset - not truly ordered, so returns an arbitrary element """
    return max(enumerate(container))[1] if container else None


def remove(
    value: 'Any',
    container: 'Container'
) -> 'Container':
    """ remove item from container """
    return type(container)(e for e in container if e != value)


def remove_t(
    value: 'Any',
    container: 'Tuple'
) -> 'Tuple':
    """ remove item from tuple """
    return tuple(e for e in container if e != value)


def remove_f(
    value: 'Any',
    container: 'FrozenSet'
) -> 'FrozenSet':
    """ remove item from frozenset """
    # return container - {value}
    return type(container)(e for e in container if e != value)


def other_t(
    container: 'Tuple',
    value: 'Any'
) -> 'Any':
    """ other value in the tuple """
    # Only proceed if the value is actually in the container
    if value not in container:
        return None
    
    filtered = tuple(e for e in container if e != value)
    return filtered[0] if filtered else None


def other_f(
    container: 'FrozenSet',
    value: 'Any'
) -> 'Any':
    """ other value in the frozenset """
    # Only proceed if the value is actually in the container
    if value not in container:
        return None
    
    filtered = remove_f(value, container)
    return next(iter(filtered)) if filtered else None


def apply(
    function: 'Callable',
    container: 'Container'
) -> 'Container':
    """ apply function to each item in container """
    return type(container)(function(e) for e in container)


def apply_t(
    function: 'Callable',
    container: 'Tuple'
) -> 'Tuple':
    """ apply function to each item in tuple """
    return tuple(function(e) for e in container)


def apply_f(
    function: 'Callable',
    container: 'FrozenSet'
) -> 'FrozenSet':
    """ apply function to each item in frozenset """
    return type(container)(function(e) for e in container)


def rapply(
    functions: 'Container',
    value: 'Any'
) -> 'Container':
    """ apply each function in container to value """
    return type(functions)(function(value) for function in functions)


def rapply_t(
    functions: 'Tuple',
    value: 'Any'
) -> 'Tuple':
    """ apply each function in tuple to value """
    return tuple(function(value) for function in functions)


def rapply_f(
    functions: 'FrozenSet',
    value: 'Any'
) -> 'FrozenSet':
    """ apply each function in frozenset to value """
    return type(functions)(function(value) for function in functions)


def mapply(
    function: 'Callable',
    container: 'ContainerContainer'
) -> 'FrozenSet':
    """ apply and merge """
    return merge(apply(function, container))


def mapply_t(
    function: 'Callable',
    container: 'Tuple'
) -> 'Tuple':
    """ apply and merge for tuples"""
    return merge_t(apply_t(function, container))


def mapply_f(
    function: 'Callable',
    container: 'FrozenSet'
) -> 'FrozenSet':
    """ apply and merge for frozensets """
    return merge_f(apply_f(function, container))


def papply(
    function: 'Callable',
    a: 'Tuple',
    b: 'Tuple'
) -> 'Tuple':
    """ apply function on two vectors """
    return tuple(function(i, j) for i, j in zip(a, b))


def mpapply(
    function: 'Callable',
    a: 'Tuple',
    b: 'Tuple'
) -> 'Tuple':
    """ apply function on two vectors and merge """
    return merge_t(papply(function, a, b))


def prapply(
    function,
    a: 'Container',
    b: 'Container'
) -> 'FrozenSet':
    """ apply function on cartesian product """
    return frozenset(function(i, j) for j in b for i in a)


# def mostcolor(
#     element: Element
# ) -> 'Integer':
#     """ most common color """
#     values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
#     return max(set(values), key=values.count)
    

def mostcolor_t(
    grid: 'Grid'
) -> 'Integer':
    """ most common color """
    values = [v for r in grid for v in r]
    return max(set(values), key=values.count)
    

def mostcolor_f(
    obj: 'Object'
) -> 'Integer':
    """ most common color """
    values = [v for _, _, v in obj]
    return max(set(values), key=values.count)
    

# def leastcolor(
#     element: Element
# ) -> 'Integer':
#     """ least common color """
#     values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
#     return min(set(values), key=values.count)


def leastcolor_t(
    grid: 'Grid'
) -> 'Integer':
    """ least common color """
    values = [v for r in grid for v in r]
    return min(set(values), key=values.count)


def leastcolor_f(
    obj: 'Object'
) -> 'Integer':
    """ least common color """
    values = [v for _, _, v in obj]
    return min(set(values), key=values.count)


# def height(
#     piece: Piece
# ) -> 'Integer':
#     """ height of grid or patch """
#     if len(piece) == 0:
#         return 0
#     if isinstance(piece, tuple):
#         return len(piece)
#     return lowermost(piece) - uppermost(piece) + 1


# def width(
#     piece: Piece
# ) -> 'Integer':
#     """ width of grid or patch """
#     if len(piece) == 0:
#         return 0
#     if isinstance(piece, tuple):
#         return len(piece[0])
#     return rightmost(piece) - leftmost(piece) + 1


def height_t(
    piece: 'Tuple'
) -> 'Integer':
    """ height of grid """
    return len(piece)


def height_f(
    piece: 'Indices'
) -> 'Integer':
    """ height of patch """
    return 0 if len(piece) == 0 else lowermost(piece) - uppermost(piece) + 1


def height_i(
    piece: 'Indices'
) -> 'Integer':
    """ height of patch """
    return 0 if len(piece) == 0 else lowermost_i(piece) - uppermost_i(piece) + 1


def height_o(
    piece: 'Object'
) -> 'Integer':
    """ height of patch """
    return 0 if len(piece) == 0 else lowermost_o(piece) - uppermost_o(piece) + 1


def width_t(
    piece: 'Tuple'
) -> 'Integer':
    """ width of grid """
    return len(piece[0]) if piece else 0


def width_f(
    piece: 'Indices'
) -> 'Integer':
    """ width of patch """
    return 0 if len(piece) == 0 else rightmost(piece) - leftmost(piece) + 1


def width_i(
    piece: 'Indices'
) -> 'Integer':
    """ width of patch """
    return 0 if len(piece) == 0 else rightmost_i(piece) - leftmost_i(piece) + 1


def width_o(
    piece: 'Object'
) -> 'Integer':
    """ width of patch """
    return 0 if len(piece) == 0 else rightmost_o(piece) - leftmost_o(piece) + 1


def shape_t(
    piece: 'Tuple'
) -> 'IJ':
    """ height and width of grid """
    return (len(piece), len(piece[0]) if piece else 0)


def shape_f(
    piece: 'FrozenSet'
) -> 'IJ':
    """ height and width of patch """
    return (height_f(piece), width_f(piece))


def col_row(
    patch: 'Patch',
    type: 'R4'
) -> 'Integer':
    """ indices of corners """
    if type == 0:
        return lowermost(patch)
    elif type == 1:
        return uppermost(patch)
    elif type == 2:
        return leftmost(patch)
    elif type == 3:
        return rightmost(patch)


def lowermost(
    patch: 'Patch'
) -> 'Integer':
    """ row index of lowermost occupied cell """
    return max(i for i, j in toindices(patch)) if patch else -math.inf


def lowermost_i(
    indices: 'Indices'
) -> 'Integer':
    """ row index of lowermost occupied cell """
    return max(i for i, j in toindices_i(indices)) if indices else -math.inf


def lowermost_o(
    obj: 'Object'
) -> 'Integer':
    """ row index of lowermost occupied cell """
    return max(i for i, j in toindices_o(obj)) if obj else -math.inf


def uppermost(
    patch: 'Patch'
) -> 'Integer':
    """ row index of uppermost occupied cell """
    return min(i for i, j in toindices(patch)) if patch else math.inf


def uppermost_i(
    indices: 'Indices'
) -> 'Integer':
    """ row index of uppermost occupied cell """
    return min(i for i, j in toindices_i(indices)) if indices else math.inf


def uppermost_o(
    obj: 'Object'
) -> 'Integer':
    """ row index of uppermost occupied cell """
    return min(i for i, j in toindices_o(obj)) if obj else math.inf


def leftmost(
    patch: 'Patch'
) -> 'Integer':
    """ column index of leftmost occupied cell """
    return min(j for i, j in toindices(patch)) if patch else math.inf


def leftmost_i(
    indices: 'Indices'
) -> 'Integer':
    """ column index of leftmost occupied cell """
    return min(j for i, j in toindices_i(indices)) if indices else math.inf


def leftmost_o(
    obj: 'Object'
) -> 'Integer':
    """ column index of leftmost occupied cell """
    return min(j for i, j in toindices_o(obj)) if obj else math.inf


def rightmost(
    patch: 'Patch'
) -> 'Integer':
    """ column index of rightmost occupied cell """
    return max(j for i, j in toindices(patch)) if patch else -math.inf


def rightmost_i(
    indices: 'Indices'
) -> 'Integer':
    """ column index of rightmost occupied cell """
    return max(j for i, j in toindices_i(indices))


def rightmost_o(
    obj: 'Object'
) -> 'Integer':
    """ column index of rightmost occupied cell """
    return max(j for i, j in toindices_o(obj))


def square_t(
    piece: 'Tuple'
) -> 'Boolean':
    """ whether the grid forms a square """
    return len(piece) == len(piece[0]) if piece else False


def square_f(
    piece: 'FrozenSet'
) -> 'Boolean':
    """ whether the patch forms a square """
    return height_f(piece) * width_f(piece) == len(piece) and height_f(piece) == width_f(piece)


# def palette(
#     element: Element
# ) -> 'IntegerSet':
#     """ colors occurring in object or grid """
#     if isinstance(element, tuple):
#         return frozenset({v for r in element for v in r})
#     return frozenset({v for v, _ in element})


def palette_t(
    element: 'Tuple'
) -> 'IntegerSet':
    """ colors occurring in grid """
    return frozenset(v for r in element for v in r)


def palette_f(
    element: 'FrozenSet'
) -> 'IntegerSet':
    """ colors occurring in object """
    return frozenset(c for _, _, c in element)


def normalize_t(
    piece: 'Tuple'
) -> 'Tuple':
    """ moves upper left corner of grid to origin (no-op for grid) """
    return piece


def normalize(
    indices: 'Indices'
) -> 'Indices':
    """ moves upper left corner of indices to origin """
    if len(indices) == 0:
        return indices
    return shift(indices, (-uppermost(indices), -leftmost(indices)))


def normalize_i(
    indices: 'Indices'
) -> 'Indices':
    """ moves upper left corner of indices to origin """
    if len(indices) == 0:
        return indices
    return shift(indices, (-uppermost_i(indices), -leftmost_i(indices)))


def normalize_o(
    obj: 'Object'
) -> 'Object':
    """ moves upper left corner of obj to origin """
    if len(obj) == 0:
        return obj
    return shift(obj, (-uppermost_o(obj), -leftmost_o(obj)))


def hmirror_t(
    piece: 'Tuple'
) -> 'Tuple':
    """ mirroring grid along horizontal """
    return piece[::-1]


def hmirror_f(
    piece: 'FrozenSet'
) -> 'FrozenSet':
    """ mirroring patch along horizontal """
    if len(piece) == 0:
        return frozenset()
    
    d = ulcorner(piece)[0] + lrcorner(piece)[0]
    if len(next(iter(piece))) == 3:
        return frozenset((d - i, j, c) for i, j, c in piece)
    return frozenset((d - i, j) for i, j in piece)


def hmirror_i(
    indices: 'Indices'
) -> 'Indices':
    """ mirroring patch along horizontal """
    if len(indices) == 0:
        return frozenset()
    
    d = ulcorner(indices)[0] + lrcorner(indices)[0]
    return frozenset((d - i, j) for i, j in indices)


def hmirror_o(
    obj: 'Object'
) -> 'Object':
    """ mirroring patch along horizontal """
    if len(obj) == 0:
        return frozenset()
    
    d = ulcorner(obj)[0] + lrcorner(obj)[0]
    return frozenset((d - i, j, c) for i, j, c in obj)


def vmirror_t(
    piece: 'Tuple'
) -> 'Tuple':
    """ mirroring grid along vertical """
    return tuple(row[::-1] for row in piece)


def vmirror_f(
    piece: 'FrozenSet'
) -> 'FrozenSet':
    """ mirroring patch along vertical """
    if len(piece) == 0:
        return frozenset()
    
    d = ulcorner(piece)[1] + lrcorner(piece)[1]
    if len(next(iter(piece))) == 3:
        return frozenset((i, d - j, c) for i, j, c in piece)
    return frozenset((i, d - j) for i, j in piece)


def vmirror_i(
    indices: 'Indices'
) -> 'Indices':
    """ mirroring patch along vertical """
    if len(indices) == 0:
        return frozenset()
    
    d = ulcorner(indices)[1] + lrcorner(indices)[1]
    return frozenset((i, d - j) for i, j in indices)


def vmirror_o(
    obj: 'Object'
) -> 'Object':
    """ mirroring patch along vertical """
    if len(obj) == 0:
        return frozenset()
    
    d = ulcorner(obj)[1] + lrcorner(obj)[1]
    return frozenset((i, d - j, c) for i, j, c in obj)


def dmirror_t(
    piece: 'Tuple'
) -> 'Tuple':
    """ mirroring grid along diagonal """
    return tuple(zip(*piece))


def dmirror_f(
    piece: 'FrozenSet'
) -> 'FrozenSet':
    """ mirroring patch along diagonal """
    if len(piece) == 0:
        return frozenset()
    
    a, b = ulcorner(piece)
    if len(next(iter(piece))) == 3:
        return frozenset((j - b + a, i - a + b, c) for i, j, c in piece)
    return frozenset((j - b + a, i - a + b) for i, j in piece)


def dmirror_i(
    indices: 'Indices'
) -> 'Indices':
    """ mirroring patch along diagonal """
    if len(indices) == 0:
        return frozenset()
    
    a, b = ulcorner(indices)
    return frozenset((j - b + a, i - a + b) for i, j in indices)


def dmirror_o(
    obj: 'Object'
) -> 'Object':
    """ mirroring patch along diagonal """
    if len(obj) == 0:
        return frozenset()
    
    a, b = ulcorner(obj)
    return frozenset((j - b + a, i - a + b, c) for i, j, c in obj)


def cmirror_t(
    piece: 'Tuple'
) -> 'Tuple':
    """ mirroring grid along counterdiagonal """
    return tuple(zip(*(r[::-1] for r in piece[::-1])))


def cmirror_f(
    piece: 'FrozenSet'
) -> 'FrozenSet':
    """ mirroring patch along counterdiagonal """
    return frozenset() if len(piece) == 0 else vmirror(dmirror(vmirror(piece)))


def upscale_t(
    element: 'Tuple',
    factor: 'Integer'
) -> 'Tuple':
    """ upscale grid """
    g = ()
    for row in element:
        upscaled_row = ()
        for value in row:
            upscaled_row = upscaled_row + tuple(value for _ in range(factor))
        g = g + tuple(upscaled_row for _ in range(factor))
    return g


def upscale_f(
    element: 'FrozenSet',
    factor: 'Integer'
) -> 'FrozenSet':
    """ upscale object """
    if len(element) == 0:
        return frozenset()
    di_inv, dj_inv = ulcorner(element)
    di, dj = (-di_inv, -dj_inv)
    normed_obj = shift(element, (di, dj))
    o = set()
    for i, j, c in normed_obj:
        for io, jo in itertools.product(range(factor), range(factor)):
            o.add((i * factor + io, j * factor + jo, c))
    return shift(frozenset(o), (di_inv, dj_inv))


def downscale(
    grid: 'Grid',
    factor: 'Integer'
) -> 'Grid':
    """ downscale grid """
    h, w = len(grid), len(grid[0])
    g = ()
    for i in range(h):
        r = ()
        for j in range(w):
            if j % factor == 0:
                r = r + (grid[i][j],)
        g = g + (r, )
    h = len(g)
    dsg = ()
    for i in range(h):
        if i % factor == 0:
            dsg = dsg + (g[i],)
    return dsg


def hconcat(
    a: 'Grid',
    b: 'Grid'
) -> 'Grid':
    """ concatenate two grids horizontally """
    return tuple(i + j for i, j in zip(a, b))


def vconcat(
    a: 'Grid',
    b: 'Grid'
) -> 'Grid':
    """ concatenate two grids vertically """
    return a + b


def subgrid(
    patch: 'Patch',
    grid: 'Grid'
) -> 'Grid':
    """ smallest subgrid containing object """
    if patch == frozenset():
        return ()
    return crop(grid, ulcorner(patch), shape_f(patch))


def hsplit(
    grid: 'Grid',
    n: 'Integer'
) -> 'Tuple':
    """ split grid horizontally """
    h, w = len(grid), len(grid[0]) // n
    offset = len(grid[0]) % n != 0
    return tuple(crop(grid, (0, w * i + i * offset), (h, w)) for i in range(n))


def vsplit(
    grid: 'Grid',
    n: 'Integer'
) -> 'Tuple':
    """ split grid vertically """
    h, w = len(grid) // n, len(grid[0])
    offset = len(grid) % n != 0
    return tuple(crop(grid, (h * i + i * offset, 0), (h, w)) for i in range(n))


def cellwise(
    a: 'Grid',
    b: 'Grid',
    fallback: 'Integer'
) -> 'Grid':
    """ cellwise match of two grids """
    h, w = len(a), len(a[0])
    resulting_grid = ()
    for i in range(h):
        row = ()
        for j in range(w):
            a_value = a[i][j]
            value = a_value if a_value == b[i][j] else fallback
            row = row + (value,)
        resulting_grid = resulting_grid + (row, )
    return resulting_grid


def replace(
    grid: 'Grid',
    replacee: 'C_',
    replacer: 'C_'
) -> 'Grid':
    """ color substitution """
    return tuple(tuple(replacer if v == replacee else v for v in r) for r in grid)


def switch(
    grid: 'Grid',
    a: 'C_',
    b: 'C_'
) -> 'Grid':
    """ color switching """
    return tuple(
        tuple(v if v not in [a, b] else {a: b, b: a}[v] for v in r)
        for r in grid
    )


def center(
    patch: 'Patch'
) -> 'IJ':
    """ center of the patch """
    if uppermost(patch) is None:
        return None
    if leftmost(patch) is None:
        return None
    return (uppermost(patch) + height_f(patch) // 2, leftmost(patch) + width_f(patch) // 2)


def position(
    a: 'Patch',
    b: 'Patch'
) -> 'IJ':
    """ relative position between two patches """
    ia, ja = center(toindices(a))
    ib, jb = center(toindices(b))
    if ia == ib:
        return (0, 1 if ja < jb else -1)
    elif ja == jb:
        return (1 if ia < ib else -1, 0)
    elif ia < ib:
        return (1, 1 if ja < jb else -1)
    elif ia > ib:
        return (-1, 1 if ja < jb else -1)


def index(
    grid: 'Grid',
    loc: 'IJ'
) -> 'Integer':
    """ color at location """
    i, j = loc
    h, w = len(grid), len(grid[0])
    if not (0 <= i < h and 0 <= j < w):
        return None
    return grid[loc[0]][loc[1]] 


def canvas(
    color: 'C_',
    dimensions: 'IJ'
) -> 'Grid':
    """ grid construction """
    return tuple(tuple(color for j in range(dimensions[1])) for i in range(dimensions[0]))


def corners(
    patch: 'Patch'
) -> 'Indices':
    """ indices of corners """
    return frozenset({ulcorner(patch), urcorner(patch), llcorner(patch), lrcorner(patch)})


def connect(
    a: 'IJ',
    b: 'IJ'
) -> 'Indices':
    """ line between two points """
    # print(f"Connecting {a} to {b}")

    ai, aj = a
    bi, bj = b
    si = min(ai, bi)
    ei = max(ai, bi) + 1
    sj = min(aj, bj)
    ej = max(aj, bj) + 1
    if ai == bi:
        return frozenset((ai, j) for j in range(sj, ej))
    elif aj == bj:
        return frozenset((i, aj) for i in range(si, ei))
    elif bi - ai == bj - aj:
        return frozenset((i, j) for i, j in zip(range(si, ei), range(sj, ej)))
    elif bi - ai == aj - bj:
        return frozenset((i, j) for i, j in zip(range(si, ei), range(ej - 1, sj - 1, -1)))
    return frozenset()


def cover(
    grid: 'Grid',
    patch: 'Patch'
) -> 'Grid':
    """ remove object from grid """
    return fill(grid, mostcolor_t(grid), toindices(patch))


def trim(
    grid: 'Grid'
) -> 'Grid':
    """ trim border of grid """
    return tuple(r[1:-1] for r in grid[1:-1])


def move(
    grid: 'Grid',
    obj: 'Object',
    offset: 'IJ'
) -> 'Grid':
    """ move object on grid """
    return paint(cover(grid, obj), shift(obj, offset))


def tophalf(
    grid: 'Grid'
) -> 'Grid':
    """ upper half of grid """
    return grid[:len(grid) // 2]


def bottomhalf(
    grid: 'Grid'
) -> 'Grid':
    """ lower half of grid """
    return grid[len(grid) // 2 + len(grid) % 2:]


def lefthalf(
    grid: 'Grid'
) -> 'Grid':
    """ left half of grid """
    return rot270(tophalf(rot90(grid)))


def righthalf(
    grid: 'Grid'
) -> 'Grid':
    """ right half of grid """
    return rot270(bottomhalf(rot90(grid)))


def vfrontier(
    location: 'IJ'
) -> 'Indices':
    """ vertical frontier """
    return frozenset((i, location[1]) for i in range(30))


def hfrontier(
    location: 'IJ'
) -> 'Indices':
    """ horizontal frontier """
    return frozenset((location[0], j) for j in range(30))


def backdrop(
    patch: 'Patch'
) -> 'Indices':
    """ indices in bounding box of patch """
    if not hasattr(patch, '__len__') or len(patch) == 0:
        return frozenset()
    indices = toindices(patch)
    si, sj = ulcorner(indices)
    ei, ej = lrcorner(patch)
    return frozenset((i, j) for i in range(si, ei + 1) for j in range(sj, ej + 1))


def delta(
    patch: 'Patch'
) -> 'Indices':
    """ indices in bounding box but not part of patch """
    if not hasattr(patch, '__len__') or len(patch) == 0:
        return frozenset()
    return backdrop(patch) - toindices(patch)


def gravitate(
    source: 'Patch',
    destination: 'Patch'
) -> 'IJ':
    """ direction to move source until adjacent to destination """
    si, sj = center(source)
    di, dj = center(destination)
    i, j = 0, 0
    if vmatching(source, destination):
        i = 1 if si < di else -1
    else:
        j = 1 if sj < dj else -1
    gi, gj = i, j
    c = 0
    while not adjacent(source, destination) and c < 42:
        c += 1
        gi += i
        gj += j
        source = shift(source, (i, j))
    return (gi - i, gj - j)


def inbox(
    patch: 'Patch'
) -> 'Indices':
    """ inbox for patch """
    ai, aj = uppermost(patch) + 1, leftmost(patch) + 1
    bi, bj = lowermost(patch) - 1, rightmost(patch) - 1
    si, sj = min(ai, bi), min(aj, bj)
    ei, ej = max(ai, bi), max(aj, bj)
    vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(vlines | hlines)


def outbox(
    patch: 'Patch'
) -> 'Indices':
    """ outbox for patch """
    ai, aj = uppermost(patch) - 1, leftmost(patch) - 1
    bi, bj = lowermost(patch) + 1, rightmost(patch) + 1
    si, sj = min(ai, bi), min(aj, bj)
    ei, ej = max(ai, bi), max(aj, bj)
    vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(vlines | hlines)


def box(
    patch: 'Patch'
) -> 'Indices':
    """ outline of patch """
    if len(patch) == 0:
        return patch
    ai, aj = ulcorner(patch)
    bi, bj = lrcorner(patch)
    si, sj = min(ai, bi), min(aj, bj)
    ei, ej = max(ai, bi), max(aj, bj)
    vlines = {(i, sj) for i in range(si, ei + 1)} | {(i, ej) for i in range(si, ei + 1)}
    hlines = {(si, j) for j in range(sj, ej + 1)} | {(ei, j) for j in range(sj, ej + 1)}
    return frozenset(vlines | hlines)


def shoot(
    start: 'IJ',
    direction: 'IJ'
) -> 'Indices':
    """ line from starting point and direction """
    return connect(start, (start[0] + 42 * direction[0], start[1] + 42 * direction[1]))


def occurrences(
    grid: 'Grid',
    obj: 'Object'
) -> 'Indices':
    """ locations of occurrences of object in grid """
    occs = set()
    normed = normalize(obj)
    h, w = len(grid), len(grid[0])
    oh, ow = shape_f(obj)
    h2, w2 = h - oh + 1, w - ow + 1
    for i in range(h2):
        for j in range(w2):
            occurs = all(
                (0 <= a < h and 0 <= b < w and grid[a][b] == v)
                for a, b, v in shift(normed, (i, j))
            )
            if occurs:
                occs.add((i, j))
    return frozenset(occs)


def frontiers(
    grid: 'Grid'
) -> 'Objects':
    """ set of frontiers """
    h, w = len(grid), len(grid[0])
    row_indices = tuple(i for i, r in enumerate(grid) if len(set(r)) == 1)
    column_indices = tuple(j for j, c in enumerate(dmirror_t(grid)) if len(set(c)) == 1)
    hfrontiers = frozenset({frozenset({(i, j, grid[i][j]) for j in range(w)}) for i in row_indices})
    vfrontiers = frozenset({frozenset({(i, j, grid[i][j]) for i in range(h)}) for j in column_indices})
    return hfrontiers | vfrontiers


def compress(
    grid: 'Grid'
) -> 'Grid':
    """ removes frontiers from grid """
    ri = tuple(i for i, r in enumerate(grid) if len(set(r)) == 1)
    ci = tuple(j for j, c in enumerate(dmirror_t(grid)) if len(set(c)) == 1)
    return tuple(tuple(v for j, v in enumerate(r) if j not in ci) for i, r in enumerate(grid) if i not in ri)


def hperiod(
    obj: 'Object'
) -> 'Integer':
    """ horizontal periodicity """
    normalized = normalize(obj)
    w = width_f(normalized)
    for p in range(1, w):
        offsetted = shift(normalized, (0, -p))
        pruned = frozenset({(i, j, c) for i, j, c in offsetted if j >= 0})
        if pruned.issubset(normalized):
            return p
    return w


def vperiod(
    obj: 'Object'
) -> 'Integer':
    """ vertical periodicity """
    normalized = normalize(obj)
    h = height_f(normalized)
    for p in range(1, h):
        offsetted = shift(normalized, (-p, 0))
        pruned = frozenset({(i, j, c) for i, j, c in offsetted if i >= 0})
        if pruned.issubset(normalized):
            return p
    return h


def toindices(
    patch: 'Patch'
) -> 'Indices':
    """ indices of object cells """
    if not hasattr(patch, '__len__') or len(patch) == 0:
        return frozenset()
    if not hasattr(next(iter(patch)), '__len__'):
        return frozenset()
    if len(next(iter(patch))) == 3:
        return frozenset((i, j) for i, j, c in patch)
    return patch


def toindices_i(
    indices: 'Indices'
) -> 'Indices':
    """ indices of object cells """
    return indices


def toindices_o(
    obj: 'Object'
) -> 'Indices':
    """ indices of object cells """
    if not hasattr(obj, '__len__') or len(obj) == 0:
        return frozenset()
    return frozenset((i, j) for i, j, c in obj)


# def shape(
#     piece: Piece
# ) -> 'IJ':
#     """ height and width of grid or patch """
#     return (height(piece), width(piece))


def shape_t(
    grid: 'Grid'
) -> 'IJ':
    """ height and width of grid or patch """
    return (height_t(grid), width_t(grid))


def shape_f(
    patch: 'Patch'
) -> 'IJ':
    """ height and width of grid or patch """
    return (height_f(patch), width_f(patch))


# def portrait(
#     piece: Piece
# ) -> 'Boolean':
#     """ whether height is greater than width """
#     return height(piece) > width(piece)


def portrait_t(
    grid: 'Grid'
) -> 'Boolean':
    """ whether height is greater than width """
    return height_t(grid) > width_t(grid)


def portrait_f(
    patch: 'Patch'
) -> 'Boolean':
    """ whether height is greater than width """
    return height_f(patch) > width_f(patch)


# def colorcount(
#     element: Element,
#     value: 'Integer'
# ) -> 'Integer':
#     """ number of cells with color """
#     if isinstance(element, tuple):
#         return sum(row.count(value) for row in element)
#     return sum(v == value for v, _ in element)


def colorcount_t(
    grid: 'Grid',
    color: 'C_'
) -> 'Integer':
    """ number of cells with color """
    return sum(row.count(color) for row in grid)


def colorcount_f(
    obj: 'Object',
    color: 'C_'
) -> 'Integer':
    """ number of cells with color """
    if not isinstance(obj, frozenset):
        return None
    return sum(c == color for _, _, c in obj)


def colorfilter(
    objs: 'Objects',
    color: 'C_'
) -> 'Objects':
    """ filter objects by color """
    return frozenset(obj for obj in objs if next(iter(obj))[2] == color)


def sizefilter(
    container: 'Container',
    n: 'Integer'
) -> 'Object':
    """ filter items by size """
    return frozenset(item for item in container if len(item) == n)


def asindices(
    grid: 'Grid'
) -> 'Indices':
    """ indices of all grid cells """
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))


def f_ofcolor(
    grid: 'Grid',
    color: 'C_'
) -> 'Indices':
    """ indices of all grid cells with color """
    return frozenset((i, j) for i, r in enumerate(grid) for j, c in enumerate(r) if c == color)


def corner(
    patch: 'Patch',
    type: 'R4'
) -> 'IJ':
    """ indices of corners """
    if type == 0:
        return ulcorner(patch)
    elif type == 1:
        return urcorner(patch)
    elif type == 2:
        return llcorner(patch)
    elif type == 3:
        return lrcorner(patch)
    return ulcorner(patch)


def ulcorner(
    patch: 'Patch'
) -> 'IJ':
    """ index of upper left corner """
    return tuple(map(min, zip(*toindices(patch))))


def ulcorner_i(
    indices: 'Indices'
) -> 'IJ':
    """ index of upper left corner """
    return tuple(map(min, zip(*toindices_i(indices))))


def ulcorner_o(
    obj: 'Object'
) -> 'IJ':
    """ index of upper left corner """
    return tuple(map(min, zip(*toindices_o(obj))))


def urcorner(
    patch: 'Patch'
) -> 'IJ':
    """ index of upper right corner """
    return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))


def urcorner_i(
    indices: 'Indices'
) -> 'IJ':
    """ index of upper right corner """
    return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices_i(indices)))))


def urcorner_o(
    obj: 'Object'
) -> 'IJ':
    """ index of upper right corner """
    return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices_o(obj)))))


def llcorner(
    patch: 'Patch'
) -> 'IJ':
    """ index of lower left corner """
    return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))


def llcorner_i(
    indices: 'Indices'
) -> 'IJ':
    """ index of lower left corner """
    return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*toindices_i(indices)))))


def llcorner_o(
    obj: 'Object'
) -> 'IJ':
    """ index of lower left corner """
    return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*toindices_o(obj)))))


def lrcorner(
    patch: 'Patch'
) -> 'IJ':
    """ index of lower right corner """
    return tuple(map(max, zip(*toindices(patch))))


def lrcorner_i(
    indices: 'Indices'
) -> 'IJ':
    """ index of lower right corner """
    return tuple(map(max, zip(*toindices_i(indices))))


def lrcorner_o(
    obj: 'Object'
) -> 'IJ':
    """ index of lower right corner """
    return tuple(map(max, zip(*toindices_o(obj))))


def crop(
    grid: 'Grid',
    start: 'IJ',
    dims: 'IJ'
) -> 'Grid':
    """ subgrid specified by start and dimension """
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])


def recolor_i(
    color: 'C_',
    indices: 'Indices'
) -> 'Object':
    """ recolor indices """
    return frozenset((i, j, color) for i, j in toindices_i(indices))


def recolor_o(
    color: 'C_',
    obj: 'Object'
) -> 'Object':
    """ recolor obj """
    return frozenset((i, j, color) for i, j in toindices_o(obj))


def shift(
    patch: 'Patch',
    directions: 'IJ'
) -> 'Patch':
    """ shift patch """
    if len(patch) == 0:
        return patch
    di, dj = directions
    if len(next(iter(patch))) == 3:
        return frozenset((i + di, j + dj, c) for i, j, c in patch)
    return frozenset((i + di, j + dj) for i, j in patch)


def normalize_i(
    indices: 'Indices'
) -> 'Indices':
    """ moves upper left corner to origin """
    if len(indices) == 0:
        return indices
    return shift(indices, (-uppermost_i(indices), -leftmost_i(indices)))


def normalize_o(
    obj: 'Object'
) -> 'Object':
    """ moves upper left corner to origin """
    if len(obj) == 0:
        return obj
    return shift(obj, (-uppermost_o(obj), -leftmost_o(obj)))


def dneighbors(
    loc: 'IJ'
) -> 'Indices':
    """ directly adjacent indices """
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})


def ineighbors(
    loc: 'IJ'
) -> 'Indices':
    """ diagonally adjacent indices """
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})


def neighbors(
    loc: 'IJ'
) -> 'Indices':
    """ adjacent indices """
    return dneighbors(loc) | ineighbors(loc)


def objects(
    grid: 'Grid',
    univalued: 'Boolean',
    diagonal: 'Boolean',
    without_bg: 'Boolean'
) -> 'Objects':
    """ objects occurring on the grid """
    bg = mostcolor_t(grid) if without_bg else None
    objs = set()
    occupied = set()
    h, w = len(grid), len(grid[0])
    unvisited = asindices(grid)
    diagfun = neighbors if diagonal else dneighbors
    for loc in unvisited:
        if loc in occupied:
            continue
        val = grid[loc[0]][loc[1]]
        if val == bg:
            continue
        # obj = {(val, loc)}
        obj = {(loc[0], loc[1], val)}
        cands = {loc}
        while len(cands) > 0:
            neighborhood = set()
            for cand in cands:
                v = grid[cand[0]][cand[1]]
                if (val == v) if univalued else (v != bg):
                    # obj.add((v, cand))
                    obj.add((cand[0], cand[1], v))
                    occupied.add(cand)
                    neighborhood |= {
                        (i, j) for i, j in diagfun(cand) if 0 <= i < h and 0 <= j < w
                    }
            cands = neighborhood - occupied
        objs.add(frozenset(obj))
    return frozenset(objs)


def partition(
    grid: 'Grid'
) -> 'Objects':
    """ each cell with the same color of the same object """
    return frozenset(
        frozenset(
            (i, j, c) for i, r in enumerate(grid) for j, c in enumerate(r) if c == color
        ) for color in palette_t(grid)
    )


def fgpartition(
    grid: 'Grid'
) -> 'Objects':
    """ each cell with the same color of the same object without background """
    return frozenset(
        frozenset(
            (i, j, c) for i, r in enumerate(grid) for j, c in enumerate(r) if c == color
        ) for color in palette_t(grid) - {mostcolor_t(grid)}
    )


# def square(
#     piece: Piece
# ) -> 'Boolean':
#     """ whether the piece forms a square """
#     return len(piece) == len(piece[0]) if isinstance(piece, tuple) else height(piece) * width(piece) == len(piece) and height(piece) == width(piece)


def square_t(
    grid: 'Grid'
) -> 'Boolean':
    """ whether the grid forms a square """
    return len(grid) == len(grid[0])


def square_f(
    patch: 'Patch'
) -> 'Boolean':
    """ whether the patch forms a square """
    return height_f(patch) * width_f(patch) == len(patch) and height_f(patch) == width_f(patch)


def vline_i(
    patch: 'Indices'
) -> 'Boolean':
    """ whether the piece forms a vertical line """
    return height_i(patch) == len(patch) and width_i(patch) == 1


def vline_o(
    patch: 'Object'
) -> 'Boolean':
    """ whether the piece forms a vertical line """
    return height_o(patch) == len(patch) and width_o(patch) == 1


def hline_i(
    patch: 'Indices'
) -> 'Boolean':
    """ whether the piece forms a horizontal line """
    return width_i(patch) == len(patch) and height_i(patch) == 1


def hline_o(
    patch: 'Object'
) -> 'Boolean':
    """ whether the piece forms a horizontal line """
    return width_o(patch) == len(patch) and height_o(patch) == 1


def hmatching(
    a: 'Patch',
    b: 'Patch'
) -> 'Boolean':
    """ whether there exists a row for which both patches have cells """
    return len(set(i for i, j in toindices(a)) & set(i for i, j in toindices(b))) > 0


def vmatching(
    a: 'Patch',
    b: 'Patch'
) -> 'Boolean':
    """ whether there exists a column for which both patches have cells """
    return len(set(j for i, j in toindices(a)) & set(j for i, j in toindices(b))) > 0


def manhattan(
    a: 'Patch',
    b: 'Patch'
) -> 'Integer':
    """ closest manhattan distance between two patches """
    try:
        return min(abs(ai - bi) + abs(aj - bj) for ai, aj in toindices(a) for bi, bj in toindices(b))
    except ValueError:
        return None


def adjacent(
    a: 'Patch',
    b: 'Patch'
) -> 'Boolean':
    """ whether two patches are adjacent """
    return manhattan(a, b) == 1


def bordering(
    patch: 'Patch',
    grid: 'Grid'
) -> 'Boolean':
    """ whether a patch is adjacent to a grid border """
    return uppermost(patch) == 0 or leftmost(patch) == 0 or lowermost(patch) == len(grid) - 1 or rightmost(patch) == len(grid[0]) - 1


def centerofmass(
    patch: 'Patch'
) -> 'IJ':
    """ center of mass """
    return tuple(map(lambda x: sum(x) // len(patch), zip(*toindices(patch))))


# def numcolors(
#     element: Element
# ) -> 'Integer':
#     """ number of colors occurring in object or grid """
#     return len(palette(element))


def numcolors_t(
    grid: 'Grid'
) -> 'Integer':
    """ number of colors occurring in object or grid """
    return len(palette_t(grid))


def numcolors_f(
    obj: 'Object'
) -> 'Integer':
    """ number of colors occurring in object or grid """
    return len(palette_f(obj))


def color(
    obj: 'Object'
) -> 'Integer':
    """ color of object """
    first_element = next(iter(obj))
    return first_element[0] if isinstance(first_element, tuple) else first_element


def toobject(
    patch: 'Patch',
    grid: 'Grid'
) -> 'Object':
    """ object from patch and grid """
    h, w = len(grid), len(grid[0])
    return frozenset((i, j, grid[i][j]) for i, j in toindices(patch) if 0 <= i < h and 0 <= j < w)


def asobject(
    grid: 'Grid'
) -> 'Object':
    """ conversion of grid to object """
    return frozenset((i, j, c) for i, r in enumerate(grid) for j, c in enumerate(r))


def rot90(
    grid: 'Grid'
) -> 'Grid':
    """ quarter clockwise rotation """
    return tuple(row for row in zip(*grid[::-1]))


def rot180(
    grid: 'Grid'
) -> 'Grid':
    """ half rotation """
    return tuple(tuple(row[::-1]) for row in grid[::-1])


def rot270(
    grid: 'Grid'
) -> 'Grid':
    """ quarter anticlockwise rotation """
    return tuple(tuple(row[::-1]) for row in zip(*grid[::-1]))[::-1]


# def hmirror(
#     piece: Piece
# ) -> Piece:
#     """ mirroring along horizontal """
#     if isinstance(piece, tuple):
#         return piece[::-1]
#     d = ulcorner(piece)[0] + lrcorner(piece)[0]
#     if isinstance(next(iter(piece))[1], tuple):
#         return frozenset((v, (d - i, j)) for v, (i, j) in piece)
#     return frozenset((d - i, j) for i, j in piece)


def hmirror_t(
    grid: 'Grid'
) -> 'Grid':
    """ mirroring along horizontal """
    return grid[::-1]


def hmirror_f(
    patch: 'Patch'
) -> 'Patch':
    """ mirroring along horizontal """
    d = ulcorner(patch)[0] + lrcorner(patch)[0]
    if len(next(iter(patch))) == 3:
        return frozenset((d - i, j, c) for i, j, c in patch)
    return frozenset((d - i, j) for i, j in patch)


def hmirror_i(
    indices: 'Indices'
) -> 'Indices':
    """ mirroring along horizontal """
    d = ulcorner(indices)[0] + lrcorner(indices)[0]
    return frozenset((d - i, j) for i, j in indices)


def hmirror_o(
    obj: 'Object'
) -> 'Object':
    """ mirroring along horizontal """
    d = ulcorner(obj)[0] + lrcorner(obj)[0]
    return frozenset((d - i, j, c) for i, j, c in obj)


# def vmirror(
#     piece: Piece
# ) -> Piece:
#     """ mirroring along vertical """
#     if isinstance(piece, tuple):
#         return tuple(row[::-1] for row in piece)
#     d = ulcorner(piece)[1] + lrcorner(piece)[1]
#     if isinstance(next(iter(piece))[1], tuple):
#         return frozenset((v, (i, d - j)) for v, (i, j) in piece)
#     return frozenset((i, d - j) for i, j in piece)


def vmirror_t(
    grid: 'Grid'
) -> 'Grid':
    """ mirroring along vertical """
    return tuple(row[::-1] for row in grid)


def vmirror_f(
    patch: 'Patch'
) -> 'Patch':
    """ mirroring along vertical """
    if path == frozenset():
        return patch
    d = ulcorner(patch)[1] + lrcorner(patch)[1]
    if len(next(iter(patch))) == 3:
        return frozenset((i, d - j, c) for i, j, c in patch)
    return frozenset((i, d - j) for i, j in patch)


def vmirror_i(
    indices: 'Indices'
) -> 'Indices':
    """ mirroring along vertical """
    d = ulcorner(indices)[1] + lrcorner(indices)[1]
    return frozenset((i, d - j) for i, j in indices)


def vmirror_o(
    obj: 'Object'
) -> 'Object':
    """ mirroring along vertical """
    d = ulcorner(obj)[1] + lrcorner(obj)[1]
    return frozenset((i, d - j, c) for i, j, c in obj)


# def dmirror(
#     piece: Piece
# ) -> Piece:
#     """ mirroring along diagonal """
#     if isinstance(piece, tuple):
#         return tuple(zip(*piece))
#     a, b = ulcorner(piece)
#     if isinstance(next(iter(piece))[1], tuple):
#         return frozenset((v, (j - b + a, i - a + b)) for v, (i, j) in piece)
#     return frozenset((j - b + a, i - a + b) for i, j in piece)


def dmirror_t(
    grid: 'Grid'
) -> 'Grid':
    """ mirroring along diagonal """
    return tuple(zip(*grid))


def dmirror_f(
    patch: 'Patch'
) -> 'Patch':
    """ mirroring along diagonal """
    a, b = ulcorner(patch)
    if len(next(iter(patch))) == 3:
        return frozenset((j - b + a, i - a + b, c) for i, j, c in patch)
    return frozenset((j - b + a, i - a + b) for i, j in patch)


def dmirror_i(
    indices: 'Indices'
) -> 'Indices':
    """ mirroring along diagonal """
    a, b = ulcorner(indices)
    return frozenset((j - b + a, i - a + b) for i, j in indices)


def dmirror_o(
    obj: 'Object'
) -> 'Object':
    """ mirroring along diagonal """
    a, b = ulcorner(obj)
    return frozenset((j - b + a, i - a + b, c) for i, j, c in obj)


# def cmirror(
#     piece: Piece
# ) -> Piece:
#     """ mirroring along counterdiagonal """
#     if isinstance(piece, tuple):
#         return tuple(zip(*(r[::-1] for r in piece[::-1])))
#     return vmirror(dmirror(vmirror(piece)))


def cmirror_t(
    grid: 'Grid'
) -> 'Grid':
    """ mirroring along counterdiagonal """
    return tuple(zip(*(r[::-1] for r in grid[::-1])))


def cmirror_f(
    patch: 'Patch'
) -> 'Patch':
    """ mirroring along counterdiagonal """
    return vmirror_f(dmirror_f(vmirror_f(patch)))


def cmirror_i(
    indices: 'Indices'
) -> 'Indices':
    """ mirroring along counterdiagonal """
    return vmirror_f(dmirror_f(vmirror_f(indices)))


def cmirror_o(
    obj: 'Object'
) -> 'Object':
    """ mirroring along counterdiagonal """
    return vmirror_f(dmirror_f(vmirror_f(obj)))


def fill(
    grid: 'Grid',
    color: 'C_',
    patch: 'Patch'
) -> 'Grid':
    """ fill color at indices """
    h, w = len(grid), len(grid[0])
    grid_filled = list(list(row) for row in grid)
    for i, j in toindices(patch):
        if 0 <= i < h and 0 <= j < w:
            grid_filled[i][j] = color
    return tuple(tuple(row) for row in grid_filled)


def paint(
    grid: 'Grid',
    obj: 'Object'
) -> 'Grid':
    """ paint object to grid """
    h, w = len(grid), len(grid[0])
    grid_painted = list(list(row) for row in grid)
    for i, j, c in obj:
        if 0 <= i < h and 0 <= j < w:
            grid_painted[i][j] = c
    return tuple(tuple(row) for row in grid_painted)


def underfill(
    grid: 'Grid',
    color: 'C_',
    patch: 'Patch'
) -> 'Grid':
    """ fill color at indices that are background """
    h, w = len(grid), len(grid[0])
    bg = mostcolor_t(grid)
    g = [list(r) for r in grid]
    for i, j in toindices(patch):
        if 0 <= i < h and 0 <= j < w and g[i][j] == bg:
            g[i][j] = color
    return tuple(tuple(r) for r in g)


def underpaint(
    grid: 'Grid',
    obj: 'Object'
) -> 'Grid':
    """ paint object to grid where there is background """
    h, w = len(grid), len(grid[0])
    bg = mostcolor_t(grid)
    g = [list(r) for r in grid]
    for i, j, c in obj:
        if 0 <= i < h and 0 <= j < w and g[i][j] == bg:
            g[i][j] = c
    return tuple(tuple(r) for r in g)


def hupscale(
    grid: 'Grid',
    factor: 'Integer'
) -> 'Grid':
    """ upscale grid horizontally """
    g = ()
    for row in grid:
        r = ()
        for value in row:
            r = r + tuple(value for _ in range(factor))
        g = g + (r,)
    return g


def vupscale(
    grid: 'Grid',
    factor: 'Integer'
) -> 'Grid':
    """ upscale grid vertically """
    g = ()
    for row in grid:
        g = g + tuple(row for _ in range(factor))
    return g


# def upscale(
#     element: Element,
#     factor: 'Integer'
# ) -> Element:
#     """ upscale object or grid """
#     if isinstance(element, tuple):
#         g = tuple()
#         for row in element:
#             upscaled_row = tuple()
#             for value in row:
#                 upscaled_row = upscaled_row + tuple(value for num in range(factor))
#             g = g + tuple(upscaled_row for num in range(factor))
#         return g
#     else:
#         if len(element) == 0:
#             return frozenset()
#         di_inv, dj_inv = ulcorner(element)
#         di, dj = (-di_inv, -dj_inv)
#         normed_obj = shift(element, (di, dj))
#         o = set()
#         for value, (i, j) in normed_obj:
#             for io in range(factor):
#                 for jo in range(factor):
#                     o.add((value, (i * factor + io, j * factor + jo)))
#         return shift(frozenset(o), (di_inv, dj_inv))


def upscale_t(
    grid: 'Grid',
    factor: 'Integer'
) -> 'Grid':
    """ upscale grid """
    g = ()
    for row in grid:
        upscaled_row = ()
        for value in row:
            upscaled_row = upscaled_row + tuple(value for _ in range(factor))
        g = g + tuple(upscaled_row for _ in range(factor))
    return g


def upscale_f(
    obj: 'Object',
    factor: 'Integer'
) -> 'Object':
    """ upscale object """
    if len(obj) == 0:
        return frozenset()
    di_inv, dj_inv = ulcorner(obj)
    di, dj = (-di_inv, -dj_inv)
    normed_obj = shift(obj, (di, dj))
    o = set()
    for i, j, c in normed_obj:
        for io, jo in itertools.product(range(factor), range(factor)):
            o.add((i * factor + io, j * factor + jo, c))
    return shift(frozenset(o), (di_inv, dj_inv))

