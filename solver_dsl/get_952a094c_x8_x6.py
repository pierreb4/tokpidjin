def get_952a094c_x8_x6(a1: Callable, a2: Any, a3: Callable) -> Callable:
    return chain(lbind(a1, a2), a3, initset)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Any'}

func_d = {('get_952a094c_x8_x6', 'Callable', 'Callable', 'Any', 'Callable'): 'chain(lbind(a1, a2), a3, initset)'}

