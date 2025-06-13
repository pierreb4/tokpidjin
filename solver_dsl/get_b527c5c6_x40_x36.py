def get_b527c5c6_x40_x36(a1: Callable, a2: Callable, a3: Container[Container]) -> Callable:
    return mapply(fork(mapply, a1, a2), a3)

# {'a3': 'Container[Container]', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_b527c5c6_x40_x36', 'Callable', 'Callable', 'Callable', 'Container[Container]'): 'mapply(fork(mapply, a1, a2), a3)'}

