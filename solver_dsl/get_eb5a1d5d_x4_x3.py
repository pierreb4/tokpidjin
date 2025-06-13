def get_eb5a1d5d_x4_x3(a1: Callable, a2: Callable) -> Callable:
    return compose(a1, fork(remove, a2, identity))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_eb5a1d5d_x4_x3', 'Callable', 'Callable', 'Callable'): 'compose(a1, fork(remove, a2, identity))'}

