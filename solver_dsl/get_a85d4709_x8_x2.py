def get_a85d4709_x8_x2(a1: Callable, a2: Callable) -> Callable:
    return chain(lbind(mapply, hfrontier), a1, a2)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable'}

func_d = {('get_a85d4709_x8_x2', 'Callable', 'Callable', 'Callable'): 'chain(lbind(mapply, hfrontier), a1, a2)'}

