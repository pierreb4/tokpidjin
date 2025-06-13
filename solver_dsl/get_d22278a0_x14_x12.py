def get_d22278a0_x14_x12(a1: Callable, a2: Any, a3: Callable) -> Callable:
    return chain(a1, lbind(compose, a2), a3)

# {'a1': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_d22278a0_x14_x12', 'Callable', 'Callable', 'Any', 'Callable'): 'chain(a1, lbind(compose, a2), a3)'}

