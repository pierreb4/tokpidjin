def get_22233c11_x6_x5(a1: Callable, a2: Callable) -> Callable:
    return compose(toindices, fork(shift, a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_22233c11_x6_x5', 'Callable', 'Callable', 'Callable'): 'compose(toindices, fork(shift, a1, a2))'}

