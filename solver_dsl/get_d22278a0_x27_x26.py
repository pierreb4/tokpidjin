def get_d22278a0_x27_x26(a1: Callable, a2: Callable, a3: Callable, a4: Callable) -> Callable:
    return fork(intersection, a1, chain(a2, a3, a4))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable', 'a4': 'Callable'}

func_d = {('get_d22278a0_x27_x26', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(intersection, a1, chain(a2, a3, a4))'}

