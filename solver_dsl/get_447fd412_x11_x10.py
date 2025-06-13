def get_447fd412_x11_x10(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return chain(a1, a2, fork(difference, identity, a3))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Callable'}

func_d = {('get_447fd412_x11_x10', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(a1, a2, fork(difference, identity, a3))'}

