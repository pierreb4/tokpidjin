def get_447fd412_x11_x3(a1: Callable, a2: Callable) -> Callable:
    return chain(lbind(rbind, subtract), a1, a2)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_447fd412_x11_x3', 'Callable', 'Callable', 'Callable'): 'chain(lbind(rbind, subtract), a1, a2)'}

