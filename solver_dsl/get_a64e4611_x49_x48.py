def get_a64e4611_x49_x48(a1: Callable, a2: Callable) -> Callable:
    return fork(both, a1, compose(a2, initset))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_a64e4611_x49_x48', 'Callable', 'Callable', 'Callable'): 'fork(both, a1, compose(a2, initset))'}

