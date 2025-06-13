def get_a64e4611_x24_x21(a1: Callable, a2: Callable, a3: Callable, a4: Callable) -> Callable:
    return fork(mapply, chain(a1, a2, a3), a4)

# {'a4': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_a64e4611_x24_x21', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(mapply, chain(a1, a2, a3), a4)'}

