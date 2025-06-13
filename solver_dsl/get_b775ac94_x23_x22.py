def get_b775ac94_x23_x22(a1: Callable, a2: Callable) -> Callable:
    return fork(multiply, shape_f, chain(toivec, a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_b775ac94_x23_x22', 'Callable', 'Callable', 'Callable'): 'fork(multiply, shape_f, chain(toivec, a1, a2))'}

