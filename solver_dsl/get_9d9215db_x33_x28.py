def get_9d9215db_x33_x28(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(connect, compose(a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_9d9215db_x33_x28', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(connect, compose(a1, a2), a3)'}

