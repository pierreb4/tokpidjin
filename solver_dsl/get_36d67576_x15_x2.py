def get_36d67576_x15_x2(a1: Callable, a2: Callable) -> Callable:
    return fork(mapply, compose(a1, normalize), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_36d67576_x15_x2', 'Callable', 'Callable', 'Callable'): 'fork(mapply, compose(a1, normalize), a2)'}

