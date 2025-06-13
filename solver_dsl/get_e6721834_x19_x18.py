def get_e6721834_x19_x18(a1: Callable, a2: Callable) -> Callable:
    return fork(shift, identity, fork(subtract, a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_e6721834_x19_x18', 'Callable', 'Callable', 'Callable'): 'fork(shift, identity, fork(subtract, a1, a2))'}

