def get_e6721834_x26_x25(a1: FrozenSet, a2: Callable) -> Callable:
    return mfilter_f(a1, chain(positive, decrement, a2))

# {'a1': 'FrozenSet', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_e6721834_x26_x25', 'Callable', 'FrozenSet', 'Callable'): 'mfilter_f(a1, chain(positive, decrement, a2))'}

