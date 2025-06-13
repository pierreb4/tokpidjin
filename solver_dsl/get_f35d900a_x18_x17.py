def get_f35d900a_x18_x17(a1: Callable, a2: Callable) -> Callable:
    return fork(manhattan, initset, chain(initset, a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_f35d900a_x18_x17', 'Callable', 'Callable', 'Callable'): 'fork(manhattan, initset, chain(initset, a1, a2))'}

