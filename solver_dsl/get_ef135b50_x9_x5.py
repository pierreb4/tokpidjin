def get_ef135b50_x9_x5(a1: Container, a2: Callable) -> FrozenSet:
    return sfilter_f(product(a1, a1), a2)

# {'a2': 'Callable', 'return': 'FrozenSet', 'a1': 'Container'}

func_d = {('get_ef135b50_x9_x5', 'FrozenSet', 'Container', 'Callable'): 'sfilter_f(product(a1, a1), a2)'}

