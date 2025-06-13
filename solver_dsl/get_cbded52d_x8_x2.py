def get_cbded52d_x8_x2(a1: Callable, a2: Callable) -> Callable:
    return fork(recolor_i, compose(color, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_cbded52d_x8_x2', 'Callable', 'Callable', 'Callable'): 'fork(recolor_i, compose(color, a1), a2)'}

