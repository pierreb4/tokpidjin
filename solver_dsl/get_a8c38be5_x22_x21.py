def get_a8c38be5_x22_x21(a1: Callable, a2: Callable) -> Callable:
    return chain(a1, a2, lbind(matcher, normalize))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_a8c38be5_x22_x21', 'Callable', 'Callable', 'Callable'): 'chain(a1, a2, lbind(matcher, normalize))'}

