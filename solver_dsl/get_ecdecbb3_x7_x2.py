def get_ecdecbb3_x7_x2(a1: Callable, a2: Callable) -> Callable:
    return fork(connect, compose(center, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_ecdecbb3_x7_x2', 'Callable', 'Callable', 'Callable'): 'fork(connect, compose(center, a1), a2)'}

