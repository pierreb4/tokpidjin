def get_9aec4887_x12_x11(a1: Callable, a2: Callable, a3: Callable, a4: Callable) -> Callable:
    return chain(a1, a2, chain(a3, a4, initset))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Callable', 'a4': 'Callable'}

func_d = {('get_9aec4887_x12_x11', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(a1, a2, chain(a3, a4, initset))'}

