def get_1caeab9d_x10_x9(a1: Callable, a2: Container[Container]) -> Callable:
    return mapply(fork(shift, identity, a1), a2)

# {'a2': 'Container[Container]', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_1caeab9d_x10_x9', 'Callable', 'Callable', 'Container[Container]'): 'mapply(fork(shift, identity, a1), a2)'}

