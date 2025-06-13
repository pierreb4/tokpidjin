def get_3befdf3e_x25_x24(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(intersection, a1, fork(mapply, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_3befdf3e_x25_x24', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(intersection, a1, fork(mapply, a2, a3))'}

