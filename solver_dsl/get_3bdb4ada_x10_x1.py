def get_3bdb4ada_x10_x1(a1: Callable) -> Callable:
    return fork(sfilter, rbind(get_nth_f, F0), a1)

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_3bdb4ada_x10_x1', 'Callable', 'Callable'): 'fork(sfilter, rbind(get_nth_f, F0), a1)'}

