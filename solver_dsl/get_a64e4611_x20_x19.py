def get_a64e4611_x20_x19(a1: Callable, a2: Callable, a3: Callable, a4: Callable) -> Callable:
    return fork(a1, a2, compose(a3, a4))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Callable', 'a4': 'Callable'}

func_d = {('get_a64e4611_x20_x19', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(a1, a2, compose(a3, a4))'}

