def get_99fa7670_x13_x10(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(connect, compose(a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_99fa7670_x13_x10', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(connect, compose(a1, a2), a3)'}

