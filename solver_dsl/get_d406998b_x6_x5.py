def get_d406998b_x6_x5(a1: FrozenSet, a2: Callable) -> Callable:
    return sfilter_f(a1, compose(even, a2))

# {'a1': 'FrozenSet', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_d406998b_x6_x5', 'Callable', 'FrozenSet', 'Callable'): 'sfilter_f(a1, compose(even, a2))'}

