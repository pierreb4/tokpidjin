def get_234bbc79_x30_x28(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(astuple, fork(combine, a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_234bbc79_x30_x28', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(astuple, fork(combine, a1, a2), a3)'}

