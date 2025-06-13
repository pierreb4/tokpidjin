def get_49d1d64f_x14_x13(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(astuple, chain(a1, a2, a3), identity)

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_49d1d64f_x14_x13', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(astuple, chain(a1, a2, a3), identity)'}

