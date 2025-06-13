def get_a48eeaf7_x10_x9(a1: Callable, a2: Callable) -> Callable:
    return compose(a1, compose(a2, initset))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_a48eeaf7_x10_x9', 'Callable', 'Callable', 'Callable'): 'compose(a1, compose(a2, initset))'}

