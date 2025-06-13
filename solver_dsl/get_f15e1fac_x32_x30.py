def get_f15e1fac_x32_x30(a1: Callable, a2: Any, a3: Callable) -> Callable:
    return chain(a1, lbind(compose, a2), a3)

# {'a1': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_f15e1fac_x32_x30', 'Callable', 'Callable', 'Any', 'Callable'): 'chain(a1, lbind(compose, a2), a3)'}

