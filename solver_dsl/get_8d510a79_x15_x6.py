def get_8d510a79_x15_x6(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return chain(invert, a1, compose(a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_8d510a79_x15_x6', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(invert, a1, compose(a2, a3))'}

