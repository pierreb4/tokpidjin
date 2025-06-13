def get_b527c5c6_x8_x7(a1: Callable, a2: Callable) -> Callable:
    return compose(invert, fork(equality, a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_b527c5c6_x8_x7', 'Callable', 'Callable', 'Callable'): 'compose(invert, fork(equality, a1, a2))'}

