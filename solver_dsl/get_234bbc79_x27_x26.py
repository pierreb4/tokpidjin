def get_234bbc79_x27_x26(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(shift, a1, compose(a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_234bbc79_x27_x26', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(shift, a1, compose(a2, a3))'}

