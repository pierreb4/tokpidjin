def get_aba27056_x28_x27(a1: Callable, a2: Callable) -> Callable:
    return compose(fork(both, a1, a2), initset)

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_aba27056_x28_x27', 'Callable', 'Callable', 'Callable'): 'compose(fork(both, a1, a2), initset)'}

