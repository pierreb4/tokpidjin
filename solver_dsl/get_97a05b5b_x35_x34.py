def get_97a05b5b_x35_x34(a1: Callable, a2: Callable, a3: Callable, a4: Callable) -> Callable:
    return fork(sfilter, a1, chain(a2, a3, a4))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable', 'a4': 'Callable'}

func_d = {('get_97a05b5b_x35_x34', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(sfilter, a1, chain(a2, a3, a4))'}

