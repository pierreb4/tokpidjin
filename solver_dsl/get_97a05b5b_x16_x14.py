def get_97a05b5b_x16_x14(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(combine, compose(a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_97a05b5b_x16_x14', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(combine, compose(a1, a2), a3)'}

