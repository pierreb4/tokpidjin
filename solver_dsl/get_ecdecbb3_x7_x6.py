def get_ecdecbb3_x7_x6(a1: Callable, a2: Callable) -> Callable:
    return fork(connect, a1, fork(add, a1, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_ecdecbb3_x7_x6', 'Callable', 'Callable', 'Callable'): 'fork(connect, a1, fork(add, a1, a2))'}

