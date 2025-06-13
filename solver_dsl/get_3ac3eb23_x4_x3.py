def get_3ac3eb23_x4_x3(a1: Callable, a2: Callable) -> Callable:
    return fork(recolor_i, color, chain(ineighbors, a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_3ac3eb23_x4_x3', 'Callable', 'Callable', 'Callable'): 'fork(recolor_i, color, chain(ineighbors, a1, a2))'}

