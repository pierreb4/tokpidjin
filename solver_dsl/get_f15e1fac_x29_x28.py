def get_f15e1fac_x29_x28(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(both, a1, fork(greater, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_f15e1fac_x29_x28', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(both, a1, fork(greater, a2, a3))'}

