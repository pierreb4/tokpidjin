def get_1a07d186_x15_x10(a1: Callable, a2: Container[Container]) -> Callable:
    return mapply(fork(shift, identity, a1), a2)

# {'a2': 'Container[Container]', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_1a07d186_x15_x10', 'Callable', 'Callable', 'Container[Container]'): 'mapply(fork(shift, identity, a1), a2)'}

