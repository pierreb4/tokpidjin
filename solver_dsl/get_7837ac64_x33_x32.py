def get_7837ac64_x33_x32(a1: Callable, a2: Callable) -> Callable:
    return compose(flip, chain(a1, palette_f, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_7837ac64_x33_x32', 'Callable', 'Callable', 'Callable'): 'compose(flip, chain(a1, palette_f, a2))'}

