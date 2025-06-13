def get_a699fb00_x5_x4(a1: FrozenSet, a2: Union[FrozenSet[Tuple[int, Tuple[int, int]]], FrozenSet[Tuple[int, int]]]) -> Union[FrozenSet[Tuple[int, Tuple[int, int]]], FrozenSet[Tuple[int, int]]]:
    return intersection(a1, shift(a2, LEFT))

# {'a1': 'FrozenSet', 'return': 'Union[FrozenSet[Tuple[int, Tuple[int, int]]], FrozenSet[Tuple[int, int]]]', 'a2': 'Union[FrozenSet[Tuple[int, Tuple[int, int]]], FrozenSet[Tuple[int, int]]]'}

func_d = {('get_a699fb00_x5_x4', 'Union[FrozenSet[Tuple[int, Tuple[int, int]]], FrozenSet[Tuple[int, int]]]', 'FrozenSet', 'Union[FrozenSet[Tuple[int, Tuple[int, int]]], FrozenSet[Tuple[int, int]]]'): 'intersection(a1, shift(a2, LEFT))'}

