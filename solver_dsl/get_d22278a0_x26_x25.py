def get_d22278a0_x26_x25(a1: Callable, a2: Callable) -> Callable:
    return chain(a1, a2, lbind(rbind, equality))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_d22278a0_x26_x25', 'Callable', 'Callable', 'Callable'): 'chain(a1, a2, lbind(rbind, equality))'}

