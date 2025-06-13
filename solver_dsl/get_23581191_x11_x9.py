def get_23581191_x11_x9(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return fork(intersection, a1, a2)(a3)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Any'}

func_d = {('get_23581191_x11_x9', 'Callable', 'Callable', 'Callable', 'Any'): 'fork(intersection, a1, a2)(a3)'}

