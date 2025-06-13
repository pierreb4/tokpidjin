def get_9aec4887_x17_x13(a1: Callable, a2: Container) -> Callable:
    return apply(fork(astuple, a1, identity), a2)

# {'a2': 'Container', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_9aec4887_x17_x13', 'Callable', 'Callable', 'Container'): 'apply(fork(astuple, a1, identity), a2)'}

