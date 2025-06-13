def get_b775ac94_x14_x11(a1: Callable, a2: Callable) -> Callable:
    return fork(insert, a1, fork(difference, identity, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_b775ac94_x14_x11', 'Callable', 'Callable', 'Callable'): 'fork(insert, a1, fork(difference, identity, a2))'}

