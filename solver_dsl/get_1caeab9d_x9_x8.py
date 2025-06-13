def get_1caeab9d_x9_x8(a1: Callable, a2: Callable) -> Callable:
    return fork(shift, identity, chain(toivec, a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_1caeab9d_x9_x8', 'Callable', 'Callable', 'Callable'): 'fork(shift, identity, chain(toivec, a1, a2))'}

