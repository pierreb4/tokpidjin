def get_6a1e5592_x21_x17(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(subtract, fork(add, a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_6a1e5592_x21_x17', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(subtract, fork(add, a1, a2), a3)'}

