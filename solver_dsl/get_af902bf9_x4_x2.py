def get_af902bf9_x4_x2(a1: Container, a2: Callable) -> FrozenSet:
    return mfilter_f(prapply(connect, a1, a1), a2)

# {'a2': 'Callable', 'return': 'FrozenSet', 'a1': 'Container'}

func_d = {('get_af902bf9_x4_x2', 'FrozenSet', 'Container', 'Callable'): 'mfilter_f(prapply(connect, a1, a1), a2)'}

