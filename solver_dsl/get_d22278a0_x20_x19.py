def get_d22278a0_x20_x19(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return lbind(compose, chain(a1, a2, a3))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_d22278a0_x20_x19', 'Callable', 'Callable', 'Callable', 'Callable'): 'lbind(compose, chain(a1, a2, a3))'}

