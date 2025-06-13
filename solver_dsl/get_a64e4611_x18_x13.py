def get_a64e4611_x18_x13(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return chain(lbind(a1, multiply), a2, a3)

# {'a2': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_a64e4611_x18_x13', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(lbind(a1, multiply), a2, a3)'}

