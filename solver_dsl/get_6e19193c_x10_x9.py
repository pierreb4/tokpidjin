def get_6e19193c_x10_x9(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(subtract, a1, chain(a2, a3, toindices))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_6e19193c_x10_x9', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(subtract, a1, chain(a2, a3, toindices))'}

