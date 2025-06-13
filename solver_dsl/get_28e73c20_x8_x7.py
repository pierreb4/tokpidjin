def get_28e73c20_x8_x7(a1: Callable, a2: Callable) -> Callable:
    return compose(a1, chain(a2, decrement, height_t))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_28e73c20_x8_x7', 'Callable', 'Callable', 'Callable'): 'compose(a1, chain(a2, decrement, height_t))'}

