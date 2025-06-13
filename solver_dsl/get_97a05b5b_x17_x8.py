def get_97a05b5b_x17_x8(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return chain(compose(a1, a2), a3, normalize)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_97a05b5b_x17_x8', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(compose(a1, a2), a3, normalize)'}

