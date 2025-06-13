def get_b527c5c6_x15_x14(a1: Callable, a2: Callable) -> Callable:
    return fork(equality, compose(a1, a2), a1)

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_b527c5c6_x15_x14', 'Callable', 'Callable', 'Callable'): 'fork(equality, compose(a1, a2), a1)'}

