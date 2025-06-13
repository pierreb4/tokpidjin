def get_447fd412_x18_x17(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return compose(a1, fork(apply, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_447fd412_x18_x17', 'Callable', 'Callable', 'Callable', 'Callable'): 'compose(a1, fork(apply, a2, a3))'}

