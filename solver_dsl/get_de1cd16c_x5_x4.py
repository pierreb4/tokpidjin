def get_de1cd16c_x5_x4(a1: Callable, a2: FrozenSet, a3: FrozenSet) -> FrozenSet:
    return apply(a1, difference(a2, a3))

# {'a1': 'Callable', 'return': 'FrozenSet', 'a2': 'FrozenSet', 'a3': 'FrozenSet'}

func_d = {('get_de1cd16c_x5_x4', 'FrozenSet', 'Callable', 'FrozenSet', 'FrozenSet'): 'apply(a1, difference(a2, a3))'}

