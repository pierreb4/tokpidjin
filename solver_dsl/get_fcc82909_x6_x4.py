def get_fcc82909_x6_x4(a1: Callable) -> Callable:
    return fork(add, rbind(corner, R3), a1)

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_fcc82909_x6_x4', 'Callable', 'Callable'): 'fork(add, rbind(corner, R3), a1)'}

