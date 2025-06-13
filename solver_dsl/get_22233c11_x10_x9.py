def get_22233c11_x10_x9(a1: Callable, a2: Callable) -> Callable:
    return fork(difference, a1, compose(a2, toindices))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_22233c11_x10_x9', 'Callable', 'Callable', 'Callable'): 'fork(difference, a1, compose(a2, toindices))'}

