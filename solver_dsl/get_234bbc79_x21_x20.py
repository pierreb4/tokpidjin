def get_234bbc79_x21_x20(a1: Callable, a2: Callable) -> Callable:
    return fork(sfilter, identity, compose(a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_234bbc79_x21_x20', 'Callable', 'Callable', 'Callable'): 'fork(sfilter, identity, compose(a1, a2))'}

