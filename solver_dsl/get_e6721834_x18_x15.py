def get_e6721834_x18_x15(a1: Callable, a2: Callable, a3: Callable, a4: Callable) -> Callable:
    return fork(subtract, chain(a1, a2, a3), a4)

# {'a4': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_e6721834_x18_x15', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(subtract, chain(a1, a2, a3), a4)'}

