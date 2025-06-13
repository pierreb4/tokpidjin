def get_90f3ed37_x18_x14(a1: Callable, a2: Callable, a3: Callable, a4: Callable, a5: Callable) -> Callable:
    return fork(a1, chain(a2, a3, a4), a5)

# {'a1': 'Callable', 'a5': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable', 'a4': 'Callable'}

func_d = {('get_90f3ed37_x18_x14', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(a1, chain(a2, a3, a4), a5)'}

