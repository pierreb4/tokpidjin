def get_e509e548_x12_x11(a1: FrozenSet, a2: Callable) -> Callable:
    return mfilter_f(a1, fork(equality, size, a2))

# {'a1': 'FrozenSet', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_e509e548_x12_x11', 'Callable', 'FrozenSet', 'Callable'): 'mfilter_f(a1, fork(equality, size, a2))'}

