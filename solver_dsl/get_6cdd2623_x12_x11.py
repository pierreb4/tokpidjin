def get_6cdd2623_x12_x11(a1: FrozenSet, a2: Callable, a3: Callable) -> Callable:
    return mfilter_f(a1, fork(both, a2, a3))

# {'a1': 'FrozenSet', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_6cdd2623_x12_x11', 'Callable', 'FrozenSet', 'Callable', 'Callable'): 'mfilter_f(a1, fork(both, a2, a3))'}

