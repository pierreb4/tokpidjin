def get_50846271_x21_x16(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(combine, fork(connect, a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_50846271_x21_x16', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(combine, fork(connect, a1, a2), a3)'}

