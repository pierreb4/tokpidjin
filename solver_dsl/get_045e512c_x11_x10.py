def get_045e512c_x11_x10(a1: Callable, a2: Callable, a3: Callable, a4: Callable) -> Callable:
    return compose(a1, chain(a2, a3, a4))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable', 'a4': 'Callable'}

func_d = {('get_045e512c_x11_x10', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'compose(a1, chain(a2, a3, a4))'}

