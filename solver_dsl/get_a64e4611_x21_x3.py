def get_a64e4611_x21_x3(a1: Callable, a2: Callable) -> Callable:
    return chain(lbind(lbind, shift), a1, a2)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_a64e4611_x21_x3', 'Callable', 'Callable', 'Callable'): 'chain(lbind(lbind, shift), a1, a2)'}

