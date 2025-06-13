def get_fcc82909_x7_x6(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(astuple, a1, fork(add, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_fcc82909_x7_x6', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(astuple, a1, fork(add, a2, a3))'}

