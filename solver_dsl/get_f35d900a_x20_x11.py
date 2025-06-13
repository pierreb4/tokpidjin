def get_f35d900a_x20_x11(a1: FrozenSet, a2: FrozenSet, a3: Callable) -> FrozenSet:
    return sfilter_f(difference(a1, a2), a3)

# {'a3': 'Callable', 'return': 'FrozenSet', 'a1': 'FrozenSet', 'a2': 'FrozenSet'}

func_d = {('get_f35d900a_x20_x11', 'FrozenSet', 'FrozenSet', 'FrozenSet', 'Callable'): 'sfilter_f(difference(a1, a2), a3)'}

