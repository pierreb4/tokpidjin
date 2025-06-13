def get_57aa92db_x24_x23(a1: Callable, a2: Callable) -> Callable:
    return fork(subtract, a1, compose(a2, width_f))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_57aa92db_x24_x23', 'Callable', 'Callable', 'Callable'): 'fork(subtract, a1, compose(a2, width_f))'}

