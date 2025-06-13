def get_253bf280_x2_x1(a1: Grid) -> FrozenSet[Tuple[int, int]]:
    return prapply(connect, f_ofcolor(a1, EIGHT), f_ofcolor(a1, EIGHT))

# {'return': 'FrozenSet[Tuple[int, int]]', 'a1': 'Grid'}

func_d = {('get_253bf280_x2_x1', 'FrozenSet[Tuple[int, int]]', 'Grid'): 'prapply(connect, f_ofcolor(a1, EIGHT), f_ofcolor(a1, EIGHT))'}

