def get_9d9215db_x33_x32(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(connect, a1, compose(a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_9d9215db_x33_x32', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(connect, a1, compose(a2, a3))'}

