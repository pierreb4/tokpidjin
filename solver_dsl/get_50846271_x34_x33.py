def get_50846271_x34_x33(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return chain(a1, a2, fork(combine, dneighbors, a3))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Callable'}

func_d = {('get_50846271_x34_x33', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(a1, a2, fork(combine, dneighbors, a3))'}

