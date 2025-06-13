def get_6cf79266_x11_x9(a1: Callable, a2: Callable) -> Callable:
    return chain(flip, matcher(a1, ZERO), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_6cf79266_x11_x9', 'Callable', 'Callable', 'Callable'): 'chain(flip, matcher(a1, ZERO), a2)'}

