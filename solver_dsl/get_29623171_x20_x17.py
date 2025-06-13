def get_29623171_x20_x17(a1: Callable, a2: Any) -> Callable:
    return compose(flip, matcher(a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Any'}

func_d = {('get_29623171_x20_x17', 'Callable', 'Callable', 'Any'): 'compose(flip, matcher(a1, a2))'}

