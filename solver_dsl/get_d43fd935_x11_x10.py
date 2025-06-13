def get_d43fd935_x11_x10(a1: FrozenSet, a2: Callable, a3: Callable) -> Callable:
    return sfilter_f(a1, fork(either, a2, a3))

# {'a1': 'FrozenSet', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_d43fd935_x11_x10', 'Callable', 'FrozenSet', 'Callable', 'Callable'): 'sfilter_f(a1, fork(either, a2, a3))'}

