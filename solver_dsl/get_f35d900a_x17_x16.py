def get_f35d900a_x17_x16(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return chain(initset, a1, chain(a2, a3, initset))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_f35d900a_x17_x16', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(initset, a1, chain(a2, a3, initset))'}

