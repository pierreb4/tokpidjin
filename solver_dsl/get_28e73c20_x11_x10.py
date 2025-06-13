def get_28e73c20_x11_x10(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(vconcat, a1, fork(vconcat, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_28e73c20_x11_x10', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(vconcat, a1, fork(vconcat, a2, a3))'}

