def get_cbded52d_x6_x3(a1: Callable, a2: Callable) -> Callable:
    return fork(connect, compose(center, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_cbded52d_x6_x3', 'Callable', 'Callable', 'Callable'): 'fork(connect, compose(center, a1), a2)'}

