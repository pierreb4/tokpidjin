def get_b527c5c6_x16_x15(a1: Callable, a2: Callable) -> Callable:
    return compose(invert, fork(equality, a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_b527c5c6_x16_x15', 'Callable', 'Callable', 'Callable'): 'compose(invert, fork(equality, a1, a2))'}

