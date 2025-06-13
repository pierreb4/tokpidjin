def get_7837ac64_x23_x22(a1: Callable, a2: Callable, a3: Callable, a4: Callable) -> Callable:
    return compose(a1, chain(a2, a3, a4))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable', 'a4': 'Callable'}

func_d = {('get_7837ac64_x23_x22', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'compose(a1, chain(a2, a3, a4))'}

