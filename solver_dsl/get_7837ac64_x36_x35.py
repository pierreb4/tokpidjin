def get_7837ac64_x36_x35(a1: Callable, a2: Callable) -> Callable:
    return fork(both, a1, matcher(a2, ONE))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_7837ac64_x36_x35', 'Callable', 'Callable', 'Callable'): 'fork(both, a1, matcher(a2, ONE))'}

