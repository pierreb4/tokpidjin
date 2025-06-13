def get_d22278a0_x37_x36(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(intersection, a1, compose(a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_d22278a0_x37_x36', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(intersection, a1, compose(a2, a3))'}

