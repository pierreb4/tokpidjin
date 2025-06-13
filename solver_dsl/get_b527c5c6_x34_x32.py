def get_b527c5c6_x34_x32(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(a1, compose(invert, a2), a3)

# {'a1': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_b527c5c6_x34_x32', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(a1, compose(invert, a2), a3)'}

