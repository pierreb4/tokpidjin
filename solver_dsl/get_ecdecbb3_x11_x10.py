def get_ecdecbb3_x11_x10(a1: Container, a2: Objects) -> FrozenSet[FrozenSet[Tuple[int, Tuple[int, int]]]]:
    return product(a1, colorfilter(a2, EIGHT))

# {'a1': 'Container', 'return': 'FrozenSet[FrozenSet[Tuple[int, Tuple[int, int]]]]', 'a2': 'Objects'}

func_d = {('get_ecdecbb3_x11_x10', 'FrozenSet[FrozenSet[Tuple[int, Tuple[int, int]]]]', 'Container', 'Objects'): 'product(a1, colorfilter(a2, EIGHT))'}

