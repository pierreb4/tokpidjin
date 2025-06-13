def get_7df24a62_x5_x4(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return chain(a1, a2, compose(normalize, a3))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Callable'}

func_d = {('get_7df24a62_x5_x4', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(a1, a2, compose(normalize, a3))'}

