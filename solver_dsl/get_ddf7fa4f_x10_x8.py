def get_ddf7fa4f_x10_x8(a1: Container, a2: Container, a3: Callable) -> FrozenSet:
    return sfilter_f(product(a1, a2), a3)

# {'a3': 'Callable', 'return': 'FrozenSet', 'a1': 'Container', 'a2': 'Container'}

func_d = {('get_ddf7fa4f_x10_x8', 'FrozenSet', 'Container', 'Container', 'Callable'): 'sfilter_f(product(a1, a2), a3)'}

