def get_b775ac94_x13_x12(a1: Callable, a2: Callable, a3: Callable, a4: Callable) -> Callable:
    return fork(extract, a1, chain(a2, a3, a4))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable', 'a4': 'Callable'}

func_d = {('get_b775ac94_x13_x12', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(extract, a1, chain(a2, a3, a4))'}

