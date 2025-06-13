def get_447fd412_x17_x11(a1: Callable, a2: Callable, a3: Callable, a4: Callable) -> Callable:
    return fork(apply, chain(a1, a2, a3), a4)

# {'a4': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_447fd412_x17_x11', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(apply, chain(a1, a2, a3), a4)'}

