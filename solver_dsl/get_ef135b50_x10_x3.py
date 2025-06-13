def get_ef135b50_x10_x3(a1: Callable, a2: Callable, a3: Container[Container]) -> Callable:
    return mapply(fork(connect, a1, a2), a3)

# {'a3': 'Container[Container]', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_ef135b50_x10_x3', 'Callable', 'Callable', 'Callable', 'Container[Container]'): 'mapply(fork(connect, a1, a2), a3)'}

