def get_3befdf3e_x24_x23(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(mapply, a1, chain(a2, corners, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_3befdf3e_x24_x23', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(mapply, a1, chain(a2, corners, a3))'}

