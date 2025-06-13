def get_57aa92db_x13_x10(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(subtract, compose(a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_57aa92db_x13_x10', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(subtract, compose(a1, a2), a3)'}

