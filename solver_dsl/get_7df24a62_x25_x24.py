def get_7df24a62_x25_x24(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(product, a1, compose(a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_7df24a62_x25_x24', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(product, a1, compose(a2, a3))'}

