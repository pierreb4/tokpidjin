def get_97a05b5b_x17_x16(a1: Callable, a2: Callable, a3: Callable) -> Callable:
    return chain(a1, fork(combine, a2, a3), normalize)

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable', 'a3': 'Callable'}

func_d = {('get_97a05b5b_x17_x16', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(a1, fork(combine, a2, a3), normalize)'}

