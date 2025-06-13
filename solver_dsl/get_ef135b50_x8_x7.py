def get_ef135b50_x8_x7(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(equality, a1, compose(a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_ef135b50_x8_x7', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(equality, a1, compose(a2, a3))'}

