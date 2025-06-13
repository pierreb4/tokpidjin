def get_6a1e5592_x17_x12(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(add, chain(a1, size, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_6a1e5592_x17_x12', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(add, chain(a1, size, a2), a3)'}

