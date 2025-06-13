def get_97a05b5b_x30_x29(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return compose(chain(size, a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_97a05b5b_x30_x29', 'Callable', 'Callable', 'Callable', 'Callable'): 'compose(chain(size, a1, a2), a3)'}

