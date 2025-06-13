def get_29623171_x6_x4(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return compose(fork(a1, identity, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_29623171_x6_x4', 'Callable', 'Callable', 'Callable', 'Callable'): 'compose(fork(a1, identity, a2), a3)'}

