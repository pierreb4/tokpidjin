def get_e6721834_x23_x19(a1: Callable, a2: Container) -> Callable:
    return apply(fork(shift, identity, a1), a2)

# {'a2': 'Container', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_e6721834_x23_x19', 'Callable', 'Callable', 'Container'): 'apply(fork(shift, identity, a1), a2)'}

