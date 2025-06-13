def get_8d510a79_x8_x7(a1: Callable, a2: Callable) -> Callable:
    return fork(shoot, identity, compose(a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_8d510a79_x8_x7', 'Callable', 'Callable', 'Callable'): 'fork(shoot, identity, compose(a1, a2))'}

