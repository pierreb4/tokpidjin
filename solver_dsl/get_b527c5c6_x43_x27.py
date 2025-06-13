def get_b527c5c6_x43_x27(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(mapply, compose(a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_b527c5c6_x43_x27', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(mapply, compose(a1, a2), a3)'}

