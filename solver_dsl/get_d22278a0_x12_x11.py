def get_d22278a0_x12_x11(a1: Callable, a2: Callable) -> Callable:
    return lbind(compose, compose(a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_d22278a0_x12_x11', 'Callable', 'Callable', 'Callable'): 'lbind(compose, compose(a1, a2))'}

