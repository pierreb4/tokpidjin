def get_97a05b5b_x36_x35(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(apply, a1, fork(sfilter, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_97a05b5b_x36_x35', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(apply, a1, fork(sfilter, a2, a3))'}

