def get_a85d4709_x8_x5(a1: Callable, a2: Any, a3: Callable) -> Callable:
    return chain(a1, lbind(sfilter, a2), a3)

# {'a1': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_a85d4709_x8_x5', 'Callable', 'Callable', 'Any', 'Callable'): 'chain(a1, lbind(sfilter, a2), a3)'}

