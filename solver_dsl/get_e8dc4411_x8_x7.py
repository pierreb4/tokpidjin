def get_e8dc4411_x8_x7(a1: FrozenSet, a2: Callable) -> FrozenSet:
    return intersection(a1, a2(a1))

# {'a1': 'FrozenSet', 'return': 'FrozenSet', 'a2': 'Callable'}

func_d = {('get_e8dc4411_x8_x7', 'FrozenSet', 'FrozenSet', 'Callable'): 'intersection(a1, a2(a1))'}

