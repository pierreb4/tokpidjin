def get_97a05b5b_x28_x27(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return compose(a1, chain(a2, a3, normalize))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_97a05b5b_x28_x27', 'Callable', 'Callable', 'Callable', 'Callable'): 'compose(a1, chain(a2, a3, normalize))'}

