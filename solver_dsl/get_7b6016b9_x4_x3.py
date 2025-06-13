def get_7b6016b9_x4_x3(a1: FrozenSet, a2: Callable) -> Callable:
    return mfilter_f(a1, compose(flip, a2))

# {'a1': 'FrozenSet', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_7b6016b9_x4_x3', 'Callable', 'FrozenSet', 'Callable'): 'mfilter_f(a1, compose(flip, a2))'}

