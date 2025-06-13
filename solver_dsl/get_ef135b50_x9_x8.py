def get_ef135b50_x9_x8(a1: FrozenSet, a2: Callable, a3: Callable) -> Callable:
    return sfilter_f(a1, fork(equality, a2, a3))

# {'a1': 'FrozenSet', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_ef135b50_x9_x8', 'Callable', 'FrozenSet', 'Callable', 'Callable'): 'sfilter_f(a1, fork(equality, a2, a3))'}

