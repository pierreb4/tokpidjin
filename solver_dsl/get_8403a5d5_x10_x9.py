def get_8403a5d5_x10_x9(a1: Container, a2: Callable, a3: Callable) -> Callable:
    return sfilter(a1, compose(a2, a3))

# {'a1': 'Container', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_8403a5d5_x10_x9', 'Callable', 'Container', 'Callable', 'Callable'): 'sfilter(a1, compose(a2, a3))'}

