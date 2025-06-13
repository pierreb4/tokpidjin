def get_234bbc79_x28_x27(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(combine, a1, fork(shift, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_234bbc79_x28_x27', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(combine, a1, fork(shift, a2, a3))'}

