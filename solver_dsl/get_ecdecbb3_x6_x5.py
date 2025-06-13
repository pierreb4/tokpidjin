def get_ecdecbb3_x6_x5(a1: Callable, a2: Callable) -> Callable:
    return fork(add, a1, compose(crement, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_ecdecbb3_x6_x5', 'Callable', 'Callable', 'Callable'): 'fork(add, a1, compose(crement, a2))'}

