def get_8d510a79_x16_x15(a1: Callable, a2: Callable) -> Callable:
    return fork(shoot, identity, chain(invert, a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_8d510a79_x16_x15', 'Callable', 'Callable', 'Callable'): 'fork(shoot, identity, chain(invert, a1, a2))'}

