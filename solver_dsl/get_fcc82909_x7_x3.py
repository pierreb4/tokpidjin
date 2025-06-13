def get_fcc82909_x7_x3(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(astuple, compose(a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_fcc82909_x7_x3', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(astuple, compose(a1, a2), a3)'}

