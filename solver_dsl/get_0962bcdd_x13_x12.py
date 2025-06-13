def get_0962bcdd_x13_x12(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(combine, a1, fork(connect, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_0962bcdd_x13_x12', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(combine, a1, fork(connect, a2, a3))'}

