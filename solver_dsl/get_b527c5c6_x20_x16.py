def get_b527c5c6_x20_x16(a1: Callable, a2: Callable) -> Callable:
    return fork(add, compose(invert, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_b527c5c6_x20_x16', 'Callable', 'Callable', 'Callable'): 'fork(add, compose(invert, a1), a2)'}

