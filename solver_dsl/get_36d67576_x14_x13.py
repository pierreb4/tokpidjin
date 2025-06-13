def get_36d67576_x14_x13(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(apply, a1, chain(a2, a3, normalize))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_36d67576_x14_x13', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(apply, a1, chain(a2, a3, normalize))'}

