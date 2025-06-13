def get_f35d900a_x20_x19(a1: FrozenSet, a2: Callable) -> Callable:
    return sfilter_f(a1, compose(even, a2))

# {'a1': 'FrozenSet', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_f35d900a_x20_x19', 'Callable', 'FrozenSet', 'Callable'): 'sfilter_f(a1, compose(even, a2))'}

