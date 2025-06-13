def get_3e980e27_x30_x29(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return chain(a1, a2, fork(shift, identity, a3))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Callable'}

func_d = {('get_3e980e27_x30_x29', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(a1, a2, fork(shift, identity, a3))'}

