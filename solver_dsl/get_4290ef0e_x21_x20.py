def get_4290ef0e_x21_x20(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(insert, a1, fork(insert, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_4290ef0e_x21_x20', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(insert, a1, fork(insert, a2, a3))'}

