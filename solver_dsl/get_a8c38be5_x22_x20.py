def get_a8c38be5_x22_x20(a1: Callable, a2: Any, a3: Callable) -> Callable:
    return chain(a1, lbind(extract, a2), a3)

# {'a1': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_a8c38be5_x22_x20', 'Callable', 'Callable', 'Any', 'Callable'): 'chain(a1, lbind(extract, a2), a3)'}

