def get_f35d900a_x13_x9(a1: Callable, a2: Container[Container]) -> FrozenSet:
    return lbind(a1, mapply(toindices, a2))

# {'a1': 'Callable', 'return': 'FrozenSet', 'a2': 'Container[Container]'}

func_d = {('get_f35d900a_x13_x9', 'FrozenSet', 'Callable', 'Container[Container]'): 'lbind(a1, mapply(toindices, a2))'}

