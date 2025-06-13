def get_ba26e723_x5_x4(a1: Callable, a2: Callable) -> Callable:
    return fork(equality, identity, compose(a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_ba26e723_x5_x4', 'Callable', 'Callable', 'Callable'): 'fork(equality, identity, compose(a1, a2))'}

