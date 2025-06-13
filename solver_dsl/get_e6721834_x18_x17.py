def get_e6721834_x18_x17(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(subtract, a1, compose(a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_e6721834_x18_x17', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(subtract, a1, compose(a2, a3))'}

