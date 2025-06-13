def get_3bdb4ada_x9_x8(a1: Callable) -> Callable:
    return compose(a1, lbind(rbind, astuple))

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_3bdb4ada_x9_x8', 'Callable', 'Callable'): 'compose(a1, lbind(rbind, astuple))'}

