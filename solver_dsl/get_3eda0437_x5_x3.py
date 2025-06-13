def get_3eda0437_x5_x3(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return chain(fork(apply, a1, a2), asobject, a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_3eda0437_x5_x3', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(fork(apply, a1, a2), asobject, a3)'}

