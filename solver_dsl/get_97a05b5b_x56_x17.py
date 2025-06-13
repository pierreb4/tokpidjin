def get_97a05b5b_x56_x17(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(apply, chain(a1, a2, normalize), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_97a05b5b_x56_x17', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(apply, chain(a1, a2, normalize), a3)'}

