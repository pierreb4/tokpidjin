def get_3bdb4ada_x6_x5(a1: Callable, a2: Callable) -> Callable:
    return compose(even, fork(subtract, a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_3bdb4ada_x6_x5', 'Callable', 'Callable', 'Callable'): 'compose(even, fork(subtract, a1, a2))'}

