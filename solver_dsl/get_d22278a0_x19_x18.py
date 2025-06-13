def get_d22278a0_x19_x18(a1: Callable, a2: Callable, a3: Callable, a4: Callable) -> Callable:
    return chain(fork(add, a1, a2), a3, a4)

# {'a3': 'Callable', 'a4': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_d22278a0_x19_x18', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(fork(add, a1, a2), a3, a4)'}

