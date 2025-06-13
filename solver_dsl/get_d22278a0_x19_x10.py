def get_d22278a0_x19_x10(a1: Callable, a2: Callable, a3: Callable, a4: Callable) -> Callable:
    return chain(a1, a2, fork(subtract, a3, a4))

# {'a1': 'Callable', 'a2': 'Callable', 'return': 'Callable', 'a3': 'Callable', 'a4': 'Callable'}

func_d = {('get_d22278a0_x19_x10', 'Callable', 'Callable', 'Callable', 'Callable', 'Callable'): 'chain(a1, a2, fork(subtract, a3, a4))'}

