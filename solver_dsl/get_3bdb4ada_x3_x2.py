def get_3bdb4ada_x3_x2(a1: Callable) -> Callable:
    return compose(rbind(get_nth_f, L1), a1)

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_3bdb4ada_x3_x2', 'Callable', 'Callable'): 'compose(rbind(get_nth_f, L1), a1)'}

