def get_3bdb4ada_x22_x10(a1: Callable, a2: Callable, a3: Container[Container]) -> Callable:
    return mapply(fork(sfilter, a1, a2), a3)

# {'a3': 'Container[Container]', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_3bdb4ada_x22_x10', 'Callable', 'Callable', 'Callable', 'Container[Container]'): 'mapply(fork(sfilter, a1, a2), a3)'}

