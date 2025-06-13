def get_36fdfd69_x10_x4(a1: Container, a2: Callable) -> FrozenSet:
    return sfilter_f(product(a1, a1), a2)

# {'a2': 'Callable', 'return': 'FrozenSet', 'a1': 'Container'}

func_d = {('get_36fdfd69_x10_x4', 'FrozenSet', 'Container', 'Callable'): 'sfilter_f(product(a1, a1), a2)'}

