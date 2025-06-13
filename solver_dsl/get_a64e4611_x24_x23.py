def get_a64e4611_x24_x23(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return fork(mapply, a1, fork(occurrences, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_a64e4611_x24_x23', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(mapply, a1, fork(occurrences, a2, a3))'}

