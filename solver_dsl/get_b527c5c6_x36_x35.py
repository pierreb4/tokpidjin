def get_b527c5c6_x36_x35(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(mapply, a1, compose(a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_b527c5c6_x36_x35', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(mapply, a1, compose(a2, a3))'}

