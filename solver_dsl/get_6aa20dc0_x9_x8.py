def get_6aa20dc0_x9_x8(a1: Callable, a2: Callable) -> Callable:
    return compose(a1, fork(difference, identity, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_6aa20dc0_x9_x8', 'Callable', 'Callable', 'Callable'): 'compose(a1, fork(difference, identity, a2))'}

