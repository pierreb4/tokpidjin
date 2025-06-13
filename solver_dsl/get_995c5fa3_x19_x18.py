def get_995c5fa3_x19_x18(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(add, a1, fork(add, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_995c5fa3_x19_x18', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(add, a1, fork(add, a2, a3))'}

