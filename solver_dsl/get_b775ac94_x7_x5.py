def get_b775ac94_x7_x5(a1: Callable, a2: Callable) -> Callable:
    return chain(a1, lbind(rbind, equality), a2)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_b775ac94_x7_x5', 'Callable', 'Callable', 'Callable'): 'chain(a1, lbind(rbind, equality), a2)'}

