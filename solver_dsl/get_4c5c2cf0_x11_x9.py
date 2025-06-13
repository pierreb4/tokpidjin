def get_4c5c2cf0_x11_x9(a1: Callable, a2: Callable) -> Callable:
    return compose(fork(equality, identity, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_4c5c2cf0_x11_x9', 'Callable', 'Callable', 'Callable'): 'compose(fork(equality, identity, a1), a2)'}

