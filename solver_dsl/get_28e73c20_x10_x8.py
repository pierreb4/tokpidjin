def get_28e73c20_x10_x8(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(vconcat, compose(a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_28e73c20_x10_x8', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(vconcat, compose(a1, a2), a3)'}

