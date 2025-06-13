def get_9af7a82c_x10_x9(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return compose(a1, chain(a2, a3, size))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_9af7a82c_x10_x9', 'Callable', 'Callable', 'Callable', 'Callable'): 'compose(a1, chain(a2, a3, size))'}

