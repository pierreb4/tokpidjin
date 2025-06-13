def get_50846271_x6_x4(a1: Callable, a2: Callable) -> Callable:
    return fork(both, compose(a1, size), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_50846271_x6_x4', 'Callable', 'Callable', 'Callable'): 'fork(both, compose(a1, size), a2)'}

