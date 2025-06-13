def get_a64e4611_x19_x18(a1: Callable, a2: Callable, a3: Callable, a4: Callable) -> Callable:
    return compose(chain(a1, a2, a3), a4)

# {'a4': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_a64e4611_x19_x18', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'compose(chain(a1, a2, a3), a4)'}

