def get_6e19193c_x10_x3(a1: Callable, a2: Callable) -> Callable:
    return fork(subtract, compose(a1, delta), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_6e19193c_x10_x3', 'Callable', 'Callable', 'Callable'): 'fork(subtract, compose(a1, delta), a2)'}

