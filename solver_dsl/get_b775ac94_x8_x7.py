def get_b775ac94_x8_x7(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(sfilter, identity, chain(a1, a2, a3))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_b775ac94_x8_x7', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(sfilter, identity, chain(a1, a2, a3))'}

