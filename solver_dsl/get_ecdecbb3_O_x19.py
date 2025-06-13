def get_ecdecbb3_O_x19(a1: Grid, a2: Container[Container]) -> FrozenSet:
    return fill(a1, EIGHT, mapply(neighbors, a2))

# {'a1': 'Grid', 'return': 'FrozenSet', 'a2': 'Container[Container]'}

func_d = {('get_ecdecbb3_O_x19', 'FrozenSet', 'Grid', 'Container[Container]'): 'fill(a1, EIGHT, mapply(neighbors, a2))'}

