def get_22168020_x4_x3(a1: Callable, a2: Callable) -> Callable:
    return compose(merge, fork(a1, a2, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_22168020_x4_x3', 'Callable', 'Callable', 'Callable'): 'compose(merge, fork(a1, a2, a2))'}

