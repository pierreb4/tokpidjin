def get_91714a58_x12_x11(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return compose(a1, chain(a2, a3, neighbors))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_91714a58_x12_x11', 'Callable', 'Callable', 'Callable', 'Callable'): 'compose(a1, chain(a2, a3, neighbors))'}

