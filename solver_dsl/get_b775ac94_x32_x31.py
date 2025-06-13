def get_b775ac94_x32_x31(a1: Callable, a2: Callable, a3: Callable, a4: Callable) -> Callable:
    return chain(a1, a2, fork(intersection, a3, a4))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Callable', 'a4': 'Callable'}

func_d = {('get_b775ac94_x32_x31', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(a1, a2, fork(intersection, a3, a4))'}

