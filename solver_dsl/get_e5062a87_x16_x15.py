def get_e5062a87_x16_x15(a1: FrozenSet, a2: Callable, a3: Callable) -> Callable:
    return sfilter_f(a1, chain(flip, a2, a3))

# {'a1': 'FrozenSet', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_e5062a87_x16_x15', 'Callable', 'FrozenSet', 'Callable', 'Callable'): 'sfilter_f(a1, chain(flip, a2, a3))'}

