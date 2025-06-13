def get_234bbc79_x30_x29(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(astuple, a1, fork(remove, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_234bbc79_x30_x29', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(astuple, a1, fork(remove, a2, a3))'}

