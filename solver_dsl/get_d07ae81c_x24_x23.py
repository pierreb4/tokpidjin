def get_d07ae81c_x24_x23(a1: Callable, a2: Callable) -> Callable:
    return compose(fork(combine, a1, a2), center)

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_d07ae81c_x24_x23', 'Callable', 'Callable', 'Callable'): 'compose(fork(combine, a1, a2), center)'}

