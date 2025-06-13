def get_d2abd087_x8_x7(a1: FrozenSet, a2: Callable) -> Callable:
    return mfilter_f(a1, compose(flip, a2))

# {'a1': 'FrozenSet', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_d2abd087_x8_x7', 'Callable', 'FrozenSet', 'Callable'): 'mfilter_f(a1, compose(flip, a2))'}

