def get_a64e4611_x9_x7(a1: Callable) -> Callable:
    return compose(fork(product, identity, identity), a1)

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_a64e4611_x9_x7', 'Callable', 'Callable'): 'compose(fork(product, identity, identity), a1)'}

