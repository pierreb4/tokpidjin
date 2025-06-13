def get_72322fa7_x24_x23(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(apply, a1, compose(a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_72322fa7_x24_x23', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(apply, a1, compose(a2, a3))'}

