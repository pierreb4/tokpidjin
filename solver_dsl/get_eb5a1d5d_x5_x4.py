def get_eb5a1d5d_x5_x4(a1: Callable, a2: Callable) -> Callable:
    return fork(vconcat, identity, compose(a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_eb5a1d5d_x5_x4', 'Callable', 'Callable', 'Callable'): 'fork(vconcat, identity, compose(a1, a2))'}

