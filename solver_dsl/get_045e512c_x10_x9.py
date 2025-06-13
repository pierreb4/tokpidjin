def get_045e512c_x10_x9(a1: Callable, a2: Callable, a3: Any) -> Callable:
    return chain(a1, a2, lbind(position, a3))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Any'}

func_d = {('get_045e512c_x10_x9', 'Callable', 'Callable', 'Callable', 'Any'): 'chain(a1, a2, lbind(position, a3))'}

