def get_d07ae81c_x23_x19(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(combine, fork(combine, a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_d07ae81c_x23_x19', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(combine, fork(combine, a1, a2), a3)'}

