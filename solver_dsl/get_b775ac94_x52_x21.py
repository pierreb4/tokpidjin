def get_b775ac94_x52_x21(a1: Callable, a2: Callable) -> Callable:
    return fork(multiply, shape_f, fork(position, a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_b775ac94_x52_x21', 'Callable', 'Callable', 'Callable'): 'fork(multiply, shape_f, fork(position, a1, a2))'}

