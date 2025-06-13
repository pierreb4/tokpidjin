def get_a85d4709_x8_x7(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return chain(a1, a2, lbind(matcher, a3))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Any'}

func_d = {('get_a85d4709_x8_x7', 'Callable', 'Callable', 'Callable', 'Any'): 'chain(a1, a2, lbind(matcher, a3))'}

