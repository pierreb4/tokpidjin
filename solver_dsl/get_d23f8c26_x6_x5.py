def get_d23f8c26_x6_x5(a1: Callable, a2: Any) -> Callable:
    return compose(flip, matcher(a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Any'}

func_d = {('get_d23f8c26_x6_x5', 'Callable', 'Callable', 'Any'): 'compose(flip, matcher(a1, a2))'}

