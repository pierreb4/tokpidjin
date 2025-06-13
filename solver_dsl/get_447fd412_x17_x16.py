def get_447fd412_x17_x16(a1: Callable, a2: Callable, a3: Callable, a4: Callable) -> Callable:
    return fork(apply, a1, chain(a2, a3, a4))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable', 'a4': 'Callable'}

func_d = {('get_447fd412_x17_x16', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(apply, a1, chain(a2, a3, a4))'}

