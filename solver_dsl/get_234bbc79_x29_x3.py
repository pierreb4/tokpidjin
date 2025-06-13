def get_234bbc79_x29_x3(a1: Callable, a2: Callable) -> Callable:
    return fork(remove, compose(a1, a2), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_234bbc79_x29_x3', 'Callable', 'Callable', 'Callable'): 'fork(remove, compose(a1, a2), a2)'}

