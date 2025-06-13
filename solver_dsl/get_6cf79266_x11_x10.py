def get_6cf79266_x11_x10(a1: Callable) -> Callable:
    return chain(flip, a1, lbind(add, NEG_UNITY))

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_6cf79266_x11_x10', 'Callable', 'Callable'): 'chain(flip, a1, lbind(add, NEG_UNITY))'}

