def get_4290ef0e_x29_x28(a1: Callable, a2: Callable) -> Callable:
    return compose(a1, fork(a2, identity, identity))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_4290ef0e_x29_x28', 'Callable', 'Callable', 'Callable'): 'compose(a1, fork(a2, identity, identity))'}

