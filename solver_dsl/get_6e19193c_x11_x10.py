def get_6e19193c_x11_x10(a1: Callable, a2: Callable) -> Callable:
    return fork(shoot, a1, fork(subtract, a1, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_6e19193c_x11_x10', 'Callable', 'Callable', 'Callable'): 'fork(shoot, a1, fork(subtract, a1, a2))'}

