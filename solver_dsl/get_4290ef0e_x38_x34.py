def get_4290ef0e_x38_x34(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return compose(fork(add, a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_4290ef0e_x38_x34', 'Callable', 'Callable', 'Callable', 'Callable'): 'compose(fork(add, a1, a2), a3)'}

