def get_f15e1fac_x29_x26(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(both, fork(greater, a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_f15e1fac_x29_x26', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(both, fork(greater, a1, a2), a3)'}

