def get_b775ac94_x39_x21(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return chain(tojvec, a1, fork(position, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_b775ac94_x39_x21', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(tojvec, a1, fork(position, a2, a3))'}

