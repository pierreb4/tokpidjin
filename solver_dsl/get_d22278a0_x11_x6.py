def get_d22278a0_x11_x6(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return compose(chain(even, a1, a2), a3)

# {'a3': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_d22278a0_x11_x6', 'Callable', 'Callable', 'Callable', 'Callable'): 'compose(chain(even, a1, a2), a3)'}

