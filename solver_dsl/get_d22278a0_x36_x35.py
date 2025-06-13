def get_d22278a0_x36_x35(a1: Callable, a2: Callable, a3: Callable, a4: Callable) -> Callable:
    return compose(a1, fork(a2, a3, a4))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable', 'a4': 'Callable'}

func_d = {('get_d22278a0_x36_x35', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'compose(a1, fork(a2, a3, a4))'}

