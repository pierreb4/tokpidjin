def get_22233c11_x10_x6(a1: Callable, a2: Callable) -> Callable:
    return fork(difference, compose(toindices, a1), a2)

# {'a2': 'Callable', 'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_22233c11_x10_x6', 'Callable', 'Callable', 'Callable'): 'fork(difference, compose(toindices, a1), a2)'}

