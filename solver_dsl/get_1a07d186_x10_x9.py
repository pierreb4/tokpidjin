def get_1a07d186_x10_x9(a1: Callable) -> Callable:
    return fork(shift, identity, fork(gravitate, identity, a1))

# {'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_1a07d186_x10_x9', 'Callable', 'Callable'): 'fork(shift, identity, fork(gravitate, identity, a1))'}

