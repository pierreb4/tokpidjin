def get_fcc82909_x3_x1(a1: Callable) -> Callable:
    return compose(rbind(add, DOWN), a1)

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_fcc82909_x3_x1', 'Callable', 'Callable'): 'compose(rbind(add, DOWN), a1)'}

