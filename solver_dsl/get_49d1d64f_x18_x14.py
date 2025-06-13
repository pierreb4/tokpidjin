def get_49d1d64f_x18_x14(a1: Callable, a2: Container) -> Callable:
    return apply(fork(astuple, a1, identity), a2)

# {'a2': 'Container', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_49d1d64f_x18_x14', 'Callable', 'Callable', 'Container'): 'apply(fork(astuple, a1, identity), a2)'}

