def get_3bdb4ada_x7_x6(a1: Callable) -> Callable:
    return lbind(compose, compose(even, a1))

# {'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_3bdb4ada_x7_x6', 'Callable', 'Callable'): 'lbind(compose, compose(even, a1))'}

