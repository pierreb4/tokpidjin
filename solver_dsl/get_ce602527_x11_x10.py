def get_ce602527_x11_x10(a1: Callable, a2: Callable) -> Callable:
    return chain(size, a1, chain(toindices, a2, normalize))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_ce602527_x11_x10', 'Callable', 'Callable', 'Callable'): 'chain(size, a1, chain(toindices, a2, normalize))'}

