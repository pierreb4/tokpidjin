def get_b190f7f5_x11_x9(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return chain(a1, merge, a2)(a3)

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Any'}

func_d = {('get_b190f7f5_x11_x9', 'Callable', 'Callable', 'Callable', 'Any'): 'chain(a1, merge, a2)(a3)'}

