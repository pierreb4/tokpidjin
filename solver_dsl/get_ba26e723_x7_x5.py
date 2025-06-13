def get_ba26e723_x7_x5(a1: Callable, a2: Callable) -> Callable:
    return compose(fork(equality, identity, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_ba26e723_x7_x5', 'Callable', 'Callable', 'Callable'): 'compose(fork(equality, identity, a1), a2)'}

