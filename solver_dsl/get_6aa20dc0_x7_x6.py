def get_6aa20dc0_x7_x6(a1: Callable, a2: Callable) -> Callable:
    return fork(sfilter, identity, compose(a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_6aa20dc0_x7_x6', 'Callable', 'Callable', 'Callable'): 'fork(sfilter, identity, compose(a1, a2))'}

