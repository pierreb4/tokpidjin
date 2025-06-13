def get_b775ac94_x17_x16(a1: Callable, a2: Callable) -> Callable:
    return fork(combine, a1, chain(a2, delta, a1))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_b775ac94_x17_x16', 'Callable', 'Callable', 'Callable'): 'fork(combine, a1, chain(a2, delta, a1))'}

