def get_447fd412_x9_x8(a1: Callable, a2: Callable) -> Callable:
    return fork(sfilter, identity, compose(a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_447fd412_x9_x8', 'Callable', 'Callable', 'Callable'): 'fork(sfilter, identity, compose(a1, a2))'}

