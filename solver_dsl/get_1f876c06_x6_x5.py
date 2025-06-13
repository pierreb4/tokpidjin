def get_1f876c06_x6_x5(a1: Callable, a2: Callable) -> Callable:
    return fork(recolor_i, color, fork(connect, a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_1f876c06_x6_x5', 'Callable', 'Callable', 'Callable'): 'fork(recolor_i, color, fork(connect, a1, a2))'}

