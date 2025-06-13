def get_ecdecbb3_x15_x14(a1: FrozenSet, a2: Callable) -> Callable:
    return mfilter_f(a1, compose(a2, size))

# {'a1': 'FrozenSet', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_ecdecbb3_x15_x14', 'Callable', 'FrozenSet', 'Callable'): 'mfilter_f(a1, compose(a2, size))'}

