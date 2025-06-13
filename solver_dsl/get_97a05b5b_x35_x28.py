def get_97a05b5b_x35_x28(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(sfilter, compose(a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_97a05b5b_x35_x28', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(sfilter, compose(a1, a2), a3)'}

