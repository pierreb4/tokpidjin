def get_3befdf3e_x24_x21(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(mapply, compose(a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_3befdf3e_x24_x21', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(mapply, compose(a1, a2), a3)'}

