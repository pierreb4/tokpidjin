def get_952a094c_x14_x10(a1: Callable, a2: Container) -> Callable:
    return apply(fork(astuple, a1, identity), a2)

# {'a2': 'Container', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_952a094c_x14_x10', 'Callable', 'Callable', 'Container'): 'apply(fork(astuple, a1, identity), a2)'}

