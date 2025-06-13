def get_e6721834_x13_x12(a1: Callable, a2: Any) -> Callable:
    return compose(flip, matcher(a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Any'}

func_d = {('get_e6721834_x13_x12', 'Callable', 'Callable', 'Any'): 'compose(flip, matcher(a1, a2))'}

