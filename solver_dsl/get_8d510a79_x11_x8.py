def get_8d510a79_x11_x8(a1: Callable, a2: Callable) -> Callable:
    return fork(sfilter, fork(shoot, identity, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_8d510a79_x11_x8', 'Callable', 'Callable', 'Callable'): 'fork(sfilter, fork(shoot, identity, a1), a2)'}

