def get_4290ef0e_x30_x24(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return chain(fork(a1, positive, decrement), a2, a3)

# {'a2': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_4290ef0e_x30_x24', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(fork(a1, positive, decrement), a2, a3)'}

