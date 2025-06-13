def get_36d67576_x14_x11(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(apply, chain(a1, a2, normalize), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_36d67576_x14_x11', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(apply, chain(a1, a2, normalize), a3)'}

