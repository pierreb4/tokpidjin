def get_ecdecbb3_x17_x6(a1: Callable, a2: Callable, a3: Container) -> Callable:
    return apply(fork(add, a1, a2), a3)

# {'a3': 'Container', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_ecdecbb3_x17_x6', 'Callable', 'Callable', 'Callable', 'Container'): 'apply(fork(add, a1, a2), a3)'}

