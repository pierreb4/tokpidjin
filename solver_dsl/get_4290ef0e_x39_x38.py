def get_4290ef0e_x39_x38(a1: Callable, a2: Callable) -> Callable:
    return compose(invert, compose(a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_4290ef0e_x39_x38', 'Callable', 'Callable', 'Callable'): 'compose(invert, compose(a1, a2))'}

