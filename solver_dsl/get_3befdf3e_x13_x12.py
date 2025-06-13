def get_3befdf3e_x13_x12(a1: Callable, a2: Callable) -> Callable:
    return fork(rapply, chain(initset, a1, a2), identity)

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_3befdf3e_x13_x12', 'Callable', 'Callable', 'Callable'): 'fork(rapply, chain(initset, a1, a2), identity)'}

