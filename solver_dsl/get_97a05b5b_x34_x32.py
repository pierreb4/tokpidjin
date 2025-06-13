def get_97a05b5b_x34_x32(a1: Callable, a2: Callable) -> Callable:
    return chain(a1, lbind(rbind, equality), a2)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_97a05b5b_x34_x32', 'Callable', 'Callable', 'Callable'): 'chain(a1, lbind(rbind, equality), a2)'}

