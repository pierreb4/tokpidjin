def get_29623171_x12_x9(a1: Callable, a2: Callable, a3: Container) -> Callable:
    return apply(fork(product, a1, a2), a3)

# {'a3': 'Container', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_29623171_x12_x9', 'Callable', 'Callable', 'Callable', 'Container'): 'apply(fork(product, a1, a2), a3)'}

