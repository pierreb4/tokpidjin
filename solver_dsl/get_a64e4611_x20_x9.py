def get_a64e4611_x20_x9(a1: Callable, a2: Callable, a3: Callable, a4: Callable) -> Callable:
    return fork(a1, compose(a2, a3), a4)

# {'a1': 'Callable', 'a4': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_a64e4611_x20_x9', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(a1, compose(a2, a3), a4)'}

