def get_d22278a0_x19_x5(a1: Callable, a2: Any, a3: Callable) -> Callable:
    return chain(a1, lbind(apply, a2), a3)

# {'a1': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_d22278a0_x19_x5', 'Callable', 'Callable', 'Any', 'Callable'): 'chain(a1, lbind(apply, a2), a3)'}

