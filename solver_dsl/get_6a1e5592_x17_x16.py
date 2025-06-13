def get_6a1e5592_x17_x16(a1: Callable, a2: Callable) -> Callable:
    return fork(add, a1, compose(invert, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_6a1e5592_x17_x16', 'Callable', 'Callable', 'Callable'): 'fork(add, a1, compose(invert, a2))'}

