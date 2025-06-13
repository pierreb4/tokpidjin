def get_7df24a62_x25_x20(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(product, compose(a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_7df24a62_x25_x20', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(product, compose(a1, a2), a3)'}

