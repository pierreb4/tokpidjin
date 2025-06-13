def get_50846271_x6_x5(a1: Callable) -> Callable:
    return fork(both, a1, fork(either, vline_i, hline_i))

# {'a1': 'Callable', 'return': 'Callable'}

func_d = {('get_50846271_x6_x5', 'Callable', 'Callable'): 'fork(both, a1, fork(either, vline_i, hline_i))'}

