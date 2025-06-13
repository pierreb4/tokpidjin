def get_9af7a82c_x12_x11(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return compose(a1, fork(vconcat, a2, a3))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_9af7a82c_x12_x11', 'Callable', 'Callable', 'Callable', 'Callable'): 'compose(a1, fork(vconcat, a2, a3))'}

