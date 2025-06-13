def get_b775ac94_x14_x13(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(insert, fork(extract, a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_b775ac94_x14_x13', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(insert, fork(extract, a1, a2), a3)'}

