def get_72322fa7_x24_x22(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(apply, compose(a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_72322fa7_x24_x22', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(apply, compose(a1, a2), a3)'}

