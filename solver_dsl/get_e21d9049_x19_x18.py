def get_e21d9049_x19_x18(a1: Callable, a2: Callable) -> Callable:
    return compose(fork(either, a1, a2), initset)

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_e21d9049_x19_x18', 'Callable', 'Callable', 'Callable'): 'compose(fork(either, a1, a2), initset)'}

