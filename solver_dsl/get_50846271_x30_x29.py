def get_50846271_x30_x29(a1: Callable, a2: Callable) -> Callable:
    return fork(insert, a1, compose(initset, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_50846271_x30_x29', 'Callable', 'Callable', 'Callable'): 'fork(insert, a1, compose(initset, a2))'}

