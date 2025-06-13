def get_6a1e5592_x31_x30(a1: Callable, a2: Callable) -> Callable:
    return chain(a1, a2, lbind(lbind, shift))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_6a1e5592_x31_x30', 'Callable', 'Callable', 'Callable'): 'chain(a1, a2, lbind(lbind, shift))'}

