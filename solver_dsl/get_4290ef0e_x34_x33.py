def get_4290ef0e_x34_x33(a1: Callable, a2: Callable) -> Callable:
    return fork(add, a1, compose(double, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_4290ef0e_x34_x33', 'Callable', 'Callable', 'Callable'): 'fork(add, a1, compose(double, a2))'}

