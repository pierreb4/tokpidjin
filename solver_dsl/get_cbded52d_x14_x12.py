def get_cbded52d_x14_x12(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(either, fork(vmatching, a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_cbded52d_x14_x12', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(either, fork(vmatching, a1, a2), a3)'}

