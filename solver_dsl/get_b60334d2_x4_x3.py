def get_b60334d2_x4_x3(a1: Grid, a2: Container[Container]) -> FrozenSet:
    return fill(a1, ONE, mapply(dneighbors, a2))

# {'a1': 'Grid', 'return': 'FrozenSet', 'a2': 'Container[Container]'}

func_d = {('get_b60334d2_x4_x3', 'FrozenSet', 'Grid', 'Container[Container]'): 'fill(a1, ONE, mapply(dneighbors, a2))'}

