def get_a64e4611_x16_x5(a1: Callable, a2: Callable) -> Callable:
    return rbind(a1, compose(asobject, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_a64e4611_x16_x5', 'Callable', 'Callable', 'Callable'): 'rbind(a1, compose(asobject, a2))'}

