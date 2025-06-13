def get_a85d4709_x15_x8(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return chain(a1, a2, a3)(ONE)

# {'a1': 'Callable', 'a2': 'Callable', 'a3': 'Callable', 'return': 'Callable'}

func_d = {('get_a85d4709_x15_x8', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(a1, a2, a3)(ONE)'}

