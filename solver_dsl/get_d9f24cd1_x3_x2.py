def get_d9f24cd1_x3_x2(a1: Container, a2: Grid) -> FrozenSet[Tuple[int, int]]:
    return prapply(connect, a1, f_ofcolor(a2, GRAY))

# {'a1': 'Container', 'return': 'FrozenSet[Tuple[int, int]]', 'a2': 'Grid'}

func_d = {('get_d9f24cd1_x3_x2', 'FrozenSet[Tuple[int, int]]', 'Container', 'Grid'): 'prapply(connect, a1, f_ofcolor(a2, GRAY))'}

