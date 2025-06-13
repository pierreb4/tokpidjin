def get_b527c5c6_x34_x33(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(a1, a2, compose(increment, a3))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Callable'}

func_d = {('get_b527c5c6_x34_x33', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(a1, a2, compose(increment, a3))'}

