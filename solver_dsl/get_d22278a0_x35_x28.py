def get_d22278a0_x35_x28(a1: Callable, a2: Callable) -> Callable:
    return fork(lbind(fork, greater), a1, a2)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_d22278a0_x35_x28', 'Callable', 'Callable', 'Callable'): 'fork(lbind(fork, greater), a1, a2)'}

