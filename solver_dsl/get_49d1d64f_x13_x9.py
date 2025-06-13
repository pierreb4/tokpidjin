def get_49d1d64f_x13_x9(a1: Callable, a2: Callable, a3: Any, a4: Callable) -> Callable:
    return chain(a1, lbind(a2, a3), a4)

# {'a1': 'Callable', 'a4': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Any'}

func_d = {('get_49d1d64f_x13_x9', 'Callable', 'Callable', 'Callable', 'Any', 'Callable'): 'chain(a1, lbind(a2, a3), a4)'}

