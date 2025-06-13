def get_0e206a2e_x30_x28(a1: Callable, a2: Callable, a3: Container) -> Callable:
    return apply(fork(compose, a1, a2), a3)

# {'a3': 'Container', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_0e206a2e_x30_x28', 'Callable', 'Callable', 'Callable', 'Container'): 'apply(fork(compose, a1, a2), a3)'}

