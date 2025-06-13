def get_b775ac94_x25_x24(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return a1(fork(shift, a2, a3))

# {'a1': 'Callable', 'a2': 'Callable', 'a3': 'Callable', 'return': 'Callable'}

func_d = {('get_b775ac94_x25_x24', 'Callable', 'Callable', 'Callable', 'Callable'): 'a1(fork(shift, a2, a3))'}

