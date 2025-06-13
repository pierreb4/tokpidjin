def get_3e980e27_x24_x11(a1: Callable, a2: Callable, a3: Callable, a4: Any) -> Callable:
    return chain(a1, a2, a3)(a4)

# {'a1': 'Callable', 'a2': 'Callable', 'a3': 'Callable', 'return': 'Callable', 'a4': 'Any'}

func_d = {('get_3e980e27_x24_x11', 'Callable', 'Callable', 'Callable', 'Callable', 'Any'): 'chain(a1, a2, a3)(a4)'}

