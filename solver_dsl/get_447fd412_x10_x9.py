def get_447fd412_x10_x9(a1: Callable) -> Callable:
    return fork(difference, identity, fork(sfilter, identity, a1))

# {'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_447fd412_x10_x9', 'Callable', 'Callable'): 'fork(difference, identity, fork(sfilter, identity, a1))'}

