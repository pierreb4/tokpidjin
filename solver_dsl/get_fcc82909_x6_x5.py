def get_fcc82909_x6_x5(a1: Callable) -> Callable:
    return fork(add, a1, compose(toivec, numcolors_f))

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_fcc82909_x6_x5', 'Callable', 'Callable'): 'fork(add, a1, compose(toivec, numcolors_f))'}

