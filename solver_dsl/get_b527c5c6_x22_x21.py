def get_b527c5c6_x22_x21(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(shoot, a1, fork(astuple, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_b527c5c6_x22_x21', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(shoot, a1, fork(astuple, a2, a3))'}

