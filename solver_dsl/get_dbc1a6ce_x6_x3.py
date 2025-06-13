def get_dbc1a6ce_x6_x3(a1: Callable, a2: Callable, a3: Container) -> Callable:
    return apply(fork(connect, a1, a2), a3)

# {'a3': 'Container', 'return': 'Callable', 'a1': 'Callable', 'a2': 'Callable'}

func_d = {('get_dbc1a6ce_x6_x3', 'Callable', 'Callable', 'Callable', 'Container'): 'apply(fork(connect, a1, a2), a3)'}

