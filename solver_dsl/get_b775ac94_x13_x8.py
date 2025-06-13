def get_b775ac94_x13_x8(a1: Callable, a2: Callable) -> Callable:
    return fork(extract, fork(sfilter, identity, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_b775ac94_x13_x8', 'Callable', 'Callable', 'Callable'): 'fork(extract, fork(sfilter, identity, a1), a2)'}

