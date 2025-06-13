def get_444801d8_x6_x3(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(recolor_i, chain(a1, a2, delta), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_444801d8_x6_x3', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(recolor_i, chain(a1, a2, delta), a3)'}

