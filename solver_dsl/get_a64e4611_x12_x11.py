def get_a64e4611_x12_x11(a1: Callable, a2: Callable) -> Callable:
    return rbind(fork, fork(multiply, a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_a64e4611_x12_x11', 'Callable', 'Callable', 'Callable'): 'rbind(fork, fork(multiply, a1, a2))'}

