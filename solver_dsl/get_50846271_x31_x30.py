def get_50846271_x31_x30(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(insert, a1, fork(insert, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_50846271_x31_x30', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(insert, a1, fork(insert, a2, a3))'}

