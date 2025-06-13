def get_97a05b5b_x63_x62(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return chain(flip, a1, chain(a2, a3, palette_f))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_97a05b5b_x63_x62', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(flip, a1, chain(a2, a3, palette_f))'}

