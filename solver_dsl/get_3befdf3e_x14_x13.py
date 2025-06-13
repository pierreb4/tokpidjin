def get_3befdf3e_x14_x13(a1: Callable, a2: Callable) -> Callable:
    return compose(a1, fork(rapply, a2, identity))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_3befdf3e_x14_x13', 'Callable', 'Callable', 'Callable'): 'compose(a1, fork(rapply, a2, identity))'}

