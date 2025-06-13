def get_3e980e27_x11_x2(a1: Callable, a2: Callable) -> Callable:
    return chain(a1, lbind(lbind, shift), a2)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_3e980e27_x11_x2', 'Callable', 'Callable', 'Callable'): 'chain(a1, lbind(lbind, shift), a2)'}

