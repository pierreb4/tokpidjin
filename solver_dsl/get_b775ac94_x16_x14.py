def get_b775ac94_x16_x14(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return chain(a1, delta, fork(insert, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_b775ac94_x16_x14', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(a1, delta, fork(insert, a2, a3))'}

