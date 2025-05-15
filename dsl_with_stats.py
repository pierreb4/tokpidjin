"""
DSL module with statistics tracking enabled.
This version tracks function call statistics including argument types.
"""

from arc_types import *
from typing import Dict, List, Tuple, Any
from stats_tracker import track_stats

@track_stats
def identity(
    x: Any
) -> Any:
    """ identity function """
    return x


@track_stats
def add(
    a: Numerical,
    b: Numerical
) -> Numerical:
    """ addition """
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] + b[0], a[1] + b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a + b[0], a + b[1])
    return (a[0] + b, a[1] + b)


@track_stats
def subtract(
    a: Numerical,
    b: Numerical
) -> Numerical:
    """ subtraction """
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] - b[0], a[1] - b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a - b[0], a - b[1])
    return (a[0] - b, a[1] - b)


@track_stats
def multiply(
    a: Numerical,
    b: Numerical
) -> Numerical:
    """ multiplication """
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] * b[0], a[1] * b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a * b[0], a * b[1])
    return (a[0] * b, a[1] * b)
    

@track_stats
def divide(
    a: Numerical,
    b: Numerical
) -> Numerical:
    """ floor division """
    if isinstance(a, int) and isinstance(b, int):
        return a // b
    elif isinstance(a, tuple) and isinstance(b, tuple):
        return (a[0] // b[0], a[1] // b[1])
    elif isinstance(a, int) and isinstance(b, tuple):
        return (a // b[0], a // b[1])
    return (a[0] // b, a[1] // b)


@track_stats
def invert(
    n: Numerical
) -> Numerical:
    """ inversion with respect to addition """
    return -n if isinstance(n, int) else (-n[0], -n[1])


@track_stats
def even(
    n: Integer
) -> Boolean:
    """ evenness """
    return n % 2 == 0


@track_stats
def double(
    n: Numerical
) -> Numerical:
    """ scaling by two """
    return n * 2 if isinstance(n, int) else (n[0] * 2, n[1] * 2)


@track_stats
def halve(
    n: Numerical
) -> Numerical:
    """ scaling by one half """
    return n // 2 if isinstance(n, int) else (n[0] // 2, n[1] // 2)


@track_stats
def flip(
    b: Boolean
) -> Boolean:
    """ logical not """
    return not b


@track_stats
def equality(
    a: Any,
    b: Any
) -> Boolean:
    """ equality """
    return a == b


@track_stats
def contained(
    value: Any,
    container: Container
) -> Boolean:
    """ element of """
    return value in container


@track_stats
def combine(
    a: Container,
    b: Container
) -> Container:
    """ union """
    return type(a)((*a, *b))


@track_stats
def intersection(
    a: FrozenSet,
    b: FrozenSet
) -> FrozenSet:
    """ returns the intersection of two containers """
    return a & b


@track_stats
def and_tuple(
    a: Tuple, 
    b: Tuple 
) -> Tuple:
    """ returns the intersection of two tuples """
    return tuple((Counter(a) & Counter(b)).elements())

@track_stats
def difference(
    a: FrozenSet,
    b: FrozenSet
) -> FrozenSet:
    """ set difference """
    return type(a)(e for e in a if e not in b)


@track_stats
def difference_tuple(
    a: Tuple, 
    b: Tuple
) -> Tuple:
    """ set difference """
    return type(a)(e for e in a if e not in b)


@track_stats
def dedupe(
    tup: Tuple
) -> Tuple:
    """ remove duplicates """
    return tuple(e for i, e in enumerate(tup) if tup.index(e) == i)


@track_stats
def order(
    container: Container,
    compfunc: Callable
) -> Tuple:
    """ order container by custom key """
    return tuple(sorted(container, key=compfunc))


@track_stats
def repeat(
    item: Any,
    num: Integer
) -> Tuple:
    """ repetition of item within vector """
    return tuple(item for i in range(num))


@track_stats
def greater(
    a: Integer,
    b: Integer
) -> Boolean:
    """ greater """
    return a > b


@track_stats
def size(
    container: Container
) -> Integer:
    """ cardinality """
    return len(container)


@track_stats
def merge(
    containers: ContainerContainer
) -> Container:
    """ merging """
    return type(containers)(e for c in containers for e in c)


@track_stats
def maximum(
    container: IntegerSet
) -> Integer:
    """ maximum """
    return max(container, default=0)


@track_stats
def minimum(
    container: IntegerSet
) -> Integer:
    """ minimum """
    return min(container, default=0)


@track_stats
def valmax(
    container: Container,
    compfunc: Callable
) -> Integer:
    """ maximum by custom function """
    return compfunc(max(container, key=compfunc, default=0))


@track_stats
def valmin(
    container: Container,
    compfunc: Callable
) -> Integer:
    """ minimum by custom function """
    return compfunc(min(container, key=compfunc, default=0))


@track_stats
def argmax(
    container: Container,
    compfunc: Callable
) -> Any:
    """ largest item by custom order """
    return max(container, key=compfunc)


@track_stats
def argmin(
    container: Container,
    compfunc: Callable
) -> Any:
    """ smallest item by custom order """
    return min(container, key=compfunc)


@track_stats
def mostcommon(
    container: Container
) -> Any:
    """ most common item """
    return max(set(container), key=container.count)


@track_stats
def leastcommon(
    container: Container
) -> Any:
    """ least common item """
    return min(set(container), key=container.count)


@track_stats
def initset(
    value: Any
) -> FrozenSet:
    """ initialize container """
    return frozenset({value})


@track_stats
def both(
    a: Boolean,
    b: Boolean
) -> Boolean:
    """ logical and """
    return a and b


@track_stats
def either(
    a: Boolean,
    b: Boolean
) -> Boolean:
    """ logical or """
    return a or b


@track_stats
def increment(
    x: Numerical
) -> Numerical:
    """ incrementing """
    return x + 1 if isinstance(x, int) else (x[0] + 1, x[1] + 1)


@track_stats
def decrement(
    x: Numerical
) -> Numerical:
    """ decrementing """
    return x - 1 if isinstance(x, int) else (x[0] - 1, x[1] - 1)


@track_stats
def crement(
    x: Numerical
) -> Numerical:
    """ incrementing positive and decrementing negative """
    if isinstance(x, int):
        return 0 if x == 0 else (x + 1 if x > 0 else x - 1)
    return (
        0 if x[0] == 0 else (x[0] + 1 if x[0] > 0 else x[0] - 1),
        0 if x[1] == 0 else (x[1] + 1 if x[1] > 0 else x[1] - 1)
    )


@track_stats
def sign(
    x: Numerical
) -> Numerical:
    """ sign """
    if isinstance(x, int):
        return 0 if x == 0 else (1 if x > 0 else -1)
    return (
        0 if x[0] == 0 else (1 if x[0] > 0 else -1),
        0 if x[1] == 0 else (1 if x[1] > 0 else -1)
    )


@track_stats
def positive(
    x: Integer
) -> Boolean:
    """ positive """
    return x > 0


@track_stats
def toivec(
    i: Integer
) -> IntegerTuple:
    """ vector pointing vertically """
    return (i, 0)


@track_stats
def tojvec(
    j: Integer
) -> IntegerTuple:
    """ vector pointing horizontally """
    return (0, j)


@track_stats
def sfilter(
    container: Container,
    condition: Callable
) -> Container:
    """ keep elements in container that satisfy condition """
    return type(container)(e for e in container if condition(e))


@track_stats
def mfilter(
    container: Container,
    function: Callable
) -> FrozenSet:
    """ filter and merge """
    return merge(sfilter(container, function))


@track_stats
def extract(
    container: Container,
    condition: Callable
) -> Any:
    """ first element of container that satisfies condition """
    return next(e for e in container if condition(e))


@track_stats
def totuple(
    container: FrozenSet
) -> Tuple:
    """ conversion to tuple """
    return tuple(container)


@track_stats
def first(
    container: Container
) -> Any:
    """ first item of container """
    return next(iter(container))


@track_stats
def last(
    container: Container
) -> Any:
    """ last item of container """
    return max(enumerate(container))[1]


@track_stats
def insert(
    value: Any,
    container: FrozenSet
) -> FrozenSet:
    """ insert item into container """
    return container.union(frozenset({value}))


@track_stats
def remove(
    value: Any,
    container: Container
) -> Container:
    """ remove item from container """
    return type(container)(e for e in container if e != value)


@track_stats
def other(
    container: Container,
    value: Any
) -> Any:
    """ other value in the container """
    return first(remove(value, container))


@track_stats
def interval(
    start: Integer,
    stop: Integer,
    step: Integer
) -> Tuple:
    """ range """
    return tuple(range(start, stop, step))


@track_stats
def astuple(
    a: Integer,
    b: Integer
) -> IntegerTuple:
    """ constructs a tuple """
    return (a, b)


@track_stats
def product(
    a: Container,
    b: Container
) -> FrozenSet:
    """ cartesian product """
    return frozenset((i, j) for j in b for i in a)


@track_stats
def pair(
    a: Tuple,
    b: Tuple
) -> TupleTuple:
    """ zipping of two tuples """
    return tuple(zip(a, b))


@track_stats
def branch(
    condition: Boolean,
    a: Any,
    b: Any
) -> Any:
    """ if else branching """
    return a if condition else b


@track_stats
def compose(
    outer: Callable,
    inner: Callable
) -> Callable:
    """ function composition """
    return lambda x: outer(inner(x))


@track_stats
def chain(
    h: Callable,
    g: Callable,
    f: Callable,
) -> Callable:
    """ function composition with three functions """
    return lambda x: h(g(f(x)))


@track_stats
def matcher(
    function: Callable,
    target: Any
) -> Callable:
    """ construction of equality function """
    return lambda x: function(x) == target


@track_stats
def rbind(
    function: Callable,
    fixed: Any
) -> Callable:
    """ fix the rightmost argument """
    n = function.__code__.co_argcount
    if n == 2:
        return lambda x: function(x, fixed)
    elif n == 3:
        return lambda x, y: function(x, y, fixed)
    else:
        return lambda x, y, z: function(x, y, z, fixed)


@track_stats
def lbind(
    function: Callable,
    fixed: Any
) -> Callable:
    """ fix the leftmost argument """
    n = function.__code__.co_argcount
    if n == 2:
        return lambda y: function(fixed, y)
    elif n == 3:
        return lambda y, z: function(fixed, y, z)
    else:
        return lambda y, z, a: function(fixed, y, z, a)


@track_stats
def power(
    function: Callable,
    n: Integer
) -> Callable:
    """ power of function """
    if n == 1:
        return function
    return compose(function, power(function, n - 1))


@track_stats
def fork(
    outer: Callable,
    a: Callable,
    b: Callable
) -> Callable:
    """ creates a wrapper function """
    return lambda x: outer(a(x), b(x))


@track_stats
def apply(
    function: Callable,
    container: Container
) -> Container:
    """ apply function to each item in container """
    return type(container)(function(e) for e in container)


@track_stats
def rapply(
    functions: Container,
    value: Any
) -> Container:
    """ apply each function in container to value """
    return type(functions)(function(value) for function in functions)


@track_stats
def mapply(
    function: Callable,
    container: ContainerContainer
) -> FrozenSet:
    """ apply and merge """
    return merge(apply(function, container))


@track_stats
def mapply_tuple(
    function: Callable,
    container: ContainerContainer
) -> Tuple:
    """ apply and merge """
    return merge(apply(function, container))


@track_stats
def papply(
    function: Callable,
    a: Tuple,
    b: Tuple
) -> Tuple:
    """ apply function on two vectors """
    return tuple(function(i, j) for i, j in zip(a, b))


@track_stats
def mpapply(
    function: Callable,
    a: Tuple,
    b: Tuple
) -> Tuple:
    """ apply function on two vectors and merge """
    return merge(papply(function, a, b))


@track_stats
def prapply(
    function,
    a: Container,
    b: Container
) -> FrozenSet:
    """ apply function on cartesian product """
    return frozenset(function(i, j) for j in b for i in a)


@track_stats
def mostcolor(
    element: Element
) -> Integer:
    """ most common color """
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return max(set(values), key=values.count)
    

@track_stats
def leastcolor(
    element: Element
) -> Integer:
    """ least common color """
    values = [v for r in element for v in r] if isinstance(element, tuple) else [v for v, _ in element]
    return min(set(values), key=values.count)


@track_stats
def height(
    piece: Piece
) -> Integer:
    """ height of grid or patch """
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece)
    return lowermost(piece) - uppermost(piece) + 1


@track_stats
def tuple_height(
    piece: PieceTuple
) -> Integer:
    """ height of grid or patch """
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece)
    return lowermost(piece) - uppermost(piece) + 1


@track_stats
def width(
    piece: Piece
) -> Integer:
    """ width of grid or patch """
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return rightmost(piece) - leftmost(piece) + 1


@track_stats
def tuple_width(
    piece: PieceTuple
) -> Integer:
    """ width of grid or patch """
    if len(piece) == 0:
        return 0
    if isinstance(piece, tuple):
        return len(piece[0])
    return rightmost(piece) - leftmost(piece) + 1


@track_stats
def shape(
    piece: Piece
) -> IntegerTuple:
    """ height and width of grid or patch """
    return (height(piece), width(piece))


@track_stats
def portrait(
    piece: Piece
) -> Boolean:
    """ whether height is greater than width """
    return height(piece) > width(piece)


@track_stats
def colorcount(
    element: Element,
    value: Integer
) -> Integer:
    """ number of cells with color """
    if isinstance(element, tuple):
        return sum(row.count(value) for row in element)
    return sum(v == value for v, _ in element)


@track_stats
def colorfilter(
    objs: Objects,
    value: Integer
) -> Objects:
    """ filter objects by color """
    return frozenset(obj for obj in objs if next(iter(obj))[0] == value)


@track_stats
def sizefilter(
    container: Container,
    n: Integer
) -> FrozenSet:
    """ filter items by size """
    return frozenset(item for item in container if len(item) == n)


@track_stats
def asindices(
    grid: Grid
) -> Indices:
    """ indices of all grid cells """
    return frozenset((i, j) for i in range(len(grid)) for j in range(len(grid[0])))


@track_stats
def asindice_tuple(
    grid: Grid
) -> IndiceTuple:
    """ indices of all grid cells """
    return tuple((i, j) for i in range(len(grid)) for j in range(len(grid[0])))


@track_stats
def ofcolor(
    grid: Grid,
    value: Integer
) -> Indices:
    """ indices of all grid cells with value """
    return frozenset((i, j) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value)


@track_stats
def ulcorner(
    patch: Patch
) -> IntegerTuple:
    """ index of upper left corner """
    return tuple(map(min, zip(*toindices(patch))))


@track_stats
def urcorner(
    patch: Patch
) -> IntegerTuple:
    """ index of upper right corner """
    return tuple(map(lambda ix: {0: min, 1: max}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))


@track_stats
def llcorner(
    patch: Patch
) -> IntegerTuple:
    """ index of lower left corner """
    return tuple(map(lambda ix: {0: max, 1: min}[ix[0]](ix[1]), enumerate(zip(*toindices(patch)))))


@track_stats
def lrcorner(
    patch: Patch
) -> IntegerTuple:
    """ index of lower right corner """
    return tuple(map(max, zip(*toindices(patch))))


@track_stats
def crop(
    grid: Grid,
    start: IntegerTuple,
    dims: IntegerTuple
) -> Grid:
    """ subgrid specified by start and dimension """
    return tuple(r[start[1]:start[1]+dims[1]] for r in grid[start[0]:start[0]+dims[0]])


@track_stats
def toindices(
    patch: Patch
) -> Indices:
    """ indices of object cells """
    if len(patch) == 0:
        return frozenset()
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset(index for value, index in patch)
    return patch


@track_stats
def recolor(
    value: Integer,
    patch: Patch
) -> Object:
    """ recolor patch """
    return frozenset((value, index) for index in toindices(patch))


@track_stats
def shift(
    patch: Patch,
    directions: IntegerTuple
) -> Patch:
    """ shift patch """
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return frozenset((value, (i + di, j + dj)) for value, (i, j) in patch)
    return frozenset((i + di, j + dj) for i, j in patch)


@track_stats
def shift_tuple(
    patch: PatchTuple,
    directions: IntegerTuple
) -> PatchTuple:
    """ shift patch """
    if len(patch) == 0:
        return patch
    di, dj = directions
    if isinstance(next(iter(patch))[1], tuple):
        return tuple((value, (i + di, j + dj)) for value, (i, j) in patch)
    return tuple((i + di, j + dj) for i, j in patch)


@track_stats
def normalize(
    patch: Patch
) -> Patch:
    """ moves upper left corner to origin """
    if len(patch) == 0:
        return patch
    return shift(patch, (-uppermost(patch), -leftmost(patch)))


@track_stats
def dneighbors(
    loc: IntegerTuple
) -> Indices:
    """ directly adjacent indices """
    return frozenset({(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)})


@track_stats
def dneighbor_tuple(
    loc: IntegerTuple
) -> IndiceTuple:
    """ directly adjacent indices """
    return ((loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1))


@track_stats
def ineighbors(
    loc: IntegerTuple
) -> Indices:
    """ diagonally adjacent indices """
    return frozenset({(loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1)})


@track_stats
def ineighbor_tuple(
    loc: IntegerTuple
) -> IndiceTuple:
    """ diagonally adjacent indices """
    return ((loc[0] - 1, loc[1] - 1), (loc[0] - 1, loc[1] + 1), (loc[0] + 1, loc[1] - 1), (loc[0] + 1, loc[1] + 1))


@track_stats
def neighbors(
    loc: IntegerTuple
) -> Indices:
    """ adjacent indices """
    return dneighbors(loc) | ineighbors(loc)


@track_stats
def neighbor_tuple(
    loc: IntegerTuple
) -> IndiceTuple:
    """ adjacent indices """
    return tuple(set(dneighbor_tuple(loc)) | set(ineighbor_tuple(loc)))


@track_stats
def objects(
    grid: Grid,
    univalued: Boolean,
    diagonal: Boolean,
    without_bg: Boolean
) -> Objects:
    """ objects occurring on the grid """
    bg = mostcolor(grid) if without_bg else None
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
        obj = {(val, loc)}
        cands = {loc}
        while len(cands) > 0:
            neighborhood = set()
            for cand in cands:
                v = grid[cand[0]][cand[1]]
                if (val == v) if univalued else (v != bg):
                    obj.add((v, cand))
                    occupied.add(cand)
                    neighborhood |= {
                        (i, j) for i, j in diagfun(cand) if 0 <= i < h and 0 <= j < w
                    }
            cands = neighborhood - occupied
        objs.add(frozenset(obj))
    return frozenset(objs)


@track_stats
def object_tuple(
    grid: Grid,
    univalued: Boolean,
    diagonal: Boolean,
    without_bg: Boolean
) -> ObjectTuple:
    """ objects occurring on the grid """
    bg = mostcolor(grid) if without_bg else None
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
        obj = {(val, loc)}
        cands = {loc}
        while len(cands) > 0:
            neighborhood = set()
            for cand in cands:
                v = grid[cand[0]][cand[1]]
                if (val == v) if univalued else (v != bg):
                    obj.add((v, cand))
                    occupied.add(cand)
                    neighborhood |= {
                        (i, j) for i, j in diagfun(cand) if 0 <= i < h and 0 <= j < w
                    }
            cands = neighborhood - occupied
        objs.add(tuple(obj))
    return tuple(objs)


@track_stats
def partition(
    grid: Grid
) -> Objects:
    """ each cell with the same value part of the same object """
    return frozenset(
        frozenset(
            (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
        ) for value in palette(grid)
    )


@track_stats
def partition_tuple(
    grid: Grid
) -> ObjectsTuple:
    """ each cell with the same value part of the same object """
    return tuple(
        tuple(
            (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
        ) for value in palette_tuple(grid)
    )


@track_stats
def fgpartition(
    grid: Grid
) -> Objects:
    """ each cell with the same value part of the same object without background """
    return frozenset(
        frozenset(
            (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
        ) for value in palette(grid) - {mostcolor(grid)}
    )


@track_stats
def fgpartition_tuple(
    grid: Grid
) -> ObjectsTuple:
    """ each cell with the same value part of the same object without background """
    return tuple(
        tuple(
            (v, (i, j)) for i, r in enumerate(grid) for j, v in enumerate(r) if v == value
        ) for value in palette(grid) - {mostcolor(grid)}
    )


@track_stats
def uppermost(
    patch: Patch
) -> Integer:
    """ row index of uppermost occupied cell """
    return min(i for i, j in toindices(patch))


@track_stats
def lowermost(
    patch: Patch
) -> Integer:
    """ row index of lowermost occupied cell """
    return max(i for i, j in toindices(patch))


@track_stats
def leftmost(
    patch: Patch
) -> Integer:
    """ column index of leftmost occupied cell """
    return min(j for i, j in toindices(patch))


@track_stats
def rightmost(
    patch: Patch
) -> Integer:
    """ column index of rightmost occupied cell """
    return max(j for i, j in toindices(patch))


@track_stats
def square(
    piece: Piece
) -> Boolean:
    """ whether the piece forms a square """
    return len(piece) == len(piece[0]) if isinstance(piece, tuple) else height(piece) * width(piece) == len(piece) and height(piece) == width(piece)


@track_stats
def vline(
    patch: Patch
) -> Boolean:
    """ whether the piece forms a vertical line """
    return height(patch) == len(patch) and width(patch) == 1


@track_stats
def hline(
    patch: Patch
) -> Boolean:
    """ whether the piece forms a horizontal line """
    return width(patch) == len(patch) and height(patch) == 1


@track_stats
def palette(
    grid: Grid
) -> FrozenSet:
    """ set of colors occurring in grid """
    return frozenset(v for r in grid for v in r)


@track_stats
def palette_tuple(
    grid: Grid
) -> Tuple:
    """ set of colors occurring in grid """
    return tuple(set(v for r in grid for v in r))


@track_stats
def color(
    obj: Object
) -> Integer:
    """ color of object """
    return next(iter(obj))[0]


@track_stats
def color_tuple(
    obj: ObjectTuple
) -> Integer:
    """ color of object """
    return next(iter(obj))[0]


@track_stats
def colors(
    objs: Objects
) -> FrozenSet:
    """ colors of objects """
    return frozenset(color(obj) for obj in objs)


@track_stats
def colors_tuple(
    objs: ObjectsTuple
) -> Tuple:
    """ colors of objects """
    return tuple(color_tuple(obj) for obj in objs)


@track_stats
def togrid(
    objs: Objects,
    dims: IntegerTuple
) -> Grid:
    """ convert objects to grid """
    h, w = dims
    grid = [[0 for j in range(w)] for i in range(h)]
    for obj in objs:
        for val, (i, j) in obj:
            if 0 <= i < h and 0 <= j < w:
                grid[i][j] = val
    return tuple(tuple(r) for r in grid)


@track_stats
def togrid_tuple(
    objs: ObjectsTuple,
    dims: IntegerTuple
) -> Grid:
    """ convert objects to grid """
    h, w = dims
    grid = [[0 for j in range(w)] for i in range(h)]
    for obj in objs:
        for val, (i, j) in obj:
            if 0 <= i < h and 0 <= j < w:
                grid[i][j] = val
    return tuple(tuple(r) for r in grid)


@track_stats
def background(
    grid: Grid
) -> Integer:
    """ background color """
    return mostcolor(grid)


@track_stats
def foreground(
    grid: Grid
) -> Integer:
    """ foreground color """
    return leastcolor(grid)


@track_stats
def rotate(
    grid: Grid
) -> Grid:
    """ rotate grid 90 degrees clockwise """
    return tuple(tuple(grid[len(grid) - 1 - i][j] for i in range(len(grid))) for j in range(len(grid[0])))


@track_stats
def flip_h(
    grid: Grid
) -> Grid:
    """ flip grid horizontally """
    return tuple(tuple(r[len(r) - 1 - j] for j in range(len(r))) for r in grid)


@track_stats
def flip_v(
    grid: Grid
) -> Grid:
    """ flip grid vertically """
    return tuple(grid[len(grid) - 1 - i] for i in range(len(grid)))


@track_stats
def trim(
    grid: Grid
) -> Grid:
    """ trim empty rows and columns """
    h, w = len(grid), len(grid[0])
    rows = [i for i in range(h) if any(grid[i][j] != 0 for j in range(w))]
    if not rows:
        return ((0,),)
    cols = [j for j in range(w) if any(grid[i][j] != 0 for i in range(h))]
    if not cols:
        return tuple((0,) for i in range(len(rows)))
    return tuple(tuple(grid[i][j] for j in cols) for i in rows)


@track_stats
def pad(
    grid: Grid,
    n: Integer
) -> Grid:
    """ pad grid with zeros """
    h, w = len(grid), len(grid[0])
    return tuple(
        tuple(0 for j in range(w + 2 * n)) if i < n or i >= h + n else
        tuple(0 for j in range(n)) + grid[i - n] + tuple(0 for j in range(n))
        for i in range(h + 2 * n)
    )


@track_stats
def replace(
    grid: Grid,
    old: Integer,
    new: Integer
) -> Grid:
    """ replace color in grid """
    return tuple(tuple(new if v == old else v for v in r) for r in grid)


@track_stats
def fill(
    grid: Grid,
    value: Integer,
    indices: Indices
) -> Grid:
    """ fill indices with value """
    result = [list(r) for r in grid]
    for i, j in indices:
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            result[i][j] = value
    return tuple(tuple(r) for r in result)


@track_stats
def fill_tuple(
    grid: Grid,
    value: Integer,
    indices: IndiceTuple
) -> Grid:
    """ fill indices with value """
    result = [list(r) for r in grid]
    for i, j in indices:
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            result[i][j] = value
    return tuple(tuple(r) for r in result)


@track_stats
def copy(
    grid: Grid
) -> Grid:
    """ copy grid """
    return tuple(tuple(v for v in r) for r in grid)


@track_stats
def empty(
    h: Integer,
    w: Integer
) -> Grid:
    """ empty grid """
    return tuple(tuple(0 for j in range(w)) for i in range(h))


@track_stats
def stack_v(
    a: Grid,
    b: Grid
) -> Grid:
    """ stack grids vertically """
    if not a:
        return b
    if not b:
        return a
    if len(a[0]) != len(b[0]):
        return a
    return tuple(r for r in a) + tuple(r for r in b)


@track_stats
def stack_h(
    a: Grid,
    b: Grid
) -> Grid:
    """ stack grids horizontally """
    if not a:
        return b
    if not b:
        return a
    if len(a) != len(b):
        return a
    return tuple(a[i] + b[i] for i in range(len(a)))


@track_stats
def concat_v(
    grids: Container
) -> Grid:
    """ concatenate grids vertically """
    if not grids:
        return tuple()
    result = tuple()
    for grid in grids:
        result = stack_v(result, grid)
    return result


@track_stats
def concat_h(
    grids: Container
) -> Grid:
    """ concatenate grids horizontally """
    if not grids:
        return tuple()
    result = tuple()
    for grid in grids:
        result = stack_h(result, grid)
    return result


@track_stats
def subgrid(
    grid: Grid,
    obj: Object
) -> Grid:
    """ extract subgrid containing object """
    if not obj:
        return ((0,),)
    indices = toindices(obj)
    i_min = min(i for i, j in indices)
    i_max = max(i for i, j in indices)
    j_min = min(j for i, j in indices)
    j_max = max(j for i, j in indices)
    result = [[0 for j in range(j_max - j_min + 1)] for i in range(i_max - i_min + 1)]
    for val, (i, j) in obj:
        result[i - i_min][j - j_min] = val
    return tuple(tuple(r) for r in result)


@track_stats
def subgrid_tuple(
    grid: Grid,
    obj: ObjectTuple
) -> Grid:
    """ extract subgrid containing object """
    if not obj:
        return ((0,),)
    indices = toindices(obj)
    i_min = min(i for i, j in indices)
    i_max = max(i for i, j in indices)
    j_min = min(j for i, j in indices)
    j_max = max(j for i, j in indices)
    result = [[0 for j in range(j_max - j_min + 1)] for i in range(i_max - i_min + 1)]
    for val, (i, j) in obj:
        result[i - i_min][j - j_min] = val
    return tuple(tuple(r) for r in result)


@track_stats
def place(
    grid: Grid,
    obj: Object,
    loc: IntegerTuple
) -> Grid:
    """ place object at location """
    result = [list(r) for r in grid]
    for val, (i, j) in obj:
        ni, nj = i - ulcorner(obj)[0] + loc[0], j - ulcorner(obj)[1] + loc[1]
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
            result[ni][nj] = val
    return tuple(tuple(r) for r in result)


@track_stats
def place_tuple(
    grid: Grid,
    obj: ObjectTuple,
    loc: IntegerTuple
) -> Grid:
    """ place object at location """
    result = [list(r) for r in grid]
    for val, (i, j) in obj:
        ni, nj = i - ulcorner(obj)[0] + loc[0], j - ulcorner(obj)[1] + loc[1]
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
            result[ni][nj] = val
    return tuple(tuple(r) for r in result)


@track_stats
def inside(
    grid: Grid,
    loc: IntegerTuple
) -> Boolean:
    """ whether location is inside grid """
    return 0 <= loc[0] < len(grid) and 0 <= loc[1] < len(grid[0])


@track_stats
def get(
    grid: Grid,
    loc: IntegerTuple
) -> Integer:
    """ get value at location """
    if inside(grid, loc):
        return grid[loc[0]][loc[1]]
    return 0


@track_stats
def set(
    grid: Grid,
    loc: IntegerTuple,
    value: Integer
) -> Grid:
    """ set value at location """
    if not inside(grid, loc):
        return grid
    result = [list(r) for r in grid]
    result[loc[0]][loc[1]] = value
    return tuple(tuple(r) for r in result)


@track_stats
def draw_h(
    grid: Grid,
    i: Integer,
    j_start: Integer,
    j_end: Integer,
    value: Integer
) -> Grid:
    """ draw horizontal line """
    result = [list(r) for r in grid]
    for j in range(min(j_start, j_end), max(j_start, j_end) + 1):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            result[i][j] = value
    return tuple(tuple(r) for r in result)


@track_stats
def draw_v(
    grid: Grid,
    j: Integer,
    i_start: Integer,
    i_end: Integer,
    value: Integer
) -> Grid:
    """ draw vertical line """
    result = [list(r) for r in grid]
    for i in range(min(i_start, i_end), max(i_start, i_end) + 1):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            result[i][j] = value
    return tuple(tuple(r) for r in result)


@track_stats
def draw_line(
    grid: Grid,
    start: IntegerTuple,
    end: IntegerTuple,
    value: Integer
) -> Grid:
    """ draw line """
    result = [list(r) for r in grid]
    i_start, j_start = start
    i_end, j_end = end
    if i_start == i_end:
        for j in range(min(j_start, j_end), max(j_start, j_end) + 1):
            if 0 <= i_start < len(grid) and 0 <= j < len(grid[0]):
                result[i_start][j] = value
    elif j_start == j_end:
        for i in range(min(i_start, i_end), max(i_start, i_end) + 1):
            if 0 <= i < len(grid) and 0 <= j_start < len(grid[0]):
                result[i][j_start] = value
    else:
        di = i_end - i_start
        dj = j_end - j_start
        steps = max(abs(di), abs(dj))
        for s in range(steps + 1):
            i = i_start + di * s // steps
            j = j_start + dj * s // steps
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                result[i][j] = value
    return tuple(tuple(r) for r in result)


@track_stats
def draw_rect(
    grid: Grid,
    start: IntegerTuple,
    end: IntegerTuple,
    value: Integer
) -> Grid:
    """ draw rectangle """
    result = [list(r) for r in grid]
    i_start, j_start = start
    i_end, j_end = end
    for i in range(min(i_start, i_end), max(i_start, i_end) + 1):
        for j in range(min(j_start, j_end), max(j_start, j_end) + 1):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                result[i][j] = value
    return tuple(tuple(r) for r in result)


@track_stats
def draw_frame(
    grid: Grid,
    start: IntegerTuple,
    end: IntegerTuple,
    value: Integer
) -> Grid:
    """ draw rectangle frame """
    result = [list(r) for r in grid]
    i_start, j_start = start
    i_end, j_end = end
    for i in range(min(i_start, i_end), max(i_start, i_end) + 1):
        for j in range(min(j_start, j_end), max(j_start, j_end) + 1):
            if (i == i_start or i == i_end or j == j_start or j == j_end) and 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                result[i][j] = value
    return tuple(tuple(r) for r in result)


@track_stats
def draw_poly(
    grid: Grid,
    points: Container,
    value: Integer
) -> Grid:
    """ draw polygon """
    result = grid
    for i in range(len(points)):
        result = draw_line(result, points[i], points[(i + 1) % len(points)], value)
    return result


@track_stats
def flood(
    grid: Grid,
    loc: IntegerTuple,
    value: Integer
) -> Grid:
    """ flood fill """
    if not inside(grid, loc):
        return grid
    result = [list(r) for r in grid]
    old = grid[loc[0]][loc[1]]
    if old == value:
        return grid
    queue = [loc]
    while queue:
        i, j = queue.pop(0)
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0])) or result[i][j] != old:
            continue
        result[i][j] = value
        queue.append((i - 1, j))
        queue.append((i + 1, j))
        queue.append((i, j - 1))
        queue.append((i, j + 1))
    return tuple(tuple(r) for r in result)


@track_stats
def boundary(
    grid: Grid,
    value: Integer
) -> Indices:
    """ boundary of color """
    indices = ofcolor(grid, value)
    h, w = len(grid), len(grid[0])
    return frozenset((i, j) for i, j in indices if any(
        0 <= ni < h and 0 <= nj < w and grid[ni][nj] != value
        for ni, nj in dneighbors((i, j))
    ))


@track_stats
def boundary_tuple(
    grid: Grid,
    value: Integer
) -> IndiceTuple:
    """ boundary of color """
    indices = ofcolor(grid, value)
    h, w = len(grid), len(grid[0])
    return tuple((i, j) for i, j in indices if any(
        0 <= ni < h and 0 <= nj < w and grid[ni][nj] != value
        for ni, nj in dneighbors((i, j))
    ))


@track_stats
def outline(
    grid: Grid,
    value: Integer
) -> Indices:
    """ outline of color """
    indices = ofcolor(grid, value)
    h, w = len(grid), len(grid[0])
    return frozenset((i, j) for i in range(h) for j in range(w) if grid[i][j] != value and any(
        0 <= ni < h and 0 <= nj < w and grid[ni][nj] == value
        for ni, nj in dneighbors((i, j))
    ))


@track_stats
def outline_tuple(
    grid: Grid,
    value: Integer
) -> IndiceTuple:
    """ outline of color """
    indices = ofcolor(grid, value)
    h, w = len(grid), len(grid[0])
    return tuple((i, j) for i in range(h) for j in range(w) if grid[i][j] != value and any(
        0 <= ni < h and 0 <= nj < w and grid[ni][nj] == value
        for ni, nj in dneighbors((i, j))
    ))


@track_stats
def overlay(
    a: Grid,
    b: Grid
) -> Grid:
    """ overlay b on a """
    h = max(len(a), len(b))
    w = max(len(a[0]), len(b[0]))
    result = [[0 for j in range(w)] for i in range(h)]
    for i in range(min(len(a), h)):
        for j in range(min(len(a[0]), w)):
            result[i][j] = a[i][j]
    for i in range(min(len(b), h)):
        for j in range(min(len(b[0]), w)):
            if b[i][j] != 0:
                result[i][j] = b[i][j]
    return tuple(tuple(r) for r in result)


@track_stats
def mask(
    a: Grid,
    b: Grid
) -> Grid:
    """ mask a with b """
    h = min(len(a), len(b))
    w = min(len(a[0]), len(b[0]))
    result = [[0 for j in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            if b[i][j] != 0:
                result[i][j] = a[i][j]
    return tuple(tuple(r) for r in result)


@track_stats
def submask(
    a: Grid,
    b: Grid
) -> Grid:
    """ mask a with b """
    h = min(len(a), len(b))
    w = min(len(a[0]), len(b[0]))
    result = [[0 for j in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            if b[i][j] == 0:
                result[i][j] = a[i][j]
    return tuple(tuple(r) for r in result)


@track_stats
def combine_h(
    a: Grid,
    b: Grid
) -> Grid:
    """ combine horizontally """
    h = max(len(a), len(b))
    w = len(a[0]) + len(b[0])
    result = [[0 for j in range(w)] for i in range(h)]
    for i in range(min(len(a), h)):
        for j in range(len(a[0])):
            result[i][j] = a[i][j]
    for i in range(min(len(b), h)):
        for j in range(len(b[0])):
            result[i][j + len(a[0])] = b[i][j]
    return tuple(tuple(r) for r in result)


@track_stats
def combine_v(
    a: Grid,
    b: Grid
) -> Grid:
    """ combine vertically """
    h = len(a) + len(b)
    w = max(len(a[0]), len(b[0]))
    result = [[0 for j in range(w)] for i in range(h)]
    for i in range(len(a)):
        for j in range(min(len(a[0]), w)):
            result[i][j] = a[i][j]
    for i in range(len(b)):
        for j in range(min(len(b[0]), w)):
            result[i + len(a)][j] = b[i][j]
    return tuple(tuple(r) for r in result)


@track_stats
def repeat_h(
    grid: Grid,
    n: Integer
) -> Grid:
    """ repeat horizontally """
    if n <= 0:
        return ((0,),)
    result = grid
    for i in range(n - 1):
        result = combine_h(result, grid)
    return result


@track_stats
def repeat_v(
    grid: Grid,
    n: Integer
) -> Grid:
    """ repeat vertically """
    if n <= 0:
        return ((0,),)
    result = grid
    for i in range(n - 1):
        result = combine_v(result, grid)
    return result


@track_stats
def repeat_grid(
    grid: Grid,
    n: Integer,
    m: Integer
) -> Grid:
    """ repeat grid """
    return repeat_v(repeat_h(grid, n), m)


@track_stats
def crop_to(
    grid: Grid,
    h: Integer,
    w: Integer
) -> Grid:
    """ crop to size """
    return tuple(tuple(grid[i][j] for j in range(min(len(grid[0]), w))) for i in range(min(len(grid), h)))


@track_stats
def resize(
    grid: Grid,
    h: Integer,
    w: Integer
) -> Grid:
    """ resize grid """
    result = [[0 for j in range(w)] for i in range(h)]
    for i in range(min(len(grid), h)):
        for j in range(min(len(grid[0]), w)):
            result[i][j] = grid[i][j]
    return tuple(tuple(r) for r in result)


@track_stats
def scale(
    grid: Grid,
    n: Integer
) -> Grid:
    """ scale grid """
    if n <= 0:
        return ((0,),)
    h, w = len(grid), len(grid[0])
    result = [[0 for j in range(w * n)] for i in range(h * n)]
    for i in range(h):
        for j in range(w):
            for di in range(n):
                for dj in range(n):
                    result[i * n + di][j * n + dj] = grid[i][j]
    return tuple(tuple(r) for r in result)


@track_stats
def hmirror(
    grid: Grid
) -> Grid:
    """ horizontal mirror """
    h, w = len(grid), len(grid[0])
    result = [[0 for j in range(w * 2)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            result[i][j] = grid[i][j]
            result[i][w * 2 - 1 - j] = grid[i][j]
    return tuple(tuple(r) for r in result)


@track_stats
def vmirror(
    grid: Grid
) -> Grid:
    """ vertical mirror """
    h, w = len(grid), len(grid[0])
    result = [[0 for j in range(w)] for i in range(h * 2)]
    for i in range(h):
        for j in range(w):
            result[i][j] = grid[i][j]
            result[h * 2 - 1 - i][j] = grid[i][j]
    return tuple(tuple(r) for r in result)


@track_stats
def hmirror_extend(
    grid: Grid
) -> Grid:
    """ horizontal mirror extension """
    h, w = len(grid), len(grid[0])
    result = [[0 for j in range(w * 2 - 1)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            result[i][j] = grid[i][j]
            if j < w - 1:
                result[i][w * 2 - 2 - j] = grid[i][j]
    return tuple(tuple(r) for r in result)


@track_stats
def vmirror_extend(
    grid: Grid
) -> Grid:
    """ vertical mirror extension """
    h, w = len(grid), len(grid[0])
    result = [[0 for j in range(w)] for i in range(h * 2 - 1)]
    for i in range(h):
        for j in range(w):
            result[i][j] = grid[i][j]
            if i < h - 1:
                result[h * 2 - 2 - i][j] = grid[i][j]
    return tuple(tuple(r) for r in result)


@track_stats
def transpose(
    grid: Grid
) -> Grid:
    """ transpose grid """
    h, w = len(grid), len(grid[0])
    result = [[0 for j in range(h)] for i in range(w)]
    for i in range(h):
        for j in range(w):
            result[j][i] = grid[i][j]
    return tuple(tuple(r) for r in result)


@track_stats
def diagonal(
    grid: Grid
) -> Grid:
    """ diagonal grid """
    h, w = len(grid), len(grid[0])
    result = [[0 for j in range(h)] for i in range(w)]
    for i in range(h):
        for j in range(w):
            result[j][h - 1 - i] = grid[i][j]
    return tuple(tuple(r) for r in result)


@track_stats
def antidiagonal(
    grid: Grid
) -> Grid:
    """ antidiagonal grid """
    h, w = len(grid), len(grid[0])
    result = [[0 for j in range(h)] for i in range(w)]
    for i in range(h):
        for j in range(w):
            result[w - 1 - j][i] = grid[i][j]
    return tuple(tuple(r) for r in result)


@track_stats
def invert_colors(
    grid: Grid
) -> Grid:
    """ invert colors """
    max_color = max(v for r in grid for v in r)
    return tuple(tuple(max_color - v for v in r) for r in grid)


@track_stats
def sort_colors(
    grid: Grid
) -> Grid:
    """ sort colors """
    colors = sorted(set(v for r in grid for v in r))
    color_map = {c: i for i, c in enumerate(colors)}
    return tuple(tuple(color_map[v] for v in r) for r in grid)


@track_stats
def sort_rows(
    grid: Grid
) -> Grid:
    """ sort rows """
    return tuple(sorted(grid))


@track_stats
def sort_cols(
    grid: Grid
) -> Grid:
    """ sort columns """
    return transpose(sort_rows(transpose(grid)))


@track_stats
def unique_rows(
    grid: Grid
) -> Grid:
    """ unique rows """
    return tuple(r for i, r in enumerate(grid) if grid.index(r) == i)


@track_stats
def unique_cols(
    grid: Grid
) -> Grid:
    """ unique columns """
    return transpose(unique_rows(transpose(grid)))


@track_stats
def count_unique_rows(
    grid: Grid
) -> Integer:
    """ count unique rows """
    return len(set(grid))


@track_stats
def count_unique_cols(
    grid: Grid
) -> Integer:
    """ count unique columns """
    return len(set(transpose(grid)))


@track_stats
def count_unique_colors(
    grid: Grid
) -> Integer:
    """ count unique colors """
    return len(set(v for r in grid for v in r))


@track_stats
def count_colors(
    grid: Grid
) -> Integer:
    """ count colors """
    return len(set(v for r in grid for v in r if v != 0))


@track_stats
def count_nonzero(
    grid: Grid
) -> Integer:
    """ count nonzero """
    return sum(1 for r in grid for v in r if v != 0)


@track_stats
def count_value(
    grid: Grid,
    value: Integer
) -> Integer:
    """ count value """
    return sum(1 for r in grid for v in r if v == value)


@track_stats
def count_values(
    grid: Grid
) -> Dict:
    """ count values """
    return {v: sum(1 for r in grid for vv in r if vv == v) for v in set(v for r in grid for v in r)}


@track_stats
def count_row_values(
    grid: Grid,
    i: Integer
) -> Dict:
    """ count values in row """
    if not (0 <= i < len(grid)):
        return {}
    return {v: grid[i].count(v) for v in set(grid[i])}


@track_stats
def count_col_values(
    grid: Grid,
    j: Integer
) -> Dict:
    """ count values in column """
    if not (0 <= j < len(grid[0])):
        return {}
    return {v: sum(1 for i in range(len(grid)) if grid[i][j] == v) for v in set(grid[i][j] for i in range(len(grid)))}


@track_stats
def count_row_nonzero(
    grid: Grid,
    i: Integer
) -> Integer:
    """ count nonzero in row """
    if not (0 <= i < len(grid)):
        return 0
    return sum(1 for v in grid[i] if v != 0)


@track_stats
def count_col_nonzero(
    grid: Grid,
    j: Integer
) -> Integer:
    """ count nonzero in column """
    if not (0 <= j < len(grid[0])):
        return 0
    return sum(1 for i in range(len(grid)) if grid[i][j] != 0)


@track_stats
def count_row_value(
    grid: Grid,
    i: Integer,
    value: Integer
) -> Integer:
    """ count value in row """
    if not (0 <= i < len(grid)):
        return 0
    return sum(1 for v in grid[i] if v == value)


@track_stats
def count_col_value(
    grid: Grid,
    j: Integer,
    value: Integer
) -> Integer:
    """ count value in column """
    if not (0 <= j < len(grid[0])):
        return 0
    return sum(1 for i in range(len(grid)) if grid[i][j] == value)


@track_stats
def count_row_unique(
    grid: Grid,
    i: Integer
) -> Integer:
    """ count unique in row """
    if not (0 <= i < len(grid)):
        return 0
    return len(set(grid[i]))


@track_stats
def count_col_unique(
    grid: Grid,
    j: Integer
) -> Integer:
    """ count unique in column """
    if not (0 <= j < len(grid[0])):
        return 0
    return len(set(grid[i][j] for i in range(len(grid))))


@track_stats
def count_row_unique_nonzero(
    grid: Grid,
    i: Integer
) -> Integer:
    """ count unique nonzero in row """
    if not (0 <= i < len(grid)):
        return 0
    return len(set(v for v in grid[i] if v != 0))


@track_stats
def count_col_unique_nonzero(
    grid: Grid,
    j: Integer
) -> Integer:
    """ count unique nonzero in column """
    if not (0 <= j < len(grid[0])):
        return 0
    return len(set(grid[i][j] for i in range(len(grid)) if grid[i][j] != 0))


@track_stats
def count_row_runs(
    grid: Grid,
    i: Integer
) -> Integer:
    """ count runs in row """
    if not (0 <= i < len(grid)):
        return 0
    if not grid[i]:
        return 0
    return sum(1 for j in range(1, len(grid[i])) if grid[i][j] != grid[i][j - 1]) + 1


@track_stats
def count_col_runs(
    grid: Grid,
    j: Integer
) -> Integer:
    """ count runs in column """
    if not (0 <= j < len(grid[0])):
        return 0
    if not grid:
        return 0
    return sum(1 for i in range(1, len(grid)) if grid[i][j] != grid[i - 1][j]) + 1


@track_stats
def count_row_value_runs(
    grid: Grid,
    i: Integer,
    value: Integer
) -> Integer:
    """ count value runs in row """
    if not (0 <= i < len(grid)):
        return 0
    if not grid[i]:
        return 0
    runs = 0
    in_run = False
    for j in range(len(grid[i])):
        if grid[i][j] == value:
            if not in_run:
                runs += 1
                in_run = True
        else:
            in_run = False
    return runs


@track_stats
def count_col_value_runs(
    grid: Grid,
    j: Integer,
    value: Integer
) -> Integer:
    """ count value runs in column """
    if not (0 <= j < len(grid[0])):
        return 0
    if not grid:
        return 0
    runs = 0
    in_run = False
    for i in range(len(grid)):
        if grid[i][j] == value:
            if not in_run:
                runs += 1
                in_run = True
        else:
            in_run = False
    return runs


@track_stats
def count_row_value_run_lengths(
    grid: Grid,
    i: Integer,
    value: Integer
) -> List:
    """ count value run lengths in row """
    if not (0 <= i < len(grid)):
        return []
    if not grid[i]:
        return []
    runs = []
    run_length = 0
    for j in range(len(grid[i])):
        if grid[i][j] == value:
            run_length += 1
        elif run_length > 0:
            runs.append(run_length)
            run_length = 0
    if run_length > 0:
        runs.append(run_length)
    return runs


@track_stats
def count_col_value_run_lengths(
    grid: Grid,
    j: Integer,
    value: Integer
) -> List:
    """ count value run lengths in column """
    if not (0 <= j < len(grid[0])):
        return []
    if not grid:
        return []
    runs = []
    run_length = 0
    for i in range(len(grid)):
        if grid[i][j] == value:
            run_length += 1
        elif run_length > 0:
            runs.append(run_length)
            run_length = 0
    if run_length > 0:
        runs.append(run_length)
    return runs


@track_stats
def count_row_value_max_run(
    grid: Grid,
    i: Integer,
    value: Integer
) -> Integer:
    """ count value max run in row """
    if not (0 <= i < len(grid)):
        return 0
    if not grid[i]:
        return 0
    max_run = 0
    run_length = 0
    for j in range(len(grid[i])):
        if grid[i][j] == value:
            run_length += 1
        else:
            max_run = max(max_run, run_length)
            run_length = 0
    max_run = max(max_run, run_length)
    return max_run


@track_stats
def count_col_value_max_run(
    grid: Grid,
    j: Integer,
    value: Integer
) -> Integer:
    """ count value max run in column """
    if not (0 <= j < len(grid[0])):
        return 0
    if not grid:
        return 0
    max_run = 0
    run_length = 0
    for i in range(len(grid)):
        if grid[i][j] == value:
            run_length += 1
        else:
            max_run = max(max_run, run_length)
            run_length = 0
    max_run = max(max_run, run_length)
    return max_run


@track_stats
def count_row_value_min_run(
    grid: Grid,
    i: Integer,
    value: Integer
) -> Integer:
    """ count value min run in row """
    if not (0 <= i < len(grid)):
        return 0
    if not grid[i]:
        return 0
    runs = count_row_value_run_lengths(grid, i, value)
    return min(runs) if runs else 0


@track_stats
def count_col_value_min_run(
    grid: Grid,
    j: Integer,
    value: Integer
) -> Integer:
    """ count value min run in column """
    if not (0 <= j < len(grid[0])):
        return 0
    if not grid:
        return 0
    runs = count_col_value_run_lengths(grid, j, value)
    return min(runs) if runs else 0


@track_stats
def count_row_value_avg_run(
    grid: Grid,
    i: Integer,
    value: Integer
) -> Integer:
    """ count value avg run in row """
    if not (0 <= i < len(grid)):
        return 0
    if not grid[i]:
        return 0
    runs = count_row_value_run_lengths(grid, i, value)
    return sum(runs) // len(runs) if runs else 0


@track_stats
def count_col_value_avg_run(
    grid: Grid,
    j: Integer,
    value: Integer
) -> Integer:
    """ count value avg run in column """
    if not (0 <= j < len(grid[0])):
        return 0
    if not grid:
        return 0
    runs = count_col_value_run_lengths(grid, j, value)
    return sum(runs) // len(runs) if runs else 0


@track_stats
def count_row_value_median_run(
    grid: Grid,
    i: Integer,
    value: Integer
) -> Integer:
    """ count value median run in row """
    if not (0 <= i < len(grid)):
        return 0
    if not grid[i]:
        return 0
    runs = count_row_value_run_lengths(grid, i, value)
    return runs[len(runs) // 2] if runs else 0


@track_stats
def count_col_value_median_run(
    grid: Grid,
    j: Integer,
    value: Integer
) -> Integer:
    """ count value median run in column """
    if not (0 <= j < len(grid[0])):
        return 0
    if not grid:
        return 0
    runs = count_col_value_run_lengths(grid, j, value)
    return runs[len(runs) // 2] if runs else 0


@track_stats
def count_row_value_mode_run(
    grid: Grid,
    i: Integer,
    value: Integer
) -> Integer:
    """ count value mode run in row """
    if not (0 <= i < len(grid)):
        return 0
    if not grid[i]:
        return 0
    runs = count_row_value_run_lengths(grid, i, value)
    return max(set(runs), key=runs.count) if runs else 0


@track_stats
def count_col_value_mode_run(
    grid: Grid,
    j: Integer,
    value: Integer
) -> Integer:
    """ count value mode run in column """
    if not (0 <= j < len(grid[0])):
        return 0
    if not grid:
        return 0
    runs = count_col_value_run_lengths(grid, j, value)
    return max(set(runs), key=runs.count) if runs else 0


@track_stats
def count_row_value_sum_run(
    grid: Grid,
    i: Integer,
    value: Integer
) -> Integer:
    """ count value sum run in row """
    if not (0 <= i < len(grid)):
        return 0
    if not grid[i]:
        return 0
    runs = count_row_value_run_lengths(grid, i, value)
    return sum(runs) if runs else 0


@track_stats
def count_col_value_sum_run(
    grid: Grid,
    j: Integer,
    value: Integer
) -> Integer:
    """ count value sum run in column """
    if not (0 <= j < len(grid[0])):
        return 0
    if not grid:
        return 0
    runs = count_col_value_run_lengths(grid, j, value)
    return sum(runs) if runs else 0


@track_stats
def count_row_value_product_run(
    grid: Grid,
    i: Integer,
    value: Integer
) -> Integer:
    """ count value product run in row """
    if not (0 <= i < len(grid)):
        return 0
    if not grid[i]:
        return 0
    runs = count_row_value_run_lengths(grid, i, value)
    product = 1
    for run in runs:
        product *= run
    return product if runs else 0


@track_stats
def count_col_value_product_run(
    grid: Grid,
    j: Integer,
    value: Integer
) -> Integer:
    """ count value product run in column """
    if not (0 <= j < len(grid[0])):
        return 0
    if not grid:
        return 0
    runs = count_col_value_run_lengths(grid, j, value)
    product = 1
    for run in runs:
        product *= run
    return product if runs else 0
