def get_82819916_x16_x15(a1: Callable, a2: Callable) -> Callable:
    return compose(a1, compose(toivec, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_82819916_x16_x15', 'Callable', 'Callable', 'Callable'): 'compose(a1, compose(toivec, a2))'}

