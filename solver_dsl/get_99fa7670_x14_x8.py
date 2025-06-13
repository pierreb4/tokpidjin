def get_99fa7670_x14_x8(a1: Callable, a2: Callable) -> Callable:
    return fork(recolor_i, compose(color, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_99fa7670_x14_x8', 'Callable', 'Callable', 'Callable'): 'fork(recolor_i, compose(color, a1), a2)'}

