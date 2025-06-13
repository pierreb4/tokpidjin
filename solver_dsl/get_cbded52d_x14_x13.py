def get_cbded52d_x14_x13(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(either, a1, fork(hmatching, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_cbded52d_x14_x13', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(either, a1, fork(hmatching, a2, a3))'}

