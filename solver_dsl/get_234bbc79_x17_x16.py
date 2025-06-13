def get_234bbc79_x17_x16(a1: Callable, a2: Callable, a3: Callable, a4: Callable) -> Callable:
    return compose(a1, fork(a2, a3, a4))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable', 'a4': 'Callable'}

func_d = {('get_234bbc79_x17_x16', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'compose(a1, fork(a2, a3, a4))'}

