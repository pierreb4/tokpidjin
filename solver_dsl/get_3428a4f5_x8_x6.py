def get_3428a4f5_x8_x6(a1: FrozenSet, a2: Grid) -> FrozenSet[Tuple[int, int]]:
    return intersection(a1, f_ofcolor(a2, TWO))

# {'a1': typing.FrozenSet, 'return': typing.FrozenSet[typing.Tuple[int, int]], 'a2': 'Grid', 'TWO': 'C_'}
