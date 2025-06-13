def get_d22278a0_x10_x9(a1: Callable, a2: Callable) -> Callable:
    return fork(subtract, a1, compose(center, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_d22278a0_x10_x9', 'Callable', 'Callable', 'Callable'): 'fork(subtract, a1, compose(center, a2))'}

