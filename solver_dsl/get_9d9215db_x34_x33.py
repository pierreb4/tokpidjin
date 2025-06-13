def get_9d9215db_x34_x33(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return chain(normalize, a1, fork(connect, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_9d9215db_x34_x33', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(normalize, a1, fork(connect, a2, a3))'}

