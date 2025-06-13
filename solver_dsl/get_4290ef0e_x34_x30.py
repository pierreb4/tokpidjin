def get_4290ef0e_x34_x30(a1: Callable, a2: Callable, a3: Callable, a4: Callable) -> Callable:
    return fork(add, chain(a1, a2, a3), a4)

# {'a4': 'Callable', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_4290ef0e_x34_x30', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'fork(add, chain(a1, a2, a3), a4)'}

