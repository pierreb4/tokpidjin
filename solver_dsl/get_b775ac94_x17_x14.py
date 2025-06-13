def get_b775ac94_x17_x14(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(combine, fork(insert, a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_b775ac94_x17_x14', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(combine, fork(insert, a1, a2), a3)'}

