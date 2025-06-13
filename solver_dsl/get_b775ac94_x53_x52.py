def get_b775ac94_x53_x52(a1: Callable, a2: Callable) -> Callable:
    return fork(shift, a1, fork(multiply, shape_f, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_b775ac94_x53_x52', 'Callable', 'Callable', 'Callable'): 'fork(shift, a1, fork(multiply, shape_f, a2))'}

