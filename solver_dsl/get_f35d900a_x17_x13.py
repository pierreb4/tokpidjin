def get_f35d900a_x17_x13(a1: Callable, a2: Any, a3: Callable) -> Callable:
    return chain(initset, lbind(a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Any'}

func_d = {('get_f35d900a_x17_x13', 'Callable', 'Callable', 'Any', 'Callable'): 'chain(initset, lbind(a1, a2), a3)'}

