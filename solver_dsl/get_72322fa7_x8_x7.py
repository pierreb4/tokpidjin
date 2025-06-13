def get_72322fa7_x8_x7(a1: Callable, a2: Callable) -> Callable:
    return fork(sfilter, identity, compose(a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_72322fa7_x8_x7', 'Callable', 'Callable', 'Callable'): 'fork(sfilter, identity, compose(a1, a2))'}

