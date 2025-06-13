def get_a64e4611_x22_x5(a1: Callable, a2: Callable) -> Callable:
    return compose(compose(asobject, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_a64e4611_x22_x5', 'Callable', 'Callable', 'Callable'): 'compose(compose(asobject, a1), a2)'}

