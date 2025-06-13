def get_b527c5c6_x21_x12(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(astuple, fork(add, a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_b527c5c6_x21_x12', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(astuple, fork(add, a1, a2), a3)'}

