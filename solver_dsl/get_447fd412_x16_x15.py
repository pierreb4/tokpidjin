def get_447fd412_x16_x15(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return chain(a1, fork(combine, identity, a2), a3)

# {'a1': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_447fd412_x16_x15', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(a1, fork(combine, identity, a2), a3)'}

