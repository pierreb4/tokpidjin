def get_045e512c_x10_x8(a1: Callable, a2: Callable) -> Callable:
    return chain(a1, lbind(rbind, multiply), a2)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_045e512c_x10_x8', 'Callable', 'Callable', 'Callable'): 'chain(a1, lbind(rbind, multiply), a2)'}

