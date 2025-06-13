def get_57aa92db_x13_x12(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(subtract, a1, compose(a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_57aa92db_x13_x12', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(subtract, a1, compose(a2, a3))'}

