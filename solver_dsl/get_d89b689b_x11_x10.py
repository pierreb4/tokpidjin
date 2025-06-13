def get_d89b689b_x11_x10(a1: Callable, a2: Callable) -> Callable:
    return fork(recolor_i, color, compose(a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_d89b689b_x11_x10', 'Callable', 'Callable', 'Callable'): 'fork(recolor_i, color, compose(a1, a2))'}

