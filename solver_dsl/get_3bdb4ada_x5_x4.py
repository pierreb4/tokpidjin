def get_3bdb4ada_x5_x4(a1: Callable, a2: Callable) -> Callable:
    return fork(subtract, a1, power(a2, TWO))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_3bdb4ada_x5_x4', 'Callable', 'Callable', 'Callable'): 'fork(subtract, a1, power(a2, TWO))'}

