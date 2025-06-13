def get_fcc82909_x8_x7(a1: Callable, a2: Callable) -> Callable:
    return compose(box, fork(astuple, a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_fcc82909_x8_x7', 'Callable', 'Callable', 'Callable'): 'compose(box, fork(astuple, a1, a2))'}

