def get_b527c5c6_x12_x11(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(add, a1, fork(equality, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_b527c5c6_x12_x11', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(add, a1, fork(equality, a2, a3))'}

