def get_150deff5_x6_x5(a1: Grid, a2: Callable, a3: Container[Container]) -> FrozenSet:
    return fill(a1, EIGHT, mapply(a2, a3))

# {'a1': 'Grid', 'return': 'FrozenSet', 'a2': 'Callable', 'a3': 'Container[Container]'}

func_d = {('get_150deff5_x6_x5', 'FrozenSet', 'Grid', 'Callable', 'Container[Container]'): 'fill(a1, EIGHT, mapply(a2, a3))'}

