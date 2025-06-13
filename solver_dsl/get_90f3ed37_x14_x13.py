def get_90f3ed37_x14_x13(a1: Callable, a2: Callable, a3: Callable, a4: Callable) -> Callable:
    return chain(a1, a2, compose(a3, a4))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Callable', 'a4': 'Callable'}

func_d = {('get_90f3ed37_x14_x13', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(a1, a2, compose(a3, a4))'}

