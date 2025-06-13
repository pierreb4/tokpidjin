def get_b527c5c6_x33_x31(a1: Callable) -> Callable:
    return compose(increment, chain(decrement, a1, shape_f))

# {'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_b527c5c6_x33_x31', 'Callable', 'Callable'): 'compose(increment, chain(decrement, a1, shape_f))'}

