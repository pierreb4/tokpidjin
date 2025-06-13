def get_99fa7670_x14_x13(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(recolor_i, a1, fork(connect, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_99fa7670_x14_x13', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(recolor_i, a1, fork(connect, a2, a3))'}

