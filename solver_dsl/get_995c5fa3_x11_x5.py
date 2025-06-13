def get_995c5fa3_x11_x5(a1: Callable, a2: Callable) -> Callable:
    return fork(add, compose(double, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_995c5fa3_x11_x5', 'Callable', 'Callable', 'Callable'): 'fork(add, compose(double, a1), a2)'}

