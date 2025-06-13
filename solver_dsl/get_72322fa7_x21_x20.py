def get_72322fa7_x21_x20(a1: Callable, a2: Callable) -> Callable:
    return fork(subtract, a1, compose(a1, a2))

# {'a1': 'Callable', 'return': 'Callable', 'a2': 'Callable'}

func_d = {('get_72322fa7_x21_x20', 'Callable', 'Callable', 'Callable'): 'fork(subtract, a1, compose(a1, a2))'}

