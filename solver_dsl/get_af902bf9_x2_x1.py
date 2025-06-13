def get_af902bf9_x2_x1(a1: Grid) -> FrozenSet[Tuple[int, int]]:
    return prapply(connect, f_ofcolor(a1, FOUR), f_ofcolor(a1, FOUR))

# {'return': 'FrozenSet[Tuple[int, int]]', 'a1': 'Grid'}

func_d = {('get_af902bf9_x2_x1', 'FrozenSet[Tuple[int, int]]', 'Grid'): 'prapply(connect, f_ofcolor(a1, FOUR), f_ofcolor(a1, FOUR))'}

