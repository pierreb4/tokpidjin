def get_72322fa7_x9_x8(a1: Callable, a2: Callable) -> Callable:
    return compose(a1, fork(sfilter, identity, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_72322fa7_x9_x8', 'Callable', 'Callable', 'Callable'): 'compose(a1, fork(sfilter, identity, a2))'}

