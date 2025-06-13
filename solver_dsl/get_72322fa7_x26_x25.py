def get_72322fa7_x26_x25(a1: Callable, a2: Callable, a3: Container[Container]) -> Callable:
    return mapply(fork(mapply, a1, a2), a3)

# {'a3': 'Container[Container]', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_72322fa7_x26_x25', 'Callable', 'Callable', 'Callable', 'Container[Container]'): 'mapply(fork(mapply, a1, a2), a3)'}

