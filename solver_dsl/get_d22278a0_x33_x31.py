def get_d22278a0_x33_x31(a1: Callable, a2: Any, a3: Callable) -> Callable:
    return chain(a1, lbind(lbind, a2), a3)

# {'a1': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_d22278a0_x33_x31', 'Callable', 'Callable', 'Any', 'Callable'): 'chain(a1, lbind(lbind, a2), a3)'}

