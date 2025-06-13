def get_fafffa47_x8_x7(a1: FrozenSet, a2: Grid) -> FrozenSet[Tuple[int, int]]:
    return intersection(a1, f_ofcolor(a2, ZERO))

# {'a1': 'FrozenSet', 'return': 'FrozenSet[Tuple[int, int]]', 'a2': 'Grid'}

func_d = {('get_fafffa47_x8_x7', 'FrozenSet[Tuple[int, int]]', 'FrozenSet', 'Grid'): 'intersection(a1, f_ofcolor(a2, ZERO))'}

