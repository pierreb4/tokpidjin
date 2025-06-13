def get_c8cbb738_x7_x6(a1: Callable) -> Callable:
    return fork(shift, identity, chain(halve, a1, shape_f))

# {'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_c8cbb738_x7_x6', 'Callable', 'Callable'): 'fork(shift, identity, chain(halve, a1, shape_f))'}

