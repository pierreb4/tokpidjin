def get_e509e548_x6_x5(a1: Callable, a2: Callable) -> Callable:
    return compose(a1, chain(palette_t, trim, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_e509e548_x6_x5', 'Callable', 'Callable', 'Callable'): 'compose(a1, chain(palette_t, trim, a2))'}

