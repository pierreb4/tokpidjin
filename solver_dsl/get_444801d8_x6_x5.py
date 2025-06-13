def get_444801d8_x6_x5(a1: Callable, a2: Callable) -> Callable:
    return fork(recolor_i, a1, compose(a2, backdrop))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_444801d8_x6_x5', 'Callable', 'Callable', 'Callable'): 'fork(recolor_i, a1, compose(a2, backdrop))'}

