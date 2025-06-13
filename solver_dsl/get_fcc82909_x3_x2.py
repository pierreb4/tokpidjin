def get_fcc82909_x3_x2(a1: Callable) -> Callable:
    return compose(a1, rbind(corner, R2))

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_fcc82909_x3_x2', 'Callable', 'Callable'): 'compose(a1, rbind(corner, R2))'}

