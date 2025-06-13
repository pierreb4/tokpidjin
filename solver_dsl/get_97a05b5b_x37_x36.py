def get_97a05b5b_x37_x36(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(mapply, a1, fork(apply, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_97a05b5b_x37_x36', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(mapply, a1, fork(apply, a2, a3))'}

