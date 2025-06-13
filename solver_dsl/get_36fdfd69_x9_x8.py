def get_36fdfd69_x9_x8(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return compose(a1, fork(manhattan, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_36fdfd69_x9_x8', 'Callable', 'Callable', 'Callable', 'Callable'): 'compose(a1, fork(manhattan, a2, a3))'}

