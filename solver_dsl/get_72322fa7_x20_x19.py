def get_72322fa7_x20_x19(a1: Callable, a2: Callable) -> Callable:
    return compose(a1, fork(difference, identity, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_72322fa7_x20_x19', 'Callable', 'Callable', 'Callable'): 'compose(a1, fork(difference, identity, a2))'}

