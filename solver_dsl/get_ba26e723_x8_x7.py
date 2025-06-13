def get_ba26e723_x8_x7(a1: FrozenSet, a2: Callable, a3: Callable) -> Callable:
    return sfilter_f(a1, compose(a2, a3))

# {'a1': 'FrozenSet', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_ba26e723_x8_x7', 'Callable', 'FrozenSet', 'Callable', 'Callable'): 'sfilter_f(a1, compose(a2, a3))'}

