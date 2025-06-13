def get_50846271_x38_x21(a1: Callable, a2: Callable, a3: Container[Container]) -> Callable:
    return mapply(fork(combine, a1, a2), a3)

# {'a3': 'Container[Container]', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_50846271_x38_x21', 'Callable', 'Callable', 'Callable', 'Container[Container]'): 'mapply(fork(combine, a1, a2), a3)'}

