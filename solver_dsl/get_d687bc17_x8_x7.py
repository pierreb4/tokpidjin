def get_d687bc17_x8_x7(a1: Callable, a2: Any) -> Callable:
    return chain(a1, lbind(colorfilter, a2), color)

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Any'}

func_d = {('get_d687bc17_x8_x7', 'Callable', 'Callable', 'Any'): 'chain(a1, lbind(colorfilter, a2), color)'}

