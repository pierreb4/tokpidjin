def get_d22278a0_x14_x13(a1: Callable, a2: Callable) -> Callable:
    return chain(a1, a2, lbind(rbind, astuple))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_d22278a0_x14_x13', 'Callable', 'Callable', 'Callable'): 'chain(a1, a2, lbind(rbind, astuple))'}

