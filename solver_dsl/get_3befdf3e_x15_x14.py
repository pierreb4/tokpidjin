def get_3befdf3e_x15_x14(a1: Callable, a2: Callable) -> Callable:
    return compose(backdrop, compose(a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_3befdf3e_x15_x14', 'Callable', 'Callable', 'Callable'): 'compose(backdrop, compose(a1, a2))'}

