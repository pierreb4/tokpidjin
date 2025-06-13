def get_6d58a25d_x17_x16(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(both, a1, compose(a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_6d58a25d_x17_x16', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(both, a1, compose(a2, a3))'}

