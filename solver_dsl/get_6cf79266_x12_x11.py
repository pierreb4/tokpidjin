def get_6cf79266_x12_x11(a1: Callable, a2: Callable) -> Callable:
    return fork(both, a1, chain(flip, a1, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_6cf79266_x12_x11', 'Callable', 'Callable', 'Callable'): 'fork(both, a1, chain(flip, a1, a2))'}

