def get_1f642eb9_x7_x6(a1: Callable) -> Callable:
    return fork(shift, identity, compose(crement, a1))

# {'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_1f642eb9_x7_x6', 'Callable', 'Callable'): 'fork(shift, identity, compose(crement, a1))'}

