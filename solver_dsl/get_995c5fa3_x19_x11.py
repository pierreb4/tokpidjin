def get_995c5fa3_x19_x11(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(add, fork(add, a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_995c5fa3_x19_x11', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(add, fork(add, a1, a2), a3)'}

