def get_f15e1fac_x32_x31(a1: Callable, a2: Callable) -> Callable:
    return chain(a1, a2, lbind(lbind, astuple))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_f15e1fac_x32_x31', 'Callable', 'Callable', 'Callable'): 'chain(a1, a2, lbind(lbind, astuple))'}

