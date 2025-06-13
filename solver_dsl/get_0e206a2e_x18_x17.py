def get_0e206a2e_x18_x17(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(apply, a1, chain(a2, a3, normalize))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_0e206a2e_x18_x17', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(apply, a1, chain(a2, a3, normalize))'}

