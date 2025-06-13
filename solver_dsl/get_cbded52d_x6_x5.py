def get_cbded52d_x6_x5(a1: Callable, a2: Callable) -> Callable:
    return fork(connect, a1, compose(center, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_cbded52d_x6_x5', 'Callable', 'Callable', 'Callable'): 'fork(connect, a1, compose(center, a2))'}

