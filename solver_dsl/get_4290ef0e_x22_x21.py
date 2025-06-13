def get_4290ef0e_x22_x21(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return compose(a1, fork(insert, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_4290ef0e_x22_x21', 'Callable', 'Callable', 'Callable', 'Callable'): 'compose(a1, fork(insert, a2, a3))'}

