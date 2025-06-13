def get_f15e1fac_x26_x24(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(greater, compose(a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_f15e1fac_x26_x24', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(greater, compose(a1, a2), a3)'}

