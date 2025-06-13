def get_a64e4611_x21_x20(a1: Callable, a2: Callable, a3: Callable, a4: Callable, a5: Callable) -> Callable:
    return chain(a1, a2, fork(a3, a4, a5))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Callable', 'a4': 'Callable', 'a5': 'Callable'}

func_d = {('get_a64e4611_x21_x20', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(a1, a2, fork(a3, a4, a5))'}

