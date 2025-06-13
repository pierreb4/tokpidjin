def get_7df24a62_x5_x1(a1: Callable, a2: Callable) -> Callable:
    return chain(lbind(lbind, shift), a1, a2)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_7df24a62_x5_x1', 'Callable', 'Callable', 'Callable'): 'chain(lbind(lbind, shift), a1, a2)'}

