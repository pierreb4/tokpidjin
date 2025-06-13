def get_7837ac64_x36_x33(a1: Callable, a2: Callable) -> Callable:
    return fork(both, compose(flip, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_7837ac64_x36_x33', 'Callable', 'Callable', 'Callable'): 'fork(both, compose(flip, a1), a2)'}

