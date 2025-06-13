def get_feca6190_x8_x7(a1: Callable) -> Callable:
    return fork(recolor_i, color, compose(a1, center))

# {'return': 'Callable', 'a1': 'Callable'}

func_d = {('get_feca6190_x8_x7', 'Callable', 'Callable'): 'fork(recolor_i, color, compose(a1, center))'}

