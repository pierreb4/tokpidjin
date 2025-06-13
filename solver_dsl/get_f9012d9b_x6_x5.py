def get_f9012d9b_x6_x5(a1: FrozenSet, a2: Callable) -> Callable:
    return mfilter_f(a1, chain(flip, a2, palette_t))

# {'a1': 'FrozenSet', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_f9012d9b_x6_x5', 'Callable', 'FrozenSet', 'Callable'): 'mfilter_f(a1, chain(flip, a2, palette_t))'}

