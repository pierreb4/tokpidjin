def get_50846271_x33_x32(a1: Callable, a2: Callable) -> Callable:
    return fork(combine, dneighbors, fork(insert, a1, a2))

# {'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_50846271_x33_x32', 'Callable', 'Callable', 'Callable'): 'fork(combine, dneighbors, fork(insert, a1, a2))'}

