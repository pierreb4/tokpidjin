def get_ddf7fa4f_x4_x2(a1: Callable, a2: Callable) -> Callable:
    return fork(recolor_o, compose(color, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_ddf7fa4f_x4_x2', 'Callable', 'Callable', 'Callable'): 'fork(recolor_o, compose(color, a1), a2)'}

