def get_3bdb4ada_x3_x1(a1: Callable) -> Callable:
    return compose(a1, rbind(get_nth_f, F0))

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_3bdb4ada_x3_x1', 'Callable', 'Callable'): 'compose(a1, rbind(get_nth_f, F0))'}

