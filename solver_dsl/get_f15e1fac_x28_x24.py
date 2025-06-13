def get_f15e1fac_x28_x24(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(greater, a1, compose(a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_f15e1fac_x28_x24', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(greater, a1, compose(a2, a3))'}

