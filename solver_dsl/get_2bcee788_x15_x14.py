def get_2bcee788_x15_x14(a1: FrozenSet, a2: Callable) -> Callable:
    return sfilter_f(a1, compose(flip, a2))

# {'a1': 'FrozenSet', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_2bcee788_x15_x14', 'Callable', 'FrozenSet', 'Callable'): 'sfilter_f(a1, compose(flip, a2))'}

