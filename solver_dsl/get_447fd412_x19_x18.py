def get_447fd412_x19_x18(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(mapply, a1, compose(a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_447fd412_x19_x18', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(mapply, a1, compose(a2, a3))'}

