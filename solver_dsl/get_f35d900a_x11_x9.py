def get_f35d900a_x11_x9(a1: FrozenSet, a2: Container[Container]) -> FrozenSet:
    return difference(a1, mapply(toindices, a2))

# {'a1': 'FrozenSet', 'return': 'FrozenSet', 'a2': 'Container[Container]'}

func_d = {('get_f35d900a_x11_x9', 'FrozenSet', 'FrozenSet', 'Container[Container]'): 'difference(a1, mapply(toindices, a2))'}

