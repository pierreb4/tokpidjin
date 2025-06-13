def get_97a05b5b_x24_x18(a1: Callable, a2: Callable) -> Callable:
    return chain(compose(positive, size), a1, a2)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_97a05b5b_x24_x18', 'Callable', 'Callable', 'Callable'): 'chain(compose(positive, size), a1, a2)'}

