def get_7df24a62_x20_x19(a1: Callable, a2: Callable) -> Callable:
    return compose(a1, chain(increment, a2, height_f))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_7df24a62_x20_x19', 'Callable', 'Callable', 'Callable'): 'compose(a1, chain(increment, a2, height_f))'}

