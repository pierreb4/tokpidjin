def get_d07ae81c_x23_x22(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(combine, a1, fork(combine, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_d07ae81c_x23_x22', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(combine, a1, fork(combine, a2, a3))'}

