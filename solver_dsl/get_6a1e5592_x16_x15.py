def get_6a1e5592_x16_x15(a1: Callable, a2: Callable) -> Callable:
    return compose(invert, chain(a1, size, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_6a1e5592_x16_x15', 'Callable', 'Callable', 'Callable'): 'compose(invert, chain(a1, size, a2))'}

