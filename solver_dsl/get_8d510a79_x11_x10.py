def get_8d510a79_x11_x10(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(sfilter, a1, compose(a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_8d510a79_x11_x10', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(sfilter, a1, compose(a2, a3))'}

